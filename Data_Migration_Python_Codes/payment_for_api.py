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

my_bill_id_list = list()

def mapping_func(invoice_from_qb):
    # Term -> "payment_terms_label"
    # term_dict = dict()
    # term_dict["6"] = "By 5th"
    # term_dict["1"] = "Due on receipt"
    # term_dict["12"] = "Immediate"
    # term_dict["7"] = "Net"
    # term_dict["9"] = "Net 10"
    # term_dict["2"] = "Net 15"
    # term_dict["3"] = "Net 30"
    # term_dict["14"] = "Net 45"
    # term_dict["8"] = "Net 45 Days"
    # term_dict["15"] = "Net 5"
    # term_dict["4"] = "Net 60"
    # term_dict["5"] = "Net 7"
    # term_dict["13"] = "Net 75"
    # term_dict["11"] = "Net 90"
    # term_dict["10"] = "quarterly"

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
    contacts_from_zohofout = open('data_from_zoho/contact_details_flynow.json')
    contacts_from_zoho = json.load(contacts_from_zohofout)
    
    chart_of_accounts_from_zohofout = open('data_from_zoho/coa_details_flynow.json')
    chart_of_accounts_from_zoho = json.load(chart_of_accounts_from_zohofout)
    
    invoice_qb_id_against_invoice_id_from_zohofout = open('data_from_zoho/bill_qb_id_against_bill_id_from_zoho_flynow.json')
    invoice_qb_id_against_invoice_id_from_zoho = json.load(invoice_qb_id_against_invoice_id_from_zohofout)

    payment_method_fout = open('data_from_zoho/payment_method_details_flynow.json')
    payment_method_dict = json.load(payment_method_fout)

    account_id_details = open('data_from_zoho/account_details_fly.json')
    account_id_dict = json.load(account_id_details)

    null_value = None

    tds_section_dict = dict()
    tds_section_dict["20"] = ["194J-(1)-Fees for Professinal and Technical Services","1234697000000015036"]
    # tds_section_dict["21"] = ["194J-(2)-Remuneration to Director",""]
    tds_section_dict["0"] = ["",""]
    tds_section_dict["16"] = ["194H-Commission or Brokerage (5%)","1234697000000015032"]
    # tds_section_dict["18"]=["194I-(2)-Rent-Plant and Machinery (2%)","414484000006616028"]
    # tds_section_dict["10"]=["194C(2)-Sub-Contracts / Advertisements (2%)","414484000006616058"]
    tds_section_dict["17"]=["194I-(1)-Rent-Land and building (10%)","1234697000000015034"]
    tds_section_dict["9"]=["194C(1)-Contracts (2%)","1234697000000015030"]

    mapping_dict = dict()

    mapping_dict["vendor_id"] = contacts_from_zoho[invoice_from_qb["VendorRef"]["name"]]
    mapping_dict["id_from_qb"] = invoice_from_qb["Id"]

    mapping_dict["payment_mode"] = null_value
    if "PayType" in invoice_from_qb:
        mapping_dict["payment_mode"] = invoice_from_qb["PayType"]
        if mapping_dict["payment_mode"] == 'CreditCard':
            mapping_dict["payment_mode"] = 'Credit Card'

    mapping_dict["paid_through_account_id"] = None
    if mapping_dict['payment_mode'] == 'Credit Card':
        # print(invoice_from_qb["Id"])
        # if "CreditCardPayment" not in invoice_from_qb:
        #     return None

        if "CCAccountRef" not in invoice_from_qb["CreditCardPayment"]:
            return None

        # account_name = invoice_from_qb["CreditCardPayment"]["CCAccountRef"]["name"]
        # mapping_dict["paid_through_account_id"] = chart_of_accounts_from_zoho[account_name]
        account_name = invoice_from_qb["CreditCardPayment"]["CCAccountRef"]["name"]
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
            mapping_dict["paid_through_account_id"] = account_id
        else:
            print(f"Id: {invoice_from_qb['Id']} and Account Name: {account_name}")

    elif mapping_dict['payment_mode'] == 'Check':
        # print(invoice_from_qb["Id"])

        if "BankAccountRef" not in invoice_from_qb["CheckPayment"]:
            return None

        # account_name = invoice_from_qb["CheckPayment"]["BankAccountRef"]["name"]
        # mapping_dict["paid_through_account_id"] = chart_of_accounts_from_zoho[account_name]

        account_name = invoice_from_qb["CheckPayment"]["BankAccountRef"]["name"]
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
            mapping_dict["paid_through_account_id"] = account_id
        else:
            print(f"Id: {invoice_from_qb['Id']} and Account Name: {account_name}")

    if not mapping_dict["paid_through_account_id"]:
        print(f'ACCOUNT_ID EMPTY for {invoice_from_qb["Id"]}')

    # mapping_dict["account_id"] = chart_of_accounts_from_zoho[invoice_from_qb["DepositToAccountRef"]["name"]]
    mapping_dict["date"] = invoice_from_qb["TxnDate"]
    # mapping_dict["amount"] = invoice_from_qb["TotalAmt"]

    mapping_dict['payment_number'] = None
    if "DocNumber" in invoice_from_qb:
        mapping_dict['payment_number'] = invoice_from_qb['DocNumber']

    cf_0_dict = dict()
    cf_0_dict['label'] = 'Payment Number'
    cf_0_dict['value'] = mapping_dict['payment_number']

    if mapping_dict['payment_number']:
        mapping_dict['custom_fields'] = [cf_0_dict]

    if "PaymentRefNum" in invoice_from_qb:
        mapping_dict["reference_number"] = invoice_from_qb["PaymentRefNum"]
    else:
        mapping_dict["reference_number"] = null_value

    if "PrivateNote" in invoice_from_qb:
        mapping_dict["description"] = invoice_from_qb["PrivateNote"]
    else:
        mapping_dict["description"] = ""

    if "ExchangeRate" in invoice_from_qb:
        mapping_dict["exchange_rate"] = invoice_from_qb["ExchangeRate"]
    else:
        mapping_dict["exchange_rate"] = null_value

    mapping_dict["date"] = invoice_from_qb["TxnDate"]

    # exclude_flag = False
    invoice_list = list()
    amount_applied = 0
    for line_item in invoice_from_qb["Line"]:
        linked_txn = line_item["LinkedTxn"]
        if len(linked_txn) == 1:
            if linked_txn[0]["TxnType"] == "Bill":
                invoice_dict = dict()
                # invoice_dict["invoice_id"] = invoice_qb_id_against_invoice_id_from_zoho[linked_txn[0]["TxnId"]]
                invoice_id = invoice_qb_id_against_invoice_id_from_zoho.get(linked_txn[0]["TxnId"])
                if invoice_id:
                    invoice_dict["bill_id"] = invoice_id
                else:
                    print(f'Id : {invoice_from_qb["Id"]} - {linked_txn[0]["TxnId"]}')
                    # print(f'{linked_txn[0]["TxnId"]}')
                    invoice_dict["bill_id"] = None
                    return None
                
                invoice_dict["amount_applied"] = line_item["Amount"]
                amount_applied = amount_applied + invoice_dict["amount_applied"]
                invoice_list.append(invoice_dict)
        else:
            print(invoice_from_qb["Id"])

    mapping_dict["bills"] = invoice_list
    mapping_dict["amount"] = amount_applied


    return mapping_dict

def mapping_func_another(invoice_from_qb):

    global my_bill_id_list
    # Term -> "payment_terms_label"
    # term_dict = dict()
    # term_dict["6"] = "By 5th"
    # term_dict["1"] = "Due on receipt"
    # term_dict["12"] = "Immediate"
    # term_dict["7"] = "Net"
    # term_dict["9"] = "Net 10"
    # term_dict["2"] = "Net 15"
    # term_dict["3"] = "Net 30"
    # term_dict["14"] = "Net 45"
    # term_dict["8"] = "Net 45 Days"
    # term_dict["15"] = "Net 5"
    # term_dict["4"] = "Net 60"
    # term_dict["5"] = "Net 7"
    # term_dict["13"] = "Net 75"
    # term_dict["11"] = "Net 90"
    # term_dict["10"] = "quarterly"

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
    contacts_from_zohofout = open('data_from_zoho/contact_details_PR.json')
    contacts_from_zoho = json.load(contacts_from_zohofout)
    
    chart_of_accounts_from_zohofout = open('data_from_zoho/coa_details_PR.json')
    chart_of_accounts_from_zoho = json.load(chart_of_accounts_from_zohofout)
    
    invoice_qb_id_against_invoice_id_from_zohofout = open('data_from_zoho/bill_qb_id_against_bill_id_from_zoho_PR.json')
    invoice_qb_id_against_invoice_id_from_zoho = json.load(invoice_qb_id_against_invoice_id_from_zohofout)
    # invoice_qb_id_against_invoice_id_from_zoho = {
    #     "3336":"127706000006150215",
    #     "2146":"127706000006165249",
    #     "1105":"127706000006150348",
    #     "1484":"127706000006158351"
    # }

    payment_method_fout = open('data_from_zoho/payment_method_details_PR.json')
    payment_method_dict = json.load(payment_method_fout)

    account_id_details = open('data_from_zoho/account_details_pr.json')
    account_id_dict = json.load(account_id_details)

    null_value = None

    tds_section_dict = dict()
    tds_section_dict["20"] = ["194J-(1)-Fees for Professinal and Technical Services","1208528000000015036"]
    # tds_section_dict["21"] = ["194J-(2)-Remuneration to Director",""]
    tds_section_dict["0"] = ["",""]

    mapping_dict = dict()

    mapping_dict["vendor_id"] = contacts_from_zoho[invoice_from_qb["VendorRef"]["name"]]
    mapping_dict["id_from_qb"] = invoice_from_qb["Id"]

    mapping_dict["payment_mode"] = null_value
    if "PayType" in invoice_from_qb:
        mapping_dict["payment_mode"] = invoice_from_qb["PayType"]
        if mapping_dict["payment_mode"] == 'CreditCard':
            mapping_dict["payment_mode"] = 'Credit Card'

    mapping_dict["paid_through_account_id"] = None
    if mapping_dict['payment_mode'] == 'Credit Card':
        # print(invoice_from_qb["Id"])
        # if "CreditCardPayment" not in invoice_from_qb:
        #     return None

        # if "CCAccountRef" not in invoice_from_qb["CreditCardPayment"]:
        #     return None

        # account_name = invoice_from_qb["CreditCardPayment"]["CCAccountRef"]["name"]
        # mapping_dict["paid_through_account_id"] = chart_of_accounts_from_zoho[account_name]

        if "CreditCardPayment" in invoice_from_qb and "CCAccountRef" in invoice_from_qb["CreditCardPayment"]:
            account_name = invoice_from_qb["CreditCardPayment"]["CCAccountRef"]["name"]
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
                mapping_dict["paid_through_account_id"] = account_id
            else:
                print(f"Id: {invoice_from_qb['Id']} and Account Name: {account_name}")

    elif mapping_dict['payment_mode'] == 'Check':
        # print(invoice_from_qb["Id"])
        
        # if "BankAccountRef" not in invoice_from_qb["CheckPayment"]:
        #     return None

        # account_name = invoice_from_qb["CheckPayment"]["BankAccountRef"]["name"]
        # mapping_dict["paid_through_account_id"] = chart_of_accounts_from_zoho[account_name]

        if "CheckPayment" in invoice_from_qb and "BankAccountRef" in invoice_from_qb["CheckPayment"]:
            account_name = invoice_from_qb["CheckPayment"]["BankAccountRef"]["name"]
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
                mapping_dict["paid_through_account_id"] = account_id
            else:
                print(f"Id: {invoice_from_qb['Id']} and Account Name: {account_name}")

    if not mapping_dict["paid_through_account_id"]:
        # print(f'ACCOUNT_ID EMPTY for {invoice_from_qb["Id"]}')
        pass

    # mapping_dict["account_id"] = chart_of_accounts_from_zoho[invoice_from_qb["DepositToAccountRef"]["name"]]
    mapping_dict["date"] = invoice_from_qb["TxnDate"]
    # mapping_dict["amount"] = invoice_from_qb["TotalAmt"]

    mapping_dict['payment_number'] = None
    if "DocNumber" in invoice_from_qb:
        mapping_dict['payment_number'] = invoice_from_qb['DocNumber']

    # cf_0_dict = dict()
    # cf_0_dict['label'] = 'Payment Number'
    # cf_0_dict['value'] = mapping_dict['payment_number']

    # if mapping_dict['payment_number']:
    #     mapping_dict['custom_fields'] = [cf_0_dict]

    if "PaymentRefNum" in invoice_from_qb:
        mapping_dict["reference_number"] = invoice_from_qb["PaymentRefNum"]
    else:
        mapping_dict["reference_number"] = null_value

    if "PrivateNote" in invoice_from_qb:
        mapping_dict["description"] = invoice_from_qb["PrivateNote"]
    else:
        mapping_dict["description"] = ""

    if "ExchangeRate" in invoice_from_qb:
        mapping_dict["exchange_rate"] = invoice_from_qb["ExchangeRate"]
    else:
        mapping_dict["exchange_rate"] = null_value

    mapping_dict["date"] = invoice_from_qb["TxnDate"]

    # exclude_flag = False
    invoice_list = list()
    amount_applied = 0
    for line_item in invoice_from_qb["Line"]:
        linked_txn = line_item["LinkedTxn"]
        if len(linked_txn) == 1:
            if linked_txn[0]["TxnType"] == "Bill":
                invoice_dict = dict()
                # invoice_dict["invoice_id"] = invoice_qb_id_against_invoice_id_from_zoho[linked_txn[0]["TxnId"]]
                invoice_id = invoice_qb_id_against_invoice_id_from_zoho.get(linked_txn[0]["TxnId"])
                if invoice_id:
                    invoice_dict["bill_id"] = invoice_id
                else:
                    print(f'Id : {invoice_from_qb["Id"]} - {linked_txn[0]["TxnId"]}')
                    # print(f'{linked_txn[0]["TxnId"]}')
                    my_bill_id_list.append([invoice_from_qb["Id"],linked_txn[0]["TxnId"]])

                    invoice_dict["bill_id"] = None
                    return None
                
                invoice_dict["amount_applied"] = line_item["Amount"]
                amount_applied = amount_applied + invoice_dict["amount_applied"]
                invoice_list.append(invoice_dict)
        else:
            print(invoice_from_qb["Id"])

    mapping_dict["bills"] = invoice_list
    mapping_dict["amount"] = amount_applied


    return mapping_dict

def mapping_func_for_vendor_advance(invoice_from_qb):

    global my_bill_id_list
    # Term -> "payment_terms_label"
    # term_dict = dict()
    # term_dict["6"] = "By 5th"
    # term_dict["1"] = "Due on receipt"
    # term_dict["12"] = "Immediate"
    # term_dict["7"] = "Net"
    # term_dict["9"] = "Net 10"
    # term_dict["2"] = "Net 15"
    # term_dict["3"] = "Net 30"
    # term_dict["14"] = "Net 45"
    # term_dict["8"] = "Net 45 Days"
    # term_dict["15"] = "Net 5"
    # term_dict["4"] = "Net 60"
    # term_dict["5"] = "Net 7"
    # term_dict["13"] = "Net 75"
    # term_dict["11"] = "Net 90"
    # term_dict["10"] = "quarterly"

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
    contacts_from_zohofout = open('data_from_zoho/contact_details_PR.json')
    contacts_from_zoho = json.load(contacts_from_zohofout)
    
    chart_of_accounts_from_zohofout = open('data_from_zoho/coa_details_PR.json')
    chart_of_accounts_from_zoho = json.load(chart_of_accounts_from_zohofout)
    
    invoice_qb_id_against_invoice_id_from_zohofout = open('data_from_zoho/bill_qb_id_against_bill_id_from_zoho_PR.json')
    invoice_qb_id_against_invoice_id_from_zoho = json.load(invoice_qb_id_against_invoice_id_from_zohofout)
    # invoice_qb_id_against_invoice_id_from_zoho = {
    #     "3336":"127706000006150215",
    #     "2146":"127706000006165249",
    #     "1105":"127706000006150348",
    #     "1484":"127706000006158351"
    # }

    payment_method_fout = open('data_from_zoho/payment_method_details_PR.json')
    payment_method_dict = json.load(payment_method_fout)

    account_id_details = open('data_from_zoho/account_details_pr.json')
    account_id_dict = json.load(account_id_details)

    null_value = None

    tds_section_dict = dict()
    tds_section_dict["20"] = ["194J-(1)-Fees for Professinal and Technical Services","1208528000000015036"]
    # tds_section_dict["21"] = ["194J-(2)-Remuneration to Director",""]
    tds_section_dict["0"] = ["",""]

    mapping_dict = dict()

    mapping_dict["vendor_id"] = contacts_from_zoho[invoice_from_qb["VendorRef"]["name"]]
    mapping_dict["id_from_qb"] = invoice_from_qb["Id"]

    mapping_dict["payment_mode"] = null_value
    if "PayType" in invoice_from_qb:
        mapping_dict["payment_mode"] = invoice_from_qb["PayType"]
        if mapping_dict["payment_mode"] == 'CreditCard':
            mapping_dict["payment_mode"] = 'Credit Card'

    mapping_dict["paid_through_account_id"] = None
    if mapping_dict['payment_mode'] == 'Credit Card':
        # print(invoice_from_qb["Id"])
        # if "CreditCardPayment" not in invoice_from_qb:
        #     return None

        # if "CCAccountRef" not in invoice_from_qb["CreditCardPayment"]:
        #     return None

        # account_name = invoice_from_qb["CreditCardPayment"]["CCAccountRef"]["name"]
        # mapping_dict["paid_through_account_id"] = chart_of_accounts_from_zoho[account_name]

        if "CreditCardPayment" in invoice_from_qb and "CCAccountRef" in invoice_from_qb["CreditCardPayment"]:
            account_name = invoice_from_qb["CreditCardPayment"]["CCAccountRef"]["name"]
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
                mapping_dict["paid_through_account_id"] = account_id
            else:
                print(f"Id: {invoice_from_qb['Id']} and Account Name: {account_name}")

    elif mapping_dict['payment_mode'] == 'Check':
        # print(invoice_from_qb["Id"])
        
        # if "BankAccountRef" not in invoice_from_qb["CheckPayment"]:
        #     return None

        # account_name = invoice_from_qb["CheckPayment"]["BankAccountRef"]["name"]
        # mapping_dict["paid_through_account_id"] = chart_of_accounts_from_zoho[account_name]

        if "CheckPayment" in invoice_from_qb and "BankAccountRef" in invoice_from_qb["CheckPayment"]:
            account_name = invoice_from_qb["CheckPayment"]["BankAccountRef"]["name"]
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
                mapping_dict["paid_through_account_id"] = account_id
            else:
                print(f"Id: {invoice_from_qb['Id']} and Account Name: {account_name}")

    if not mapping_dict["paid_through_account_id"]:
        # print(f'ACCOUNT_ID EMPTY for {invoice_from_qb["Id"]}')
        pass

    # mapping_dict["account_id"] = chart_of_accounts_from_zoho[invoice_from_qb["DepositToAccountRef"]["name"]]
    mapping_dict["date"] = invoice_from_qb["TxnDate"]
    mapping_dict["amount"] = invoice_from_qb["TotalAmt"]

    mapping_dict['payment_number'] = None
    if "DocNumber" in invoice_from_qb:
        mapping_dict['payment_number'] = invoice_from_qb['DocNumber']

    # cf_0_dict = dict()
    # cf_0_dict['label'] = 'Payment Number'
    # cf_0_dict['value'] = mapping_dict['payment_number']

    # if mapping_dict['payment_number']:
    #     mapping_dict['custom_fields'] = [cf_0_dict]

    if "PaymentRefNum" in invoice_from_qb:
        mapping_dict["reference_number"] = invoice_from_qb["PaymentRefNum"]
    else:
        mapping_dict["reference_number"] = null_value

    if "PrivateNote" in invoice_from_qb:
        mapping_dict["description"] = invoice_from_qb["PrivateNote"]
    else:
        mapping_dict["description"] = ""

    if "ExchangeRate" in invoice_from_qb:
        mapping_dict["exchange_rate"] = invoice_from_qb["ExchangeRate"]
    else:
        mapping_dict["exchange_rate"] = null_value

    mapping_dict["date"] = invoice_from_qb["TxnDate"]
    mapping_dict['is_advance_payment'] = True

    exclude_flag = False
    invoice_list = list()
    amount_applied = 0
    for line_item in invoice_from_qb["Line"]:
        linked_txn = line_item["LinkedTxn"]
        if len(linked_txn) == 1:
            if linked_txn[0]["TxnType"] == "Bill":
                invoice_dict = dict()
                # invoice_dict["invoice_id"] = invoice_qb_id_against_invoice_id_from_zoho[linked_txn[0]["TxnId"]]
                invoice_id = invoice_qb_id_against_invoice_id_from_zoho.get(linked_txn[0]["TxnId"])
                if invoice_id:
                    invoice_dict["bill_id"] = invoice_id
                else:
                    print(f'Id : {invoice_from_qb["Id"]} - {linked_txn[0]["TxnId"]}')
                    # print(f'{linked_txn[0]["TxnId"]}')
                    my_bill_id_list.append([invoice_from_qb["Id"],linked_txn[0]["TxnId"]])

                    invoice_dict["bill_id"] = None
                    return None
                
                invoice_dict["amount_applied"] = line_item["Amount"]
                # amount_applied = amount_applied + invoice_dict["amount_applied"]
                invoice_list.append(invoice_dict)
        else:
            print(invoice_from_qb["Id"])

    # mapping_dict["bills"] = invoice_list
    # mapping_dict["amount"] = amount_applied


    return mapping_dict


def generate_post_json():

    global my_bill_id_list

    # https://www.geeksforgeeks.org/read-json-file-using-python/
    # file_name = 'all_fetched_data_from_qb.json'
    # file_name = 'production_get.json'

    # file_name = '../data_from_qb_2013_04_01_to_2017_06_30_payment.json'
    # file_name = '../all_payment.json'
    # file_name = '../all_bill_payment.json'
    # file_name = 'skipped_ones.json'
    # file_name = 'failed_ones.json'
    # file_name = '../data_from_qb_before_bill_payment.json'
    file_name = '../adv_bp_PR.json'


    # file_name = 'test_invoice_data.json'


    f = open(file_name)
    parsed_data = json.load(f)

    # item_list = parsed_data["QueryResponse"]["Customer"]
    my_item_list = list()
    skipped_list = list()
    mapped_list = list()
    for item in parsed_data:
        # my_item_dict = dict()
        # my_item_dict['name'] = item["Name"]
        # my_item_dict['rate'] = item["UnitPrice"]

        # mapped_customer = mapping_func(item)
        # mapped_customer = mapping_func_another(item)
        mapped_customer = mapping_func_for_vendor_advance(item)
        if not mapped_customer:
            skipped_list.append(item)
        else:
            my_item_list.append(mapped_customer)
            mapped_list.append(item)
    
    # mapped_data = dict()
    # mapped_data["Invoice"] = my_item_list

    print(len(my_item_list))
    mapped_json = json.dumps(my_item_list,indent=4)
    with open("map_bp_adv_PR.json", "w") as outfile:
        outfile.write(mapped_json)

    print(len(skipped_list))
    mapped_json = json.dumps(skipped_list,indent=4)
    with open("skipped_bp_adv_PR.json", "w") as outfile:
        outfile.write(mapped_json)

    print(len(mapped_list))
    # mapped_json = json.dumps(mapped_list,indent=4)
    # with open("done_mapped_ones.json", "w") as outfile:
    #     outfile.write(mapped_json)

    # print(len(skipped_list))
    # mapped_json = json.dumps(skipped_list,indent=4)
    # with open("skipped_ones2.json", "w") as outfile:
    #     outfile.write(mapped_json)

    # print(len(mapped_list))
    # mapped_json = json.dumps(mapped_list,indent=4)
    # with open("done_mapped_ones2.json", "w") as outfile:
    #     outfile.write(mapped_json)

    # print(len(my_bill_id_list))
    # mapped_json = json.dumps(my_bill_id_list,indent=4)
    # with open("my_bill_id_list.json", "w") as outfile:
    #     outfile.write(mapped_json)


# 'code' variable must be updated before running this function
def post_request_zoho():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # output_file_name = 'console_output_2013_to_2017.txt'
    # output_file_name_fout = open(output_file_name)

    # ZohoBooks.fullaccess.all
    code = '1000.3f2187fa12c1465d48fab99ab199f937.619ab209c92d1634e7764f1c5b6ce6e7'
    client_id = '1000.UR9FCNRIBAJ11TLABY8K4C0UAW14BP'
    client_secret = 'e72b1a3f32e16117b3287974149f066ed1f13f0822'

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
    post_url = f'https://books.zoho.in/api/v3/invoices?organization_id={organization_id}'

    # f = open('mapped.json')
    f = open('leftover_mapped.json')

    parsed_data2 = json.load(f)
    items_list = parsed_data2["Invoice"]

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_invoice_id.txt","a")
    # error_response_save_file = open("error_console_for_failed_invoice.txt","a")


    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")
    # error_response_save_file.write(f"NEW WRITE STARTED: {dt_string}\n")

    for item in items_list:
        while True:
            print(f'Processing for invoice_number: {item["invoice_number"]}||{item["date"]}||{item["customer_id"]}....')
            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(1)

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
                # It means success
                break
            else:
                print(f'ERROR occurred: {id_from_qb}||{item["invoice_number"]}||{item["date"]}||{item["customer_id"]} was able to be pushed')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]}\n')   
                break

        print(f'Successfully created invoice named: {item["invoice_number"]}||{item["date"]}||{item["customer_id"]}')

def post_request_zoho_bill_payment():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # output_file_name = 'console_output_2013_to_2017.txt'
    # output_file_name_fout = open(output_file_name)

    # ZohoBooks.fullaccess.all
    # code = '1000.3f2187fa12c1465d48fab99ab199f937.619ab209c92d1634e7764f1c5b6ce6e7'
    # client_id = '1000.UR9FCNRIBAJ11TLABY8K4C0UAW14BP'
    # client_secret = 'e72b1a3f32e16117b3287974149f066ed1f13f0822'

    # code = '1000.aff2d39e4d596cc0d668c3df54ffd43f.98a5bbbc2fcadb956cd988e8fca7d533'
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
    
    # refresh_token = parsed_data1["refresh_token"]
    # access_token = parsed_data1["access_token"]
    refresh_token = '1000.6b4ef41c1de75191c5b45a1e84ecbb7e.8b6c034a53aa47da15323fa0411d4811'
    access_token = '1000.ff3a75be05d8abbbcd08c56091d3ed2c.2a5211ca13037e2713604d09511b617b'
    # expires_in = parsed_data["expires_in"]

    # response_save_file.write(f"ACCESS TOKEN {access_token} and REFRESH TOKEN {refresh_token}\n")

    organization_id = '60019790139'
    post_url = f'https://books.zoho.in/api/v3/vendorpayments?organization_id={organization_id}'

    # f = open('mapped.json')
    # f = open('failed_mapped.json')
    # f = open('to_again_mapped.json')
    # f = open('payment_mapped.json')
    f = open('map_bp_adv_PR.json')
    # f = open('failed_bills_.json')



    parsed_data2 = json.load(f)
    # items_list = parsed_data2["Bill"]
    items_list = parsed_data2


    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_bill_payment_PR.txt","a")
    error_response_save_file = open("error_console_for_failed_invoice.txt","a")


    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")
    # error_response_save_file.write(f"NEW WRITE STARTED: {dt_string}\n")

    for item in items_list:
        # original_bill_number = item["bill_number"]
        no_of_times_to_try = 0
        while True:
            print(f'Processing for payment: {item["id_from_qb"]}....')
            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(0.7)

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
                response_save_file.write(f'{parsed_data3["vendorpayment"]["payment_id"]} : {id_from_qb}\n')

                print(f'{id_from_qb} is successfully pushed')
                # It means success
                break
            else:
                print(f'ERROR occurred: {id_from_qb}||{item["id_from_qb"]}||{item["date"]}||{item["vendor_id"]} was not able to be pushed')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                response_save_file.write(f'Failed to PUSH : {id_from_qb} -> msg is {parsed_data3["message"]}\n')   
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
# post_request_zoho()
post_request_zoho_bill_payment()



        

