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
    refresh_token = 'AB11669980025m7lXyPHCWeEjrz7h3gGkkWHtxTje3hNYyqVcD'
    access_token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..Meeel1_e4WaYr48zJL4DNg.6pBI23FmygL3pjIZgKYfnoqFZEY20bEoIfOwWRhVAPRW07nkmS6zee2IymJfJm5u57kKVXOnd9XdFX_j6Jqvqh2pECmHo0ml0yLUaDstfVI7FZHuWSVjn_aVxEZpFWLI5zLiWr_sRtYzS_9xvdtOIHu5_WUkrYk2b5dMT2uqcntDuTBSAL_1YHcAn9NAPeDaz82H1FmjzTs8XaGyRnTaGo5mi06nDa-xSrk8T-R1Dw3NqWy4PQ6rGBVoWmHZuhp7mwc93SnaoO6OLrLJmP4Sv_pwuVY8Z8oPJYji48aN0P3VeXIGRRwQ5NyxZPQngRUycoZeD6D2wV2wS-vTDN_aROkcjPbwFbOZKZ42XS2_hBQ5uhlIY198isAfcj_RDSXy_cAucUsCAZ74tzTRDkZ93JHbuNUItmqeQ_8tMOC6AfUs0QX3WPKu69o10mp7eN4qYl7lzKa-dTFBp5DwOHuG4hTUda13SzXuu8JYLT5jGg7lPDQLkED3O4we3YB0pvbtBMnxNysBiyPu-yMpXzzZcPxa3i2meAIzSs7OZxpR_PPLBbpPcangoyg3R-0OzhhmxciDAhy81Lh9GV3xVg3sg-SHo2eLSV2_IMZjHy9FEdP6q_kSaGOqjR4kxMlXLKjTLYu4n62DPqytPEdPVcU4eYLAbqNjb98e3H3fCKdw3xGK2attE1eEc7F-hYE8FiVaaQkGy5VfgBIqcl8-YoMt8IoCPOXy8xTCF8pl4-D52Dc.KCbeOJJRXM0d1gwSlRxSow'
    realmID = '721365895'

    client_id = 'ABqlhReO5D58T7LiiKME4tNGKS15b7cMcWHKvXYhrnEvJeMSnk'
    client_secret = '3DjOe2o5Y8TwrCS1Q1BZMxU7J4anWrYHWOL2gftz'

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

    file_name = 'data_from_qb.json'
    fp = open(file_name,'a')
    startPosition = 1
    no_of_objects_fetched = 0
    flag = True
    while flag == True:
        selectQuery = f'select * from Invoice startPosition {startPosition}'
        sandbox_getURL = f"{sandboxURL}/v3/company/{realmID}/query?query={selectQuery}&minorversion=65"
        production_getURL = f"{productionURL}/v3/company/{realmID}/query?query={selectQuery}&minorversion=65"
        headers["Authorization"] = f"Bearer {access_token}"
        r = requests.get(sandbox_getURL,headers=headers)
        # r = requests.get(production_getURL,headers=headers)


        # print(r.status_code)
        if r.status_code == 200:
            parsed_data = r.json()

            if "QueryResponse" in parsed_data:
                if "Invoice" in parsed_data["QueryResponse"]:
                    for element in parsed_data["QueryResponse"]["Invoice"]:
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


def mapping_func(invoice_from_qb):
    # Term -> "payment_terms_label"
    term_dict = dict()
    term_dict["5"] = "50% Advance Payment"
    term_dict["1"] = "Due on receipt"
    term_dict["2"] = "Net 15"
    term_dict["3"] = "Net 30"
    term_dict["4"] = "Net 60"


    # taxcode_list = ['54', '62', '52', '13', '55', '58', '66', '70', '53', '57', '59', '65', '68']
    taxcode_to_id = dict()
    taxcode_to_id["13"] = "1208528000000016163"
    taxcode_to_id["11"] = "1208528000000016159"
    taxcode_to_id["19"] = "1208528000000016151"
    taxcode_to_id["7"] = "1208528000000016155"
    taxcode_to_id["3"] = "1208528000000016167"
    taxcode_to_id["6"] = "1208528000000016091"
    taxcode_to_id["16"] = "1208528000000016095"
    taxcode_to_id["4"] = "1208528000000016097"
    taxcode_to_id["17"] = "1208528000000016099"
    taxcode_to_id["21"] = "1208528000000016093"
    # taxcode_to_id["25"] = ""
    taxcode_to_id["15"] = ""
    

    # taxcode_dict = dict()
    # taxcode_dict["18"] = "0% GST"
    # taxcode_dict["15"] = "0% IGST"
    # taxcode_dict["26"] = "0.25% GST"
    # taxcode_dict["24"] = "0.25% IGST"
    # taxcode_dict["17"] = "12.0% GST"
    # taxcode_dict["19"] = "12.0% IGST"
    # taxcode_dict["7"] = "12.36% ST"
    # taxcode_dict["8"] = "14.0% VAT"
    # taxcode_dict["2"] = "14.00% ST"
    # taxcode_dict["9"] = "14.5% ST"
    # taxcode_dict["6"] = "15.0% ST"
    # taxcode_dict["21"] = "18.0% GST"
    # taxcode_dict["13"] = "18.0% IGST"
    # taxcode_dict["5"] = "2.0% CST"
    # taxcode_dict["16"] = "28.0% GST"
    # taxcode_dict["20"] = "28.0% IGST"
    # taxcode_dict["25"] = "3.0% GST"
    # taxcode_dict["23"] = "3.0% IGST"
    # taxcode_dict["3"] = "4.0% VAT"
    # taxcode_dict["12"] = "5.0% GST"
    # taxcode_dict["22"] = "5.0% IGST"
    # taxcode_dict["10"] = "5.0% VAT"
    # taxcode_dict["28"] = "6.0% GST"
    # taxcode_dict["27"] = "6.0% IGST"
    # taxcode_dict["14"] = "Exempt GST"
    # taxcode_dict["11"] = "Exempt IGST"
    # taxcode_dict["4"] = "Out of Scope"

    tax_rate_fout = open('tax_id_and_name_PR.json')
    tax_rate_details = json.load(tax_rate_fout)

    items_from_zohofout = open('data_from_zoho/item_details_PR.json')
    items_from_zoho = json.load(items_from_zohofout)
    contacts_from_zohofout = open('data_from_zoho/contact_details_PR.json')
    contacts_from_zoho = json.load(contacts_from_zohofout)
    chart_of_accounts_from_zohofout = open('data_from_zoho/coa_details_PR.json')
    chart_of_accounts_from_zoho = json.load(chart_of_accounts_from_zohofout)

    null_value = None

    tds_section_dict = dict()
    tds_section_dict["20"] = ["194J-(1)-Fees for Professinal and Technical Services","1208528000000097009"]
    # tds_section_dict["21"] = ["194J-(2)-Remuneration to Director",""]
    tds_section_dict["0"] = ["",""]

    mapping_dict = dict()

    if "DocNumber" in invoice_from_qb:
        # invoice_number is string
        mapping_dict["invoice_number"] = invoice_from_qb["DocNumber"]
    else:
        mapping_dict["invoice_number"] = invoice_from_qb["TxnDate"]

    if "TxnDate" in invoice_from_qb:
        # invoice_number is string
        # mapping_dict["invoice_date"] = invoice_from_qb["TxnDate"]
        mapping_dict["date"] = invoice_from_qb["TxnDate"]

    else:
        # mapping_dict["invoice_date"] = null_value
        mapping_dict["date"] = invoice_from_qb["TxnDate"]


    # CustomField

    # Definition Id 0
    # cf_id_0_dict = dict()
    # # mapping_dict["cf_id_0_name"] = invoice_from_qb["CustomField"][0]["Name"]
    # # cf_id_0_dict["customfield_id"] = "127706000001666001"
    # # cf_id_0_dict["customfield_id"] = "127706000001666001"
    # cf_id_0_dict["label"] = 'Month(s)/Onetime'
    # if "StringValue" in invoice_from_qb["CustomField"][0]:
    #     # mapping_dict["cf_id_0_value"] = invoice_from_qb["CustomField"][0]["StringValue"]
    #     cf_id_0_dict["value"] = invoice_from_qb["CustomField"][0]["StringValue"]
    # else:
    #     # mapping_dict["cf_id_0_value"] = null_value
    #     cf_id_0_dict["value"] = null_value


    # cf_id_1_dict = dict()
    # # mapping_dict["cf_id_1_name"] = invoice_from_qb["CustomField"][1]["Name"]
    # # cf_id_1_dict["customfield_id"] = "127706000001666005"
    # cf_id_1_dict['label'] = 'PO No'
    # if "StringValue" in invoice_from_qb["CustomField"][1]:
    #     # mapping_dict["cf_id_1_value"] = invoice_from_qb["CustomField"][1]["StringValue"]
    #     cf_id_1_dict["value"] = invoice_from_qb["CustomField"][1]["StringValue"]
    # else:
    #     # mapping_dict["cf_id_1_value"] = null_value
    #     cf_id_1_dict["value"] = null_value

        
    # cf_id_2_dict = dict()
    # # mapping_dict["cf_id_2_name"] = invoice_from_qb["CustomField"][2]["Name"]
    # # cf_id_2_dict["customfield_id"] = "127706000001666009"
    # cf_id_2_dict["label"] = 'No of months'
    # if "StringValue" in invoice_from_qb["CustomField"][2]:
    #     # mapping_dict["cf_id_2_value"] = invoice_from_qb["CustomField"][2]["StringValue"]
    #     cf_id_2_dict["value"] = invoice_from_qb["CustomField"][2]["StringValue"]
    # else:
    #     # mapping_dict["cf_id_2_value"] = null_value
    #     cf_id_2_dict["value"] = null_value
    
    # cf_id_3_dict = dict()
    # cf_id_3_dict["label"] = 'Department'
    # if "DepartmentRef" in invoice_from_qb:
    #     cf_id_3_dict["value"] = invoice_from_qb["DepartmentRef"]["name"]
    # else:
    #     cf_id_3_dict["value"] = null_value
    
    # cf_id_4_dict = dict()
    # cf_id_4_dict["label"] = 'Class'
    # if "ClassRef" in invoice_from_qb:
    #     cf_id_4_dict["value"] = invoice_from_qb["ClassRef"]["name"]
    # else:
    #     cf_id_4_dict["value"] = null_value


    custom_field_list = list()
    # custom_field_list.append(cf_id_0_dict)
    # custom_field_list.append(cf_id_1_dict)
    # custom_field_list.append(cf_id_2_dict)
    # custom_field_list.append(cf_id_3_dict)
    # custom_field_list.append(cf_id_4_dict)

    mapping_dict["custom_fields"] = custom_field_list

    print(invoice_from_qb["Id"])
    mapping_dict["id_from_qb"] = invoice_from_qb["Id"]

    line_items_list = list()
    tds_mapping_dict = dict()
    
    if "Line" in invoice_from_qb:
        qb_line_items = invoice_from_qb["Line"]

        my_item_list = list()

        for item in qb_line_items:
            # item_id is string

            my_item_dict = dict()

            detail_type = item["DetailType"]

            if detail_type == "SalesItemLineDetail":

                my_item_dict["description"] = null_value
                if "Description" in item:
                    my_item_dict["description"] = item["Description"]

                # my_item_dict["hsn_or_sac"] = "We will get from item_id"
                # WE WILL GET item_id FROM item_name
                # my_item_dict["item_name"] = item["SalesItemLineDetail"]["ItemRef"]["name"]
                # print(invoice_from_qb["Id"])
                if "name" in item["SalesItemLineDetail"]["ItemRef"]:
                    item_name = item["SalesItemLineDetail"]["ItemRef"]["name"].split(":")[-1]
                    my_item_dict["item_id"] = items_from_zoho[item_name]
                else:
                    # my_item_dict["item_id"] = item["SalesItemLineDetail"]["ItemRef"]["value"]
                    # print(invoice_from_qb["Id"])
                    continue
                
                if "UnitPrice" in item["SalesItemLineDetail"]:
                    my_item_dict["rate"] = item["SalesItemLineDetail"]["UnitPrice"]
                else:
                    my_item_dict["rate"] = null_value

                if "Qty" in item["SalesItemLineDetail"]:
                    my_item_dict["quantity"] = item["SalesItemLineDetail"]["Qty"]
                else:
                    my_item_dict["quantity"] = null_value

                if my_item_dict["rate"] is None or my_item_dict["quantity"] is None:
                    my_item_dict["quantity"] = 1
                    my_item_dict["rate"] = item["Amount"]
                    # print(invoice_from_qb["Id"])

                if my_item_dict["quantity"] < 0:
                    my_item_dict["quantity"] *= -1
                    my_item_dict["rate"] *= -1

                my_item_dict["discount_amount"] = null_value
                if "DiscountAmt" in item["SalesItemLineDetail"]:
                    my_item_dict["discount_amount"] = item["SalesItemLineDetail"]["DiscountAmt"]

                if "TaxCodeRef" in item["SalesItemLineDetail"]:
                    tax_code_value = taxcode_to_id[item["SalesItemLineDetail"]["TaxCodeRef"]["value"]]
                    if tax_code_value == '15':
                        my_item_dict["gst_treatment_code"] = "out_of_scope"
                    else:
                        my_item_dict["tax_id"] = taxcode_to_id[item["SalesItemLineDetail"]["TaxCodeRef"]["value"]]
                else:
                    my_item_dict["gst_treatment_code"] = "out_of_scope"
            # elif detail_type == "SubTotalLineDetail":
            #     # amount = item["Amount"]
            #     my_item_dict["amount"] = item["Amount"]
            # elif detail_type == "DiscountLineDetail":
            #     # percent_based_or_not = item["PercentBased"]
            #     my_item_dict["discount_percent_based_or_not"] = item["PercentBased"]
            elif detail_type == "TDSLineDetail":
                # is_tds_available = True
                tds_amount = item["Amount"]

                if not tds_amount:
                    # if tds_amount is 0
                    continue
                if "TDSSectionTypeId" in item["TDSLineDetail"]:
                    tds_section_type_id = item["TDSLineDetail"]["TDSSectionTypeId"]
                
                    tds_amount = item["Amount"]
                    if tds_amount:
                        tds_tax_name = tds_section_dict[str(tds_section_type_id)][0]
                        tds_tax_id = tds_section_dict[str(tds_section_type_id)][1]
                
                        # "tds_amount": 1875.0,
                        # "tax_account_id": "",
                        # "tds_tax_id": "424818000000010036",
                        # "tds_tax_name": "Professional Fees (10%)"
                        # my_item_dict["tds_detail_section_type_id"] = item["TDSLineDetail"]["TDSSectionTypeId"]

                        # mapping_dict["tds_amount"] = tds_amount
                        mapping_dict["tds_tax_name"] = tds_tax_name
                        mapping_dict["tds_tax_id"] = tds_tax_id

            my_item_list.append(my_item_dict)


    # mapping_dict["line_list"] = my_item_list
    
    my_tax_line_list = list()
    # if "TxnTaxDetail" in invoice_from_qb:
    #     # mapping_dict["total_tax"] = invoice_from_qb["TxnTaxDetail"]["TotalTax"]

    #     if "TaxLine" in invoice_from_qb["TxnTaxDetail"]:

    #         tax_line = invoice_from_qb["TxnTaxDetail"]["TaxLine"]
    #         for tax_item in tax_line:
    #             my_tax_item_dict = dict()

    #             # my_tax_item_dict["tax_amount"] = tax_item["Amount"]
    #             my_tax_item_dict["rate"] = tax_item["Amount"]
    #             my_tax_item_dict["quantity"] = 1

    #             tax_detail_type = tax_item["DetailType"]

    #             if tax_detail_type == "TaxLineDetail":

    #                 tax_name = tax_rate_details[tax_item["TaxLineDetail"]["TaxRateRef"]["value"]][0]
    #                 my_tax_item_dict["account_id"] = chart_of_accounts_from_zoho[tax_name]

    #                 my_tax_item_dict["description"] = tax_name
    #                 # my_tax_item_dict["tax_name"] = tax_rate_details[tax_item["TaxLineDetail"]["TaxRateRef"]["value"]]
    #                 # my_tax_item_dict["net_amount_taxable"] = tax_item["TaxLineDetail"]["NetAmountTaxable"]

    #                 my_tax_item_dict["gst_treatment_code"] = "out_of_scope"


    #             my_item_list.append(my_tax_item_dict)



    # if tds_mapping_dict and tds_mapping_dict["description"]:
    #     my_item_list.append(tds_mapping_dict)

    # mapping_dict["tax_detail_list"] = my_tax_line_list
    cleaned_my_item_list = [item for item in my_item_list if item]

    mapping_dict["line_items"] = cleaned_my_item_list

    # From customer_name we will get the customer_id
    if "CustomerRef" in invoice_from_qb:
        # mapping_dict["customer_name"] = invoice_from_qb["CustomerRef"]["name"]
        customer_name = invoice_from_qb["CustomerRef"]["name"]

        mapping_dict["customer_id"] = contacts_from_zoho[customer_name]
    else:
        mapping_dict["customer_name"] = null_value

    # Search invoices by due date. Default date format is yyyy-mm-dd
    if "DueDate" in invoice_from_qb:
        mapping_dict["due_date"] = invoice_from_qb["DueDate"]
    else:
        mapping_dict["due_date"] = null_value

    if "ShipAddr" in invoice_from_qb:
        mapping_dict["place_of_supply"] = invoice_from_qb["ShipAddr"]["CountrySubDivisionCode"]
    else:
        mapping_dict["place_of_supply"] = null_value

    # mapping_dict["status"] = "sent"

    customer_notes = ""
    if "PrivateNote" in invoice_from_qb:
        customer_notes += invoice_from_qb["PrivateNote"]

    if "CustomerMemo" in invoice_from_qb:
        customer_notes += ' ' + invoice_from_qb["CustomerMemo"]["value"]

    mapping_dict["notes"] = customer_notes

    # During create invoice there is no field for
    # "sub_total", "total", "tax_total"
    # -----------------------------------------------------------------------
    # if "HomeTotalAmt" in invoice_from_qb:
    #     mapping_dict["sub_total_home_amount"] = invoice_from_qb["HomeTotalAmt"]
    # else:
    #     mapping_dict["sub_total_home_amount"] = null_value
    
    # if "TotalAmt" in invoice_from_qb:
    #     mapping_dict["total_amount"] = invoice_from_qb["TotalAmt"]
    # else:
    #     mapping_dict["total_amount"] = null_value
    
    # -----------------------------------------------------------------------

    if "SalesTermRef" in invoice_from_qb:
        mapping_dict["payment_terms_label"] = term_dict[invoice_from_qb["SalesTermRef"]["value"]]
    else:
        mapping_dict["payment_terms_label"] = null_value

    if "ExchangeRate" in invoice_from_qb:
        mapping_dict["exchange_rate"] = invoice_from_qb["ExchangeRate"]
    else:
        mapping_dict["exchange_rate"] = null_value

    return mapping_dict

# def for_excel():
#     fin = open("mapped.json")
#     parsed_data = json.load(fin)

#     invoice_list = list()
#     for invoice in parsed_data["Customer"]:
#         invoice_dict = dict()

#         invoice_number = invoice["invoice_number"]

#         for line_item in invoice["line_list"]:
#             if "item_name" in line_item:
#                 invoice_dict["invoice_number"] = invoice_number
#                 invoice_dict["item_name"] = line_item["item_name"]
#                 invoice_dict["rate"] = line_item["rate"]
#                 invoice_dict["quantity"] = line_item["quantity"]
#                 invoice_dict["discount_amount"] = line_item["discount_amount"]
#                 invoice_dict["tax_name"] = line_item["tax_name"]

#                 invoice_dict["customer_name"] = invoice["customer_name"]
#                 invoice_dict["exchange_rate"] = invoice["exchange_rate"]
#                 invoice_dict["payment_terms_label"] = invoice["payment_terms_label"]
#                 invoice_dict["due_date"] = invoice["due_date"]
#                 invoice_dict["sub_total_home_amount"] = invoice["sub_total_home_amount"]
#                 invoice_dict["total_amount"] = invoice["total_amount"]

#                 invoice_list.append(invoice_dict)


#     mapped_data = dict()
#     mapped_data["Invoice"] = invoice_list

#     mapped_json = json.dumps(mapped_data,indent=4)

#     with open("for_excel_mapped.json", "w") as outfile:
#         outfile.write(mapped_json)



def generate_post_json():

    # https://www.geeksforgeeks.org/read-json-file-using-python/
    # file_name = 'all_fetched_data_from_qb.json'
    # file_name = 'production_get.json'

    # file_name = '../excel/data_from_qb_2013_04_01_to_2017_06_30_invoice.json'
    # file_name = '../excel/failed_invoice.json'
    file_name = '../data_from_qb_invoice_pr.json'

    # file_name = 'test_invoice_data.json'

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
    mapped_data["Invoice"] = my_item_list

    mapped_json = json.dumps(mapped_data,indent=4)

    with open("mapped_inv_PR.json", "w") as outfile:
        outfile.write(mapped_json)

def for_duplicate_invoice_number(contact_id,dup_invoice_number):
    contacts_from_zohofout = open('data_from_zoho/contact_details_PR.json')
    contacts_from_zoho = json.load(contacts_from_zohofout)

    new_invoice_number = ""
    for k,v in contacts_from_zoho.items():
        if v == contact_id:
            new_invoice_number  = k.split(" ")[0] + dup_invoice_number
            break

    contacts_from_zohofout.close()

    return new_invoice_number

def new_invoice_number_gen(contact_id,dup_invoice_number):
    contacts_from_zohofout = open('data_from_zoho/contact_details_.json')
    contacts_from_zoho = json.load(contacts_from_zohofout)

    new_invoice_number = ""
    for k,v in contacts_from_zoho.items():
        if v == contact_id:
            new_invoice_number  = k.split(" ")[0][:3] + dup_invoice_number
            if len(new_invoice_number) > 16:
                new_invoice_number = k.split(" ")[0][0] + dup_invoice_number
            
            break

    contacts_from_zohofout.close()

    return new_invoice_number


# 'code' variable must be updated before running this function
def post_request_zoho():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # output_file_name = 'console_output_2013_to_2017.txt'
    # output_file_name_fout = open(output_file_name)

    # ZohoBooks.fullaccess.all
    # code = '1000.3f2187fa12c1465d48fab99ab199f937.619ab209c92d1634e7764f1c5b6ce6e7'
    # client_id = '1000.UR9FCNRIBAJ11TLABY8K4C0UAW14BP'
    # client_secret = 'e72b1a3f32e16117b3287974149f066ed1f13f0822'

    code = '1000.6e3f9cf65cac47fdfe03ea6fccdafda2.92604c0d54757c02f8b3100b9f46a188'
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
    

    response_save_file = open("saved_invoice_id_PR.txt","a")
    

    # refresh_token = parsed_data1["refresh_token"]
    # access_token = parsed_data1["access_token"]
    refresh_token = '1000.f54b294d5cf8be23fba547686283aa08.380170953bd57f19e9d6173e0687eadc'
    access_token = '1000.d080b787cd07491afe5cceb03c74921f.b7ae9f124fa6916ca87f8f5eab576426'
    # expires_in = parsed_data["expires_in"]

    # print(refresh_token)
    # print(access_token)

    response_save_file.write(f"ACCESS TOKEN {access_token} and REFRESH TOKEN {refresh_token}\n")

    organization_id = '60019790139'
    post_url = f'https://books.zoho.in/api/v3/invoices?organization_id={organization_id}'

    # f = open('mapped.json')
    # f = open('mapped1.json')
    # f = open('failed_mapped1.json')
    f = open('mapped_inv_PR.json')
    # f = open('failed_invoices1.json')
    # f = open('mapped2.json')



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

    for item in items_list["Invoice"]:
        original_invoice_number = item["invoice_number"]
        no_of_times_to_try = 0
        while True:
            print(f'Processing for invoice_number: {item["invoice_number"]}||{item["date"]}||{item["customer_id"]}....')
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
                # It means success
                break
            elif parsed_data3["code"] == 1001:
                """
                {
                    "code": 1001,
                    "message": "Invoice 2/BF02serv/2013-14 already exists"
                }
                """
                old_invoice_number = item["invoice_number"]
                new_invoice_number = for_duplicate_invoice_number(item["customer_id"],old_invoice_number)
                if not new_invoice_number:
                    # if new_invoice_number is EMPTY STRING
                    response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]} ## INVOICE_NUMBER {old_invoice_number} to NULL String returned\n')
                    break

                item["invoice_number"] = new_invoice_number
                response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]} ## INVOICE_NUMBER {old_invoice_number} to {item["invoice_number"]}\n')
                response_save_file.flush()

            elif parsed_data3["code"] == 71530:
                # Please ensure that the Invoice number does not exceed 16 characters. It can contain alphabets, numerals, hyphens(-), and/or slash(/).
                
                old_invoice_number = item["invoice_number"]
                # old_invoice_number = old_invoice_number.replace('-','')
                old_invoice_number = old_invoice_number.replace(' ','')
                if len(old_invoice_number) > 16:
                    new_invoice_number = new_invoice_number_gen(item["customer_id"],original_invoice_number)
                    new_invoice_number = new_invoice_number.replace('.','')
                    item["invoice_number"] = new_invoice_number
                else:
                    # Remove all the . from the string
                    item["invoice_number"] = old_invoice_number.replace('.','')
                    item["invoice_number"] = old_invoice_number.replace('_','')
                    # item["invoice_number"] = old_invoice_number.replace('-','')
                
                response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]} ## INVOICE_NUMBER {old_invoice_number} to {item["invoice_number"]}\n')
                response_save_file.flush()

            else:
                print(f'ERROR occurred: {id_from_qb}||{item["invoice_number"]}||{item["date"]}||{item["customer_id"]} was not able to be pushed')
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
def post_invoice_as_sent():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # output_file_name = 'console_output_2013_to_2017.txt'
    # output_file_name_fout = open(output_file_name)

    # ZohoBooks.fullaccess.all
    # code = '1000.3f2187fa12c1465d48fab99ab199f937.619ab209c92d1634e7764f1c5b6ce6e7'
    # client_id = '1000.UR9FCNRIBAJ11TLABY8K4C0UAW14BP'
    # client_secret = 'e72b1a3f32e16117b3287974149f066ed1f13f0822'

    client_id = '1000.WVUN689ZVG2LQONSCPA4AMBLU61PMX'
    client_secret = 'eacbaa6f3306186b1882e6bd1f819703b8df9cabdf'

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
    
    # refresh_token = parsed_data1["refresh_token"]
    # access_token = parsed_data1["access_token"]

    refresh_token = '1000.262182b6bc23c8a983ba1be6d30958c7.f89c89720f032b246a28106ea0ec37d0'
    access_token = '1000.8f0d3115276fea6f8a04cd10eb8555ef.3929361eee9bf28cbf57eecc60be54b7'
    
    # expires_in = parsed_data["expires_in"]

    # organization_id = '60015983411'
    organization_id = '60001574931'
    # post_url = f'https://books.zoho.in/api/v3/invoices?organization_id={organization_id}'

    # f = open('mapped.json')
    # f = open('leftover_mapped.json')
    f = open('invoice_id_details.json')

    items_list = json.load(f)
    # items_list = parsed_data2["Invoice"]

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_response_for_sent.txt","a")
    error_response_save_file = open("error_console_for_failed_response.txt","a")


    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")
    error_response_save_file.write(f"NEW WRITE STARTED: {dt_string}\n")

    for item,item_v in items_list.items():
        while True:
            post_url = f'https://books.zoho.in/api/v3/invoices/{item_v}/status/sent/?organization_id={organization_id}'
            print(f'Processing for invoice_number: {item}....')
            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(0.5)

            # param = dict()
            # param['JSONString'] = item
            # r2 = requests.post(post_url,headers=headers,data=param)

            # id_from_qb = item["id_from_qb"]
            id_from_qb = item

            # if "id_from_qb" in item:
            #     del item["id_from_qb"]

            r2 = requests.post(post_url,headers=headers)

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
                # response_save_file.write(f'{parsed_data3["invoice"]["invoice_id"]} : {item["invoice_number"]}\n')
                # response_save_file.write(f'{parsed_data3["invoice"]["invoice_id"]} : {id_from_qb}\n')
                response_save_file.write(f'{id_from_qb}\n')

                print(f'{id_from_qb} is successfully marked as sent')
                # It means success
                break
            else:
                print(f'ERROR occurred: {id_from_qb} was able to be pushed')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                error_response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]}\n')   
                break

        # print(f'Successfully created invoice named: {item["invoice_number"]}||{item["date"]}||{item["customer_id"]}')


# get_items_and_write_to_file()
# generate_post_json()
post_request_zoho()
# post_invoice_as_sent()



        

