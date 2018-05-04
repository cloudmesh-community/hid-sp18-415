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

            prediction =lin_reg.predict(engine_size)
        except ValueError:
            return jsonify("Enter a number.")

        return jsonify(lin_reg.predict(hwy_mpg).tolist())




@app.route("/currentDetails", methods=['GET'])
def current_details():
    if request.method == 'GET':
        try:
            lr = lin_reg
            training_set = train_set
            labels = train_labels

            return jsonify({"score": lr.score(training_set, labels),
                            "coefficients": lr.coef_.tolist(), "intercepts": lr.intercept_})
        except (ValueError, TypeError) as e:
            return jsonify("Error when getting details - {}".format(e))

if __name__ == '__main__':
    app.run(debug=True)
