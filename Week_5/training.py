#!/usr/bin/env python
# coding: utf-8

# # Homework week 4

import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


from sklearn.metrics import auc
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer


from sklearn.model_selection import KFold
import pickle

df_car = pd.read_csv("../database/churn.csv")





## Data preprocessing
df_car.columns = df_car.columns.str.lower().str.replace(" ", "_")
categorical_col = list(df_car.select_dtypes(include=["object"]))
numerical_col = list(df_car.select_dtypes(exclude=["object"]))

# totalcharges column need to be nummerical
df_car["totalcharges"] = pd.to_numeric(df_car["totalcharges"], errors="coerce")
df_car.totalcharges.fillna(0, inplace=True)

categorical_col.remove("totalcharges")

numerical_col.append("totalcharges")

for col in categorical_col:
    df_car[col] = df_car[col].str.lower().str.replace(" ", "_")

# Convert churn column to True and False
df_car.churn = df_car.churn.apply(lambda x: True if x == "yes" else False)

# Split dataset
df_train_full, df_test = train_test_split(df_car, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_train_full, test_size=0.25, random_state=1)
y_train_full = df_train_full.churn

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.churn
y_val = df_val.churn
y_test =df_test.churn


del df_train["churn"] # df_train.drop(columns=["churn"], axis=1, inplace=True)
del df_val["churn"]
del df_test["churn"]

categorical_col.remove("churn")
categorical_col.remove("customerid")

# ## Training the model
dict_train = df_train[categorical_col+numerical_col].to_dict(orient="records")
dv = DictVectorizer()

dv.fit(dict_train)
X_train = dv.transform(dict_train)

model = LogisticRegression(solver='liblinear', C = 1, max_iter=1000)
model.fit(X_train, y_train)

# Saving model with pickle
with open('model.bin', 'wb') as f_out:
    pickle.dump((dv, model), f_out)