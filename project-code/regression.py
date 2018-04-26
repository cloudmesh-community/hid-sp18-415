import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.externals import joblib
import requests

df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vS37MqRL0SL1twLDjX5vFw-WqICPgBW0ev_4KMR2kzzcMAWkKNQo_wnbr_QqcXXuFgBXX8K-Amogx-9/pub?output=csv")

train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
df_copy = train_set.copy()

train_set_full = train_set.copy()

train_set = train_set.drop(["hwy_mpg"], axis=1)

train_labels = df_copy["hwy_mpg"]

# creating model with training data
train_set_full = train_set.copy()
train_set = train_set.drop(["hwy_mpg"], axis=1)
lin_reg = LinearRegression()

lin_reg.fit(train_set, train_labels)

hwy_mpg_pred = lin_reg.predict(test-labels)

hwy_mpg_pred

BASE_URL = "http://localhost:5000"

joblib.dump(lin_reg, "linear_regression_model.pkl")

joblib.dump(train_set, "training_data.pkl")
joblib.dump(train_labels, "training_labels.pkl")

#predict API
eng_size = {"engine_size': 8}
response = requests.post("{}/predict".format(BASE_URL), json = eng_size)

response.json()

# current details API

response = requests.get("{}/currentDetails".format(BASE_URL))

response.json()
