# Predict service
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from flask import Flask
from flask import request
from flask import jsonify

# Load model and transformation from file
app = Flask("churn")

with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

customer = {
  'gender': 'male',
  'seniorcitizen': 3,
  'partner': 'no',
  'dependents': 'no',
  'tenure': 10,
  'phoneservice': 'no',
  'multiplelines': 'no',
  'internetservice': 'dsl',
  'onlinesecurity': 'yes',
  'onlinebackup': 'no',
  'deviceprotection': 'yes',
  'techsupport': 'yes',
  'streamingtv': 'yes',
  'streamingmovies': 'yes',
  'contract': 'one_year',
  'paperlessbilling': 'yes',
  'paymentmethod': 'bank_transfer_(automatic)',
  'monthlycharges': 10.85,
  'totalcharges': 200.75
}
@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    predict = model.predict_proba(X)[0,1]
    churn = predict>=0.5
    result = {
        "churn_probability": float(predict),
        "churn": bool(churn)
    }
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=9696)