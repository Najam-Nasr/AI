import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

np.random.seed(42)

n = 600

df = pd.DataFrame({
    "total_spending": np.random.randint(500, 20000, n),
    "age": np.random.randint(18, 70, n),
    "visits": np.random.randint(1, 50, n),
    "purchase_frequency": np.random.randint(1, 20, n)
})

df.loc[df.sample(frac=0.05).index, "total_spending"] = np.nan
df.loc[df.sample(frac=0.05).index, "visits"] = np.nan

df["total_spending"] = df["total_spending"].fillna(df["total_spending"].median())
df["visits"] = df["visits"].fillna(df["visits"].median())

df["outlier_flag"] = (
    (df["total_spending"] > 18000) |
    (df["visits"] > 45)
)

df = df[df["outlier_flag"] == False]

df["customer_type"] = (
    (df["total_spending"] > 10000) &
    (df["visits"] > 20) &
    (df["purchase_frequency"] > 8)
).astype(int)

features = ["total_spending", "age", "visits", "purchase_frequency"]

X = df[features]
y = df["customer_type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = SVC(kernel="linear")
model.fit(X_train_scaled, y_train)

pred = model.predict(X_test_scaled)

print("Accuracy", accuracy_score(y_test, pred))
print("Precision", precision_score(y_test, pred))
print("Recall", recall_score(y_test, pred))
print("F1 Score", f1_score(y_test, pred))

weights = model.coef_[0]
intercept = model.intercept_[0]

print("Hyperplane Equation")
print("w1*x1 + w2*x2 + w3*x3 + w4*x4 + b = 0")
print(weights, intercept)

new_customer = pd.DataFrame([{
    "total_spending": 12000,
    "age": 35,
    "visits": 25,
    "purchase_frequency": 10
}])

new_scaled = scaler.transform(new_customer)
prediction = model.predict(new_scaled)[0]

if prediction == 1:
    print("High Value Customer")
else:
    print("Low Value Customer")
