from flask import Flask, render_template, request
import joblib
from services.recommendation import recommend_class
from services.forecast import forecast_weight
from services.analytics import generate_graph

app = Flask(__name__)

model = joblib.load("model/retention_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    attendance = int(request.form["attendance"])
    consistency = int(request.form["consistency"])
    weight = float(request.form["weight"])
    goal = request.form["goal"]

    prediction = model.predict([[attendance, consistency]])[0]
    probability = model.predict_proba([[attendance, consistency]])[0][1]

    recommendation = recommend_class(goal)
    forecast = forecast_weight(weight)

    risk = "High Risk" if prediction == 0 else "Likely to Renew"

    return render_template("result.html",
                           risk=risk,
                           probability=round(probability*100,2),
                           recommendation=recommendation,
                           forecast=forecast)

@app.route("/analytics")
def analytics():
    generate_graph()
    return render_template("analytics.html")

if __name__ == "__main__":
    app.run(debug=True)
