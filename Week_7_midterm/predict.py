# Predict service
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from flask import Flask
from flask import request
from flask import jsonify

# Load model and transformation from file
app = Flask("loan")

with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    predict = model.predict_proba(X)[0,1]
    churn = predict>=0.5
    result = {
        "loan_probability": float(predict),
        "Default": bool(churn)
    }
    return jsonify(result)

if __name__=="__main__":
    # app.run(debug=True, host="localhost", port=9696)
    app.run(debug=True, host="0.0.0.0", port=2727)