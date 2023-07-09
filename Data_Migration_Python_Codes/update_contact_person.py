import base64
import re
import json
from time import sleep
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime

def mapping_func():
    zoho_vndr=json.load(open("data_from_zoho_contacts_PR.json"))
    qb_vndr=json.load(open("qb_cstmr_PR.json"))

    email=[]
    phone=[]
    ds_nm=[]
    for j in qb_vndr:
        ds_nm.append(j["DisplayName"])
        if "PrimaryPhone" in j:
            phone.append(j["PrimaryPhone"]["FreeFormNumber"])
        elif "Mobile" in j:
            phone.append(j["Mobile"]["FreeFormNumber"])
        else:
            phone.append("")
        if "PrimaryEmailAddr" in j:
            email.append(j["PrimaryEmailAddr"]["Address"])
        else:
            email.append("")


    emp_list=[]
    map_dict=dict()
    for i in zoho_vndr:
        map_dict=dict()
        if i["contact_type"]=="customer":
            map_dict["contact_id"]=i["contact_id"]
            # map_dict["email"]=email[ds_nm.index(i["contact_name"])]
            map_dict["phone"]=phone[ds_nm.index(i["contact_name"])]
            emp_list.append(map_dict)

    with open('updt_cntct.json', 'w') as json_file:
        json.dump(emp_list, json_file,indent=2)

def json_fltr():
    with open('updt_cntct.json', 'r') as f:
        data = json.load(f)

    emp=[]
    for i in data:
        if i["email"] != "" or  i["phone"] != "" :
            emp.append(i)

    with open('updt_cntct2.json', 'w') as json_file:
            json.dump(emp, json_file,indent=2)

def post_request_zoho():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # ZohoBooks.fullaccess.all
    # code = '1000.2a73bbf05f7b47923757d07be1c8d7f1.f04c26f733bbfa8b31c584bbcdb6a38d'
    code = '1000.82c4bb14fe45c59073cb822e5f030e74.fa0de5340c040aefb4459d367756e126'
    client_id = '1000.HG016JCEMYJ8HY9CGRIRWGO7L3J6AD'
    client_secret = 'c3942592d7792a7c533d58cc1e9ae4a7726ed0af3e'

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
    
    access_token = '1000.66226189e94099c412e618db0f7e1341.897e1997dfc7a43b503a16f7a29d3114'
    refresh_token = '1000.ca87a1d3fa1c8a238af21b3f91187d3c.a61535b1f980dd5001d2e364ca99e5e4'
    # expires_in = parsed_data["expires_in"]

    organization_id = '60019790139'
    post_url = f'https://www.zohoapis.in/books/v3/contacts/contactpersons?organization_id={organization_id}'

    f = open('updt_cntct2.json')
    parsed_data2 = json.load(f)
    items_list = parsed_data2

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_contact_id_cstmr_pr.txt","a")

    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")

    for item in items_list:
        while True:
            print(f'Processing for name: {item["contact_id"]}....')
            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(2)

            # param = dict()
            # param['JSONString'] = item
            # r2 = requests.post(post_url,headers=headers,data=param)

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
                response_save_file.write(f'{item["contact_id"]}\n')
                print(f'{item["contact_id"]} is successfully pushed')
                # It means success
                break
            else:
                print(f'ERROR occurred: {item["contact_id"]} was able to be pushed')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
            

        print(f'Successfully updated item named: {item["contact_id"]}')


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
# json_fltr()
post_request_zoho()

