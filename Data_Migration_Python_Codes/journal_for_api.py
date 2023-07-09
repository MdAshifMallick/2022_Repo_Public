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
    term_dict["1"] = "Due on receipt"
    term_dict["2"] = "Net 15"
    term_dict["3"] = "Net 30"
    term_dict["4"] = "Net 60"

    # taxcode_dict = dict()
    # taxcode_dict["36"] = "(sales)ST@14%+0.5%SBC+0.5%KKS+VAT@5.5%"
    # taxcode_dict["59"] = "0% GST"
    # taxcode_dict["56"] = "0% IGST"
    # taxcode_dict["74"] = "0.25% GST"
    # taxcode_dict["72"] = "0.25% IGST"
    # taxcode_dict["22"] = "0.5% Swachh Bharat Cess"
    # taxcode_dict["58"] = "12.0% GST"
    # taxcode_dict["60"] = "12.0% IGST"
    # taxcode_dict["4"] = "12.36% ST"
    # taxcode_dict["15"] = "12.5% CST - Inactive - Inactive"
    # taxcode_dict["38"] = "12.50% VAT Purchase"
    # taxcode_dict["40"] = "13.5% VAT"
    # taxcode_dict["16"] = "14% Service Tax - Inactive"
    # taxcode_dict["17"] = "14% ST & VAT"
    # taxcode_dict["20"] = "14%ST & 2%CST"
    # taxcode_dict["3"] = "14.0% VAT"
    # taxcode_dict["19"] = "14.00% ST"
    # taxcode_dict["26"] = "14.5% ST"
    # taxcode_dict["42"] = "14.5% VAT"
    # taxcode_dict["27"] = "15.0% ST"
    # taxcode_dict["62"] = "18.0% GST"
    # taxcode_dict["54"] = "18.0% IGST"
    # taxcode_dict["9"] = "2% CST"
    # taxcode_dict["50"] = "2% KVAT"
    # taxcode_dict["14"] = "2.0% CST"
    # taxcode_dict["41"] = "20% VAT KVAT"
    # taxcode_dict["37"] = "20%VAT"
    # taxcode_dict["57"] = "28.0% GST"
    # taxcode_dict["61"] = "28.0% IGST"
    # taxcode_dict["73"] = "3.0% GST"
    # taxcode_dict["71"] = "3.0% IGST"
    # taxcode_dict["2"] = "4.0% VAT"
    # taxcode_dict["53"] = "5.0% GST"
    # taxcode_dict["63"] = "5.0% IGST"
    # taxcode_dict["5"] = "5.0% VAT"
    # taxcode_dict["6"] = "5.5% VAT"
    # taxcode_dict["76"] = "6.0% GST"
    # taxcode_dict["75"] = "6.0% IGST"
    # taxcode_dict["55"] = "Exempt GST"
    # taxcode_dict["52"] = "Exempt IGST"
    # taxcode_dict["67"] = "GST Cess @ 36%"
    # taxcode_dict["64"] = "GST Cess @ 5%"
    # taxcode_dict["28"] = "KKS"
    # taxcode_dict["30"] = "KKS@0.5"
    # taxcode_dict["43"] = "MVAT-12.5%"
    # taxcode_dict["44"] = "MVAT-13.5%"
    # taxcode_dict["46"] = "MVAT-14.5%"
    # taxcode_dict["49"] = "MVAT-20%"
    # taxcode_dict["51"] = "MVAT-25%"
    # taxcode_dict["45"] = "MVAT-5%"
    # taxcode_dict["47"] = "MVAT-5.5%"
    # taxcode_dict["48"] = "MVAT-6%"
    # taxcode_dict["13"] = "Out of Scope"
    # taxcode_dict["65"] = "Purchase GST 33% - 28%GST+5%Cess"
    # taxcode_dict["68"] = "Purchase GST 64% - 28%GST+36%CESS"
    # taxcode_dict["66"] = "Sales GST 33% - 28%GST+5%Cess"
    # taxcode_dict["69"] = "Sales GST 64% - 28%GST+36%CESS"
    # taxcode_dict["70"] = "Sales* GST64% - 28%GST+36%CESS"
    # taxcode_dict["7"] = "Service Tax & VAT"
    # taxcode_dict["11"] = "Service Tax Old Rate"
    # taxcode_dict["12"] = "ST & CST"
    # taxcode_dict["8"] = "ST & VAT"
    # taxcode_dict["21"] = "ST&CST"
    # taxcode_dict["24"] = "ST&VAT"
    # taxcode_dict["25"] = "ST(new)&CST"
    # taxcode_dict["33"] = "ST+CST(17%)"
    # taxcode_dict["32"] = "ST+VAT(20.5%)"
    # taxcode_dict["34"] = "ST+VAT(20.5) New"
    # taxcode_dict["31"] = "ST14.5%+KKS0.5%+VAT5.5%"
    # taxcode_dict["29"] = "ST15%+VAT5.5%"
    # taxcode_dict["35"] = "ST@14%+0.5%SBC+0.5%KKS+VAT@5.5%"
    # taxcode_dict["10"] = "Test"
    # taxcode_dict["23"] = "UD_14.5% ST"
    # taxcode_dict["18"] = "VAT 14.5%"
    # taxcode_dict["39"] = "Vat @ 6%"

    tax_rate_fout = open('tax_id_and_name_flynow.json')
    tax_rate_details = json.load(tax_rate_fout)

    # items_from_zohofout = open('data_from_zoho/items_data_from_zoho.json')
    # items_from_zoho = json.load(items_from_zohofout)
    contacts_from_zohofout = open('data_from_zoho/contact_details_flynow.json')
    contacts_from_zoho = json.load(contacts_from_zohofout)
    chart_of_accounts_from_zohofout = open('data_from_zoho/coa_details_flynow.json')
    chart_of_accounts_from_zoho = json.load(chart_of_accounts_from_zohofout)

    null_value = None


    tds_section_dict = dict()
    # tds_section_dict["9"] = "194C(1)-Contracts"
    # tds_section_dict["20"] = "194J-(1)-Fees for Professinal and Technical Services"
    # tds_section_dict["21"] = "194J-(2)-Remuneration to Director"
    # tds_section_dict["0"] = null_value

    mapping_dict = dict()

    if "DocNumber" in invoice_from_qb:
        # invoice_number is string
        mapping_dict["bill_number"] = invoice_from_qb["DocNumber"]
    else:
        mapping_dict["bill_number"] = null_value

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
    # cf_id_0_dict["customfield_id"] = "127706000001666001"
    # if "StringValue" in invoice_from_qb["CustomField"][0]:
    #     # mapping_dict["cf_id_0_value"] = invoice_from_qb["CustomField"][0]["StringValue"]
    #     cf_id_0_dict["value"] = invoice_from_qb["CustomField"][0]["StringValue"]
    # else:
    #     # mapping_dict["cf_id_0_value"] = null_value
    #     cf_id_0_dict["value"] = null_value


    # cf_id_1_dict = dict()
    # # mapping_dict["cf_id_1_name"] = invoice_from_qb["CustomField"][1]["Name"]
    # cf_id_1_dict["customfield_id"] = "127706000001666005"
    # if "StringValue" in invoice_from_qb["CustomField"][1]:
    #     # mapping_dict["cf_id_1_value"] = invoice_from_qb["CustomField"][1]["StringValue"]
    #     cf_id_1_dict["value"] = invoice_from_qb["CustomField"][1]["StringValue"]
    # else:
    #     # mapping_dict["cf_id_1_value"] = null_value
    #     cf_id_1_dict["value"] = null_value

        
    # cf_id_2_dict = dict()
    # # mapping_dict["cf_id_2_name"] = invoice_from_qb["CustomField"][2]["Name"]
    # cf_id_2_dict["customfield_id"] = "127706000001666009"
    # if "StringValue" in invoice_from_qb["CustomField"][2]:
    #     # mapping_dict["cf_id_2_value"] = invoice_from_qb["CustomField"][2]["StringValue"]
    #     cf_id_2_dict["value"] = invoice_from_qb["CustomField"][2]["StringValue"]
    # else:
    #     # mapping_dict["cf_id_2_value"] = null_value
    #     cf_id_2_dict["value"] = null_value


    # custom_field_list = list()
    # custom_field_list.append(cf_id_0_dict)
    # custom_field_list.append(cf_id_1_dict)
    # custom_field_list.append(cf_id_2_dict)
    # mapping_dict["custom_fields"] = custom_field_list

    print(invoice_from_qb["Id"])
    mapping_dict["id_from_qb"] = invoice_from_qb["Id"]

    line_items_list = list()
    tds_mapping_dict = dict()
    
    flag_for_customer_vendor = False
    if "Line" in invoice_from_qb:
        qb_line_items = invoice_from_qb["Line"]

        my_item_list = list()
        
        for item in qb_line_items:
            # item_id is string

            cf_dict = dict()
            cf_dict["label"] = "Class"
            cf_dict["value"] = null_value

            my_item_dict = dict()

            detail_type = item["DetailType"]

            if detail_type == "JournalEntryLineDetail":

                my_item_dict["description"] = null_value
                if "Description" in item:
                    my_item_dict["description"] = item["Description"]

                account_name = item["JournalEntryLineDetail"]["AccountRef"]["name"]
                splitted_name_list = account_name.split(':')
                if len(splitted_name_list) == 1:
                    # No colon
                    account_name = splitted_name_list[0]
                else:
                    # Colon
                    account_name = splitted_name_list[-1]

                # my_item_dict["account_id"] = chart_of_accounts_from_zoho[account_name]
                account_id = chart_of_accounts_from_zoho.get(account_name)
                if account_id:
                    my_item_dict["account_id"] = account_id
                else:
                    print(account_name)

                if "EntityRef" in item["JournalEntryLineDetail"]:
                    flag_for_customer_vendor = True
            

                # if "ClassRef" in item["JournalEntryLineDetail"]:
                #     cf_dict["value"] = item["JournalEntryLineDetail"]["ClassRef"]["name"]

                # my_item_dict["item_custom_fields"] = [cf_dict]

                # item["SalesItemLineDetail"]["TaxCodeRef"]["value"] gives the tax_id
                # tax_id is string
                # my_item_dict["tax_id"] = 'We will get very soon ...'

                # if "TaxCodeRef" in item["SalesItemLineDetail"]:
                #     my_item_dict["tax_name"] = taxcode_dict[item["SalesItemLineDetail"]["TaxCodeRef"]["value"]]
                # else:
                #     my_item_dict["tax_name"] = null_value
                
                # my_item_dict["tax_name"] = term_dict[item["SalesItemLineDetail"]["TaxCodeRef"]["value"]]

                # my_item_dict["tax_name"] = 'We will get very soon ...'
                # my_item_dict["tax_type"] = 'We will get very soon ...'
                # my_item_dict["tax_percentage"] = 'We will get very soon ...'

            # elif detail_type == "SubTotalLineDetail":
            #     # amount = item["Amount"]
            #     my_item_dict["amount"] = item["Amount"]
            # elif detail_type == "DiscountLineDetail":
            #     # percent_based_or_not = item["PercentBased"]
            #     my_item_dict["discount_percent_based_or_not"] = item["PercentBased"]
            # elif detail_type == "TDSLineDetail":

            #     tds_section_type_id = item["TDSLineDetail"]["TDSSectionTypeId"]
            #     tds_mapping_dict["description"] = tds_section_dict[str(tds_section_type_id)]
            #     tds_mapping_dict["rate"] = -item["Amount"]

            #     # TDS receivable id is 951651000000014016
            #     tds_mapping_dict["account_id"] = "951651000000014016"

                # tds_section_type_id = item["TDSLineDetail"]["TDSSectionTypeId"]
                # my_item_dict["tds_detail_section_type_id"] = item["TDSLineDetail"]["TDSSectionTypeId"]


            my_item_list.append(my_item_dict)


    # mapping_dict["line_list"] = my_item_list
    
    # my_tax_line_list = list()
    if "TxnTaxDetail" in invoice_from_qb:
        # mapping_dict["total_tax"] = invoice_from_qb["TxnTaxDetail"]["TotalTax"]

        if "TaxLine" in invoice_from_qb["TxnTaxDetail"]:

            tax_line = invoice_from_qb["TxnTaxDetail"]["TaxLine"]
            for tax_item in tax_line:
                my_tax_item_dict = dict()

                # my_tax_item_dict["tax_amount"] = tax_item["Amount"]
                my_tax_item_dict["rate"] = tax_item["Amount"]
                my_tax_item_dict["quantity"] = 1

                tax_detail_type = tax_item["DetailType"]

                if tax_detail_type == "TaxLineDetail":

                    tax_name = tax_rate_details[tax_item["TaxLineDetail"]["TaxRateRef"]["value"]][0]
                    my_tax_item_dict["account_id"] = chart_of_accounts_from_zoho[tax_name]

                    my_tax_item_dict["description"] = tax_name
                    # my_tax_item_dict["tax_name"] = tax_rate_details[tax_item["TaxLineDetail"]["TaxRateRef"]["value"]]
                    # my_tax_item_dict["net_amount_taxable"] = tax_item["TaxLineDetail"]["NetAmountTaxable"]

                    my_tax_item_dict["gst_treatment_code"] = "out_of_scope"


                my_item_list.append(my_tax_item_dict)



    # if tds_mapping_dict and tds_mapping_dict["description"]:
    #     my_item_list.append(tds_mapping_dict)

    # mapping_dict["tax_detail_list"] = my_tax_line_list
    cleaned_my_item_list = [item for item in my_item_list if item]

    mapping_dict["line_items"] = cleaned_my_item_list

    # From customer_name we will get the customer_id
    if "VendorRef" in invoice_from_qb:
        # mapping_dict["customer_name"] = invoice_from_qb["VendorRef"]["name"]
        customer_name = invoice_from_qb["VendorRef"]["name"]
        mapping_dict["vendor_id"] = contacts_from_zoho[customer_name]
    else:
        mapping_dict["vendor_id"] = null_value

    # Search invoices by due date. Default date format is yyyy-mm-dd
    if "DueDate" in invoice_from_qb:
        mapping_dict["due_date"] = invoice_from_qb["DueDate"]
    else:
        mapping_dict["due_date"] = null_value

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

    if flag_for_customer_vendor:
        mapping_dict = []

    return mapping_dict

count_missing_coa_list = list()
journal_entry_count = 1

def mapping_funcV2(invoice_from_qb):

    global journal_entry_count

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

    # taxcode_dict = dict()
    # taxcode_dict["36"] = "(sales)ST@14%+0.5%SBC+0.5%KKS+VAT@5.5%"
    # taxcode_dict["59"] = "0% GST"
    # taxcode_dict["56"] = "0% IGST"
    # taxcode_dict["74"] = "0.25% GST"
    # taxcode_dict["72"] = "0.25% IGST"
    # taxcode_dict["22"] = "0.5% Swachh Bharat Cess"
    # taxcode_dict["58"] = "12.0% GST"
    # taxcode_dict["60"] = "12.0% IGST"
    # taxcode_dict["4"] = "12.36% ST"
    # taxcode_dict["15"] = "12.5% CST - Inactive - Inactive"
    # taxcode_dict["38"] = "12.50% VAT Purchase"
    # taxcode_dict["40"] = "13.5% VAT"
    # taxcode_dict["16"] = "14% Service Tax - Inactive"
    # taxcode_dict["17"] = "14% ST & VAT"
    # taxcode_dict["20"] = "14%ST & 2%CST"
    # taxcode_dict["3"] = "14.0% VAT"
    # taxcode_dict["19"] = "14.00% ST"
    # taxcode_dict["26"] = "14.5% ST"
    # taxcode_dict["42"] = "14.5% VAT"
    # taxcode_dict["27"] = "15.0% ST"
    # taxcode_dict["62"] = "18.0% GST"
    # taxcode_dict["54"] = "18.0% IGST"
    # taxcode_dict["9"] = "2% CST"
    # taxcode_dict["50"] = "2% KVAT"
    # taxcode_dict["14"] = "2.0% CST"
    # taxcode_dict["41"] = "20% VAT KVAT"
    # taxcode_dict["37"] = "20%VAT"
    # taxcode_dict["57"] = "28.0% GST"
    # taxcode_dict["61"] = "28.0% IGST"
    # taxcode_dict["73"] = "3.0% GST"
    # taxcode_dict["71"] = "3.0% IGST"
    # taxcode_dict["2"] = "4.0% VAT"
    # taxcode_dict["53"] = "5.0% GST"
    # taxcode_dict["63"] = "5.0% IGST"
    # taxcode_dict["5"] = "5.0% VAT"
    # taxcode_dict["6"] = "5.5% VAT"
    # taxcode_dict["76"] = "6.0% GST"
    # taxcode_dict["75"] = "6.0% IGST"
    # taxcode_dict["55"] = "Exempt GST"
    # taxcode_dict["52"] = "Exempt IGST"
    # taxcode_dict["67"] = "GST Cess @ 36%"
    # taxcode_dict["64"] = "GST Cess @ 5%"
    # taxcode_dict["28"] = "KKS"
    # taxcode_dict["30"] = "KKS@0.5"
    # taxcode_dict["43"] = "MVAT-12.5%"
    # taxcode_dict["44"] = "MVAT-13.5%"
    # taxcode_dict["46"] = "MVAT-14.5%"
    # taxcode_dict["49"] = "MVAT-20%"
    # taxcode_dict["51"] = "MVAT-25%"
    # taxcode_dict["45"] = "MVAT-5%"
    # taxcode_dict["47"] = "MVAT-5.5%"
    # taxcode_dict["48"] = "MVAT-6%"
    # taxcode_dict["13"] = "Out of Scope"
    # taxcode_dict["65"] = "Purchase GST 33% - 28%GST+5%Cess"
    # taxcode_dict["68"] = "Purchase GST 64% - 28%GST+36%CESS"
    # taxcode_dict["66"] = "Sales GST 33% - 28%GST+5%Cess"
    # taxcode_dict["69"] = "Sales GST 64% - 28%GST+36%CESS"
    # taxcode_dict["70"] = "Sales* GST64% - 28%GST+36%CESS"
    # taxcode_dict["7"] = "Service Tax & VAT"
    # taxcode_dict["11"] = "Service Tax Old Rate"
    # taxcode_dict["12"] = "ST & CST"
    # taxcode_dict["8"] = "ST & VAT"
    # taxcode_dict["21"] = "ST&CST"
    # taxcode_dict["24"] = "ST&VAT"
    # taxcode_dict["25"] = "ST(new)&CST"
    # taxcode_dict["33"] = "ST+CST(17%)"
    # taxcode_dict["32"] = "ST+VAT(20.5%)"
    # taxcode_dict["34"] = "ST+VAT(20.5) New"
    # taxcode_dict["31"] = "ST14.5%+KKS0.5%+VAT5.5%"
    # taxcode_dict["29"] = "ST15%+VAT5.5%"
    # taxcode_dict["35"] = "ST@14%+0.5%SBC+0.5%KKS+VAT@5.5%"
    # taxcode_dict["10"] = "Test"
    # taxcode_dict["23"] = "UD_14.5% ST"
    # taxcode_dict["18"] = "VAT 14.5%"
    # taxcode_dict["39"] = "Vat @ 6%"

    # tax_rate_fout = open('tax_id_and_name.json')
    # tax_rate_details = json.load(tax_rate_fout)

    # items_from_zohofout = open('data_from_zoho/items_data_from_zoho.json')
    # items_from_zoho = json.load(items_from_zohofout)
    # contacts_from_zohofout = open('data_from_zoho/contacts_data_from_zoho.json')
    # contacts_from_zoho = json.load(contacts_from_zohofout)
    # chart_of_accounts_from_zohofout = open('data_from_zoho/chart_of_accounts_data_from_zoho.json')
    chart_of_accounts_from_zohofout = open('data_from_zoho/new_chart_of_accounts_data_from_zoho.json')
    chart_of_accounts_from_zoho = json.load(chart_of_accounts_from_zohofout)

    currency_from_zohofout = open('data_from_zoho/currency_data_from_zoho.json')
    currency_from_zoho = json.load(currency_from_zohofout)

    # chart_of_accounts_from_zohofout = open('data_from_zoho/my_coa_data_from_zoho.json')
    # chart_of_accounts_from_zoho = json.load(chart_of_accounts_from_zohofout)

    null_value = None


    # taxcode_to_id = dict()
    # taxcode_to_id["54"] = "127706000000863117"
    # taxcode_to_id["62"] = "127706000000863129"
    # taxcode_to_id["52"] = "127706000000863037"
    # taxcode_to_id["60"] = "127706000000863101"
    # taxcode_to_id["63"] = "127706000000863085"
    # taxcode_to_id["64"] = "127706000000863097"
    # taxcode_to_id["56"] = "127706000000863037"
    # taxcode_to_id["13"] = ""
    # taxcode_to_id["NON"] = ""
    # taxcode_to_id["55"] = "127706000000863073"
    # taxcode_to_id["58"] = "127706000000863113"
    # taxcode_to_id["66"] = "127706000002291415"
    # taxcode_to_id["70"] = "127706000002291460"
    # taxcode_to_id["53"] = "127706000000863097"
    # taxcode_to_id["57"] = "127706000000863145"
    # taxcode_to_id["59"] = "127706000000863073"
    # taxcode_to_id["65"] = "127706000002291415"
    # taxcode_to_id["68"] = "127706000002291460"

    mapping_dict = dict()

    flag_for_customer_vendor = False

    # mapping_dict["ignore_auto_number_generation"] = False

    if "TxnDate" in invoice_from_qb:
        # invoice_number is string
        # mapping_dict["invoice_date"] = invoice_from_qb["TxnDate"]
        mapping_dict["journal_date"] = invoice_from_qb["TxnDate"]
    else:
        # mapping_dict["invoice_date"] = null_value
        mapping_dict["journal_date"] = invoice_from_qb["TxnDate"]

    extracted_year = mapping_dict["journal_date"].split('-')[0]

    if "DocNumber" in invoice_from_qb:
        # invoice_number is string
        mapping_dict["entry_number"] = invoice_from_qb["DocNumber"]
        mapping_dict["journal_number_prefix"] = f'{invoice_from_qb["DocNumber"]}-'
        mapping_dict["journal_number_suffix"] = f"{journal_entry_count}"
        # mapping_dict["journal_number_suffix"] = f"{invoice_from_qb['Id']}"
    else:
        mapping_dict["entry_number"] = f"JE_{journal_entry_count}-{extracted_year}"
        mapping_dict["journal_number_prefix"] = f"JE_{journal_entry_count}-{extracted_year}-"
        mapping_dict["journal_number_suffix"] = f"{journal_entry_count}"

        # mapping_dict["entry_number"] = f"JE_{invoice_from_qb['Id']}-{extracted_year}"
        # mapping_dict["journal_number_prefix"] = f"JE_{invoice_from_qb['Id']}-{extracted_year}-"
        # mapping_dict["journal_number_suffix"] = f"{invoice_from_qb['Id']}"
    
    journal_entry_count = journal_entry_count + 1

    if len(mapping_dict["journal_number_prefix"] + mapping_dict["journal_number_suffix"]) > 16:
        length_of_journal_number_suffix = len(mapping_dict["journal_number_suffix"])
        length_of_journal_number_prefix = len(mapping_dict["journal_number_prefix"])

        upto_length = 16 - (length_of_journal_number_prefix + length_of_journal_number_suffix)
        if upto_length < 0:
            upto_length = abs(upto_length)

        # print(upto_length)
        new_journal_number_prefix = mapping_dict["journal_number_prefix"][:16-upto_length]
        # print(f'{mapping_dict["journal_number_prefix"]}------{new_journal_number_prefix}')
        mapping_dict["journal_number_prefix"] = new_journal_number_prefix

    if len(mapping_dict["journal_number_prefix"] + mapping_dict["journal_number_suffix"]) > 16:
        # pass
        print(f'{mapping_dict["journal_number_prefix"]}------{mapping_dict["journal_number_suffix"]}')


    mapping_dict["currency_id"] = null_value
    if "CurrencyRef" in invoice_from_qb:
        currency_id = currency_from_zoho.get(invoice_from_qb["CurrencyRef"]["value"])
        if currency_id:
            mapping_dict["currency_id"] = currency_from_zoho[invoice_from_qb["CurrencyRef"]["value"]]
        else:
            print(f'{invoice_from_qb["CurrencyRef"]["value"]} KEY ERROR')
            mapping_dict["currency_id"] = "SGD ERROR"
            return None


    # CustomField

    # Definition Id 0
    cf_id_0_dict = dict()
    # mapping_dict["cf_id_0_name"] = invoice_from_qb["CustomField"][0]["Name"]
    cf_id_0_dict["label"] = "Journal Number"
    cf_id_0_dict["value"] = mapping_dict["entry_number"]

    # cf_id_1_dict = dict()
    # # mapping_dict["cf_id_1_name"] = invoice_from_qb["CustomField"][1]["Name"]
    # cf_id_1_dict["customfield_id"] = "127706000001666005"
    # if "StringValue" in invoice_from_qb["CustomField"][1]:
    #     # mapping_dict["cf_id_1_value"] = invoice_from_qb["CustomField"][1]["StringValue"]
    #     cf_id_1_dict["value"] = invoice_from_qb["CustomField"][1]["StringValue"]
    # else:
    #     # mapping_dict["cf_id_1_value"] = null_value
    #     cf_id_1_dict["value"] = null_value

        
    # cf_id_2_dict = dict()
    # # mapping_dict["cf_id_2_name"] = invoice_from_qb["CustomField"][2]["Name"]
    # cf_id_2_dict["customfield_id"] = "127706000001666009"
    # if "StringValue" in invoice_from_qb["CustomField"][2]:
    #     # mapping_dict["cf_id_2_value"] = invoice_from_qb["CustomField"][2]["StringValue"]
    #     cf_id_2_dict["value"] = invoice_from_qb["CustomField"][2]["StringValue"]
    # else:
    #     # mapping_dict["cf_id_2_value"] = null_value
    #     cf_id_2_dict["value"] = null_value


    custom_field_list = list()
    custom_field_list.append(cf_id_0_dict)
    # custom_field_list.append(cf_id_1_dict)
    # custom_field_list.append(cf_id_2_dict)
    mapping_dict["custom_fields"] = custom_field_list

    # print(invoice_from_qb["Id"])
    mapping_dict["id_from_qb"] = invoice_from_qb["Id"]

    line_items_list = list()
    tds_mapping_dict = dict()
    
    # flag_for_customer_vendor = False

    if "Line" in invoice_from_qb:
        qb_line_items = invoice_from_qb["Line"]

        my_item_list = list()
        
        for item in qb_line_items:
            # item_id is string

            # cf_dict = dict()
            # cf_dict["label"] = "Class"
            # cf_dict["value"] = null_value

            my_item_dict = dict()

            detail_type = item["DetailType"]
            flag_for_customer_vendor = False
            if detail_type == "JournalEntryLineDetail":

                # if "EntityRef" in item["JournalEntryLineDetail"]:
                #     flag_for_customer_vendor = True
                #     break

                entity_details = ''
                if "Entity" in item["JournalEntryLineDetail"]:
                    entity_type = item["JournalEntryLineDetail"]["Entity"]["Type"]
                    entity_name = item["JournalEntryLineDetail"]["Entity"]["EntityRef"]["name"]

                    entity_details = f'[ {entity_type} : {entity_name} ]'

                    # print(entity_details)



                found_class_name = False
                if "ClassRef" in item["JournalEntryLineDetail"]:
                    class_name = item["JournalEntryLineDetail"]["ClassRef"]["name"]
                    found_class_name = True
                
                found_department_name = False
                if "DepartmentRef" in item["JournalEntryLineDetail"]:
                    department_name = item["JournalEntryLineDetail"]["DepartmentRef"]["name"]
                    found_department_name = True

                extra_description = ''
                if found_class_name and found_department_name:
                    extra_description = f"[Class: {class_name} - Department: {department_name}]"
                elif found_class_name:
                    extra_description = f"[Class: {class_name}]"
                elif found_department_name:
                    extra_description = f"[Department: {department_name}]"

                my_item_dict["description"] = null_value
                if "Description" in item:
                    gotten_description = item["Description"]
                    if extra_description:
                        my_item_dict["description"] = gotten_description + ' ' + extra_description + ' ' + entity_details
                    else:
                        my_item_dict["description"] = gotten_description + ' ' + entity_details
                
                my_item_dict["amount"] = null_value
                if "Amount" in item:
                    item_amount = item["Amount"]
                    if item_amount == 0.0:
                        continue
                    my_item_dict["amount"] = item["Amount"]

                posting_type = item["JournalEntryLineDetail"]["PostingType"]
                if posting_type == "Credit":
                    my_item_dict["debit_or_credit"] = "credit"
                elif posting_type == "Debit":
                    my_item_dict["debit_or_credit"] = "debit"
                else:
                    my_item_dict["debit_or_credit"] = null_value

                account_name = item["JournalEntryLineDetail"]["AccountRef"]["name"]
                splitted_name_list = account_name.split(':')
                if len(splitted_name_list) == 1:
                    # No colon
                    account_name = splitted_name_list[0]
                else:
                    # Colon
                    account_name = splitted_name_list[-1]
                
                # list_to_ignore1 = ['Accounts Receivable (Debtors) - USD', 'CGST Payable', 'SGST Payable', 'IGST Payable', 'Accounts Payable (Creditors) - CAD', 'Input IGST Tax RCM', 'Output CGST Tax RCM', 'Accounts Payable (Creditors) - GBP', 'Accounts Payable (Creditors) - SGD', 'CST Payable', 'Output SGST Tax RCM', 'Input CGST Tax RCM', 'Input SGST Tax RCM', 'Output CST 2%', 'Accounts Payable (Creditors) - EUR']
                # list_to_ignore2 = ['Accounts Receivable (Debtors)', 'Accounts Payable (Creditors)', 'Accounts Payable (Creditors) - USD', 'Advance from Customers (deleted)','Accounts Payable (Creditors) - GBP']
                list_to_ignore3 = ['Accounts Receivable (Debtors)','Provision for Doubtful Debts','Provision for Doubtful debts','','Accounts Payable (Creditors)','Accounts Payable (Creditors) - USD','Accounts Payable (Creditors) - GBP','Accounts Payable (Creditors) - SGD','Input CGST Tax RCM', 'Input SGST Tax RCM', 'Output CGST Tax RCM', 'Output SGST Tax RCM']
                # list_to_ignore = list_to_ignore1 + list_to_ignore2
                list_to_ignore = list_to_ignore3

                # if account_name in list_to_ignore:
                #     flag_for_customer_vendor = True

                if account_name in list_to_ignore:
                    account_name = 'Control Account BY ME'

                # my_item_dict["account_id"] = chart_of_accounts_from_zoho[account_name]
                account_id = chart_of_accounts_from_zoho.get(account_name)
                if account_id:
                    my_item_dict["account_id"] = account_id
                    my_item_dict["account_name"] = account_name
                else:
                    if account_name not in count_missing_coa_list:
                        count_missing_coa_list.append(account_name)
                        # print(account_name)
                
                if not my_item_dict["description"]:
                    my_item_dict["description"] = my_item_dict["account_name"]

                # my_item_dict["for_my_item_id"] = item['Id']
                # if "ClassRef" in item["JournalEntryLineDetail"]:
                #     cf_dict["value"] = item["JournalEntryLineDetail"]["ClassRef"]["name"]

                # my_item_dict["item_custom_fields"] = [cf_dict]

                # item["SalesItemLineDetail"]["TaxCodeRef"]["value"] gives the tax_id
                # tax_id is string
                # my_item_dict["tax_id"] = 'We will get very soon ...'

                # if "TaxCodeRef" in item["SalesItemLineDetail"]:
                #     my_item_dict["tax_name"] = taxcode_dict[item["SalesItemLineDetail"]["TaxCodeRef"]["value"]]
                # else:
                #     my_item_dict["tax_name"] = null_value
                
                # my_item_dict["tax_name"] = term_dict[item["SalesItemLineDetail"]["TaxCodeRef"]["value"]]

                # my_item_dict["tax_name"] = 'We will get very soon ...'
                # my_item_dict["tax_type"] = 'We will get very soon ...'
                # my_item_dict["tax_percentage"] = 'We will get very soon ...'

            # elif detail_type == "SubTotalLineDetail":
            #     # amount = item["Amount"]
            #     my_item_dict["amount"] = item["Amount"]
            # elif detail_type == "DiscountLineDetail":
            #     # percent_based_or_not = item["PercentBased"]
            #     my_item_dict["discount_percent_based_or_not"] = item["PercentBased"]
            # elif detail_type == "TDSLineDetail":

            #     tds_section_type_id = item["TDSLineDetail"]["TDSSectionTypeId"]
            #     tds_mapping_dict["description"] = tds_section_dict[str(tds_section_type_id)]
            #     tds_mapping_dict["rate"] = -item["Amount"]

            #     # TDS receivable id is 951651000000014016
            #     tds_mapping_dict["account_id"] = "951651000000014016"

                # tds_section_type_id = item["TDSLineDetail"]["TDSSectionTypeId"]
                # my_item_dict["tds_detail_section_type_id"] = item["TDSLineDetail"]["TDSSectionTypeId"]


            if flag_for_customer_vendor:
                print(invoice_from_qb['Id'],' ',account_name)
                continue


            my_item_list.append(my_item_dict)


    # mapping_dict["line_list"] = my_item_list
    
    # my_tax_line_list = list()
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
    # if "VendorRef" in invoice_from_qb:
    #     # mapping_dict["customer_name"] = invoice_from_qb["VendorRef"]["name"]
    #     customer_name = invoice_from_qb["VendorRef"]["name"]
    #     mapping_dict["vendor_id"] = contacts_from_zoho[customer_name]
    # else:
    #     mapping_dict["vendor_id"] = null_value

    # Search invoices by due date. Default date format is yyyy-mm-dd
    # if "DueDate" in invoice_from_qb:
    #     mapping_dict["due_date"] = invoice_from_qb["DueDate"]
    # else:
    #     mapping_dict["due_date"] = null_value

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

    # if "SalesTermRef" in invoice_from_qb:
    #     mapping_dict["payment_terms_label"] = term_dict[invoice_from_qb["SalesTermRef"]["value"]]
    # else:
    #     mapping_dict["payment_terms_label"] = null_value

    if "ExchangeRate" in invoice_from_qb:
        mapping_dict["exchange_rate"] = invoice_from_qb["ExchangeRate"]
    else:
        mapping_dict["exchange_rate"] = null_value

    # if flag_for_customer_vendor:
    #     mapping_dict = None

    return mapping_dict

def mapping_funcV3(invoice_from_qb):

    global journal_entry_count

    # Term -> "payment_terms_label"
    term_dict = dict()
    term_dict["5"] = "50% Advance Payment"
    term_dict["1"] = "Due on receipt"
    term_dict["2"] = "Net 15"
    term_dict["3"] = "Net 30"
    term_dict["4"] = "Net 60"


    # taxcode_dict = dict()
    # taxcode_dict["36"] = "(sales)ST@14%+0.5%SBC+0.5%KKS+VAT@5.5%"
    # taxcode_dict["59"] = "0% GST"
    # taxcode_dict["56"] = "0% IGST"
    # taxcode_dict["74"] = "0.25% GST"
    # taxcode_dict["72"] = "0.25% IGST"
    # taxcode_dict["22"] = "0.5% Swachh Bharat Cess"
    # taxcode_dict["58"] = "12.0% GST"
    # taxcode_dict["60"] = "12.0% IGST"
    # taxcode_dict["4"] = "12.36% ST"
    # taxcode_dict["15"] = "12.5% CST - Inactive - Inactive"
    # taxcode_dict["38"] = "12.50% VAT Purchase"
    # taxcode_dict["40"] = "13.5% VAT"
    # taxcode_dict["16"] = "14% Service Tax - Inactive"
    # taxcode_dict["17"] = "14% ST & VAT"
    # taxcode_dict["20"] = "14%ST & 2%CST"
    # taxcode_dict["3"] = "14.0% VAT"
    # taxcode_dict["19"] = "14.00% ST"
    # taxcode_dict["26"] = "14.5% ST"
    # taxcode_dict["42"] = "14.5% VAT"
    # taxcode_dict["27"] = "15.0% ST"
    # taxcode_dict["62"] = "18.0% GST"
    # taxcode_dict["54"] = "18.0% IGST"
    # taxcode_dict["9"] = "2% CST"
    # taxcode_dict["50"] = "2% KVAT"
    # taxcode_dict["14"] = "2.0% CST"
    # taxcode_dict["41"] = "20% VAT KVAT"
    # taxcode_dict["37"] = "20%VAT"
    # taxcode_dict["57"] = "28.0% GST"
    # taxcode_dict["61"] = "28.0% IGST"
    # taxcode_dict["73"] = "3.0% GST"
    # taxcode_dict["71"] = "3.0% IGST"
    # taxcode_dict["2"] = "4.0% VAT"
    # taxcode_dict["53"] = "5.0% GST"
    # taxcode_dict["63"] = "5.0% IGST"
    # taxcode_dict["5"] = "5.0% VAT"
    # taxcode_dict["6"] = "5.5% VAT"
    # taxcode_dict["76"] = "6.0% GST"
    # taxcode_dict["75"] = "6.0% IGST"
    # taxcode_dict["55"] = "Exempt GST"
    # taxcode_dict["52"] = "Exempt IGST"
    # taxcode_dict["67"] = "GST Cess @ 36%"
    # taxcode_dict["64"] = "GST Cess @ 5%"
    # taxcode_dict["28"] = "KKS"
    # taxcode_dict["30"] = "KKS@0.5"
    # taxcode_dict["43"] = "MVAT-12.5%"
    # taxcode_dict["44"] = "MVAT-13.5%"
    # taxcode_dict["46"] = "MVAT-14.5%"
    # taxcode_dict["49"] = "MVAT-20%"
    # taxcode_dict["51"] = "MVAT-25%"
    # taxcode_dict["45"] = "MVAT-5%"
    # taxcode_dict["47"] = "MVAT-5.5%"
    # taxcode_dict["48"] = "MVAT-6%"
    # taxcode_dict["13"] = "Out of Scope"
    # taxcode_dict["65"] = "Purchase GST 33% - 28%GST+5%Cess"
    # taxcode_dict["68"] = "Purchase GST 64% - 28%GST+36%CESS"
    # taxcode_dict["66"] = "Sales GST 33% - 28%GST+5%Cess"
    # taxcode_dict["69"] = "Sales GST 64% - 28%GST+36%CESS"
    # taxcode_dict["70"] = "Sales* GST64% - 28%GST+36%CESS"
    # taxcode_dict["7"] = "Service Tax & VAT"
    # taxcode_dict["11"] = "Service Tax Old Rate"
    # taxcode_dict["12"] = "ST & CST"
    # taxcode_dict["8"] = "ST & VAT"
    # taxcode_dict["21"] = "ST&CST"
    # taxcode_dict["24"] = "ST&VAT"
    # taxcode_dict["25"] = "ST(new)&CST"
    # taxcode_dict["33"] = "ST+CST(17%)"
    # taxcode_dict["32"] = "ST+VAT(20.5%)"
    # taxcode_dict["34"] = "ST+VAT(20.5) New"
    # taxcode_dict["31"] = "ST14.5%+KKS0.5%+VAT5.5%"
    # taxcode_dict["29"] = "ST15%+VAT5.5%"
    # taxcode_dict["35"] = "ST@14%+0.5%SBC+0.5%KKS+VAT@5.5%"
    # taxcode_dict["10"] = "Test"
    # taxcode_dict["23"] = "UD_14.5% ST"
    # taxcode_dict["18"] = "VAT 14.5%"
    # taxcode_dict["39"] = "Vat @ 6%"

    tax_rate_fout = open('tax_id_and_name_PR.json')
    tax_rate_details = json.load(tax_rate_fout)

    # items_from_zohofout = open('data_from_zoho/items_data_from_zoho.json')
    # items_from_zoho = json.load(items_from_zohofout)
    # contacts_from_zohofout = open('data_from_zoho/contacts_data_from_zoho.json')
    # contacts_from_zoho = json.load(contacts_from_zohofout)
    # chart_of_accounts_from_zohofout = open('data_from_zoho/chart_of_accounts_data_from_zoho.json')
    chart_of_accounts_from_zohofout = open('data_from_zoho/coa_details_PR.json')
    chart_of_accounts_from_zoho = json.load(chart_of_accounts_from_zohofout)

    currency_from_zohofout = open('data_from_zoho/currency_details_pr.json')
    currency_from_zoho = json.load(currency_from_zohofout)

    # chart_of_accounts_from_zohofout = open('data_from_zoho/my_coa_data_from_zoho.json')
    # chart_of_accounts_from_zoho = json.load(chart_of_accounts_from_zohofout)

    null_value = None


    # taxcode_to_id = dict()
    # taxcode_to_id["54"] = "127706000000863117"
    # taxcode_to_id["62"] = "127706000000863129"
    # taxcode_to_id["52"] = "127706000000863037"
    # taxcode_to_id["60"] = "127706000000863101"
    # taxcode_to_id["63"] = "127706000000863085"
    # taxcode_to_id["64"] = "127706000000863097"
    # taxcode_to_id["56"] = "127706000000863037"
    # taxcode_to_id["13"] = ""
    # taxcode_to_id["NON"] = ""
    # taxcode_to_id["55"] = "127706000000863073"
    # taxcode_to_id["58"] = "127706000000863113"
    # taxcode_to_id["66"] = "127706000002291415"
    # taxcode_to_id["70"] = "127706000002291460"
    # taxcode_to_id["53"] = "127706000000863097"
    # taxcode_to_id["57"] = "127706000000863145"
    # taxcode_to_id["59"] = "127706000000863073"
    # taxcode_to_id["65"] = "127706000002291415"
    # taxcode_to_id["68"] = "127706000002291460"

    mapping_dict = dict()

    flag_for_customer_vendor = False

    # mapping_dict["ignore_auto_number_generation"] = False

    if "TxnDate" in invoice_from_qb:
        # invoice_number is string
        # mapping_dict["invoice_date"] = invoice_from_qb["TxnDate"]
        mapping_dict["journal_date"] = invoice_from_qb["TxnDate"]
    else:
        # mapping_dict["invoice_date"] = null_value
        mapping_dict["journal_date"] = invoice_from_qb["TxnDate"]

    extracted_year = mapping_dict["journal_date"].split('-')[0]

    if "DocNumber" in invoice_from_qb:
        # invoice_number is string
        mapping_dict["entry_number"] = invoice_from_qb["DocNumber"]
        mapping_dict["journal_number_prefix"] = f'{invoice_from_qb["DocNumber"]}-'
        mapping_dict["journal_number_suffix"] = f"{journal_entry_count}"
        # mapping_dict["journal_number_suffix"] = f"{invoice_from_qb['Id']}"
    else:
        mapping_dict["entry_number"] = f"JE_{journal_entry_count}-{extracted_year}"
        mapping_dict["journal_number_prefix"] = f"JE_{journal_entry_count}-{extracted_year}-"
        mapping_dict["journal_number_suffix"] = f"{journal_entry_count}"

        # mapping_dict["entry_number"] = f"JE_{invoice_from_qb['Id']}-{extracted_year}"
        # mapping_dict["journal_number_prefix"] = f"JE_{invoice_from_qb['Id']}-{extracted_year}-"
        # mapping_dict["journal_number_suffix"] = f"{invoice_from_qb['Id']}"
    
    journal_entry_count = journal_entry_count + 1

    if len(mapping_dict["journal_number_prefix"] + mapping_dict["journal_number_suffix"]) > 16:
        length_of_journal_number_suffix = len(mapping_dict["journal_number_suffix"])
        length_of_journal_number_prefix = len(mapping_dict["journal_number_prefix"])

        upto_length = 16 - (length_of_journal_number_prefix + length_of_journal_number_suffix)
        if upto_length < 0:
            upto_length = abs(upto_length)

        # print(upto_length)
        new_journal_number_prefix = mapping_dict["journal_number_prefix"][:16-upto_length]
        # print(f'{mapping_dict["journal_number_prefix"]}------{new_journal_number_prefix}')
        mapping_dict["journal_number_prefix"] = new_journal_number_prefix

    if len(mapping_dict["journal_number_prefix"] + mapping_dict["journal_number_suffix"]) > 16:
        # pass
        print(f'{mapping_dict["journal_number_prefix"]}------{mapping_dict["journal_number_suffix"]}')


    mapping_dict["currency_id"] = null_value
    if "CurrencyRef" in invoice_from_qb:
        currency_id = currency_from_zoho.get(invoice_from_qb["CurrencyRef"]["value"])
        if currency_id:
            mapping_dict["currency_id"] = currency_from_zoho[invoice_from_qb["CurrencyRef"]["value"]]
        else:
            print(f'{invoice_from_qb["CurrencyRef"]["value"]} KEY ERROR')
            mapping_dict["currency_id"] = "SGD ERROR"
            return None


    # CustomField

    # Definition Id 0
    cf_id_0_dict = dict()
    # mapping_dict["cf_id_0_name"] = invoice_from_qb["CustomField"][0]["Name"]
    # cf_id_0_dict["label"] = "Journal Number"
    # cf_id_0_dict["value"] = mapping_dict["entry_number"]

    # cf_id_1_dict = dict()
    # # mapping_dict["cf_id_1_name"] = invoice_from_qb["CustomField"][1]["Name"]
    # cf_id_1_dict["customfield_id"] = "127706000001666005"
    # if "StringValue" in invoice_from_qb["CustomField"][1]:
    #     # mapping_dict["cf_id_1_value"] = invoice_from_qb["CustomField"][1]["StringValue"]
    #     cf_id_1_dict["value"] = invoice_from_qb["CustomField"][1]["StringValue"]
    # else:
    #     # mapping_dict["cf_id_1_value"] = null_value
    #     cf_id_1_dict["value"] = null_value

        
    # cf_id_2_dict = dict()
    # # mapping_dict["cf_id_2_name"] = invoice_from_qb["CustomField"][2]["Name"]
    # cf_id_2_dict["customfield_id"] = "127706000001666009"
    # if "StringValue" in invoice_from_qb["CustomField"][2]:
    #     # mapping_dict["cf_id_2_value"] = invoice_from_qb["CustomField"][2]["StringValue"]
    #     cf_id_2_dict["value"] = invoice_from_qb["CustomField"][2]["StringValue"]
    # else:
    #     # mapping_dict["cf_id_2_value"] = null_value
    #     cf_id_2_dict["value"] = null_value


    custom_field_list = list()
    # custom_field_list.append(cf_id_0_dict)
    # custom_field_list.append(cf_id_1_dict)
    # custom_field_list.append(cf_id_2_dict)
    # mapping_dict["custom_fields"] = custom_field_list

    print(invoice_from_qb["Id"])
    mapping_dict["id_from_qb"] = invoice_from_qb["Id"]

    line_items_list = list()
    tds_mapping_dict = dict()
    
    # flag_for_customer_vendor = False

    if "Line" in invoice_from_qb:
        qb_line_items = invoice_from_qb["Line"]

        my_item_list = list()
        
        for item in qb_line_items:
            # item_id is string

            # cf_dict = dict()
            # cf_dict["label"] = "Class"
            # cf_dict["value"] = null_value

            my_item_dict = dict()

            detail_type = item["DetailType"]
            flag_for_customer_vendor = False
            if detail_type == "JournalEntryLineDetail":

                # if "EntityRef" in item["JournalEntryLineDetail"]:
                #     flag_for_customer_vendor = True
                #     break

                entity_details = ''
                if "Entity" in item["JournalEntryLineDetail"]:
                    entity_type = item["JournalEntryLineDetail"]["Entity"]["Type"]
                    entity_name = item["JournalEntryLineDetail"]["Entity"]["EntityRef"]["name"]

                    entity_details = f'[ {entity_type} : {entity_name} ]'

                    # print(entity_details)



                found_class_name = False
                if "ClassRef" in item["JournalEntryLineDetail"]:
                    class_name = item["JournalEntryLineDetail"]["ClassRef"]["name"]
                    found_class_name = True
                
                found_department_name = False
                if "DepartmentRef" in item["JournalEntryLineDetail"]:
                    department_name = item["JournalEntryLineDetail"]["DepartmentRef"]["name"]
                    found_department_name = True

                extra_description = ''
                if found_class_name and found_department_name:
                    extra_description = f"[Class: {class_name} - Department: {department_name}]"
                elif found_class_name:
                    extra_description = f"[Class: {class_name}]"
                elif found_department_name:
                    extra_description = f"[Department: {department_name}]"

                my_item_dict["description"] = null_value
                if "Description" in item:
                    gotten_description = item["Description"]
                    if extra_description:
                        my_item_dict["description"] = gotten_description + ' ' + extra_description + ' ' + entity_details
                    else:
                        my_item_dict["description"] = gotten_description + ' ' + entity_details
                
                my_item_dict["amount"] = null_value
                if "Amount" in item:
                    item_amount = item["Amount"]
                    if item_amount == 0.0:
                        continue
                    my_item_dict["amount"] = item["Amount"]

                posting_type = item["JournalEntryLineDetail"]["PostingType"]
                if posting_type == "Credit":
                    my_item_dict["debit_or_credit"] = "credit"
                elif posting_type == "Debit":
                    my_item_dict["debit_or_credit"] = "debit"
                else:
                    my_item_dict["debit_or_credit"] = null_value

                account_name = item["JournalEntryLineDetail"]["AccountRef"]["name"]
                splitted_name_list = account_name.split(':')
                if len(splitted_name_list) == 1:
                    # No colon
                    account_name = splitted_name_list[0]
                else:
                    # Colon
                    account_name = splitted_name_list[-1]
                
                # list_to_ignore1 = ['Accounts Receivable (Debtors) - USD', 'CGST Payable', 'SGST Payable', 'IGST Payable', 'Accounts Payable (Creditors) - CAD', 'Input IGST Tax RCM', 'Output CGST Tax RCM', 'Accounts Payable (Creditors) - GBP', 'Accounts Payable (Creditors) - SGD', 'CST Payable', 'Output SGST Tax RCM', 'Input CGST Tax RCM', 'Input SGST Tax RCM', 'Output CST 2%', 'Accounts Payable (Creditors) - EUR']
                # list_to_ignore2 = ['Accounts Receivable (Debtors)', 'Accounts Payable (Creditors)', 'Accounts Payable (Creditors) - USD', 'Advance from Customers (deleted)','Accounts Payable (Creditors) - GBP']
                list_to_ignore3 = ['Accounts Receivable (Debtors)','Provision for Doubtful Debts','Provision for Doubtful debts','','Accounts Payable (Creditors)','Accounts Payable (Creditors) - USD','Accounts Payable (Creditors) - GBP','Accounts Payable (Creditors) - SGD','Input CGST Tax RCM', 'Input SGST Tax RCM', 'Output CGST Tax RCM', 'Output SGST Tax RCM']
                # list_to_ignore = list_to_ignore1 + list_to_ignore2
                list_to_ignore = list_to_ignore3

                # if account_name in list_to_ignore:
                #     flag_for_customer_vendor = True

                if account_name in list_to_ignore:
                    account_name = 'Control Account'

                # my_item_dict["account_id"] = chart_of_accounts_from_zoho[account_name]
                account_id = chart_of_accounts_from_zoho.get(account_name)
                if account_id:
                    my_item_dict["account_id"] = account_id
                    my_item_dict["account_name"] = account_name
                else:
                    if account_name not in count_missing_coa_list:
                        count_missing_coa_list.append(account_name)
                        # print(account_name)
                

                # my_item_dict["for_my_item_id"] = item['Id']
                # if "ClassRef" in item["JournalEntryLineDetail"]:
                #     cf_dict["value"] = item["JournalEntryLineDetail"]["ClassRef"]["name"]

                # my_item_dict["item_custom_fields"] = [cf_dict]

                # item["SalesItemLineDetail"]["TaxCodeRef"]["value"] gives the tax_id
                # tax_id is string
                # my_item_dict["tax_id"] = 'We will get very soon ...'

                # if "TaxCodeRef" in item["SalesItemLineDetail"]:
                #     my_item_dict["tax_name"] = taxcode_dict[item["SalesItemLineDetail"]["TaxCodeRef"]["value"]]
                # else:
                #     my_item_dict["tax_name"] = null_value
                
                # my_item_dict["tax_name"] = term_dict[item["SalesItemLineDetail"]["TaxCodeRef"]["value"]]

                # my_item_dict["tax_name"] = 'We will get very soon ...'
                # my_item_dict["tax_type"] = 'We will get very soon ...'
                # my_item_dict["tax_percentage"] = 'We will get very soon ...'

            # elif detail_type == "SubTotalLineDetail":
            #     # amount = item["Amount"]
            #     my_item_dict["amount"] = item["Amount"]
            # elif detail_type == "DiscountLineDetail":
            #     # percent_based_or_not = item["PercentBased"]
            #     my_item_dict["discount_percent_based_or_not"] = item["PercentBased"]
            # elif detail_type == "TDSLineDetail":

            #     tds_section_type_id = item["TDSLineDetail"]["TDSSectionTypeId"]
            #     tds_mapping_dict["description"] = tds_section_dict[str(tds_section_type_id)]
            #     tds_mapping_dict["rate"] = -item["Amount"]

            #     # TDS receivable id is 951651000000014016
            #     tds_mapping_dict["account_id"] = "951651000000014016"

                # tds_section_type_id = item["TDSLineDetail"]["TDSSectionTypeId"]
                # my_item_dict["tds_detail_section_type_id"] = item["TDSLineDetail"]["TDSSectionTypeId"]


            if flag_for_customer_vendor:
                print(invoice_from_qb['Id'],' ',account_name)
                continue


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
    #             my_tax_item_dict["amount"] = tax_item["Amount"]
    #             # my_tax_item_dict["quantity"] = 1

    #             tax_detail_type = tax_item["DetailType"]

    #             if tax_detail_type == "TaxLineDetail":

    #                 tax_name = tax_rate_details[tax_item["TaxLineDetail"]["TaxRateRef"]["value"]][0]
    #                 my_tax_item_dict["description"] = tax_name

    #                 tax_name_for_search = tax_rate_details[tax_item["TaxLineDetail"]["TaxRateRef"]["value"]][1]
    #                 if tax_name_for_search == 'IGST':
    #                     my_tax_item_dict["account_id"] = chart_of_accounts_from_zoho['Input IGST']
    #                 elif tax_name_for_search == 'CGST':
    #                     my_tax_item_dict["account_id"] = chart_of_accounts_from_zoho['Input CGST']
    #                 elif tax_name_for_search == 'SGST':
    #                     my_tax_item_dict["account_id"] = chart_of_accounts_from_zoho['Input SGST']
    #                 else:
    #                     print('JUST DIE.....')

    #                 my_tax_item_dict['debit_or_credit'] = 'debit'

    #                 # my_tax_item_dict["description"] = tax_name
    #                 # my_tax_item_dict["tax_name"] = tax_rate_details[tax_item["TaxLineDetail"]["TaxRateRef"]["value"]]
    #                 # my_tax_item_dict["net_amount_taxable"] = tax_item["TaxLineDetail"]["NetAmountTaxable"]

    #                 # my_tax_item_dict["gst_treatment_code"] = "out_of_scope"


    #             my_item_list.append(my_tax_item_dict)



    # if tds_mapping_dict and tds_mapping_dict["description"]:
    #     my_item_list.append(tds_mapping_dict)

    # mapping_dict["tax_detail_list"] = my_tax_line_list
    cleaned_my_item_list = [item for item in my_item_list if item]

    mapping_dict["line_items"] = cleaned_my_item_list

    # From customer_name we will get the customer_id
    # if "VendorRef" in invoice_from_qb:
    #     # mapping_dict["customer_name"] = invoice_from_qb["VendorRef"]["name"]
    #     customer_name = invoice_from_qb["VendorRef"]["name"]
    #     mapping_dict["vendor_id"] = contacts_from_zoho[customer_name]
    # else:
    #     mapping_dict["vendor_id"] = null_value

    # Search invoices by due date. Default date format is yyyy-mm-dd
    # if "DueDate" in invoice_from_qb:
    #     mapping_dict["due_date"] = invoice_from_qb["DueDate"]
    # else:
    #     mapping_dict["due_date"] = null_value

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

    # if "SalesTermRef" in invoice_from_qb:
    #     mapping_dict["payment_terms_label"] = term_dict[invoice_from_qb["SalesTermRef"]["value"]]
    # else:
    #     mapping_dict["payment_terms_label"] = null_value

    if "ExchangeRate" in invoice_from_qb:
        mapping_dict["exchange_rate"] = invoice_from_qb["ExchangeRate"]
    else:
        mapping_dict["exchange_rate"] = null_value

    # if flag_for_customer_vendor:
    #     mapping_dict = None

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

    # file_name = '../data_from_qb_2013_04_01_to_2017_06_30_journal_entry.json'
    # file_name = 'involved_account_not_applicable.json'
    # file_name = '../data_from_qb_2017_07_01_to_2022_07_31_journal_entry.json'
    # file_name = 'to_be_posted_data.json'
    # file_name = '../27_nov_je_post/to_push.json'
    # file_name = 'debit_credit_not_matched_data.json'
    file_name = '../data_from_qb_journal_pr.json'
    


    # file_name = 'test_invoice_data.json'
    skipped_list = list()

    f = open(file_name)
    parsed_data = json.load(f)

    # item_list = parsed_data["QueryResponse"]["Customer"]
    my_item_list = list()
    count = 0
    for item in parsed_data:
        # my_item_dict = dict()
        # my_item_dict['name'] = item["Name"]
        # my_item_dict['rate'] = item["UnitPrice"]

        # mapped_customer = mapping_func(item)
        # mapped_customer = mapping_funcV2(item)
        mapped_customer = mapping_funcV3(item)

        if mapped_customer is None:
            count = count + 1
            print(item['Id'])
            skipped_list.append(item)
        else:
            my_item_list.append(mapped_customer)
    
    # mapped_data = dict()
    # mapped_data["JournalEntry"] = my_item_list

    print(len(my_item_list))
    print(len(parsed_data))
    mapped_json = json.dumps(my_item_list,indent=4)

    print("The Customer and Vendor JE are : ",count)
    print("The coa missing list is: ",count_missing_coa_list)
    with open("mapped_Journal_PR.json", "w") as outfile:
        outfile.write(mapped_json)

    mapped_json = json.dumps(skipped_list,indent=4)
    with open("skipped_journal_PR.json", "w") as outfile:
        outfile.write(mapped_json)

def for_duplicate_invoice_number(contact_id,dup_invoice_number):
    contacts_from_zohofout = open('data_from_zoho/contacts_data_from_zoho.json')
    contacts_from_zoho = json.load(contacts_from_zohofout)

    new_invoice_number = ""
    for k,v in contacts_from_zoho.items():
        if v == contact_id:
            new_invoice_number  = k.split(" ")[0] + dup_invoice_number

    contacts_from_zohofout.close()

    return new_invoice_number

def post_request_zoho():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # output_file_name = 'console_output_2013_to_2017.txt'
    # output_file_name_fout = open(output_file_name)

    # ZohoBooks.fullaccess.all
    # code = '1000.3f2187fa12c1465d48fab99ab199f937.619ab209c92d1634e7764f1c5b6ce6e7'
    # client_id = '1000.UR9FCNRIBAJ11TLABY8K4C0UAW14BP'
    # client_secret = 'e72b1a3f32e16117b3287974149f066ed1f13f0822'

    # code = '1000.637e36e217c1f30c2bad4532e63dbae8.b8042b1085655488dc0daf30e3d31d52'
    client_id = '1000.HG016JCEMYJ8HY9CGRIRWGO7L3J6AD'
    client_secret = 'c3942592d7792a7c533d58cc1e9ae4a7726ed0af3e'

    # client_id = '1000.UR9FCNRIBAJ11TLABY8K4C0UAW14BP'
    # client_secret = 'e72b1a3f32e16117b3287974149f066ed1f13f0822'

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
    access_token = "1000.630ae0ed181c1dfb95c746bf95bcac58.85d71867ad083d0c53d79016f84c8a9e"
    refresh_token = "1000.af053ec9718b2c4619ff81c5265d18d2.2b09ce857e9089cc0f06b8d4a45444f1"
    # expires_in = parsed_data["expires_in"]

    print(refresh_token)
    print(access_token)

    organization_id = '60019790139'
    # organization_id = '60015983411'
    post_url = f'https://books.zoho.in/api/v3/journals?ignore_auto_number_generation=true&organization_id={organization_id}'

    f = open('journal_fail_pr.json')
    # f = open('failed_mapped.json')
    # f = open('to_again_mapped.json')
    # f = open('involved_account_not_applicable.json')

    parsed_data2 = json.load(f)
    # items_list = parsed_data2["JournalEntry"]
    items_list = parsed_data2


    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_journal_PR.txt","a")
    error_response_save_file = open("error_console_for_failed_invoice.txt","a")


    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")
    # error_response_save_file.write(f"NEW WRITE STARTED: {dt_string}\n")

    for item in items_list:
        while True:
            print(f'Processing for entry_number: {item["entry_number"]}||{item["id_from_qb"]}....')
            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(0.7)
            # 500ms
            # param = dict()
            # param['JSONString'] = item
            # r2 = requests.post(post_url,headers=headers,data=param)

            id_from_qb = item["id_from_qb"]

            # if "id_from_qb" in item:
            #     del item["id_from_qb"]

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
                response_save_file.write(f'{parsed_data3["journal"]["journal_id"]} : {id_from_qb}\n')

                print(f'{id_from_qb} is successfully pushed')
                response_save_file.flush()
                # It means success
                break
            # elif parsed_data3["code"] == 1001:
            #     """
            #     {
            #         "code": 1001,
            #         "message": "Invoice 2/BF02serv/2013-14 already exists"
            #     }
            #     """
            #     old_invoice_number = item["entry_number"]
            #     new_invoice_number = for_duplicate_invoice_number(item["vendor_id"],old_invoice_number)
            #     if not new_invoice_number:
            #         # if new_invoice_number is EMPTY STRING
            #         response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]} ## BILL_NUMBER {old_invoice_number} to NULL String returned\n')
            #         break

            #     item["entry_number"] = new_invoice_number
            #     response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]} ## BILL_NUMBER {old_invoice_number} to {item["entry_number"]}\n')
            else:
                print(f'ERROR occurred: {id_from_qb}||{item["entry_number"]}||{item["journal_date"]} was not able to be pushed')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]}\n')
                response_save_file.flush()
                break
        
        # response_save_file.flush()
        # print(f'Successfully created invoice named: {item["entry_number"]}||{item["journal_date"]}')
    
    response_save_file.close()

# 'code' variable must be updated before running this function
def delete_journal_entry():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # output_file_name = 'console_output_2013_to_2017.txt'
    # output_file_name_fout = open(output_file_name)

    # ZohoBooks.fullaccess.all
    # code = '1000.3f2187fa12c1465d48fab99ab199f937.619ab209c92d1634e7764f1c5b6ce6e7'
    # client_id = '1000.UR9FCNRIBAJ11TLABY8K4C0UAW14BP'
    # client_secret = 'e72b1a3f32e16117b3287974149f066ed1f13f0822'

    # code = '1000.637e36e217c1f30c2bad4532e63dbae8.b8042b1085655488dc0daf30e3d31d52'
    client_id = '1000.WVUN689ZVG2LQONSCPA4AMBLU61PMX'
    client_secret = 'eacbaa6f3306186b1882e6bd1f819703b8df9cabdf'

    # client_id = '1000.UR9FCNRIBAJ11TLABY8K4C0UAW14BP'
    # client_secret = 'e72b1a3f32e16117b3287974149f066ed1f13f0822'

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
    access_token = '1000.d4b9270734ed1d2348c69668d42ac1aa.bd3e489c9b172a76758c6c80136b4918'
    # expires_in = parsed_data["expires_in"]

    print(refresh_token)
    print(access_token)

    organization_id = '60001574931'
    # organization_id = '60015983411'
    # post_url = f'https://books.zoho.in/api/v3/journals?ignore_auto_number_generation=true&organization_id={organization_id}'

    # f = open('mapped.json')
    # f = open('failed_mapped.json')
    # f = open('to_again_mapped.json')
    # f = open('involved_account_not_applicable.json')
    f = open('to_be_deleted.json')

    parsed_data2 = json.load(f)
    # items_list = parsed_data2["JournalEntry"]
    items_list = parsed_data2


    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_deleted_journal_id.txt","a")
    error_response_save_file = open("error_console_for_failed_invoice.txt","a")


    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")
    # error_response_save_file.write(f"NEW WRITE STARTED: {dt_string}\n")

    for item in items_list:
        while True:
            post_url = f'https://books.zoho.in/api/v3/journals/{item[1]}?&organization_id={organization_id}'

            print(f'Processing for entry_number: {item[0]}....')
            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(0.5)
            # 500ms
            # param = dict()
            # param['JSONString'] = item
            # r2 = requests.post(post_url,headers=headers,data=param)

            # id_from_qb = item["id_from_qb"]
            id_from_qb = item[0]

            # if "id_from_qb" in item:
            #     del item["id_from_qb"]

            r2 = requests.delete(post_url,headers=headers)

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
                # response_save_file.write(f'{parsed_data3["journal"]["journal_id"]} : {id_from_qb}\n')
                response_save_file.write(f'{id_from_qb} is successfully deleted\n')

                print(f'{id_from_qb} is successfully deleted')
                response_save_file.flush()
                # It means success
                break
            # elif parsed_data3["code"] == 1001:
            #     """
            #     {
            #         "code": 1001,
            #         "message": "Invoice 2/BF02serv/2013-14 already exists"
            #     }
            #     """
            #     old_invoice_number = item["entry_number"]
            #     new_invoice_number = for_duplicate_invoice_number(item["vendor_id"],old_invoice_number)
            #     if not new_invoice_number:
            #         # if new_invoice_number is EMPTY STRING
            #         response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]} ## BILL_NUMBER {old_invoice_number} to NULL String returned\n')
            #         break

            #     item["entry_number"] = new_invoice_number
            #     response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]} ## BILL_NUMBER {old_invoice_number} to {item["entry_number"]}\n')
            else:
                print(f'ERROR occurred: {id_from_qb} was not able to be pushed')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]}\n')
                response_save_file.flush()
                break
        
        # response_save_file.flush()
        # print(f'Successfully created invoice named: {item["entry_number"]}||{item["journal_date"]}')
    
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
# def post_invoice_as_sent():
#     # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

#     # output_file_name = 'console_output_2013_to_2017.txt'
#     # output_file_name_fout = open(output_file_name)

#     # ZohoBooks.fullaccess.all
#     code = '1000.3f2187fa12c1465d48fab99ab199f937.619ab209c92d1634e7764f1c5b6ce6e7'
#     client_id = '1000.UR9FCNRIBAJ11TLABY8K4C0UAW14BP'
#     client_secret = 'e72b1a3f32e16117b3287974149f066ed1f13f0822'

#     gettokenurl = f'https://accounts.zoho.in/oauth/v2/token?code={code}&client_id={client_id}&client_secret={client_secret}&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code'
#     r1 = requests.post(gettokenurl)
#     """
#         {
#             "access_token": "1000.cb73ac8e8e7a97e9a477b2771fdfa546.be088fe17b6386a80add9441e1ac0cc9",
#             "refresh_token": "1000.b3bcfcb05de766156aa2966732c07f58.c471e437e710a57b63fb6e6ba99dc6a5",
#             "api_domain": "https://www.zohoapis.in",
#             "token_type": "Bearer",
#             "expires_in": 3600
#         }

#         OR

#         {
#             "error": "invalid_code"
#         }
#     """
#     parsed_data1 = r1.json()
#     if 'error' in parsed_data1:
#         # print(parsed_data1)
#         print('code is expired [invalid code]')
#         exit()
    
#     refresh_token = parsed_data1["refresh_token"]
#     access_token = parsed_data1["access_token"]
#     # expires_in = parsed_data["expires_in"]

#     organization_id = '60015983411'
#     post_url = f'https://books.zoho.in/api/v3/invoices?organization_id={organization_id}'

#     f = open('mapped.json')
#     # f = open('leftover_mapped.json')

#     parsed_data2 = json.load(f)
#     items_list = parsed_data2["Invoice"]

#     headers = CaseInsensitiveDict()
#     headers["Accept"] = "application/json"

#     # response_save_dict = dict()
#     response_save_file = open("saved_response_for_sent.txt","a")
#     error_response_save_file = open("error_console_for_failed_response.txt","a")


#     # dd/mm/YY H:M:S
#     now = datetime.now()
#     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#     # print("date and time =", dt_string)
#     response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")
#     error_response_save_file.write(f"NEW WRITE STARTED: {dt_string}\n")

#     for item in items_list:
#         while True:
#             print(f'Processing for invoice_number: {item["invoice_number"]}....')
#             # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
#             headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
#             # access token expires in 3600 seconds (60 minutes)
#             sleep(1)

#             # param = dict()
#             # param['JSONString'] = item
#             # r2 = requests.post(post_url,headers=headers,data=param)

#             id_from_qb = item["id_from_qb"]

#             # if "id_from_qb" in item:
#             #     del item["id_from_qb"]

#             r2 = requests.post(post_url,headers=headers,json=item)

#             parsed_data3 = r2.json()
#             # print(parsed_data3)
#             if parsed_data3["code"] == 57:
#                 # access_token expired
#                 """
#                     {
#                         "code": 57,
#                         "message": "You are not authorized to perform this operation"
#                     }
#                 """
#                 print("access_token_expired...")
#                 access_token = get_new_access_token_zoho(refresh_token,client_id,client_secret)
#             elif parsed_data3["code"] == 0:
#                 """
#                 {
#                     "code": 0,
#                     "message": "The contact has been created",
#                     "contact": {
#                         "contact_id": 460000000026049,
#                         "contact_name": "Bowman and Co",
#                         "company_name": "Bowman and Co",
#                         "has_transaction": true,
#                         "contact_type": "customer",
#                         "customer_sub_type": "business",
#                         "credit_limit": 1000,
#                         "is_portal_enabled": true,
#                         ....
#                     }
#                 """
#                 # response_save_dict[f'{parsed_data3["contact"]["contact_id"]}'] = item["name"]
#                 # response_save_file.write(f'{parsed_data3["invoice"]["invoice_id"]} : {item["invoice_number"]}\n')
#                 response_save_file.write(f'{parsed_data3["invoice"]["invoice_id"]} : {id_from_qb}\n')

#                 print(f'{id_from_qb} is successfully pushed')
#                 # It means success
#                 break
#             else:
#                 print(f'ERROR occurred: {id_from_qb}||{item["invoice_number"]}||{item["date"]}||{item["customer_id"]} was able to be pushed')
#                 print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
#                 error_response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]}\n')   
#                 break

#         print(f'Successfully created invoice named: {item["invoice_number"]}||{item["date"]}||{item["customer_id"]}')


# get_items_and_write_to_file()
# generate_post_json()
post_request_zoho()
# delete_journal_entry()




        

