import json

# Load the JSON file into a dictionary
with open('../data_from_qb_GeoVale.json', 'r') as f:
    data = json.load(f)
print(data[0]['Line'][0]['AccountBasedExpenseLineDetail']['TaxCodeRef']['value'])

emp=[]
emp2=[]
for i in data:
    if "AccountBasedExpenseLineDetail" in i['Line'][0]:
        if "TaxCodeRef" in i['Line'][0]["AccountBasedExpenseLineDetail"]:
            if i['Line'][0]['AccountBasedExpenseLineDetail']['TaxCodeRef']['value'] in ["15","28","4","5","14","11","10"]:
                emp.append(i)
        else:
            emp2.append(i)
    else:
        emp2.append(i)
# emp3=emp+emp2
# with open('bill_geovale_EXCLUDED.json', 'w') as json_file:
#     json.dump(emp, json_file,indent=4)