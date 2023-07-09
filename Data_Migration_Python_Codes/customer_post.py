# Realm ID : 4620816365221051280
# Refresh Token : AB11669005834yy7f3vM3AbtxyhN0GPpZohd2ppGf5h2MDb9XV expires in 101 days
# Access Token : eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..0p2dc3enERLQynKRXAPjMg.BmeLQQaZhlwL4DhQCS6iC25NFi3NU3AA3BfatKvrNq0iXBMzXEXufpRcfS9iPY8yqNLRCAu_BW7O5NaqADZEXcO1aNtK26HYcOTXAI9asgOw2Lp5leUhudtBzKb6y3wF8Buzq5UaM1BNX12dn4Mk0HijqQ3Lo4lPLc5MM_8MOr4-4uOWFdiQizGknNUgGqiqcqjvVpWZCp8i5xcOW_bf7O0EKJpQx6Wf5surj01X1f6tWX9NKftq_LQ58LfD_fB9uVirB9zdOkmcCCJ4aokBSMV47pWhB8R81QCBLFYd35RQObeU5hkIB21_nYc09covmy4P4bPA61OON6nH9hV2ofVT_FguRiuVhiuIb3Ubakl3FiSlnKuenw5Xd73GAAQRHm4kM_IlVQoc2Zun1UdSUE36fJnzx1LCCBmtZ04tDr0E6qghSfYlCECoX90MuD6qPc_EtGmkoS2b_wkIwSCeZQ3PTI4dS9Mhq878NeUo7Joek_gCmsKc0_3UbTZqaPef0kK8yEFCGCutTCBm6cuGwGa8kyQnLQyFGEulzIm7oULn0hEi8UHPBR92-lKo1Gmsq9EzYnGdkQ3img5kf6cOgE01Bqlb2Ek4VwPjaOYgtUBGg8SCwfEZdEjQRaMx3y7A9k7oEIUO8SmVWtKtvH3m3CzqNzn9PMv5zXNi1xSWaMFSbJU8RlD3i9B8Y-i1KqvXz9UNjHlR3uFvEvs7W2Y9K90S5dkW61OVptOT-rncxmuJgGNIF9wj1zcpgQsMdXp3.VOLnrFPCYY0T2xxdUl97Rw
# expires in 60 minutes

import base64
import re
import json
from time import sleep
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime

# 'access_token' variable must be updated before running this function
def get_items_and_write_to_file():
    # Sandbox URL
    sandboxURL = 'https://sandbox-quickbooks.api.intuit.com'
    productionURL = 'https://quickbooks.api.intuit.com'
    auth_URL = 'https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer'

    # These must be changed
    refresh_token = 'AB11684481329AReVNMWH795OGbIRyxh8PcfwsL9tn4dYG6hrq'
    access_token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..ywv2CS6eaXNBScL7AMyUug.U3sYkR_G8lvWYPR28EPrl21410DHVTFMqvk0KwMuNwTKrUmvQX7TZWrRS6f3Fjb9Lzz-4-hbTUsHTgiKRwEnjasvWPYLUSftWk3fChvzmwn-43A-2AkS42R7w269V1Ti73hWm4LyDaBq2SIlnvGdr3Z9huMmFn69rF8eYJDG9fs_5vJZAlxzq1TkVZsrlNGaHjdcpDlemgx5WAiE2Jn6KP-a6VWUB757nOk-Z72JT7XsOlgS0Kc-WD6vLWFYPuX7kgcx-dzBoGiyUOdQNBhJZTLgx_DhoRc58CKPGaxOKkURUHYu7kLMyo9AtC-HGXGS0kGlHaQWqY9VdYMDNMT8prbd_KYM03cKyWEFQA0nEtDKhqNWesrlSm6m7n6m1VHYaoBtCpT12QhIA1yU71mLDiyawV4QkEBnBPrn5MfXLvPtY_hJNFxICtEF_y9XvJEpPBsWF1SUK3kN15WimoEtIWL_Hfr4-iyoF-IOhGaZZDdnXSrS_QbhSxwJOBoGZo6imm5s6rjM94Ku5HRNJVC3F4veahaKeaTpIS76h5-6UYAvFnfja1MNjGvGW7zAwjgkylkKtGfDevZXHwFo7rpU2M7MH1ci7S6hc2dX3ekB2zOI7T54REgfWEchqDDo5JZ6d0-6jmsVBERabbn5ZC_Du4Lz1bb_EQNyxvLzKLa2mXmKxfGy5nmXqSqtq9qEXWY2iekca0qM0HE5WiaWD_PUJetu724g5l3oasyTMmYFxw0.gq_T9gGrWy3sIuPtYF-tYg'
    realmID = '123146076026514'

    client_id = 'ABX6LIzIgdo7Qd5bjOuF4FBPY8h9p56N0T3h472BkANYnHjFnY'
    client_secret = 'hv4lHtjgqs7APsJJEhlaeky0488TjYXDeTioWfFw'

    # Authorization: Basic {base64encode(client_id:client_secret)}
    sample_string = f"{client_id}:{client_secret}"
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    # auth_headers is used for getting access_token using refresh_token
    auth_headers = CaseInsensitiveDict()
    auth_headers["Content-Type"] = "application/x-www-form-urlencoded"
    auth_headers["Accept"] = "application/json"
    auth_headers["Authorization"] = f"Basic {base64_string}"
    payload = f'grant_type=refresh_token&refresh_token={refresh_token}'

    # headers is used for GET
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    file_name = 'data_from_qb_inactive_5D.json'
    fp = open(file_name,'a')
    startPosition = 1
    no_of_objects_fetched = 0
    flag = True
    while flag == True:
        selectQuery = f'select * from Customer where Active=False startPosition {startPosition}'
        sandbox_getURL = f"{sandboxURL}/v3/company/{realmID}/query?query={selectQuery}&minorversion=65"
        production_getURL = f"{productionURL}/v3/company/{realmID}/query?query={selectQuery}&minorversion=65"
        headers["Authorization"] = f"Bearer {access_token}"
        r = requests.get(production_getURL,headers=headers)

        # print(r.status_code)
        if r.status_code == 200:
            parsed_data = r.json()

            if "QueryResponse" in parsed_data:
                if "Customer" in parsed_data["QueryResponse"]:
                    for element in parsed_data["QueryResponse"]["Customer"]:
                        indented_data = json.dumps(element,indent=4)
                        fp.write(indented_data)
                        fp.write('\n,\n')

                    maxResults = parsed_data["QueryResponse"]["maxResults"]
                    print(f"Fetched {maxResults} Objects")
                    no_of_objects_fetched += maxResults
                    startPosition = no_of_objects_fetched + 1
                else:
                    print(f"Finished...Total fetched {no_of_objects_fetched}")
                    flag = False
            else:
                # {"error":"invalid_client"}
                auth_response = requests.post(auth_URL,data=payload,headers=auth_headers)

                if "error" in auth_response:
                    """"
                    {
                        "error_description": "Incorrect or invalid refresh token",
                        "error": "invalid_grant"
                    }
                    """
                    print(f"SomeError occurred at getting new access_token after fetching {no_of_objects_fetched} objects... dumping in error.json")
                    autherrorfp = open('autherror.json','w')
                    autherror_parsed = json.dumps(auth_response.json(),indent=4)
                    autherrorfp.write(autherror_parsed)
                    exit()
                else:
                    """{"access_token":"..","token_type":"bearer","x_refresh_token_expires_in":8725268,"refresh_token":"...","expires_in":3600}"""
                    parsed_auth_response = auth_response.json()
                    access_token = parsed_auth_response["access_token"]
        else:
            print(f"SomeError occurred after fetching {no_of_objects_fetched} objects... dumping in error.json")
            errorfp = open('error.json','w')
            r_parsed = json.dumps(r.json(),indent=4)
            errorfp.write(r_parsed)
            exit()

        # if "fault" in parsed_json_object:
        #     file_name = 'error.json'
        #     print("Token might be Expired....dumping in error.json")
        #     exit()
        # else:
        #     file_name = 'all_fetched_data_from_qb.json'
        #     print("Okay...data is dumped in all_fetched_data_from_qb.json")
        
        # indented_json_object = json.dumps(r.json(),indent=4)

        # with open(file_name, "w") as outfile:
        #     outfile.write(indented_json_object)

def extract_sub_string1(whole_string,string_to_extract):
    length_of_string = len(string_to_extract)
    idx = whole_string.find(string_to_extract)
    left_part_of_string = whole_string[:idx]
    right_part_of_string = whole_string[idx+length_of_string:]

    return left_part_of_string + right_part_of_string

def extract_sub_string2(whole_string,idx,length_of_string):
    left_part_of_string = whole_string[:idx]
    right_part_of_string = whole_string[idx+length_of_string:]

    return left_part_of_string + right_part_of_string

def get_state_string(whole_string):
    states_list = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu And Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman And Nicobar Islands','Chandigarh','Dadra And Nagar Haveli','Daman And Diu','Delhi','Lakshadweep','Puducherry']
    lowercase_address_string = whole_string.lower()

    length_of_list = len(states_list)
    for i in range(length_of_list):
        if states_list[i].lower() in lowercase_address_string:
            state = states_list[i]
            idx = lowercase_address_string.find(state.lower())
            length_of_state = len(state)
            new_whole_string = extract_sub_string2(whole_string,idx,length_of_state)

            return [new_whole_string,state]

def check_for_mr_ms(whole_string):
    if whole_string.find("Mr.") != -1:
        return True
    elif whole_string.find("Ms.") != -1:
        return True
    else:
        False


def mapping_func(customer_from_qb):
    # Term -> "payment_terms_label"
    term_dict = dict()
    term_dict["5"] = "50% Advance Payment"
    term_dict["1"] = "Due on receipt"
    term_dict["2"] = "Net 15"
    term_dict["3"] = "Net 30"
    term_dict["4"] = "Net 60"



    # Curreny -> "currency_id"
    currency_dict = dict()
    currency_dict["AED"] = "1208528000000015219"
    currency_dict["AUD"] = "1208528000000000073"
    currency_dict["CAD"] = "1208528000000000067"
    currency_dict["CNY"] = "1208528000000000085"
    # currency_dict["COP"] = "414484000004130337"
    currency_dict["EUR"] = "1208528000000000079"
    currency_dict["GBP"] = "1208528000000000070"
    # currency_dict["IDR"] = "414484000002783017"
    currency_dict["INR"] = "1208528000000000064"
    # currency_dict["JOD"] = "414484000001986157"
    currency_dict["JPY"] = "1208528000000000082"
    # currency_dict["MYR"] = "414484000005082013"
    # currency_dict["NOK"] = "414484000002527213"
    # currency_dict["QAR"] = "414484000004984035"
    # currency_dict["RON"] = "414484000001666001"
    # currency_dict["SGD"] = "414484000001192067"
    currency_dict["USD"] = "1208528000000000061"
    currency_dict["ZAR"] = "1208528000000000076"
    currency_dict["SAR"] = "1208528000000015217"

    null_value = None

    # GSTRegistrationType -> gst_treatment
    gst_registration_type_dict = dict()
    gst_registration_type_dict["GST_REG_REG"] = "business_gst"
    gst_registration_type_dict["GST_REG_COMP"] = "business_registered_composition"
    gst_registration_type_dict["GST_UNREG"] = "business_none"
    gst_registration_type_dict["CONSUMER"] = "consumer"
    gst_registration_type_dict["OVERSEAS"] = "overseas"
    gst_registration_type_dict["SEZ"] = "sez_developer"
    gst_registration_type_dict["DEEMED"] = "deemed_export"

    mapped_dict = dict()
    mapped_dict["contact_name"] = customer_from_qb["DisplayName"]
    if "CompanyName" in customer_from_qb:
        mapped_dict["company_name"] = customer_from_qb["CompanyName"]
    else:
        mapped_dict["company_name"] = customer_from_qb["DisplayName"]


    if "WebAddr" in customer_from_qb:
        if "URI" in customer_from_qb["WebAddr"]:
            mapped_dict["website"] = customer_from_qb["WebAddr"]["URI"]
        else:
            mapped_dict["website"] = null_value
    else:
        mapped_dict["website"] = null_value

    # if "PrimaryEmailAddr" in customer_from_qb:
    #     email_string = customer_from_qb["PrimaryEmailAddr"]["Address"]
    #     email_list = email_string.split(",")
    #     if len(email_list) == 1:
    #         # Contains only one email
    #         mapped_dict["email"] = email_list[0]
    #     else:
    #         mapped_dict["email"] = email_list[0]
    #         contact_list = list()
    #         for element in email_list[1:]:
    #             email_dict = dict()
    #             # last_name is mandatory showing in the webpage of customer creation
    #             email_dict["last_name"] = element.split("@")[0]
    #             email_dict["email"] = element

    #             contact_list.append(email_dict)
            
    #         mapped_dict["contact_persons"] = contact_list
        
    # else:
    #     mapped_dict["email"] = null_value

    if "PrimaryEmailAddr" in customer_from_qb:
        email_string = customer_from_qb["PrimaryEmailAddr"]["Address"]
        email_list = email_string.split(",")
        if len(email_list) == 100:
            # Contains only one email
            mapped_dict["email"] = email_list[0]
        else:
            mapped_dict["email"] = email_list[0]
            contact_list = list()
            for element in email_list[0:]:
                email_dict = dict()
                email_dict["last_name"] = element.split("@")[0]
                email_dict["email"] = element
                if "PrimaryPhone" in customer_from_qb:
                    email_dict["phone"] = customer_from_qb["PrimaryPhone"]["FreeFormNumber"]
                elif "Mobile" in customer_from_qb:
                    email_dict["phone"] = customer_from_qb["Mobile"]["FreeFormNumber"]
                contact_list.append(email_dict)
            
            mapped_dict["contact_persons"] = contact_list
    else:
        mapped_dict["email"] = null_value


    
    mapped_dict["language_code"] = "en"
    mapped_dict["contact_type"] = "customer"
    mapped_dict["customer_sub_type"] = "business"
    mapped_dict["is_portal_enabled"] = "false"

    if "CurrencyRef" in customer_from_qb:
        mapped_dict["currency_id"] = currency_dict[customer_from_qb["CurrencyRef"]["value"]]
        # currency_code is mdae by me
        mapped_dict["currency_code"] = customer_from_qb["CurrencyRef"]["value"]
        # mapped_dict["currency_name"] = customer_from_qb["CurrencyRef"]["name"]

    else:
        mapped_dict["currency_id"] = null_value

    if "SalesTermRef" in customer_from_qb:
        mapped_dict["payment_terms_label"] = term_dict[customer_from_qb["SalesTermRef"]["value"]]
    else:
        mapped_dict["payment_terms_label"] = null_value
    
    if "Notes" in customer_from_qb:
        mapped_dict["notes"] = customer_from_qb["Notes"]
    else:
        mapped_dict["notes"] = null_value

    if "BillAddr" in customer_from_qb:

        name_is_not_found_flag = True # True indicating that name is not found
        name = ""
        address_string = ""
        # salutation = ""
        if "Line1" in customer_from_qb["BillAddr"]:
            tempText = customer_from_qb["BillAddr"]["Line1"]
            if check_for_mr_ms(tempText):
                name = tempText
                # salutation += name.split(' ')[0]
                name_is_not_found_flag = False # False indicating that name is found
            else:
                address_string += ' ' + tempText
        
        if "Line2" in customer_from_qb["BillAddr"]:
            tempText = customer_from_qb["BillAddr"]["Line2"]
            if name_is_not_found_flag and check_for_mr_ms(tempText):
                name = tempText
                # salutation += name.split(' ')[0]
            else:
                address_string += ' ' + tempText

        if "Line3" in customer_from_qb["BillAddr"]:
            tempText = customer_from_qb["BillAddr"]["Line3"]
            if name_is_not_found_flag and check_for_mr_ms(tempText):
                name = tempText
                # salutation += name.split(' ')[0]
            else:
                address_string += ' ' + tempText

        if "Line4" in customer_from_qb["BillAddr"]:
            tempText = customer_from_qb["BillAddr"]["Line4"]
            if name_is_not_found_flag and check_for_mr_ms(tempText):
                name = tempText
                # salutation += name.split(' ')[0]
            else:
                address_string += ' ' + tempText

        if "Line5" in customer_from_qb["BillAddr"]:
            tempText = customer_from_qb["BillAddr"]["Line5"]
            if name_is_not_found_flag and check_for_mr_ms(tempText):
                name = tempText
                # salutation += name.split(' ')[0]
            else:
                address_string += ' ' + tempText
        
        if "Line5" in customer_from_qb["BillAddr"]:
            tempText = customer_from_qb["BillAddr"]["Line5"]
            if name_is_not_found_flag and check_for_mr_ms(tempText):
                name = tempText
                # salutation += name.split(' ')[0]
            else:
                address_string += ' ' + tempText


        billing_address_dict = dict()

        print("bill_name : ",name)
        billing_address_dict["attention"] = name
        salutation = name.split(' ')[0]
        billing_address_dict["salutation"] = salutation


        if "PostalCode" in customer_from_qb["BillAddr"]:
            billing_address_dict["zip"] = int(customer_from_qb["BillAddr"]["PostalCode"])
        else:
            postal_code_re = re.search(r'\d{6}', address_string)
            if postal_code_re:
                extracted_zip_code = postal_code_re.group(0)
                billing_address_dict["zip"] = int(extracted_zip_code)

                # address_string = extract_sub_string1(address_string,extracted_zip_code)
                address_string = address_string.replace(postal_code_re.group(0), '')


            else:
                billing_address_dict["zip"] = null_value

        retList = get_state_string(address_string)
        if retList:
            # It means retList is not None
            address_string = retList[0]
            billing_address_dict["state"] = retList[1]
        else:
            billing_address_dict["state"] = null_value

        if "CountrySubDivisionCode" in customer_from_qb["BillAddr"]:
            billing_address_dict["state"] = customer_from_qb["BillAddr"]["CountrySubDivisionCode"]


        if "Country" in customer_from_qb["BillAddr"]:
            billing_address_dict["country"] = customer_from_qb["BillAddr"]["Country"]
        else:
            billing_address_dict["country"] = null_value

        if "City" in customer_from_qb["BillAddr"]:
            billing_address_dict["city"] = customer_from_qb["BillAddr"]["City"]
        else:
            billing_address_dict["city"] = null_value

        billing_address_dict["street2"] = null_value
        billing_address_dict["state_code"] = null_value

        billing_address_dict["fax"] = null_value

        # FROM HERE PARSING OF Mobile is starting ----------------------------------------------------------------------------
        phone_no_re = re.search(r'(0|91)?[7-9][0-9]{9}', address_string)
        # phone_no_re = re.search(r'(Mob: |0|91|)?[7-9][0-9]{9}', address_string)
        if phone_no_re:
            # phone_no = phone_no_re.group(0)
            # print("billing : ",phone_no)
            # billing_address_dict["phone"] = phone_no.split(' ')[-1]
            # address_string = re.sub(r'(Mob: |0|91|)?[7-9][0-9]{9}', '', address_string)
            billing_address_dict["phone"] = phone_no_re.group(0)
            address_string = address_string.replace(phone_no_re.group(0), '')
        else:
            billing_address_dict["phone"] = null_value

        if 'Mob:' in address_string:
            address_string = address_string.replace("Mob:", "")
        elif 'M:' in address_string:
            address_string = address_string.replace("M:", "")
        elif '+91' in address_string:
            address_string = address_string.replace("+91", "")
        elif 'Mob :' in address_string:
            address_string = address_string.replace("Mob :", "")
        elif '+91-' in address_string:
            address_string = address_string.replace("+91-", "")
        
        # END ----------------------------------------------------------------------------


        billing_address_dict["address"] = address_string

        mapped_dict["billing_address"] = billing_address_dict
    else:
        mapped_dict["billing_address"] = null_value


    if "ShipAddr" in customer_from_qb:
        shipping_address_dict = dict()

        name_is_not_found_flag = True # True indicating that name is not found
        name = ""
        address_string = ""
        # salutation = ""
        if "Line1" in customer_from_qb["ShipAddr"]:
            tempText = customer_from_qb["ShipAddr"]["Line1"]
            if check_for_mr_ms(tempText):
                name = tempText
                # salutation += name.split(' ')[0]
                name_is_not_found_flag = False # False indicating that name is found
            else:
                address_string += ' ' + tempText
        
        if "Line2" in customer_from_qb["ShipAddr"]:
            tempText = customer_from_qb["ShipAddr"]["Line2"]
            if name_is_not_found_flag and check_for_mr_ms(tempText):
                name = tempText
                # salutation += name.split(' ')[0]
            else:
                address_string += ' ' + tempText

        if "Line3" in customer_from_qb["ShipAddr"]:
            tempText = customer_from_qb["ShipAddr"]["Line3"]
            if name_is_not_found_flag and check_for_mr_ms(tempText):
                name = tempText
                # salutation += name.split(' ')[0]
            else:
                address_string += ' ' + tempText

        if "Line4" in customer_from_qb["ShipAddr"]:
            tempText = customer_from_qb["ShipAddr"]["Line4"]
            if name_is_not_found_flag and check_for_mr_ms(tempText):
                name = tempText
                # salutation += name.split(' ')[0]
            else:
                address_string += ' ' + tempText

        if "Line5" in customer_from_qb["ShipAddr"]:
            tempText = customer_from_qb["ShipAddr"]["Line5"]
            if name_is_not_found_flag and check_for_mr_ms(tempText):
                name = tempText
                # salutation += name.split(' ')[0]
            else:
                address_string += ' ' + tempText

        # print("ship_name : ",name)
        shipping_address_dict["attention"] = name
        salutation = name.split(' ')[0]
        shipping_address_dict["salutation"] = salutation

        if "PostalCode" in customer_from_qb["ShipAddr"]:
            shipping_address_dict["zip"] = int(customer_from_qb["ShipAddr"]["PostalCode"])
        else:
            postal_code_re = re.search(r'\d{6}', address_string)
            if postal_code_re:
                extracted_zip_code = postal_code_re.group(0)
                shipping_address_dict["zip"] = int(extracted_zip_code)

                # address_string = extract_sub_string1(address_string,extracted_zip_code)
                address_string = address_string.replace(postal_code_re.group(0), '')

            else:
                shipping_address_dict["zip"] = null_value
        

        shipping_address_dict["street2"] = null_value
        shipping_address_dict["state_code"] = null_value

        if "Country" in customer_from_qb["ShipAddr"]:
            shipping_address_dict["country"] = customer_from_qb["ShipAddr"]["Country"]
        else:
            shipping_address_dict["country"] = null_value

        if "City" in customer_from_qb["ShipAddr"]:
            shipping_address_dict["city"] = customer_from_qb["ShipAddr"]["City"]
        else:
            shipping_address_dict["city"] = null_value

        retList = get_state_string(address_string)
        if retList:
            # It means retList is not None
            address_string = retList[0]
            shipping_address_dict["state"] = retList[1]
        else:
            shipping_address_dict["state"] = null_value

        if "CountrySubDivisionCode" in customer_from_qb["ShipAddr"]:
            shipping_address_dict["state"] = customer_from_qb["ShipAddr"]["CountrySubDivisionCode"]
        
        shipping_address_dict["fax"] = null_value

        # FROM HERE PARSING OF Mobile is starting ----------------------------------------------------------------------------
        phone_no_re = re.search(r'(0|91)?[7-9][0-9]{9}', address_string)
        # phone_no_re = re.search(r'^((Mob: )?\+91[\-\s]?)?[0]?(91)?[789]\d{9}$', address_string)
        # phone_no_re = re.search(r'(Mob: |0|91|)?[7-9][0-9]{9}', address_string)

        if phone_no_re:
            # phone_no = phone_no_re.group(0)
            # print("shipping : ",phone_no)
            
            # shipping_address_dict["phone"] = phone_no.split(' ')[-1]
            # address_string = re.sub(r'(Mob: |0|91|)?[7-9][0-9]{9}', '', address_string)

            shipping_address_dict["phone"] = phone_no_re.group(0)
            address_string = address_string.replace(phone_no_re.group(0), '')

        else:
            shipping_address_dict["phone"] = null_value

        if 'Mob:' in address_string:
            address_string = address_string.replace("Mob:", "")
        elif 'M:' in address_string:
            address_string = address_string.replace("M:", "")
        elif '+91' in address_string:
            address_string = address_string.replace("+91", "")
        elif 'Mob :' in address_string:
            address_string = address_string.replace("Mob :", "")


        # END ----------------------------------------------------------------------------------------------------------------

        shipping_address_dict["address"] = address_string
        mapped_dict["shipping_address"] = shipping_address_dict
    else:
        mapped_dict["shipping_address"] = null_value

    mapped_dict["opening_balance_amount"] = customer_from_qb["Balance"]
    mapped_dict["tax_reg_no"] = null_value # It takes a double

    if "GSTRegistrationType" in customer_from_qb:
        mapped_dict["gst_treatment"] = gst_registration_type_dict[customer_from_qb["GSTRegistrationType"]]
        # We need gst_no for business_gst,sez_developer,deemed_export
        # We don't need gst_no for consumer,overseas,business_none
        if mapped_dict["gst_treatment"] == "business_gst" or mapped_dict["gst_treatment"] == "sez_developer" or mapped_dict["gst_treatment"] == "deemed_export":
            mapped_dict["gst_no"] = customer_from_qb["GSTIN"]
        else:
            mapped_dict["gst_no"] = null_value

    return mapped_dict
    


def generate_post_json():

    # https://www.geeksforgeeks.org/read-json-file-using-python/
    # file_name = 'all_fetched_data_from_qb.json'
    # file_name = 'data_from_qb.json'
    file_name = 'data_from_qb_active_pr.json'


    f = open(file_name)
    parsed_data = json.load(f)

    # item_list = parsed_data["QueryResponse"]["Customer"]
    my_item_list = list()
    for item in parsed_data:
        # my_item_dict = dict()
        # my_item_dict['name'] = item["Name"]
        # my_item_dict['rate'] = item["UnitPrice"]

        mapped_customer = mapping_func(item)
        my_item_list.append(mapped_customer)
    
    mapped_data = dict()
    mapped_data["Customer"] = my_item_list

    mapped_json = json.dumps(mapped_data,indent=4)

    with open("mapped_test.json", "w") as outfile:
        outfile.write(mapped_json)


# 'code' variable must be updated before running this function
def post_request_zoho():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # ZohoBooks.fullaccess.all
    code = '1000.e5b121a5fd70c1a3010f86948e29d72b.e3222606d87cf40fd485418d63ac036c'
    client_id = '1000.HG016JCEMYJ8HY9CGRIRWGO7L3J6AD'
    client_secret = 'c3942592d7792a7c533d58cc1e9ae4a7726ed0af3e'

    # gettokenurl = f'https://accounts.zoho.in/oauth/v2/token?code={code}&client_id={client_id}&client_secret={client_secret}&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code'
    # r1 = requests.post(gettokenurl)
    # """
    #     {
    #         "access_token": "1000.4e21763bd3648e78852bb8ba9531ba08.b2fa7df241b5adb948beb204fe124385",
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
    
    access_token = '1000.48e4424010f481655317cbbc7ba2d572.e7424d47206edf59a9a07b05fc9ea68e'
    refresh_token = '1000.5e31d7d0ceade0d26ad214286345d914.29d2993995e8560e4c5e463b0772af88'
    # expires_in = parsed_data["expires_in"]

    organization_id = '60019790139'
    post_url = f'https://books.zoho.in/api/v3/contacts/?organization_id={organization_id}'

    f = open('new.json')
    parsed_data2 = json.load(f)
    items_list = parsed_data2["Customer"]

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_customer_id_pr.txt","a")

    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")

    for item in items_list:
        while True:
            print(f'Processing for name: {item["contact_name"]}....')
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
                response_save_file.write(f'{parsed_data3["contact"]["contact_id"]} : {item["contact_name"]}\n')
                print(f'{item["contact_name"]} is successfully pushed')
                # It means success
                break
            else:
                print(f'ERROR occurred: {item["contact_name"]} was able to be pushed')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                continue
            

        print(f'Successfully created item named: {item["contact_name"]}')


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


# get_items_and_write_to_file()
# generate_post_json()
post_request_zoho()




        

