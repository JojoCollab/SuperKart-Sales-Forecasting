
from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("superkart_model.joblib")


@app.route("/")
def home():
    return "SuperKart Sales Prediction API is running."


@app.route("/v1/predict", methods=["POST"])
def predict():
    data = request.get_json()

    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)

    return jsonify({
        "prediction": float(prediction[0])
    })


@app.route("/v1/predictbatch", methods=["POST"])
def predict_batch():
    file = request.files["file"]

    data = pd.read_csv(file)
    predictions = model.predict(data)

    data["Predicted_Sales"] = predictions

    return data.to_json(orient="records")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
