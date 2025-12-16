import requests
from bs4 import BeautifulSoup
import re
import json
import os

WIKI_LIST_URL = "https://en.wikipedia.org/wiki/List_of_cat_breeds"

def clean_text(text):
    return re.sub(r"\[\d+\]", "", text).strip()

def find_col(header_map, keywords):
    for key, idx in header_map.items():
        for kw in keywords:
            if kw in key:
                return idx
    return None

def get_cat_breeds():
    response = requests.get(
        WIKI_LIST_URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table", class_="wikitable")

    target_table = None
    for table in tables:
        headers = [th.get_text(strip=True).lower() for th in table.find_all("th")]
        if headers and "breed" in headers[0]:
            target_table = table
            break

    if target_table is None:
        raise ValueError("Could not find cat breeds table")

    header_cells = target_table.find("tr").find_all("th")
    header_map = {
        th.get_text(strip=True).lower(): idx
        for idx, th in enumerate(header_cells)
    }

    idx_breed = find_col(header_map, ["breed"])
    idx_origin = find_col(header_map, ["origin", "country", "place"])
    idx_body = find_col(header_map, ["body"])
    idx_coat = find_col(header_map, ["coat"])

    if None in (idx_breed, idx_origin, idx_body, idx_coat):
        raise ValueError(f"Column mapping failed: {header_map}")

    breeds = []

    for row in target_table.find_all("tr")[1:]:
        cells = row.find_all(["td", "th"])
        if len(cells) <= max(idx_breed, idx_origin, idx_body, idx_coat):
            continue

        breed = clean_text(cells[idx_breed].get_text(strip=True))
        origin = clean_text(cells[idx_origin].get_text(strip=True))
        body_type = clean_text(cells[idx_body].get_text(strip=True))
        coat = clean_text(cells[idx_coat].get_text(strip=True))

        if not breed:
            continue

        breeds.append({
            "breed": breed,
            "origin": origin,
            "body_type": body_type,
            "coat_type": coat
        })
    return breeds

data = get_cat_breeds()
print(f"Scraped {len(data)} cat breeds")
os.makedirs("data/raw", exist_ok=True)

output_path = "data/raw/wikipedia_breeds.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Saved data to {output_path}")




