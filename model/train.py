import pickle
from sklearn.linear_model import LogisticRegression

# Sample dataset
X = [
    [25, 50000, 700],
    [40, 30000, 600],
    [30, 80000, 750],
    [22, 20000, 580]
]
y = [1, 0, 1, 0]

model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved")
