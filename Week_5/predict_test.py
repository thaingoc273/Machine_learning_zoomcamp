import requests

url = "http://localhost:9696/predict"
customer = {
  'gender': 'female',
  'seniorcitizen': 1,
  'partner': 'no',
  'dependents': 'no',
  'tenure': 0,
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
response = requests.post(url, json=customer).json()
if response["churn_probability"]>=0.5:
    print("Sending email to customer")    
else:
    print("Do not sending email")
print("Probability churn", response["churn_probability"])