# Import libraries
import pandas as pd

from sklearn.metrics import mutual_info_score
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

from sklearn.metrics import auc, accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score

import pickle

# Load dataset

df_data = pd.read_csv("./database/data_cleaning.csv", index_col = [0])

# Split to categorical and nummerical columns

catergorical_col = df_data.select_dtypes(include=["object"]).columns.to_list()
nummerical_col = df_data.select_dtypes(exclude=["object"]).columns.to_list()
nummerical_col.remove("loan_status")

# Split dataset

df_train_full, df_test = train_test_split(df_data[catergorical_col+nummerical_col+["loan_status"]], test_size=0.3, random_state=1)

df_train_full = df_train_full.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train_full.loan_status
y_test =df_test.loan_status

# Delete target variable

del df_train_full["loan_status"] # df_train.drop(columns=["churn"], axis=1, inplace=True)
del df_test["loan_status"]
print("Load data")

# Transformation data using DictVectorizer (One hot encoding)

dict_train = df_train_full[catergorical_col+nummerical_col].to_dict(orient="records")
dv = DictVectorizer(sparse=False)

dv.fit(dict_train)
X_train = dv.transform(dict_train)

# Test set
dict_test = df_test[catergorical_col+nummerical_col].to_dict(orient="records")
X_test = dv.transform(dict_test)

# Training model using XGBClassifier

model_xgb_classifier = xgb.XGBClassifier(max_depth=5, random_state=1)
model_xgb_classifier.fit(X_train, y_train)

# Testing model

y_test_pred_prob = model_xgb_classifier.predict_proba(X_test)[:, 1]
y_test_pred = y_test_pred_prob > 0.5

print("AUC score for test set ", roc_auc_score(y_test, y_test_pred_prob))

with open('model.bin', 'wb') as f_out:
    pickle.dump((dv, model_xgb_classifier), f_out)