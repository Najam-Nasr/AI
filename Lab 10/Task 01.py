import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

np.random.seed(42)

n = 500

areas = ['Downtown', 'Suburbs', 'Rural', 'Uptown']

df = pd.DataFrame({
    'bedrooms': np.random.randint(1, 6, n),
    'bathrooms': np.random.randint(1, 4, n),
    'square_footage': np.random.randint(500, 5000, n),
    'age': np.random.randint(0, 50, n),
    'neighborhood': np.random.choice(areas, n)
})

for c in ['bedrooms', 'square_footage', 'age']:
    df.loc[df.sample(frac=0.05).index, c] = np.nan

bonus = {
    'Downtown': 50000,
    'Uptown': 40000,
    'Suburbs': 20000,
    'Rural': 0
}

df['price'] = (
    df['square_footage'].fillna(df['square_footage'].median()) * 150 +
    df['bedrooms'].fillna(3) * 10000 +
    df['bathrooms'] * 8000 -
    df['age'].fillna(10) * 500 +
    df['neighborhood'].map(bonus) +
    np.random.randint(-15000, 15000, n)
)

df['bedrooms'] = df['bedrooms'].fillna(df['bedrooms'].median())
df['square_footage'] = df['square_footage'].fillna(df['square_footage'].median())
df['age'] = df['age'].fillna(df['age'].median())

le = LabelEncoder()
df['neighborhood_code'] = le.fit_transform(df['neighborhood'])

X = df[['bedrooms', 'bathrooms', 'square_footage', 'age', 'neighborhood_code']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100, random_state=42)

lr.fit(X_train_s, y_train)
rf.fit(X_train, y_train)

lr_pred = lr.predict(X_test_s)
rf_pred = rf.predict(X_test)

print("Linear Regression MAE", mean_absolute_error(y_test, lr_pred))
print("Linear Regression RMSE", np.sqrt(mean_squared_error(y_test, lr_pred)))
print("Linear Regression R2", r2_score(y_test, lr_pred))

print("Random Forest MAE", mean_absolute_error(y_test, rf_pred))
print("Random Forest RMSE", np.sqrt(mean_squared_error(y_test, rf_pred)))
print("Random Forest R2", r2_score(y_test, rf_pred))

new_house = pd.DataFrame([{
    'bedrooms': 3,
    'bathrooms': 2,
    'square_footage': 1800,
    'age': 10,
    'neighborhood_code': le.transform(['Suburbs'])[0]
}])

print("Linear Regression Prediction", lr.predict(scaler.transform(new_house))[0])
print("Random Forest Prediction", rf.predict(new_house)[0])


        if rank in ["Jack", "Queen", "King"]:
            face_total += 1
            if suit == "Diamonds":
                diamond_given_face += 1
            if suit == "Spades" or rank == "Queen":
                spade_or_queen += 1

    print("P(Red):", red / trials)
    print("P(Heart | Red):", heart_given_red / red_total)
    print("P(Diamond | Face):", diamond_given_face / face_total)
    print("P(Spade or Queen | Face):", spade_or_queen / face_total)

simulate()
