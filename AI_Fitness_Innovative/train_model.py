import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

print("Training started...")

# Create model folder if not exists
if not os.path.exists("model"):
    os.makedirs("model")

# Sample dataset
data = {
    "attendance": [1,2,3,4,5,8,10,12,15,18,20],
    "consistency": [1,1,2,2,3,4,5,6,7,8,9],
    "renewed": [0,0,0,0,1,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["attendance", "consistency"]]
y = df["renewed"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print("Model Accuracy:", round(accuracy*100,2), "%")

joblib.dump(model, "model/retention_model.pkl")

print("Model saved successfully inside 'model' folder.")
print("Training completed successfully.")
