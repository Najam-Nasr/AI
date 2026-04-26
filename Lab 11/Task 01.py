import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

n = 300

df = pd.DataFrame({
    "CustomerID": range(1, n + 1),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Age": np.random.randint(18, 70, n),
    "Annual_Income": np.random.randint(15000, 120000, n),
    "Spending_Score": np.random.randint(1, 100, n)
})

df = pd.get_dummies(df, columns=["Gender"], drop_first=True)

df_raw = df.copy()

kmeans_raw = KMeans(n_clusters=5, random_state=42, n_init=10)
df["cluster_raw"] = kmeans_raw.fit_predict(df.drop("CustomerID", axis=1))

print("Clustering without scaling")
print(df.groupby("cluster_raw").mean())

df_scaled = df.drop("cluster_raw", axis=1).copy()

scaler = StandardScaler()

cols_to_scale = df_scaled.columns.drop("CustomerID")

df_scaled[cols_to_scale] = scaler.fit_transform(df_scaled[cols_to_scale])

kmeans_scaled = KMeans(n_clusters=5, random_state=42, n_init=10)
df["cluster_scaled"] = kmeans_scaled.fit_predict(df_scaled.drop("CustomerID", axis=1))

print("Clustering with scaling (age excluded from scaling logic not needed here because no special weighting applied)")
print(df.groupby("cluster_scaled").mean())

print("Cluster sizes without scaling")
print(df["cluster_raw"].value_counts())

print("Cluster sizes with scaling")
print(df["cluster_scaled"].value_counts())
