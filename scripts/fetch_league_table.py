import urllib.request
import json
import re
import os
import sys

def fetch_url(url):
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    )
    with urllib.request.urlopen(req) as response:
        return response.read()

def scrape_league_table(output_dir):
    url = "https://www.fotmob.com/leagues/77/table/world-cup"
    print(f"Scraping global standings from: {url}")
    html_bytes = fetch_url(url)
    html = html_bytes.decode('utf-8')
    
    match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
    if not match:
        raise ValueError("Could not find __NEXT_DATA__ script tag")
        
    json_data = json.loads(match.group(1))
    props = json_data.get("props", {}).get("pageProps", {})
    table_list = props.get("table", [])
    
    if not table_list:
        raise ValueError("No table data found in pageProps")
        
    # extract the first table's data.tables (groups tables)
    table_data = table_list[0].get("data", {})
    raw_tables = table_data.get("tables", [])
    
    groups_standings = {}
    for group in raw_tables:
        group_name = group.get("leagueName", "Unknown Group")
        standings = []
        # In the page table structure, table.table.all contains the list of team stats in the group
        group_table = group.get("table", {})
        all_teams = group_table.get("all", [])
        for t in all_teams:
            standings.append({
                "rank": t.get("deductedPointsRank", t.get("rank")),
                "name": t.get("name"),
                "id": t.get("id"),
                "played": t.get("played"),
                "wins": t.get("wins"),
                "draws": t.get("draws"),
                "losses": t.get("losses"),
                "gf": t.get("scoresStr", "").split("-")[0].strip() if "-" in t.get("scoresStr", "") else t.get("goalsFor"),
                "ga": t.get("scoresStr", "").split("-")[1].strip() if "-" in t.get("scoresStr", "") else t.get("goalsAgainst"),
                "gd": t.get("goalConDiff"),
                "points": t.get("pts")
            })
        groups_standings[group_name] = standings
        
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "standings.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(groups_standings, f, indent=2, ensure_ascii=False)
    print(f"Saved global standings to: {output_path}")
    return output_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_league_table.py <output_dir>")
        sys.exit(1)
    out_dir = sys.argv[1]
    scrape_league_table(out_dir)
