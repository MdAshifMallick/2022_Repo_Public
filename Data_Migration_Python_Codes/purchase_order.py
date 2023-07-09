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
    refresh_token = 'AB11689848768PZKDIbt2o8sb5Uuzh14Ylhb24SueRfaGFDYJP'
    access_token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..uPsXly1Zd21L-QhtU1-PbQ.QMQxVBxFpYS6d8FXojpPrvfeCGTL-eFG1MG4lJPuPOE2t6ICsZcQGcLYSweIAXs4mr51PxeA40whk-l07wZI3Azjch0tRk5U4K-HsPqtdHKRHvO2wPzJkk4k26Ki33uVhpI9_NyGpc6yUYMouC9eGN-0eVW5DOmoYPGOjh_tAd62zhjf5z8rmlD44DshkoSVCa39smB9v7P_Ux8cj5mPHmMuK9SiRrMl9pFdzmbobluiZzplB-GDmes5k7rFIrJh6pXIZLvSyRxvbmoHciAqHmE6_cW-v030PJ0E30FS5mLcjNUmo_TJPOloa4y-REUpp35OA7N_LoM27M7NvhUYNgWq_Tv5fNJV8Qi-FmVN37IiysMcV77NWnTMBnvlt7caTidrH2q_gxkYhYv5Mp1-jFmKA4cXcqWSJnoX2atJkkiVGr-YINaH6Z6j2Frb5R0IFTkP6HQh4OjB75oNoZs6d38W1-TLkAyqlFgTO0vNJUyAE-Qhb33xZ2twtCPuAxEshIaSpg4kiIHy0lSxOcno03MCEHquM3WNcwnXIxXyttTS2YiKXyu_gsuE-MRlOfB6j-O8xhKzcOPG1uPpxeMmELsTAbmhfRqAHH-_NPuDdp3uNshIurl0Za61w663oSXoAAIFC8VZ_pvMefnqVERV44I4JX135OhrvmgJ-VOTuaE7FaJTdZtz4f5LBJX7RJnYFhUmky-kC3Yg4Un5Cs0rNkDt7jggFfJ63DCbPw7yCvI.m9gxx6ZqnEw-40u70JjtDg'
    realmID = '123145872607489'

    client_id = 'ABJJq6tFOtjXEcDQwjAFlqOKkGx8qR7bSZRYuYRMuX5Z2pceLD'
    client_secret = 'iWKjytR3AVaXBlQh8seeYG135poqlqKCQiYDwAs7'

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

    file_name = 'data_from_qb_purchase_order_PR.json'
    # file_name = 'data_from_qb_2017_03_01_to_2023_01_31_purchase_order.json'
    # file_name = 'data_from_qb_purchase_order.json'


    fp = open(file_name,'a')
    startPosition = 1
    no_of_objects_fetched = 0
    flag = True
    while flag == True:
        selectQuery = f"select * from PurchaseOrder where TxnDate >= '2022-04-01' and TxnDate <= '2023-03-31' startPosition {startPosition}"
        # selectQuery = f"select * from PurchaseOrder startPosition {startPosition}"
        sandbox_getURL = f"{sandboxURL}/v3/company/{realmID}/query?query={selectQuery}&minorversion=65"
        production_getURL = f"{productionURL}/v3/company/{realmID}/query?query={selectQuery}&minorversion=65"
        headers["Authorization"] = f"Bearer {access_token}"
        # r = requests.get(sandbox_getURL,headers=headers)
        r = requests.get(production_getURL,headers=headers)


        # print(r.status_code)
        # if r.status_code == 200:
        #     parsed_data = r.json()

        #     if "QueryResponse" in parsed_data:
        #         if "PurchaseOrder" in parsed_data["QueryResponse"]:
        #             for element in parsed_data["QueryResponse"]["PurchaseOrder"]:
        #                 indented_data = json.dumps(element,indent=4)
        #                 fp.write(indented_data)
        #                 fp.write('\n,\n')

        #             maxResults = parsed_data["QueryResponse"]["maxResults"]
        #             print(f"Fetched {maxResults} Objects")
        #             no_of_objects_fetched += maxResults
        #             startPosition = no_of_objects_fetched + 1
        #         else:
        #             print(f"Finished...Total fetched {no_of_objects_fetched}")
        #             flag = False
        #     else:
        #         # {"error":"invalid_client"}
        #         auth_response = requests.post(auth_URL,data=payload,headers=auth_headers)

        #         if "error" in auth_response.json():
        #             """"
        #             {
        #                 "error_description": "Incorrect or invalid refresh token",
        #                 "error": "invalid_grant"
        #             }
        #             """
        #             print(f"SomeError occurred at getting new access_token after fetching {no_of_objects_fetched} objects... dumping in error.json")
        #             autherrorfp = open('autherror.json','w')
        #             autherror_parsed = json.dumps(auth_response.json(),indent=4)
        #             autherrorfp.write(autherror_parsed)
        #             exit()
        #         else:
        #             """{"access_token":"..","token_type":"bearer","x_refresh_token_expires_in":8725268,"refresh_token":"...","expires_in":3600}"""
        #             parsed_auth_response = auth_response.json()
        #             access_token = parsed_auth_response["access_token"]
        #             print("GENERATING NEW ACCESS TOKEN....")

        # else:
        #     print(f"SomeError occurred after fetching {no_of_objects_fetched} objects... dumping in error.json")
        #     errorfp = open('error.json','w')
        #     r_parsed = json.dumps(r.json(),indent=4)
        #     errorfp.write(r_parsed)
        #     exit()

        parsed_data = r.json()
        if "QueryResponse" in parsed_data:
            if "PurchaseOrder" in parsed_data["QueryResponse"]:
                for element in parsed_data["QueryResponse"]["PurchaseOrder"]:
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
        elif "fault" in parsed_data:
                print('Fault Occreed.......')
                autherrorfp=open("autherror.json",'w')
                autherror_parsed=json.dumps(parsed_data,indent=4)
                autherrorfp.write(autherror_parsed) 
                exit()
        else:
            # {"error":"invalid_client"}
            auth_response = requests.post(auth_URL,data=payload,headers=auth_headers)

            if "error" in auth_response.json():
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
                print("GENERATING NEW ACCESS TOKEN....")
                print(access_token)


def mapping_func(invoice_from_qb):

    null_value = None

    # Term -> "payment_terms_label"
    term_dict = dict()
    term_dict["6"] = "By 5th"
    term_dict["1"] = "Due on receipt"
    term_dict["12"] = "Immediate"
    term_dict["7"] = "Net"
    term_dict["9"] = "Net 10"
    term_dict["2"] = "Net 15"
    term_dict["3"] = "Net 30"
    term_dict["14"] = "Net 45"
    term_dict["8"] = "Net 45 Days"
    term_dict["15"] = "Net 5"
    term_dict["4"] = "Net 60"
    term_dict["5"] = "Net 7"
    term_dict["13"] = "Net 75"
    term_dict["11"] = "Net 90"
    term_dict["10"] = "quarterly"

    taxcode_dict = dict()
    taxcode_dict["36"] = "(sales)ST@14%+0.5%SBC+0.5%KKS+VAT@5.5%"
    taxcode_dict["59"] = "0% GST"
    taxcode_dict["56"] = "0% IGST"
    taxcode_dict["74"] = "0.25% GST"
    taxcode_dict["72"] = "0.25% IGST"
    taxcode_dict["22"] = "0.5% Swachh Bharat Cess"
    taxcode_dict["58"] = "12.0% GST"
    taxcode_dict["60"] = "12.0% IGST"
    taxcode_dict["4"] = "12.36% ST"
    taxcode_dict["15"] = "12.5% CST - Inactive - Inactive"
    taxcode_dict["38"] = "12.50% VAT Purchase"
    taxcode_dict["40"] = "13.5% VAT"
    taxcode_dict["16"] = "14% Service Tax - Inactive"
    taxcode_dict["17"] = "14% ST & VAT"
    taxcode_dict["20"] = "14%ST & 2%CST"
    taxcode_dict["3"] = "14.0% VAT"
    taxcode_dict["19"] = "14.00% ST"
    taxcode_dict["26"] = "14.5% ST"
    taxcode_dict["42"] = "14.5% VAT"
    taxcode_dict["27"] = "15.0% ST"
    taxcode_dict["62"] = "18.0% GST"
    taxcode_dict["54"] = "18.0% IGST"
    taxcode_dict["9"] = "2% CST"
    taxcode_dict["50"] = "2% KVAT"
    taxcode_dict["14"] = "2.0% CST"
    taxcode_dict["41"] = "20% VAT KVAT"
    taxcode_dict["37"] = "20%VAT"
    taxcode_dict["57"] = "28.0% GST"
    taxcode_dict["61"] = "28.0% IGST"
    taxcode_dict["73"] = "3.0% GST"
    taxcode_dict["71"] = "3.0% IGST"
    taxcode_dict["2"] = "4.0% VAT"
    taxcode_dict["53"] = "5.0% GST"
    taxcode_dict["63"] = "5.0% IGST"
    taxcode_dict["5"] = "5.0% VAT"
    taxcode_dict["6"] = "5.5% VAT"
    taxcode_dict["76"] = "6.0% GST"
    taxcode_dict["75"] = "6.0% IGST"
    taxcode_dict["55"] = "Exempt GST"
    taxcode_dict["52"] = "Exempt IGST"
    taxcode_dict["67"] = "GST Cess @ 36%"
    taxcode_dict["64"] = "GST Cess @ 5%"
    taxcode_dict["28"] = "KKS"
    taxcode_dict["30"] = "KKS@0.5"
    taxcode_dict["43"] = "MVAT-12.5%"
    taxcode_dict["44"] = "MVAT-13.5%"
    taxcode_dict["46"] = "MVAT-14.5%"
    taxcode_dict["49"] = "MVAT-20%"
    taxcode_dict["51"] = "MVAT-25%"
    taxcode_dict["45"] = "MVAT-5%"
    taxcode_dict["47"] = "MVAT-5.5%"
    taxcode_dict["48"] = "MVAT-6%"
    taxcode_dict["13"] = "Out of Scope"
    taxcode_dict["65"] = "Purchase GST 33% - 28%GST+5%Cess"
    taxcode_dict["68"] = "Purchase GST 64% - 28%GST+36%CESS"
    taxcode_dict["66"] = "Sales GST 33% - 28%GST+5%Cess"
    taxcode_dict["69"] = "Sales GST 64% - 28%GST+36%CESS"
    taxcode_dict["70"] = "Sales* GST64% - 28%GST+36%CESS"
    taxcode_dict["7"] = "Service Tax & VAT"
    taxcode_dict["11"] = "Service Tax Old Rate"
    taxcode_dict["12"] = "ST & CST"
    taxcode_dict["8"] = "ST & VAT"
    taxcode_dict["21"] = "ST&CST"
    taxcode_dict["24"] = "ST&VAT"
    taxcode_dict["25"] = "ST(new)&CST"
    taxcode_dict["33"] = "ST+CST(17%)"
    taxcode_dict["32"] = "ST+VAT(20.5%)"
    taxcode_dict["34"] = "ST+VAT(20.5) New"
    taxcode_dict["31"] = "ST14.5%+KKS0.5%+VAT5.5%"
    taxcode_dict["29"] = "ST15%+VAT5.5%"
    taxcode_dict["35"] = "ST@14%+0.5%SBC+0.5%KKS+VAT@5.5%"
    taxcode_dict["10"] = "Test"
    taxcode_dict["23"] = "UD_14.5% ST"
    taxcode_dict["18"] = "VAT 14.5%"
    taxcode_dict["39"] = "Vat @ 6%"
    taxcode_dict["NON"] = null_value

    tds_section_dict = dict()
    tds_section_dict["9"] = "194C(1)-Contracts"
    tds_section_dict["20"] = "194J-(1)-Fees for Professinal and Technical Services"
    tds_section_dict["21"] = "194J-(2)-Remuneration to Director"
    tds_section_dict["0"] = "NO TDS"

    tax_rate_fout = open('tax_id_and_name.json')
    tax_rate_details = json.load(tax_rate_fout)

    mapping_dict = dict()

    mapping_dict["po_email"] = null_value
    if "POEmail" in invoice_from_qb:
        mapping_dict["po_email"] = invoice_from_qb["POEmail"]["Address"]

    mapping_dict["po_status"] = null_value
    if "POStatus" in invoice_from_qb:
        mapping_dict["po_status"] = invoice_from_qb["POStatus"]

    if "DocNumber" in invoice_from_qb:
        # invoice_number is string
        mapping_dict["po_number"] = invoice_from_qb["DocNumber"]
    else:
        mapping_dict["po_number"] = null_value

    if "TxnDate" in invoice_from_qb:
        # invoice_number is string
        mapping_dict["po_date"] = invoice_from_qb["TxnDate"]
    else:
        mapping_dict["po_date"] = null_value

    if "CurrencyRef" in invoice_from_qb:
        mapping_dict["currency_code"] = invoice_from_qb["CurrencyRef"]["value"]
        mapping_dict["currency_name"] = invoice_from_qb["CurrencyRef"]["name"]

    # CustomField
    # Definition Id 0
    # mapping_dict["cf_id_0_name"] = invoice_from_qb["CustomField"][0]["Name"]
    # if "StringValue" in invoice_from_qb["CustomField"][0]:
    #     mapping_dict["cf_id_0_value"] = invoice_from_qb["CustomField"][0]["StringValue"]
    # else:
    #     mapping_dict["cf_id_0_value"] = null_value

    # mapping_dict["cf_id_1_name"] = invoice_from_qb["CustomField"][1]["Name"]
    # if "StringValue" in invoice_from_qb["CustomField"][1]:
    #     mapping_dict["cf_id_1_value"] = invoice_from_qb["CustomField"][1]["StringValue"]
    # else:
    #     mapping_dict["cf_id_1_value"] = null_value

    # mapping_dict["cf_id_2_name"] = invoice_from_qb["CustomField"][2]["Name"]
    # if "StringValue" in invoice_from_qb["CustomField"][2]:
    #     mapping_dict["cf_id_2_value"] = invoice_from_qb["CustomField"][2]["StringValue"]
    # else:
    #     mapping_dict["cf_id_2_value"] = null_value

    mapping_dict["department_name"] = null_value
    if "DepartmentRef" in invoice_from_qb:
        mapping_dict["department_name"] = invoice_from_qb["DepartmentRef"]["name"]

    if "ExchangeRate" in invoice_from_qb:
        mapping_dict["exchange_rate"] = invoice_from_qb["ExchangeRate"]
    else:
        mapping_dict["exchange_rate"] = null_value

    if "PrivateNote" in invoice_from_qb:
        mapping_dict["private_note"] = invoice_from_qb["PrivateNote"]
    else:
        mapping_dict["private_note"] = null_value

    
    if "Line" in invoice_from_qb:
        qb_line_items = invoice_from_qb["Line"]

        my_item_list = list()
        my_item_extra_list = list()
        for item in qb_line_items:
            # item_id is string

            my_item_dict = dict()
            my_item_extra_dict = dict()

            detail_type = item["DetailType"]

            if detail_type == "AccountBasedExpenseLineDetail":

                my_item_dict["item_amount"] = item["Amount"]
                my_item_dict["item_amount_received"] = null_value
                if "Received" in item:
                    my_item_dict["item_amount_received"] = item["Received"]


                if "Description" in item:
                    my_item_dict["item_description"] = item["Description"]
                else:
                    my_item_dict["item_description"] = null_value

                # if "name" in item["AccountBasedExpenseLineDetail"]["ItemRef"]:
                #     my_item_dict["item_name"] = item["AccountBasedExpenseLineDetail"]["ItemRef"]["name"]
                # else:
                #     my_item_dict["item_name"] = null_value 
                
                if "ClassRef" in item["AccountBasedExpenseLineDetail"]:
                    my_item_dict["class_name"] = item["AccountBasedExpenseLineDetail"]["ClassRef"]["name"]
                else:
                    my_item_dict["class_name"] = null_value

                if "AccountRef" in item["AccountBasedExpenseLineDetail"]:
                    my_item_dict["account_name"] = item["AccountBasedExpenseLineDetail"]["AccountRef"]["name"]
                else:
                    my_item_dict["account_name"] = null_value

                if "BillableStatus" in item["AccountBasedExpenseLineDetail"]:
                    my_item_dict["billable_status"] = item["AccountBasedExpenseLineDetail"]["BillableStatus"]
                else:
                    my_item_dict["billable_status"] = null_value

                if "TaxCodeRef" in item["AccountBasedExpenseLineDetail"]:
                    my_item_dict["tax_name"] = taxcode_dict[item["AccountBasedExpenseLineDetail"]["TaxCodeRef"]["value"]]
                else:
                    my_item_dict["tax_name"] = null_value
            elif detail_type == "ItemBasedExpenseLineDetail":

                my_item_dict["item_amount"] = item["Amount"]
                my_item_dict["item_amount_received"] = null_value
                if "Received" in item:
                    my_item_dict["item_amount_received"] = item["Received"]
                
                if "Description" in item:
                    my_item_dict["item_description"] = item["Description"]
                else:
                    my_item_dict["item_description"] = null_value

                if "name" in item["ItemBasedExpenseLineDetail"]["ItemRef"]:
                    my_item_dict["item_name"] = item["ItemBasedExpenseLineDetail"]["ItemRef"]["name"]
                else:
                    my_item_dict["item_name"] = null_value 
                
                if "ClassRef" in item["ItemBasedExpenseLineDetail"]:
                    my_item_dict["class_name"] = item["ItemBasedExpenseLineDetail"]["ClassRef"]["name"]
                else:
                    my_item_dict["class_name"] = null_value

                if "UnitPrice" in item["ItemBasedExpenseLineDetail"]:
                    my_item_dict["item_rate"] = item["ItemBasedExpenseLineDetail"]["UnitPrice"]
                else:
                    my_item_dict["item_rate"] = null_value

                if "Qty" in item["ItemBasedExpenseLineDetail"]:
                    my_item_dict["item_quantity"] = item["ItemBasedExpenseLineDetail"]["Qty"]
                else:
                    my_item_dict["item_quantity"] = null_value

                if "BillableStatus" in item["ItemBasedExpenseLineDetail"]:
                    my_item_dict["billable_status"] = item["ItemBasedExpenseLineDetail"]["BillableStatus"]
                else:
                    my_item_dict["billable_status"] = null_value

                if "TaxCodeRef" in item["ItemBasedExpenseLineDetail"]:
                    my_item_dict["tax_name"] = taxcode_dict[item["ItemBasedExpenseLineDetail"]["TaxCodeRef"]["value"]]
                else:
                    my_item_dict["tax_name"] = null_value

                if "CustomerRef" in item["ItemBasedExpenseLineDetail"]:
                    my_item_dict["item_customer_name"] = item["ItemBasedExpenseLineDetail"]["CustomerRef"]
                else:
                    my_item_dict["item_customer_name"] = null_value
            # elif detail_type == "SubTotalLineDetail":
            #     # amount = item["Amount"]
            #     my_item_extra_dict["sub_total_amount"] = item["Amount"]
            # # elif detail_type == "DiscountLineDetail":
            # #     # percent_based_or_not = item["PercentBased"]
            # #     my_item_dict["discount_percent_based_or_not"] = item["PercentBased"]
            # elif detail_type == "TDSLineDetail":
            #     # tds_section_type_id = item["TDSLineDetail"]["TDSSectionTypeId"]
            #     # my_item_extra_dict["tds_amount"] = item["Amount"]
            #     if "TDSSectionTypeId" in item["TDSLineDetail"]:
            #         my_item_extra_dict["tds_amount"] = item["Amount"]
            #         my_item_extra_dict["tds_detail_section_type_id"] = item["TDSLineDetail"]["TDSSectionTypeId"]
            #         my_item_extra_dict["tds_detail_section_type_name"] = tds_section_dict[str(my_item_extra_dict["tds_detail_section_type_id"])]
            #     else:
            #         my_item_extra_dict["tds_amount"] = null_value
            #         my_item_extra_dict["tds_detail_section_type_id"] = null_value
            #         my_item_extra_dict["tds_detail_section_type_name"] = null_value
            my_item_extra_list.append(my_item_extra_dict)
            my_item_list.append(my_item_dict)

    mapping_dict["line_list"] = my_item_list
    mapping_dict["line_extra_list"] = my_item_extra_list

    my_tax_line_list = list()
    if "TxnTaxDetail" in invoice_from_qb:
        mapping_dict["total_tax"] = invoice_from_qb["TxnTaxDetail"]["TotalTax"]

        if "TaxLine" in invoice_from_qb["TxnTaxDetail"]:

            tax_line = invoice_from_qb["TxnTaxDetail"]["TaxLine"]
            for tax_item in tax_line:
                my_tax_item_dict = dict()

                my_tax_item_dict["tax_amount"] = tax_item["Amount"]
                tax_detail_type = tax_item["DetailType"]

                if tax_detail_type == "TaxLineDetail":
                    selected_tax_rate = tax_rate_details[tax_item["TaxLineDetail"]["TaxRateRef"]["value"]]
                    my_tax_item_dict["tax_name"] = selected_tax_rate[0]
                    my_tax_item_dict["tax_description"] = selected_tax_rate[1]
                    my_tax_item_dict["tax_rate_in_percent"] = selected_tax_rate[2]
                    my_tax_item_dict["net_amount_taxable"] = tax_item["TaxLineDetail"]["NetAmountTaxable"]
                    # my_tax_item_dict["tax_percent"] = tax_item["TaxLineDetail"]["TaxPercent"]

                my_tax_line_list.append(my_tax_item_dict)


    mapping_dict["tax_detail_list"] = my_tax_line_list

    if "VendorRef" in invoice_from_qb:
        mapping_dict["vendor_name"] = invoice_from_qb["VendorRef"]["name"]
    else:
        mapping_dict["vendor_name"] = null_value

    if "APAccountRef" in invoice_from_qb:
        mapping_dict["ap_account_name"] = invoice_from_qb["APAccountRef"]["name"]
    else:
        mapping_dict["ap_account_name"] = null_value

    if "TotalAmt" in invoice_from_qb:
        mapping_dict["total_amount"] = invoice_from_qb["TotalAmt"]
    else:
        mapping_dict["total_amount"] = null_value

    if "Memo" in invoice_from_qb:
        mapping_dict["memo"] = invoice_from_qb["Memo"]
    else:
        mapping_dict["memo"] = null_value

    # if "Balance" in invoice_from_qb:
    #     mapping_dict["balance"] = invoice_from_qb["Balance"]
    # else:
    #     mapping_dict["balance"] = null_value

    # if "HomeBalance" in invoice_from_qb:
    #     mapping_dict["home_balance"] = invoice_from_qb["HomeBalance"]
    # else:
    #     mapping_dict["home_balance"] = null_value

    # if "DiscountAmt" in invoice_from_qb:
    #     mapping_dict["discount_amount"] = invoice_from_qb["DiscountAmt"]
    # else:
    #     mapping_dict["discount_amount"] = null_value

    if "GlobalTaxCalculation" in invoice_from_qb:
        mapping_dict["global_tax_calculation"] = invoice_from_qb["GlobalTaxCalculation"]
    else:
        mapping_dict["global_tax_calculation"] = null_value

    # if "CustomerMemo" in invoice_from_qb:
    #     mapping_dict["customer_memo"] = invoice_from_qb["CustomerMemo"]["value"]
    # else:
    #     mapping_dict["customer_memo"] = null_value


    # -----------------------------------------------------------------------
    # if "HomeTotalAmt" in invoice_from_qb:
    #     mapping_dict["sub_total_home_amount"] = invoice_from_qb["HomeTotalAmt"]
    # else:
    #     mapping_dict["sub_total_home_amount"] = null_value
    
    # if "TotalAmt" in invoice_from_qb:
    #     mapping_dict["total_amount"] = invoice_from_qb["TotalAmt"]
    # else:
    #     mapping_dict["total_amount"] = null_value

    # if "HomeTotalAmt" in invoice_from_qb:
    #     mapping_dict["home_total_amount"] = invoice_from_qb["HomeTotalAmt"]
    # else:
    #     mapping_dict["home_total_amount"] = null_value
    
    # -----------------------------------------------------------------------

    # if "SalesTermRef" in invoice_from_qb:
    #     mapping_dict["payment_terms_label"] = term_dict[invoice_from_qb["SalesTermRef"]["value"]]
    # else:
    #     mapping_dict["payment_terms_label"] = null_value

    # if "ExchangeRate" in invoice_from_qb:
    #     mapping_dict["exchange_rate"] = invoice_from_qb["ExchangeRate"]
    # else:
    #     mapping_dict["exchange_rate"] = null_value

    # if "PrivateNote" in invoice_from_qb:
    #     mapping_dict["private_note"] = invoice_from_qb["PrivateNote"]
    # else:
    #     mapping_dict["private_note"] = null_value

    return mapping_dict

def for_excel():
    fin = open("mapped.json")
    parsed_data = json.load(fin)

    null_value = None

    invoice_list = list()
    for invoice in parsed_data["PurchaseOrder"]:

        invoice_number = invoice["po_number"]
        invoice_date = invoice["po_date"]
        customer_name = invoice["vendor_name"]
        # due_date = invoice["due_date"]
        # payment_terms_label = invoice["payment_terms_label"]
        exchange_rate = invoice["exchange_rate"]

        # print_status = invoice["print_status"]
        # email_status = invoice["email_status"]

        global_tax_calculation = invoice["global_tax_calculation"]
        # customer_memo = invoice["customer_memo"]
        memo = invoice["memo"]

        # balance = invoice["balance"]
        # home_balance = invoice["home_balance"]
        # discount_amount = invoice["discount_amount"]

        private_note = invoice["private_note"]
        total_amount = invoice["total_amount"]
        # home_total_amount = invoice["home_total_amount"]

        total_tax = null_value
        if "total_tax" in invoice:
            total_tax = invoice["total_tax"]

        currency_code = invoice["currency_code"]
        currency_name = invoice["currency_name"]

        po_email = invoice["po_email"]
        po_status = invoice["po_status"]
        ap_account_name = invoice["ap_account_name"]





        ### Remove the empty dictionary
        tempList = invoice["line_list"]
        line_items = [item for item in tempList if item]

        tempList = invoice["line_extra_list"]
        line_extra_items = [item for item in tempList if item]
        
        tempList = invoice["tax_detail_list"]
        tax_detail_list = [item for item in tempList if item]
        #######################################################

        # sub_total_amount = null_value
        # tds_amount = null_value
        # tds_detail_section_type_id = null_value
        # tds_detail_section_type_name = null_value

        # for line_item_extra in line_extra_items:
        #     if "sub_total_amount" in line_item_extra:
        #         sub_total_amount = line_item_extra["sub_total_amount"]

        #     if "tds_amount" in line_item_extra:
        #         tds_amount = line_item_extra["tds_amount"]

        #     if "tds_detail_section_type_id" in line_item_extra:
        #         tds_detail_section_type_id = line_item_extra["tds_detail_section_type_id"]

        #     if "tds_detail_section_type_name" in line_item_extra:
        #         tds_detail_section_type_name = line_item_extra["tds_detail_section_type_name"]


        for line_item in line_items:
            invoice_dict = dict()

            invoice_dict["s_po_number"] = invoice_number
            invoice_dict["s_po_date"] = invoice_date
            invoice_dict["s_vendor_name"] = customer_name
            # invoice_dict["s_due_date"] = due_date
            # invoice_dict["s_payment_terms_label"] = payment_terms_label
            invoice_dict["s_exchange_rate"] = exchange_rate
            invoice_dict["s_total_amount"] = total_amount
            # invoice_dict["s_home_total_amount"] = home_total_amount

            
            # invoice_dict["s_print_status"] = print_status
            # invoice_dict["s_email_status"] = email_status

            invoice_dict["s_global_tax_calculation"] = global_tax_calculation
            # invoice_dict["s_customer_memo"] = customer_memo
            
            invoice_dict["s_memo"] = memo

            # invoice_dict["s_balance"] = balance
            # invoice_dict["s_home_balance"] = home_balance
            # invoice_dict["s_discount_amount"] = discount_amount


            invoice_dict["s_total_tax"] = total_tax
            
            # invoice_dict["s_sub_total_amount"] = sub_total_amount
            # invoice_dict["s_tds_amount"] = tds_amount
            # invoice_dict["s_tds_detail_section_type_id"] = tds_detail_section_type_id
            # invoice_dict["s_tds_detail_section_type_name"] = tds_detail_section_type_name

            invoice_dict["s_currency_code"] = currency_code
            invoice_dict["s_currency_name"] = currency_name

            invoice_dict["s_private_note"] = private_note

            invoice_dict["s_po_email"] = po_email
            invoice_dict["s_po_status"] = po_status
            invoice_dict["s_ap_account_name"] = ap_account_name

            invoice_dict["item_name"] = null_value
            if "item_name" in line_item:
                invoice_dict["item_name"] = line_item["item_name"]
            
            invoice_dict["item_description"] = line_item["item_description"]
            invoice_dict["item_amount"] = line_item["item_amount"]
            invoice_dict["item_amount_received"] = line_item["item_amount_received"]
            
            invoice_dict["item_rate"] = null_value            
            if "item_rate" in line_item:
                invoice_dict["item_rate"] = line_item["item_rate"]
            
            invoice_dict["item_quantity"] = null_value
            if "item_quantity" in line_item:
                invoice_dict["item_quantity"] = line_item["item_quantity"]
            
            # invoice_dict["item_rate"] = line_item["rate"]
            # invoice_dict["item_quantity"] = line_item["quantity"]
            invoice_dict["item_class_name"] = line_item["class_name"]
            # invoice_dict["item_discount_amount"] = line_item["item_discount_amount"]
            invoice_dict["item_account_name"] = null_value
            if "account_name" in line_item:
                invoice_dict["item_account_name"] = line_item["account_name"]
            invoice_dict["item_billable_status"] = line_item["billable_status"]
            invoice_dict["item_tax_name"] = line_item["tax_name"]

            invoice_dict["item_customer_name"] = null_value
            if "item_customer_name" in line_item:
                invoice_dict["item_customer_name"] = line_item["item_customer_name"]

            # invoice_dict["item_customer_name"] = line_item["item_customer_name"]


            invoice_list.append(invoice_dict)

        
        # sub_total_amount = null_value
        # tds_amount = null_value
        # tds_detail_section_type_id = null_value
        # tds_detail_section_type_name = null_value


        for tax_item in tax_detail_list:
            invoice_dict = dict()

            invoice_dict["s_po_number"] = invoice_number
            invoice_dict["s_po_date"] = invoice_date
            invoice_dict["s_vendor_name"] = customer_name
            # invoice_dict["s_due_date"] = due_date
            # invoice_dict["s_payment_terms_label"] = payment_terms_label
            invoice_dict["s_exchange_rate"] = exchange_rate
            invoice_dict["s_total_amount"] = total_amount
            # invoice_dict["s_home_total_amount"] = home_total_amount

            
            # invoice_dict["s_print_status"] = print_status
            # invoice_dict["s_email_status"] = email_status

            invoice_dict["s_global_tax_calculation"] = global_tax_calculation
            # invoice_dict["s_customer_memo"] = customer_memo
            
            invoice_dict["s_memo"] = memo

            # invoice_dict["s_balance"] = balance
            # invoice_dict["s_home_balance"] = home_balance
            # invoice_dict["s_discount_amount"] = discount_amount

            invoice_dict["s_total_tax"] = total_tax
            
            # invoice_dict["s_sub_total_amount"] = sub_total_amount
            # invoice_dict["s_tds_amount"] = tds_amount
            # invoice_dict["s_tds_detail_section_type_id"] = tds_detail_section_type_id
            # invoice_dict["s_tds_detail_section_type_name"] = tds_detail_section_type_name

            invoice_dict["s_currency_code"] = currency_code
            invoice_dict["s_currency_name"] = currency_name

            invoice_dict["s_private_note"] = private_note

            invoice_dict["s_po_email"] = po_email
            invoice_dict["s_po_status"] = po_status
            invoice_dict["s_ap_account_name"] = ap_account_name

            invoice_dict["tax_amount"] = tax_item["tax_amount"]
            invoice_dict["tax_name"] = tax_item["tax_name"]
            invoice_dict["tax_description"] = tax_item["tax_description"]
            invoice_dict["tax_rate_in_percent"] = tax_item["tax_rate_in_percent"]
            invoice_dict["net_amount_taxable"] = tax_item["net_amount_taxable"]

            invoice_list.append(invoice_dict)

    mapped_data = dict()
    mapped_data["PurchaseOrder"] = invoice_list

    mapped_json = json.dumps(mapped_data,indent=4)

    with open("for_excel_mapped.json", "w") as outfile:
        outfile.write(mapped_json)

def generate_post_json():

    # https://www.geeksforgeeks.org/read-json-file-using-python/
    # file_name = 'all_fetched_data_from_qb.json'
    # file_name = 'production_get.json'

    # file_name = 'data_from_qb_2013_04_01_to_2017_06_30_purchase_order.json'
    file_name = 'data_from_qb_purchase_order.json'


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
    mapped_data["PurchaseOrder"] = my_item_list

    mapped_json = json.dumps(mapped_data,indent=4)

    with open("mapped.json", "w") as outfile:
        outfile.write(mapped_json)


# 'code' variable must be updated before running this function
def post_request_zoho():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # ZohoBooks.fullaccess.all
    code = '1000.94fb7777a59cd201cd0c30a751b00b1b.605d2125bb2a84fbb721530f8781dabb'
    client_id = '1000.9NTIBYXQH0INR3SN5EXCJZU1SDFQPD'
    client_secret = '1c1fca878465586e4947e8bd08d8cf64db5592c61b'

    gettokenurl = f'https://accounts.zoho.in/oauth/v2/token?code={code}&client_id={client_id}&client_secret={client_secret}&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code'
    r1 = requests.post(gettokenurl)
    """
        {
            "access_token": "1000.cb73ac8e8e7a97e9a477b2771fdfa546.be088fe17b6386a80add9441e1ac0cc9",
            "refresh_token": "1000.b3bcfcb05de766156aa2966732c07f58.c471e437e710a57b63fb6e6ba99dc6a5",
            "api_domain": "https://www.zohoapis.in",
            "token_type": "Bearer",
            "expires_in": 3600
        }

        OR

        {
            "error": "invalid_code"
        }
    """
    parsed_data1 = r1.json()
    if 'error' in parsed_data1:
        # print(parsed_data1)
        print('code is expired [invalid code]')
        exit()
    
    refresh_token = parsed_data1["refresh_token"]
    access_token = parsed_data1["access_token"]
    # expires_in = parsed_data["expires_in"]

    organization_id = '60015983411'
    post_url = f'https://books.zoho.in/api/v3/items?organization_id={organization_id}'

    f = open('mapped.json')
    parsed_data2 = json.load(f)
    items_list = parsed_data2["Item"]

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_customer_id.txt","a")

    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")

    for item in items_list:
        while True:
            print(f'Processing for name: {item["name"]}....')
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
                response_save_file.write(f'{parsed_data3["contact"]["contact_id"]} : {item["name"]}\n')
                print(f'{item["name"]} is successfully pushed')
                # It means success
                break
            else:
                print(f'ERROR occurred: {item["name"]} was able to be pushed')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
            

        print(f'Successfully created item named: {item["name"]}')


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


get_items_and_write_to_file()
# generate_post_json()
# for_excel()
# post_request_zoho()




        

