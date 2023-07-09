import base64
import re
import json
from time import sleep
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime

count_missing_coa_list = list()
journal_entry_count = 1
def mapping_funcV2(invoice_from_qb):

    global journal_entry_count

    # Term -> "payment_terms_label"
    term_dict = dict()

    # taxcode_list = ['54', '62', '52', '13', '55', '58', '66', '70', '53', '57', '59', '65', '68']
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

    # tax_rate_fout = open('data_from_zoho/tax_id_and_name_PR.json')
    # tax_rate_details = json.load(tax_rate_fout)

    # items_from_zohofout = open('data_from_zoho/items_data_from_zoho.json')
    # items_from_zoho = json.load(items_from_zohofout)
    # contacts_from_zohofout = open('data_from_zoho/contacts_data_from_zoho.json')
    # contacts_from_zoho = json.load(contacts_from_zohofout)
    # chart_of_accounts_from_zohofout = open('data_from_zoho/chart_of_accounts_data_from_zoho.json')
    # chart_of_accounts_from_zoho = json.load(chart_of_accounts_from_zohofout)

    currency_from_zohofout = open('data_from_zoho/currency_details_pr.json')
    currency_from_zoho = json.load(currency_from_zohofout)

    chart_of_accounts_from_zohofout = open('data_from_zoho/coa_details_PR.json')
    chart_of_accounts_from_zoho = json.load(chart_of_accounts_from_zohofout)

    null_value = None

    tds_section_dict = dict()
    tds_section_dict["20"] = ["194J-(1)-Fees for Professinal and Technical Services","1208528000000097009"]
    # tds_section_dict["21"] = ["194J-(2)-Remuneration to Director",""]
    tds_section_dict["0"] = ["",""]


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
    else:
        mapping_dict["entry_number"] = f"TRANSFER_{journal_entry_count}-{extracted_year}"
        mapping_dict["journal_number_prefix"] = f"TRANSFER_{journal_entry_count}-{extracted_year}-"
        mapping_dict["journal_number_suffix"] = f"{journal_entry_count}"
    
    journal_entry_count = journal_entry_count + 1


    # mapping_dict["currency_id"] = null_value
    if "CurrencyRef" in invoice_from_qb:
        mapping_dict["currency_id"] = currency_from_zoho[invoice_from_qb["CurrencyRef"]["value"]]

    # CustomField

    # Definition Id 0
    # cf_id_0_dict = dict()
    # # mapping_dict["cf_id_0_name"] = invoice_from_qb["CustomField"][0]["Name"]
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


    # custom_field_list = list()
    # custom_field_list.append(cf_id_0_dict)
    # custom_field_list.append(cf_id_1_dict)
    # custom_field_list.append(cf_id_2_dict)
    # mapping_dict["custom_fields"] = custom_field_list

    print(invoice_from_qb["Id"])
    mapping_dict["id_from_qb"] = invoice_from_qb["Id"]
    
    flag_for_customer_vendor = False

    first_line_item = dict()
    if "ToAccountRef" in invoice_from_qb:
        first_line_item["description"] = ""
        first_line_item["amount"] = invoice_from_qb["Amount"]
        first_line_item["debit_or_credit"] = 'credit'
        first_line_item["account_id"] = chart_of_accounts_from_zoho[invoice_from_qb["ToAccountRef"]["name"]]

    my_notes = ''
    
    my_item_list = list()
        
    # for item in invoice_from_qb:
            # item_id is string

            # cf_dict = dict()
            # cf_dict["label"] = "Class"
            # cf_dict["value"] = null_value
    my_item_dict = dict()
    if "FromAccountRef"  in  invoice_from_qb:      
        my_item_dict["amount"] = invoice_from_qb["Amount"]
        my_item_dict["debit_or_credit"] = "debit"
        my_item_dict["account_id"]=chart_of_accounts_from_zoho[invoice_from_qb["FromAccountRef"]["name"]]
        my_item_dict["description"]= ""

                
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
            #     # tds_mapping_dict["account_id"] = "1111479000000014016"

            #     tds_section_type_id = item["TDSLineDetail"]["TDSSectionTypeId"]
            #     my_item_dict["tds_detail_section_type_id"] = item["TDSLineDetail"]["TDSSectionTypeId"]


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
    #             print(invoice_from_qb["Id"])
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

    cleaned_my_item_list.append(first_line_item)

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

    customer_notes += my_notes
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

def generate_post_json():

    # https://www.geeksforgeeks.org/read-json-file-using-python/
    # file_name = 'all_fetched_data_from_qb.json'
    # file_name = 'production_get.json'

    # file_name = '../data_from_qb_2013_04_01_to_2017_06_30_deposit.json'
    file_name = '../trnsfr_PR.json'
    # file_name = 'left_out17_to_22.json'

    # file_name = 'involved_account_not_applicable.json'

    # file_name = 'test_invoice_data.json'

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
        mapped_customer = mapping_funcV2(item)

        if mapped_customer is None:
            count = count + 1
        else:
            my_item_list.append(mapped_customer)
    
    # mapped_data = dict()
    # mapped_data["JournalEntry"] = my_item_list

    mapped_json = json.dumps(my_item_list,indent=4)

    print("The Customer and Vendor JE are : ",count)
    print("The coa missing list is: ",count_missing_coa_list)
    with open("mapped_tnsfr_je_PR.json", "w") as outfile:
        outfile.write(mapped_json)


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
    refresh_token = '1000.973c969341b68a7ea227c3eaaad082cf.d24d917f7b60abdffe6ea564861a7684'
    access_token = '1000.613bcff35595338810d6c4484644b797.98737e6b7747b20f35c0d0619b7c1d3e'
    # expires_in = parsed_data["expires_in"]

    print(refresh_token)
    print(access_token)

    organization_id = '60019790139'
    # organization_id = '60015983411'
    post_url = f'https://books.zoho.in/api/v3/journals?ignore_auto_number_generation=true&organization_id={organization_id}'

    f = open('mapped_tnsfr_je_PR.json')
    # f = open('failed_mapped.json')
    # f = open('to_again_mapped.json')
    # f = open('involved_account_not_applicable_mapped.json')

    parsed_data2 = json.load(f)
    # items_list = parsed_data2["JournalEntry"]
    items_list = parsed_data2


    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_transfer_PR2.txt","a")
    # response_save_file = open("saved_deposit_left_out_17_to_22_id.txt","a")
    error_response_save_file = open("error_console_for_failed_invoice.txt","a")


    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")
    # error_response_save_file.write(f"NEW WRITE STARTED: {dt_string}\n")

    for item in items_list:
        while True:
            print(f'Processing for entry_number: {item["entry_number"]}||{item["journal_date"]}||{item["id_from_qb"]}....')
            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(0.5)
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



# generate_post_json()
post_request_zoho()