3# Realm ID : 4620816365221051280
# Refresh Token : AB11669005834yy7f3vM3AbtxyhN0GPpZohd2ppGf5h2MDb9XV expires in 101 days
# Access Token : eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..0p2dc3enERLQynKRXAPjMg.BmeLQQaZhlwL4DhQCS6iC25NFi3NU3AA3BfatKvrNq0iXBMzXEXufpRcfS9iPY8yqNLRCAu_BW7O5NaqADZEXcO1aNtK26HYcOTXAI9asgOw2Lp5leUhudtBzKb6y3wF8Buzq5UaM1BNX12dn4Mk0HijqQ3Lo4lPLc5MM_8MOr4-4uOWFdiQizGknNUgGqiqcqjvVpWZCp8i5xcOW_bf7O0EKJpQx6Wf5surj01X1f6tWX9NKftq_LQ58LfD_fB9uVirB9zdOkmcCCJ4aokBSMV47pWhB8R81QCBLFYd35RQObeU5hkIB21_nYc09covmy4P4bPA61OON6nH9hV2ofVT_FguRiuVhiuIb3Ubakl3FiSlnKuenw5Xd73GAAQRHm4kM_IlVQoc2Zun1UdSUE36fJnzx1LCCBmtZ04tDr0E6qghSfYlCECoX90MuD6qPc_EtGmkoS2b_wkIwSCeZQ3PTI4dS9Mhq878NeUo7Joek_gCmsKc0_3UbTZqaPef0kK8yEFCGCutTCBm6cuGwGa8kyQnLQyFGEulzIm7oULn0hEi8UHPBR92-lKo1Gmsq9EzYnGdkQ3img5kf6cOgE01Bqlb2Ek4VwPjaOYgtUBGg8SCwfEZdEjQRaMx3y7A9k7oEIUO8SmVWtKtvH3m3CzqNzn9PMv5zXNi1xSWaMFSbJU8RlD3i9B8Y-i1KqvXz9UNjHlR3uFvEvs7W2Y9K90S5dkW61OVptOT-rncxmuJgGNIF9wj1zcpgQsMdXp3.VOLnrFPCYY0T2xxdUl97Rw
# expires in 60 minutes

import base64
import re
import json
import ujson
from time import sleep
import numpy as np
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime


# 'code' variable must be updated before running this function
def post_request_zoho():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # output_file_name = 'console_output_2013_to_2017.txt'
    # output_file_name_fout = open(output_file_name)

    # ZohoBooks.fullaccess.all
    # code = '1000.3f2187fa12c1465d48fab99ab199f937.619ab209c92d1634e7764f1c5b6ce6e7'
    # client_id = '1000.UR9FCNRIBAJ11TLABY8K4C0UAW14BP'
    # client_secret = 'e72b1a3f32e16117b3287974149f066ed1f13f0822'

    # code = '1000.8febd73abf4b66797f7566c9b6bc5790.bc413cd0ff3df75c5242aa4a71dfcc33'

    client_id = '1000.L0Q7IOSHEDDA2OT1ERZXS8Q562LPYF'
    client_secret = '42332f5e29beb92cbc9cd14ab1519b2db67e6255d1'

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
    

    response_save_file = open("saved_invoice_2019_Payment_Refund.txt","a")
    

    # refresh_token = parsed_data1["refresh_token"]
    # access_token = parsed_data1["access_token"]
    refresh_token = '1000.ce01a0f6b2c276a6c41ab3d3dfaf2799.f564dceb6f78aa6d2a03cea951d0c7b7'
    access_token = '1000.101bdde0c5606e2e14c3cc6bfcc058c2.4a61b6c995e4bd514f0de10facd23b8a'
    # expires_in = parsed_data["expires_in"]

    # print(refresh_token) 
    # print(access_token)

    response_save_file.write(f"ACCESS TOKEN {access_token} and REFRESH TOKEN {refresh_token}\n")

    organization_id = '60024317687'
    post_url = f'https://books.zoho.in/api/v3/invoices?ignore_auto_number_generation=true&organization_id={organization_id}'

    # f = open('mapped.json')
    # f = open('mapped1.json')
    # f = open('failed_mapped1.json')
    # f = open('failed_invoices.json')
    # f = open('failed_invoices1.json')
    f = open('mapped_inv_2019_D_C_note.json')



    parsed_data2 = json.load(f)
    # items_list = parsed_data2["Invoice"]
    items_list = parsed_data2


    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    # response_save_file = open("saved_invoice_id.txt","a")
    error_response_save_file = open("error_console_for_failed_invoice.txt","a")


    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")
    # error_response_save_file.write(f"NEW WRITE STARTED: {dt_string}\n")
    rmv_list= []
    rmv_array = np.array([])
    for item in items_list:
        # original_invoice_number = item["invoice_number"]
        no_of_times_to_try = 0
        # if "customer_id" not in item.keys():
        #     continue
        # print(item["invoice_number"])
        while True:
            print(f'Processing for invoice_number: {item["id_from_qb"]}||{item["date"]}||{item["customer_id"]}....')
            
            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(0.5)

            if no_of_times_to_try == 5:
                print(f"Tried 5 times {item['id_from_qb']} not able to be pushed")
                response_save_file.write(f"Failed to PUSH : {item['id_from_qb']} -> Tried 5 times not able to be pushed\n")
                response_save_file.flush()
                break
    

            # param = dict()
            # param['JSONString'] = item
            # r2 = requests.post(post_url,headers=headers,data=param)

            id_from_qb = item["id_from_qb"]

            # if "id_from_qb" in item:
            #     del item["id_from_qb"]

            r2 = requests.post(post_url,headers=headers,json=item)

            parsed_data3 = r2.json()

            # For blank Invoice Number the code returned is 4018
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
                response_save_file.write(f'{parsed_data3["invoice"]["invoice_id"]} : {id_from_qb}\n')

                print(f'{id_from_qb} is successfully pushed')
                response_save_file.flush()

                # rmv_list.append(id_from_qb)
                # new_dic=[]
                # for dic in items_list:
                #     if dic["id_from_qb"] not in rmv_list:
                #         new_dic.append(dic)
                # with open('out_jan_4.json', 'w') as f:
                #     json.dump(new_dic, f,indent=4)
                #     f.flush()

                rmv_array = np.append(rmv_array,item["id_from_qb"])
                new_dic=np.array([])
                for dic in items_list:
                    if dic["id_from_qb"] not in rmv_array:
                        # new_dic.append(dic)
                        new_dic = np.append(new_dic,dic)
                with open('invoice_data.json', 'w',buffering=1024*1024) as f:
                    ujson.dump(new_dic.tolist(), f,indent=2)
                    f.flush()

                # It means success
                break
            # elif parsed_data3["code"] == 1001:
            #     """
            #     {
            #         "code": 1001,
            #         "message": "Invoice 2/BF02serv/2013-14 already exists"
            #     }
            #     """
            #     old_invoice_number = item["invoice_number"]
            #     new_invoice_number = for_duplicate_invoice_number(item["customer_id"],old_invoice_number)
            #     if not new_invoice_number:
            #         # if new_invoice_number is EMPTY STRING
            #         response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]} ## INVOICE_NUMBER {old_invoice_number} to NULL String returned\n')
            #         break

            #     item["invoice_number"] = new_invoice_number
            #     response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]} ## INVOICE_NUMBER {old_invoice_number} to {item["invoice_number"]}\n')
            #     response_save_file.flush()

            # elif parsed_data3["code"] == 71530:
            #     # Please ensure that the Invoice number does not exceed 16 characters. It can contain alphabets, numerals, hyphens(-), and/or slash(/).
                
            #     old_invoice_number = item["invoice_number"]
            #     # old_invoice_number = old_invoice_number.replace('-','')
            #     old_invoice_number = old_invoice_number.replace(' ','')
            #     if len(old_invoice_number) > 16:
            #         new_invoice_number = new_invoice_number_gen(item["customer_id"],original_invoice_number)
            #         new_invoice_number = new_invoice_number.replace('.','')
            #         item["invoice_number"] = new_invoice_number
            #     else:
            #         # Remove all the . from the string
            #         item["invoice_number"] = old_invoice_number.replace('.','')
            #         item["invoice_number"] = old_invoice_number.replace('_','')
            #         # item["invoice_number"] = old_invoice_number.replace('-','')
                
            #     response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]} ## INVOICE_NUMBER {old_invoice_number} to {item["invoice_number"]}\n')
            #     response_save_file.flush()

            else:
                print(f'ERROR occurred: {id_from_qb}||{item["id_from_qb"]}||{item["date"]}||{item["customer_id"]} was not able to be pushed')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]}\n')
                response_save_file.flush()
                break
        
            # print(f"no_of_times_to_try: {no_of_times_to_try}")
            no_of_times_to_try = no_of_times_to_try + 1

        # response_save_file.flush()
        # print(f'Successfully created invoice named: {item["invoice_number"]}||{item["date"]}||{item["customer_id"]}')
    
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
    sleep(1)

    r = requests.post(get_access_token_url)
    parsed_json = r.json()

    if 'error' in parsed_json:
        print('refresh_token is expired')
        exit()
    
    access_token = parsed_json["access_token"]

    return access_token

# 'code' variable must be updated before running this function

        # print(f'Successfully created invoice named: {item["invoice_number"]}||{item["date"]}||{item["customer_id"]}')


# get_items_and_write_to_file()
# generate_post_json()
post_request_zoho()
# post_invoice_as_sent()




        

