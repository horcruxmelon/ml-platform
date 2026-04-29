import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Training data
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 1, 0, 1, 0, 1])  # odd=0, even=1

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("Model saved!")
