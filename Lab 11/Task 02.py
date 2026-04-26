import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)

le = LabelEncoder()
df['vehicle_type'] = le.fit_transform(df['vehicle_type'])

kmeans_no_scaling = KMeans(n_clusters=3, random_state=42)
df['cluster_no_scaling'] = kmeans_no_scaling.fit_predict(df)

scaler = StandardScaler()
features_to_scale = ['vehicle_serial_no', 'mileage', 'fuel_efficiency', 'maintenance_cost']
scaled_features = scaler.fit_transform(df[features_to_scale])

X_scaled = np.hstack((scaled_features, df[['vehicle_type']].values))

kmeans_scaled = KMeans(n_clusters=3, random_state=42)
df['cluster_scaled'] = kmeans_scaled.fit_predict(X_scaled)

print(df)

print("\nWithout scaling: dominated by mileage")
print("With scaling: balanced clustering across features")
