import urllib.request
import json
import gzip
import os
import sys

def fetch_url(url):
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    )
    with urllib.request.urlopen(req) as response:
        content = response.read()
        if content[:2] == b'\x1f\x8b':
            content = gzip.decompress(content)
        return content.decode('utf-8')

def scrape_yellow_cards(output_dir):
    url = "https://data.fotmob.com/stats/77/season/24254/yellow_card.json"
    print(f"Scraping tournament yellow cards from: {url}")
    
    try:
        res = fetch_url(url)
        data = json.loads(res)
        
        top_lists = data.get("TopLists", [])
        if not top_lists:
            raise ValueError("No TopLists found in yellow cards data")
            
        stat_list = top_lists[0].get("StatList", [])
        if not stat_list:
            raise ValueError("No StatList found in yellow cards data")
            
        yellow_cards = []
        for item in stat_list:
            name = item.get('ParticipantName')
            team = item.get('TeamName')
            stat_val = item.get('StatValue')
            if name and team:
                yellow_cards.append({
                    "name": name,
                    "team": team,
                    "cards": int(stat_val) if stat_val is not None else 0
                })
                
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "yellow_cards.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(yellow_cards, f, indent=2, ensure_ascii=False)
            
        print(f"Saved tournament yellow cards to: {output_path} (Total players: {len(yellow_cards)})")
        return output_path
    except Exception as e:
        print(f"Error scraping yellow cards: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_yellow_cards.py <output_dir>")
        sys.exit(1)
        
    out_dir = sys.argv[1]
    scrape_yellow_cards(out_dir)
