#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("data/processed/cats_final.csv")

print("Dataset shape:", df.shape)
print(df[["breed", "pageviews"]].head())

features = df[
    [
        "intelligence",
        "energy_level",
        "affection_level",
        "grooming",
        "lifespan_years",
        "pageviews"
    ]
]

corr = features.corr()
print("\nCorrelation matrix:")
print(corr)

X = features.drop(columns=["pageviews"])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

k = 3 
kmeans = KMeans(n_clusters=k, random_state=42)
df["cluster"] = kmeans.fit_predict(X_scaled)

print("\nCluster counts:")
print(df["cluster"].value_counts())

df.to_csv("data/processed/cats_with_clusters.csv", index=False)
print("\nSaved clustered data to data/processed/cats_with_clusters.csv")


# In[ ]:




