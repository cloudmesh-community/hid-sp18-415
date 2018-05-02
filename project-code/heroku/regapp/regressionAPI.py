from flask import Flask, jsonify, request
import pandas as pd
import os
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            engine_size = int(data["engine_size"])

            lin_reg = joblib.load("./linear_regression_model.pkl")
        except ValueError:
            return jsonify("Please enter a number.")

        return jsonify(lin_reg.predict(hwy_mpg).tolist())




@app.route("/currentDetails", methods=['GET'])
def current_details():
    if request.method == 'GET':
        try:
            lr = joblib.load("./linear_regression_model.pkl")
            training_set = joblib.load("./training_data.pkl")
            labels = joblib.load("./training_labels.pkl")

            return jsonify({"score": lr.score(training_set, labels),
                            "coefficients": lr.coef_.tolist(), "intercepts": lr.intercept_})
        except (ValueError, TypeError) as e:
            return jsonify("Error when getting details - {}".format(e))

if __name__ == '__main__':
    app.run(debug=True)
