import base64
import ujson
import pandas
import numpy as np
import re
import io
import json
from time import sleep
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime

df=json.load(open("metasphere_item.json"))
df2=json.load(open("Item (9).json"))
# df["Item"]=df["Item"].strip()

item_id=[]
item_name=[]
rate=[]
for i in df2:
    item_id.append(i["Item ID"])
    item_name.append(i["Item Name"])
    rate.append(i["Rate"])

def mapping_func():
    emp_list=[]
    skip_list=[]
    for j in df:
        print(j["Item"])
        map_dict=dict()
        if j["Item"].strip() in item_name:
            map_dict["item_id"]=item_id[item_name.index(j["Item"].strip())]
            map_dict["rate"]=float(rate[item_name.index(j["Item"].strip())])
            map_dict["initial_stock"]=float(j["Qty"].replace(",", ""))
            map_dict["initial_stock_rate"]=float(j["Calc. Avg"])
            emp_list.append(map_dict)
        else:
            skip_list.append(j)
    print(len(skip_list))

    with open('updt_item.json', 'w') as json_file:
        json.dump(emp_list, json_file,indent=2)

def post_request_zoho():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # ZohoBooks.fullaccess.all
    # code = '1000.2a73bbf05f7b47923757d07be1c8d7f1.f04c26f733bbfa8b31c584bbcdb6a38d'
    code = '1000.7b77697d5f121a99a49ae6d48c6e515a.e4064c953ec039be2854cc4a7fc2a05f'
    client_id = '1000.WJH87XFBMWZ4SAS0PUV5J5QVLECVJU'
    client_secret = '9a7fe0e1bcb8afece29b18de5d8a7e350e4172f496'

    # gettokenurl = f'https://accounts.zoho.in/oauth/v2/token?code={code}&client_id={client_id}&client_secret={client_secret}&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code'
    # r1 = requests.post(gettokenurl)
    # """
    #     {
    #         "access_token": "1000.cb73ac8e8e7a97e9a477b2771fdfa546.be088fe17b6386a80add9441e1ac0cc9",
    #         "refresh_token": "1000.b3bcfcb05de766156aa2966732c07f58.c471e437e710a57b63fb6e6ba99dc6a5",
    #         "api_domain": "https://www.zohoapis.in",
    #         "token_type": "Bearer",
    #         "expires_in": 3600
    #     }

    #     OR

    #     {
    #         "error": "invalid_code"
    #     }
    # """
    # parsed_data1 = r1.json()
    # if 'error' in parsed_data1:
    #     # print(parsed_data1)
    #     print('code is expired [invalid code]')
    #     exit()
    
    access_token = '1000.0c5c46db52d231e64f075f2a5e97573d.c5e0db572885605211c355d050e50b86'
    refresh_token = '1000.63e9a784dc385bba7acdb96672e1a47e.3c78d4b00f9bded1b1dd64835826c775'
    # expires_in = parsed_data["expires_in"]

    organization_id = '60018527815'
    
    f = open('new.json')
    parsed_data2 = json.load(f)
    items_list = parsed_data2

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_item_id_test.txt","a")

    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")
    rmv_array = np.array([])
    
    for item in items_list:
        post_url = f'https://www.zohoapis.in/books/v3/items/{item["item_id"]}?organization_id={organization_id}'
        while True:
            print(f'Processing for name: {item["item_id"]}....')
            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(2)

            # param = dict()
            # param['JSONString'] = item
            # r2 = requests.post(post_url,headers=headers,data=param)

            r2 = requests.put(post_url,headers=headers,json=item)

            parsed_data3 = r2.json()
            # print(parsed_data3)
            if parsed_data3["code"] == 57:
                # access_token expired
                """
                    {
                        "code": 57,
                        "message": "You are not authorized to perform this operation"
                    }
                """
                print("access_token_expired...")
                access_token = get_new_access_token_zoho(refresh_token,client_id,client_secret)
            elif parsed_data3["code"] == 0:
                """
                {
                    "code": 0,
                    "message": "The contact has been created",
                    "contact": {
                        "contact_id": 460000000026049,
                        "contact_name": "Bowman and Co",
                        "company_name": "Bowman and Co",
                        "has_transaction": true,
                        "contact_type": "customer",
                        "customer_sub_type": "business",
                        "credit_limit": 1000,
                        "is_portal_enabled": true,
                        ....
                    }
                """
                # response_save_dict[f'{parsed_data3["contact"]["contact_id"]}'] = item["name"]
                response_save_file.write(f'{item["item_id"]}\n')
                print(f'{item["item_id"]} is successfully pushed')
                
                
                # rmv_array.append(item["item_id"])
                rmv_array = np.append(rmv_array,item["item_id"])
                new_dic=np.array([])
                for dic in items_list:
                    if dic["item_id"] not in rmv_array:
                        # new_dic.append(dic)
                        new_dic = np.append(new_dic,dic)
                with open('new.json', 'w',buffering=1024*1024) as f:
                    ujson.dump(new_dic.tolist(), f,indent=2)
                    f.flush()
                # It means success
                break
                
            else:
                response_save_file.write(f'ERROR occurred: {item["item_id"]} was not able to be pushed\n')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                break

        print(f'Successfully updated item named: {item["item_id"]}')
   

def get_new_access_token_zoho(refresh_token,client_id,client_secret):
    get_access_token_url = f'https://accounts.zoho.in/oauth/v2/token?refresh_token={refresh_token}&client_id={client_id}&client_secret={client_secret}&redirect_uri=http://www.zoho.in/books&grant_type=refresh_token'

    """
        {
            "access_token": "1000.196f02969066b34cb048e0692fdad334.56e78b97611d29e92dd129b87248ec72",
            "api_domain": "https://www.zohoapis.in",
            "token_type": "Bearer",
            "expires_in": 3600
        }
    """
    sleep(2)

    r = requests.post(get_access_token_url)
    parsed_json = r.json()

    if 'error' in parsed_json:
        print('refresh_token is expired')
        exit()
    
    access_token = parsed_json["access_token"]

    return access_token

# mapping_func()
post_request_zoho()