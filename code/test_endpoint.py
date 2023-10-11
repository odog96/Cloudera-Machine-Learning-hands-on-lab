import json, requests

x={"StreamingTV":"No","MonthlyCharges":70.35,"PhoneService":"No","PaperlessBilling":"No","Partner":"No","OnlineBackup":"No","gender":"Female","Contract":"Month-to-month","TotalCharges":1397.475,"StreamingMovies":"No","DeviceProtection":"No","PaymentMethod":"Bank transfer (automatic)","tenure":29,"Dependents":"No","OnlineSecurity":"No","MultipleLines":"No","InternetService":"DSL","SeniorCitizen":"No","TechSupport":"No"}
new_x = {"columns": ["gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges"], "data": [["Male", "No", "Yes", "No", 14, "Yes", "No", "DSL", "No", "No", "No", "Yes", "No", "No", "Month-to-month", "No", "Bank transfer (automatic)", 48.8, 664.4], ["Male", "No", "Yes", "No", 31, "Yes", "Yes", "Fiber optic", "Yes", "Yes", "No", "Yes", "No", "No", "Month-to-month", "Yes", "Credit card (automatic)", 90.55, 2929.75], ["Male", "No", "Yes", "Yes", 47, "Yes", "Yes", "Fiber optic", "No", "No", "Yes", "Yes", "Yes", "Yes", "Month-to-month", "Yes", "Bank transfer (automatic)", 107.35, 5118.95], ["Male", "No", "Yes", "Yes", 35, "Yes", "Yes", "DSL", "No", "No", "No", "Yes", "Yes", "Yes", "One year", "Yes", "Bank transfer (automatic)", 73.45, 2661.1], 
["Female", "No", "Yes", "No", 66, "Yes", "Yes", "Fiber optic", "Yes", "Yes", "No", "Yes", "No", "No", "One year", "No", "Electronic check", 89.0, 5898.6]]}



# parameters specificto traditionally deployed model
model_url = 'https://modelservice.ml-b74f8940-b97.go01-dem.ylcu-atmi.cloudera.site/model'
model_key = "muomi5e1r7ildyqinj9q5ep8kg5mzq7h"

########################
# test old format input 
########################

# build embedded dictionary step 1
request_dict = {"request":x}

# access key will be end point specific
BackDict = {"accessKey":model_key}
BackDict.update(request_dict)
request_dict=BackDict


r1 = requests.post(model_url, data=json.dumps(request_dict), headers={'Content-Type': 'application/json'})

r1.json()

########################
# test new format input 
########################


# build embedded dictionary step 1
request_dict = {"request":new_x}

# access key will be end point specific
BackDict = {"accessKey":model_key}
BackDict.update(request_dict)
request_dict=BackDict


r2 = requests.post(model_url, data=json.dumps(request_dict), headers={'Content-Type': 'application/json'})

r2.json()