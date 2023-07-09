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

df=json.load(open("bill_19.05.23.json"))

def mapping_func():
    emp_list=[]
    for j in df:
        print(j["No."])
        map_dict=dict()
        map_dict["vendor_name"]=j["Payee"]
        map_dict["date"]=j["Date"]
        map_dict["bill_number"]=j["No."]
        map_dict["due_date"]=j["Due date"]
        map_dict["balance"]=float(j["Balance"].replace(",",""))
        map_dict["sub_total"]=float(j["Total before tax"].replace(",",""))
        map_dict["tax_total"]=float(j["Tax"].replace(",",""))
        map_dict["total"]=float(j["Total"].replace(",",""))
        map_dict["status"]=j["Status"]
        emp_list.append(map_dict)
    with open('bill_zoho.json', 'w') as json_file:
        json.dump(emp_list, json_file,indent=2)


def post_request_zoho():
    
    # code = '1000.aff2d39e4d596cc0d668c3df54ffd43f.98a5bbbc2fcadb956cd988e8fca7d533'
    client_id = '1000.NC4B105IDKLU4H8DOBPLE1UMBZKW1A'
    client_secret = '7945823e0d091eca04d90400bb04900d39ad22aafd'

   
    refresh_token = '1000.e9a3f88cbf6ded32eb521fa7391fdd0f.e1fd392c23c658a01e4e50e443efc8ed'
    access_token = '1000.c9744267126c2a41a318c86db0ebf4db.9aad1f2f079f96c2e2b3f8d83e9b48ed'
    

    organization_id = '60015983411'
    post_url = f'https://books.zoho.in/api/v3/bills?organization_id={organization_id}'

    
    f = open('new.json')
   


    parsed_data2 = json.load(f)
    # items_list = parsed_data2["Bill"]
    items_list = parsed_data2


    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    response_save_file = open("saved_bill_id_test.txt","a")
    error_response_save_file = open("error_console_for_failed_bill.txt","a")


    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")
    # error_response_save_file.write(f"NEW WRITE STARTED: {dt_string}\n")

    for item in items_list:
        original_bill_number = item["bill_number"]
        no_of_times_to_try = 0
        while True:
            print(f'Processing for bill_number: {item["bill_number"]}||{item["date"]}||{item["vendor_id"]}....')
            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(0.5)

            if no_of_times_to_try == 5:
                print(f"Tried 5 times {item['bill_number']} not able to be pushed")
                response_save_file.write(f"Failed to PUSH : {item['bill_number']} -> Tried 5 times not able to be pushed\n")
                response_save_file.flush()
                break

            

            r2 = requests.post(post_url,headers=headers,json=item)

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
                print(access_token)
                response_save_file.write(f"ACCESS TOKEN {access_token} and REFRESH TOKEN {refresh_token}\n")
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
                # response_save_file.write(f'{parsed_data3["invoice"]["invoice_id"]} : {item["invoice_number"]}\n')
                response_save_file.write(f'{parsed_data3["bill"]["bill_id"]} : {item["bill_number"]}\n')

                print(f'{item["bill_number"]} is successfully pushed')
                # It means success
                break
            else:
                print(f'ERROR occurred: {item["bill_number"]}||{item["bill_number"]}||{item["date"]}||{item["vendor_id"]} was not able to be pushed')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                response_save_file.write(f'Failed to PUSH : {item["bill_number"]} -> msg is {parsed_data3["message"]}\n')   
                break
            
            no_of_times_to_try = no_of_times_to_try + 1

        response_save_file.flush()
        # print(f'Successfully created bill named: {item["bill_number"]}||{item["date"]}||{item["vendor_id"]}')
    
    response_save_file.close()

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


mapping_func()
# post_request_zoho()