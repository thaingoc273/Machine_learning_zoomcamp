import requests
import pandas as pd

# url = "http://0.0.0.0:2727/predict"
url = "http://loan-predict.eba-bgg3thrh.eu-north-1.elasticbeanstalk.com/predict"

df_test_small = pd.read_csv("./database/test_set.csv", index_col = [0])
df_test_small.reset_index(inplace=True)
index_customer = 12
customer = df_test_small.iloc[index_customer].to_dict()

response = requests.post(url, json=customer).json()
if response["loan_probability"]>=0.5:
    print("Do not allow customer to get a loan")    
else:
    print("Allow customer to get a loan")
print("Probability for loan", response["loan_probability"])
print("Actual loan status of the customer is",df_test_small.loc[index_customer, "loan_status"] )