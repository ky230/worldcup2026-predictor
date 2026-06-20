import urllib.request
import json
import re
import os
import sys
import gzip
import xml.etree.ElementTree as ET

def fetch_url(url):
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    )
    with urllib.request.urlopen(req) as response:
        return response.read()

def parse_standings(table_url, league_id, team_ids):
    try:
        content = fetch_url(table_url)
        # Check if content is gzipped
        if content[:2] == b'\x1f\x8b':
            content = gzip.decompress(content)
        xml_text = content.decode('utf-8')
        root = ET.fromstring(xml_text)
        
        # Look for the subt matching league_id
        subt = root.find(f".//subt[@id='{league_id}']")
        if subt is None:
            # Fallback: find any subt that has a child team matching one of team_ids
            for s in root.findall(".//subt"):
                for t in s.findall(".//t"):
                    if int(t.attrib.get("id", 0)) in team_ids:
                        subt = s
                        break
                if subt is not None:
                    break
        
        if subt is None:
            return {}
            
        standings = []
        for rank, t in enumerate(subt.findall(".//t"), 1):
            standings.append({
                "rank": rank,
                "name": t.attrib.get("name"),
                "id": int(t.attrib.get("id")),
                "points": int(t.attrib.get("p", 0)),
                "played": int(t.attrib.get("w", 0)) + int(t.attrib.get("d", 0)) + int(t.attrib.get("l", 0)),
                "wins": int(t.attrib.get("w", 0)),
                "draws": int(t.attrib.get("d", 0)),
                "losses": int(t.attrib.get("l", 0)),
                "gf": int(t.attrib.get("g", 0)),
                "ga": int(t.attrib.get("c", 0)),
                "gd": int(t.attrib.get("g", 0)) - int(t.attrib.get("c", 0))
            })
        return {
            "groupName": subt.attrib.get("name", "Unknown Group"),
            "table": standings
        }
    except Exception as e:
        print(f"Warning: Could not parse standings: {e}")
        return {}

def scrape_match(match_url, output_dir):
    print(f"Scraping match from: {match_url}")
    html_bytes = fetch_url(match_url)
    html = html_bytes.decode('utf-8')
    
    # Extract __NEXT_DATA__
    match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
    if not match:
        raise ValueError("Could not find __NEXT_DATA__ script tag")
        
    json_data = json.loads(match.group(1))
    props = json_data.get("props", {}).get("pageProps", {})
    
    general = props.get("general", {})
    content = props.get("content", {})
    match_facts = content.get("matchFacts", {})
    
    home_team = general.get("homeTeam", {}).get("name")
    away_team = general.get("awayTeam", {}).get("name")
    match_id = general.get("matchId")
    league_id = general.get("leagueId") or match_facts.get("infoBox", {}).get("Tournament", {}).get("id")
    
    print(f"Match: {home_team} vs {away_team} (ID: {match_id})")
    
    # Stadium & Referee
    stadium_name = "Unknown Stadium"
    referee_name = "Unknown Referee"
    info_box = match_facts.get("infoBox", {})
    if info_box:
        stadium = info_box.get("Stadium", {})
        if stadium:
            stadium_name = f"{stadium.get('name')}, {stadium.get('city')}"
        referee = info_box.get("Referee", {})
        if referee:
            referee_name = f"{referee.get('text')} ({referee.get('country')})"
            
    # Weather
    weather = content.get("weather", {})
    
    # H2H matches (filter for last 5 years)
    h2h_data = content.get("h2h", {})
    h2h_matches = []
    if h2h_data:
        raw_matches = h2h_data.get("matches", [])
        for m in raw_matches:
            time_str = m.get("time", {}).get("utcTime", "")
            # Filter matches from last 5 years
            year_match = re.search(r'\d{4}', time_str)
            if year_match:
                year = int(year_match.group(0))
                if year >= 2021: # Assuming current year is 2026
                    status = m.get("status", {})
                    h2h_matches.append({
                        "date": time_str[:10],
                        "home": m.get("home", {}).get("name"),
                        "away": m.get("away", {}).get("name"),
                        "score": f"{status.get('homeScore')} - {status.get('awayScore')}",
                        "league": m.get("league", {}).get("name")
                    })
                    
    # Team Form
    recent_form = {}
    team_form_list = match_facts.get("teamForm", [])
    if isinstance(team_form_list, list) and len(team_form_list) >= 2:
        for i, form in enumerate(team_form_list):
            team_name = home_team if i == 0 else away_team
            recent_form[team_name] = []
            for match_item in form:
                recent_form[team_name].append({
                    "result": match_item.get("resultString", ""),
                    "score": match_item.get("score", ""),
                    "home": match_item.get("tooltipText", {}).get("homeTeam"),
                    "away": match_item.get("tooltipText", {}).get("awayTeam"),
                    "date": match_item.get("date", {}).get("utcTime", "")[:10]
                })

    # Insights
    insights = [re.sub('<[^<]+?>', '', i.get("text", "")) for i in match_facts.get("insights", [])]
    
    # Lineups (Predicted or Confirmed)
    lineups_data = content.get("lineup", {})
    lineups = {"homeTeam": {}, "awayTeam": {}}
    if lineups_data:
        for team_key in ["homeTeam", "awayTeam"]:
            team_info = lineups_data.get(team_key, {})
            team_name = home_team if team_key == "homeTeam" else away_team
            formation = team_info.get("formation", "Unknown")
            
            starters = []
            for player in team_info.get("starters", []):
                name = player.get("name", "")
                shirt = player.get("shirtNumber", "")
                pos = player.get("position", "")
                coord = player.get("horizontalLayout", {})
                
                # Coordinate mapping
                x = coord.get("x", 0.5)
                y = coord.get("y", 0.5)
                if team_key == "homeTeam":
                    left = x * 46.75 + 1.25
                    top = y * 100
                else:
                    left = 100 - (x * 46.75 + 1.25)
                    top = (1 - y) * 100
                    
                starters.append({
                    "name": name,
                    "shirtNumber": shirt,
                    "position": pos,
                    "x": x,
                    "y": y,
                    "styleLeft": f"{left:.3f}%",
                    "styleTop": f"{top:.3f}%"
                })
                
            bench = [{"name": p.get("name", ""), "shirtNumber": p.get("shirtNumber", "")} for p in team_info.get("bench", [])]
            
            unavailable = []
            for player in team_info.get("unavailable", []):
                name = player.get("name", "")
                un_info = player.get("unavailability", {})
                un_type = un_info.get("type", "injury")
                expected = un_info.get("expectedReturn", "Unknown")
                unavailable.append({
                    "name": name,
                    "type": un_type,
                    "expectedReturn": expected
                })
                
            lineups[team_key] = {
                "teamName": team_name,
                "formation": formation,
                "starters": starters,
                "bench": bench,
                "unavailable": unavailable
            }
            
    # Fetch and parse standings if table url is available
    standings = {}
    table_meta = content.get("table", {})
    if table_meta and "url" in table_meta:
        team_ids = [general.get("homeTeam", {}).get("id"), general.get("awayTeam", {}).get("id")]
        standings = parse_standings(table_meta["url"], league_id, team_ids)

    # Output structured data
    match_data = {
        "matchId": match_id,
        "leagueId": league_id,
        "homeTeam": home_team,
        "awayTeam": away_team,
        "kickoffUTC": general.get("matchTimeUTC"),
        "stadium": stadium_name,
        "referee": referee_name,
        "weather": weather,
        "recentForm": recent_form,
        "h2h": h2h_matches,
        "insights": insights,
        "lineups": lineups,
        "standings": standings
    }
    
    # Save to file
    file_safe_name = f"{home_team.lower().replace(' ', '_')}_vs_{away_team.lower().replace(' ', '_')}.json"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, file_safe_name)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(match_data, f, indent=2, ensure_ascii=False)
    print(f"Saved match data to: {output_path}")
    return output_path

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 fetch_match_details.py <match_url> <output_dir>")
        sys.exit(1)
        
    url = sys.argv[1]
    out_dir = sys.argv[2]
    try:
        scrape_match(url, out_dir)
    except Exception as e:
        print(f"Error scraping match: {e}")
        sys.exit(1)
