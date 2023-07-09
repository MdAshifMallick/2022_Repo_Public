import json

def js_r(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)

if __name__ == "__main__":
    my_data = js_r('pinnacle customer ob.json')
    my_data2=js_r("branch_id_pinnacle.json")
    my_data3=js_r("contact_details_pinacle.json")

emp_list=[]
emp_list2=[]
for data in my_data:
    mapping_dict=dict()
    mapping_dict["contact_name"]=data["NAME"]
    mapping_dict["opening_balance_amount"]=data["OPENING BALANCE"]
    if data["NAME"] in my_data3.keys():
        mapping_dict["for_my_use"]=my_data3[data["NAME"]]
    else:
        emp_list2.append(data["NAME"])
    if data["BRANCH"] in my_data2.keys():
        mapping_dict["branch_id"]=my_data2[data["BRANCH"]]
    else:
        print(data["BRANCH"])
    emp_list.append(mapping_dict)

print(len(emp_list2))

with open('pinnacle_ob3.json', 'w') as json_file:
    json.dump(emp_list, json_file,indent=4)

