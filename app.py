from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

model = joblib.load("model.joblib")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        final = np.array([data])

        prediction = model.predict(final)

        return render_template(
            "index.html",
            prediction_text=f"Predicted Severity: {prediction[0]}"
        )
    except:
        return render_template(
            "index.html",
            prediction_text="Invalid Input"
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)