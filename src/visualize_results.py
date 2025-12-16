import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/processed/cats_with_clusters.csv")

top10 = df.sort_values("pageviews", ascending=False).head(10)

plt.figure(figsize=(8, 5))
plt.barh(top10["breed"], top10["pageviews"])
plt.xlabel("Wikipedia Pageviews")
plt.title("Top 10 Most Popular Cat Breeds")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 5))
plt.scatter(df["intelligence"], df["pageviews"], alpha=0.7)
plt.xlabel("Intelligence Score")
plt.ylabel("Wikipedia Pageviews")
plt.title("Popularity vs Intelligence")
plt.tight_layout()
plt.show()

traits = [
    "pageviews",
    "intelligence",
    "energy_level",
    "affection_level",
    "grooming",
    "lifespan_years"
]

corr = df[traits].corr()

plt.figure(figsize=(7, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Popularity and Cat Traits")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 5))
sns.scatterplot(
    data=df,
    x="energy_level",
    y="grooming",
    hue="cluster",
    palette="Set2"
)
plt.xlabel("Energy Level")
plt.ylabel("Grooming Requirement")
plt.title("Cat Breed Clusters by Traits")
plt.tight_layout()
plt.show()




