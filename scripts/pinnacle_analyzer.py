#!/usr/bin/env python3
import json
import math
import argparse
import os

def solve_poisson_lambda_total(p_under, max_iter=100, tol=1e-6):
    """
    Solve for lambda_total in P(Goals <= 2) = e^-L * (1 + L + L^2/2) = p_under
    using binary search.
    """
    low, high = 0.001, 20.0
    for _ in range(max_iter):
        mid = (low + high) / 2.0
        val = math.exp(-mid) * (1.0 + mid + (mid**2) / 2.0)
        if val > p_under:  # mid is too small (prob is too high)
            low = mid
        else:
            high = mid
        if abs(high - low) < tol:
            break
    return (low + high) / 2.0

def get_poisson_pmf(lam, k):
    if lam <= 0:
        return 1.0 if k == 0 else 0.0
    return (lam**k) * math.exp(-lam) / math.factorial(k)

def compute_poisson_probs(lambda_h, lambda_a, max_goals=12):
    """
    Compute probability matrix for goals up to max_goals.
    """
    probs = {}
    for h in range(max_goals + 1):
        for a in range(max_goals + 1):
            p_h = get_poisson_pmf(lambda_h, h)
            p_a = get_poisson_pmf(lambda_a, a)
            probs[(h, a)] = p_h * p_a
    return probs

def fit_lambdas(p_under, p_ai_home, p_ai_draw, p_ai_away):
    """
    Fit lambda_h and lambda_a such that lambda_h + lambda_a = lambda_total
    and we minimize MSE against the AI probabilities.
    """
    lambda_total = solve_poisson_lambda_total(p_under)
    best_mse = float('inf')
    best_lh = 0.0
    
    # Grid search lambda_h from 0.01 to lambda_total - 0.01
    steps = 2000
    for i in range(1, steps):
        lh = (i / steps) * lambda_total
        la = lambda_total - lh
        
        matrix = compute_poisson_probs(lh, la)
        p_h = sum(p for (h, a), p in matrix.items() if h > a)
        p_d = sum(p for (h, a), p in matrix.items() if h == a)
        p_a = sum(p for (h, a), p in matrix.items() if h < a)
        
        mse = (p_h - p_ai_home)**2 + (p_d - p_ai_draw)**2 + (p_a - p_ai_away)**2
        if mse < best_mse:
            best_mse = mse
            best_lh = lh
            
    return best_lh, lambda_total - best_lh, lambda_total

def optimize_split_kelly(p_win_full, p_win_half, p_push, p_lose_half, p_lose_full, b):
    """
    Solve for f* that maximizes E[ln(1 + f * X)]
    X is payoff:
      b with prob p_win_full
      0.5*b with prob p_win_half
      0 with prob p_push
      -0.5 with prob p_lose_half
      -1 with prob p_lose_full
    Convex optimization using golden section search in range [0, 0.99]
    """
    # Payoffs
    x_val = [b, 0.5 * b, 0.0, -0.5, -1.0]
    p_val = [p_win_full, p_win_half, p_push, p_lose_half, p_lose_full]
    
    # Calculate EV
    ev = sum(p * x for p, x in zip(p_val, x_val))
    if ev <= 0:
        return 0.0
        
    def expected_log_utility(f):
        # Prevent math domain error
        total = 0.0
        for p, x in zip(p_val, x_val):
            val = 1.0 + f * x
            if val <= 1e-9:
                return -float('inf')
            total += p * math.log(val)
        return total

    # Golden section search
    a, b_interval = 0.0, 0.999
    r = (math.sqrt(5) - 1) / 2
    k1 = b_interval - r * (b_interval - a)
    k2 = a + r * (b_interval - a)
    
    f1 = expected_log_utility(k1)
    f2 = expected_log_utility(k2)
    
    while (b_interval - a) > 1e-6:
        if f1 > f2:
            b_interval = k2
            k2 = k1
            f2 = f1
            k1 = b_interval - r * (b_interval - a)
            f1 = expected_log_utility(k1)
        else:
            a = k1
            k1 = k2
            f1 = f2
            k2 = a + r * (b_interval - a)
            f2 = expected_log_utility(k2)
            
    return (a + b_interval) / 2.0

def evaluate_handicap(lh, la, handicap_line, odds):
    """
    Evaluate winning/losing/pushing probabilities for Handicap.
    handicap_line is home handicap (e.g. -1.0 or -0.25 or +2.75).
    """
    matrix = compute_poisson_probs(lh, la)
    b = odds - 1.0
    
    p_win_full = 0.0
    p_win_half = 0.0
    p_push = 0.0
    p_lose_half = 0.0
    p_lose_full = 0.0
    
    for (h, a), p in matrix.items():
        gd = h - a
        diff = gd + handicap_line
        
        if diff > 0.25:
            p_win_full += p
        elif abs(diff - 0.25) < 1e-5:
            p_win_half += p
        elif abs(diff) < 1e-5:
            p_push += p
        elif abs(diff + 0.25) < 1e-5:
            p_lose_half += p
        else:
            p_lose_full += p
            
    # Calculate EV
    ev = p_win_full * b + p_win_half * (0.5 * b) + p_lose_half * (-0.5) + p_lose_full * (-1.0)
    
    # Kelly
    full_k = optimize_split_kelly(p_win_full, p_win_half, p_push, p_lose_half, p_lose_full, b)
    
    return {
        "probabilities": {
            "win_full": p_win_full,
            "win_half": p_win_half,
            "push": p_push,
            "lose_half": p_lose_half,
            "lose_full": p_lose_full
        },
        "ev": ev,
        "full_kelly": full_k
    }

def get_fair_probabilities(odds_dict):
    """
    Remove margin from decimal odds using simple normalization.
    """
    implied = {k: 1.0 / v for k, v in odds_dict.items() if v > 1.0}
    sum_implied = sum(implied.values())
    fair = {k: v / sum_implied for k, v in implied.items()}
    margin = sum_implied - 1.0
    return fair, margin

def select_correct_scores(lh, la, raw_correct_scores, p_ai_home, p_ai_away):
    """
    Select 3 Steady correct scores and 3 Upset correct scores.
    """
    matrix = compute_poisson_probs(lh, la)
    
    # Sort all scores in Poisson model by probability
    sorted_scores = sorted(matrix.items(), key=lambda item: item[1], reverse=True)
    
    # Steady scores (Top 3 overall)
    steady = []
    for (h, a), p in sorted_scores:
        score_str = f"{h}-{a}"
        odds = raw_correct_scores.get(score_str, 0.0)
        steady.append({
            "score": score_str,
            "probability": p,
            "odds": odds
        })
        if len(steady) == 3:
            break
            
    steady_scores = {s["score"] for s in steady}
    
    # Upset scores:
    # If Home is favorite (p_ai_home > 0.55): Draw (h==a) or Away win (h<a)
    # If Away is favorite (p_ai_away > 0.55): Draw (h==a) or Home win (h>a)
    # Otherwise: Draws or narrow wins
    upset_candidates = []
    is_home_fav = p_ai_home > 0.55
    is_away_fav = p_ai_away > 0.55
    
    for (h, a), p in sorted_scores:
        score_str = f"{h}-{a}"
        if score_str in steady_scores:
            continue
        # Limit to reasonable scorelines to stay logical
        if h > 3 or a > 3:
            continue
            
        is_upset = False
        if is_home_fav:
            if h <= a: # Draw or Away win
                is_upset = True
        elif is_away_fav:
            if h >= a: # Draw or Home win
                is_upset = True
        else:
            # For close matches, Draws (e.g. 2-2, 0-0, 1-1) or clean sheet narrow wins
            if h == a or (h == 1 and a == 0) or (h == 0 and a == 1):
                is_upset = True
                
        if is_upset:
            odds = raw_correct_scores.get(score_str, 0.0)
            upset_candidates.append({
                "score": score_str,
                "probability": p,
                "odds": odds
            })
            if len(upset_candidates) == 3:
                break
                
    return steady, upset_candidates

def main():
    parser = argparse.ArgumentParser(description="Pinnacle Odds and Correct Score Analyzer")
    parser.add_argument("--home", required=True)
    parser.add_argument("--away", required=True)
    parser.add_argument("--p-home", type=float, required=True)
    parser.add_argument("--p-draw", type=float, required=True)
    parser.add_argument("--p-away", type=float, required=True)
    parser.add_argument("--odds-home", type=float, required=True)
    parser.add_argument("--odds-draw", type=float, required=True)
    parser.add_argument("--odds-away", type=float, required=True)
    parser.add_argument("--odds-over", type=float, required=True)
    parser.add_argument("--odds-under", type=float, required=True)
    parser.add_argument("--handicap-line", type=float, required=True, help="Home handicap line, e.g. -1.0 or -0.25")
    parser.add_argument("--handicap-odds", type=float, required=True, help="Odds for the chosen home handicap line")
    parser.add_argument("--handicap-odds-away", type=float, help="Odds for the chosen away handicap line (optional)")
    parser.add_argument("--correct-scores", required=True, help="JSON string or comma-separated pairs of score:odds e.g. 1-0:6.5,2-0:7.0")
    parser.add_argument("--output-file", help="Path to write the output JSON analysis")
    
    args = parser.parse_args()
    
    # Parse correct scores
    raw_scores = {}
    try:
        if args.correct_scores.startswith("{"):
            raw_scores = json.loads(args.correct_scores)
        else:
            for pair in args.correct_scores.split(","):
                k, v = pair.split(":")
                raw_scores[k.strip()] = float(v.strip())
    except Exception as e:
        print(f"Error parsing correct scores: {e}")
        
    # Remove margins
    win_draw_loss_odds = {"home": args.odds_home, "draw": args.odds_draw, "away": args.odds_away}
    fair_1x2, margin_1x2 = get_fair_probabilities(win_draw_loss_odds)
    
    over_under_odds = {"over": args.odds_over, "under": args.odds_under}
    fair_ou, margin_ou = get_fair_probabilities(over_under_odds)
    
    # Fit Poisson goals model
    lh, la, l_total = fit_lambdas(fair_ou["under"], args.p_home, args.p_draw, args.p_away)
    
    # Calculate 1X2 expected values
    ev_home = args.p_home * (args.odds_home - 1.0) - (1.0 - args.p_home)
    ev_draw = args.p_draw * (args.odds_draw - 1.0) - (1.0 - args.p_draw)
    ev_away = args.p_away * (args.odds_away - 1.0) - (1.0 - args.p_away)
    
    # Calculate Let Handicap probabilities and EV for Home
    hc_eval = evaluate_handicap(lh, la, args.handicap_line, args.handicap_odds)
    
    # Assign Away handicap odds
    if args.handicap_odds_away is not None and args.handicap_odds_away > 0:
        odds_away_hc = args.handicap_odds_away
    else:
        margin_hc = 0.03
        odds_away_hc = round(1.0 / (1.0 + margin_hc - 1.0 / args.handicap_odds), 3)
    
    # Symmetrically calculate Away handicap probabilities
    p_win_full_away = hc_eval["probabilities"]["lose_full"]
    p_win_half_away = hc_eval["probabilities"]["lose_half"]
    p_push_away = hc_eval["probabilities"]["push"]
    p_lose_half_away = hc_eval["probabilities"]["win_half"]
    p_lose_full_away = hc_eval["probabilities"]["win_full"]
    b_away = odds_away_hc - 1.0
    
    ev_away_hc = p_win_full_away * b_away + p_win_half_away * (0.5 * b_away) + p_lose_half_away * (-0.5) + p_lose_full_away * (-1.0)
    full_k_away = optimize_split_kelly(p_win_full_away, p_win_half_away, p_push_away, p_lose_half_away, p_lose_full_away, b_away)

    # Select Correct Scores
    steady_scores, upset_scores = select_correct_scores(lh, la, raw_scores, args.p_home, args.p_away)
    
    # Format results
    results = {
        "match": f"{args.home} vs {args.away}",
        "ai_probabilities": {
            "home": args.p_home,
            "draw": args.p_draw,
            "away": args.p_away
        },
        "pinnacle_odds": {
            "home": args.odds_home,
            "draw": args.odds_draw,
            "away": args.odds_away,
            "margin_1x2": margin_1x2
        },
        "market_implied_probabilities": {
            "fair": fair_1x2
        },
        "ev": {
            "home": ev_home,
            "draw": ev_draw,
            "away": ev_away
        },
        "poisson_model": {
            "lambdas": {
                "home": lh,
                "away": la,
                "total": l_total
            }
        },
        "handicap": {
            "line": args.handicap_line,
            "odds_home": args.handicap_odds,
            "odds_away": odds_away_hc,
            "probabilities_home": hc_eval["probabilities"],
            "probabilities_away": {
                "win_full": p_win_full_away,
                "win_half": p_win_half_away,
                "push": p_push_away,
                "lose_half": p_lose_half_away,
                "lose_full": p_lose_full_away
            },
            "ev_home": hc_eval["ev"],
            "ev_away": ev_away_hc,
            "kelly_home": {
                "full_kelly": hc_eval["full_kelly"],
                "half_kelly": hc_eval["full_kelly"] * 0.5,
                "recommended_bet": round(200.0 * hc_eval["full_kelly"] * 0.5, 2)
            },
            "kelly_away": {
                "full_kelly": full_k_away,
                "half_kelly": full_k_away * 0.5,
                "recommended_bet": round(200.0 * full_k_away * 0.5, 2)
            }
        },
        "correct_scores": {
            "steady": steady_scores,
            "upset": upset_scores
        }
    }
    
    # Also calculate 1X2 Kelly for Home/Draw/Away if positive EV
    kelly_1x2 = {}
    for outcome, ev, odds, prob in [("home", ev_home, args.odds_home, args.p_home),
                                    ("draw", ev_draw, args.odds_draw, args.p_draw),
                                    ("away", ev_away, args.odds_away, args.p_away)]:
        if ev > 0:
            full_k = (prob * odds - 1.0) / (odds - 1.0)
            kelly_1x2[outcome] = {
                "full_kelly": full_k,
                "half_kelly": full_k * 0.5,
                "recommended_bet": round(200.0 * full_k * 0.5, 2)
            }
        else:
            kelly_1x2[outcome] = {
                "full_kelly": 0.0,
                "half_kelly": 0.0,
                "recommended_bet": 0.0
            }
    results["kelly_1x2"] = kelly_1x2
    
    print(json.dumps(results, indent=2, ensure_ascii=False))
    
    if args.output_file:
        os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
        with open(args.output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
            
if __name__ == "__main__":
    main()
