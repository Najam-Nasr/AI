import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

emails = [
    "Win money now click here",
    "Meeting scheduled for tomorrow",
    "Congratulations you won a prize",
    "Please review the attached document",
    "Free offer just for you click link",
    "Project deadline is next week",
    "Claim your reward immediately",
    "Let’s have lunch tomorrow"
]

labels = [1, 0, 1, 0, 1, 0, 1, 0]

df = pd.DataFrame({
    "email": emails,
    "label": labels
})

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["email"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Model Evaluation")
print("Accuracy:", accuracy_score(y_test, pred))
print("Precision:", precision_score(y_test, pred))
print("Recall:", recall_score(y_test, pred))
print("F1 Score:", f1_score(y_test, pred))

new_emails = [
    "You have won a free iphone click now",
    "Can we meet tomorrow for discussion"
]

new_x = vectorizer.transform(new_emails)
new_pred = model.predict(new_x)

print("Email Predictions")

for email, p in zip(new_emails, new_pred):
    if p == 1:
        print(email, "=> Spam Email")
    else:
        print(email, "=> Not Spam Email")
