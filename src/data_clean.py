import json
import pandas as pd
import re
import os

os.makedirs("data/processed", exist_ok=True)
def midpoint(value):
    if pd.isna(value):
        return None
    nums = re.findall(r"\d+", str(value))
    nums = [int(n) for n in nums]
    if not nums:
        return None
    return sum(nums) / len(nums)

def clean_name(name):
    return name.lower().strip() if isinstance(name, str) else None

with open("data/raw/pageviews.json", "r", encoding="utf-8") as f:
    wiki = pd.DataFrame(json.load(f))

wiki["breed_clean"] = wiki["breed"].apply(clean_name)

with open("data/raw/catapi_breeds.json", "r", encoding="utf-8") as f:
    catapi = pd.DataFrame(json.load(f))

catapi["breed_clean"] = catapi["name"].apply(clean_name)

catapi["weight_kg"] = catapi["weight"].apply(
    lambda x: midpoint(x.get("metric")) if isinstance(x, dict) else None
)

catapi["lifespan_years"] = catapi["life_span"].apply(midpoint)

trait_cols = [
    "intelligence",
    "energy_level",
    "affection_level",
    "grooming",
    "child_friendly",
    "dog_friendly",
    "adaptability"
]

catapi_traits = catapi[
    ["breed_clean", "weight_kg", "lifespan_years"] + trait_cols
]

df = pd.merge(
    wiki,
    catapi_traits,
    on="breed_clean",
    how="inner"
)

df = df.dropna(subset=[
    "pageviews",
    "lifespan_years",
    "intelligence"
])

output_path = "data/processed/cats_final.csv"
df.to_csv(output_path, index=False)

print(f"Final dataset saved to {output_path}")





