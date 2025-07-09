import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample synthetic data
data = {
    'TaskType': [0, 0, 1, 1, 2, 2, 0, 1, 2, 0, 1, 2],
    'Resources': [2, 10, 3, 9, 4, 8, 7, 6, 5, 10, 10, 10],
    'Duration': [10, 3, 9, 2, 8, 3, 4, 4, 4, 2, 2, 2],
    'Delayed':  [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

# Train model
X = df[['TaskType', 'Resources', 'Duration']]
y = df['Delayed']
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model to .pkl
joblib.dump(model, 'delay_risk_model.pkl')
print("✅ Model saved as delay_risk_model.pkl")
