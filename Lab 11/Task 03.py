import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'student_id': [1,2,3,4,5,6,7,8,9,10],
    'GPA': [3.5,2.8,3.9,1.8,2.5,3.2,3.7,2.0,3.0,2.2],
    'study_hours': [15,8,20,5,7,12,18,6,10,9],
    'attendance_rate': [90,75,95,60,70,85,92,65,80,78]
}

df = pd.DataFrame(data)

X = df[['GPA','study_hours','attendance_rate']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []
for k in range(2,7):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(2,7), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("K")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

plt.scatter(df['study_hours'], df['GPA'], c=df['cluster'])
plt.xlabel("Study Hours")
plt.ylabel("GPA")
plt.title("Student Clusters")
plt.show()

print(df[['student_id','cluster']])
