import requests
import json
import time

CATAPI_URL = "https://api.thecatapi.com/v1/breeds"
HEADERS = {
    "User-Agent": "DSCI510-CatProject/1.0"
}

def get_catapi_breeds():
    response = requests.get(CATAPI_URL, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.json()


def save_catapi_data(output_path="data/raw/catapi_breeds.json"):
    data = get_catapi_breeds()

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Saved {len(data)} cat breeds to {output_path}")

save_catapi_data()




