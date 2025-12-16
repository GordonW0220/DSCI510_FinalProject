import requests
import datetime
import time
import json
import os

BASE_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article"
HEADERS = {"User-Agent": "DSCI510-CatProject/1.0"}

def format_title(title):
    return title.replace(" ", "_")

def get_pageviews(page_title, months=12):
    end = datetime.date.today().replace(day=1)
    start_month = end.month - months
    start_year = end.year

    if start_month <= 0:
        start_month += 12
        start_year -= 1

    start = datetime.date(start_year, start_month, 1)

    url = (
        f"{BASE_URL}/en.wikipedia/all-access/all-agents/"
        f"{format_title(page_title)}/monthly/"
        f"{start.strftime('%Y%m%d')}/{end.strftime('%Y%m%d')}"
    )

    r = requests.get(url, headers=HEADERS)

    if r.status_code != 200:
        return None

    data = r.json()
    views = [item["views"] for item in data.get("items", [])]

    return sum(views) if views else None

def save_pageviews(breeds, output_path="data/raw/pageviews.json", months=12):
    os.makedirs("data/raw", exist_ok=True)

    results = []

    for b in breeds:
        name = b.get("breed")
        if not name:
            continue

        views = get_pageviews(name, months=months)
        time.sleep(0.1)

        results.append({
            "breed": name,
            "pageviews": views
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Saved pageviews for {len(results)} breeds to {output_path}")
    
with open("data/raw/wikipedia_breeds.json", "r", encoding="utf-8") as f:
    wiki_breeds = json.load(f)

save_pageviews(wiki_breeds)





