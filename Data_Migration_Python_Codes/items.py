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
    refresh_token = 'AB11669730876vEOwrUIUdWvD7OFE3QvTIDoQG5etIr1BjZM4p'
    access_token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..TlHX2OJ_lO0ujBQ_RQFT6w.JLBhIcJWAFyyo-alK_pVCYp57tAom8riTiVZp7omVUlDh30DwXbfCQ6oilPLwVEmDrfzDzcU-vptEfneZ4D_VKZHHLTaK3WKGBcFzBcLE0C9-N0DHqTd_N0NoHDlkoZVjqVSapuZqATuh0kklnjO3z5zdqgvGdyK80dzIwcaAclHJGeflxzLhnRSWOfMe5JEHYaePor65kIqxBCbEYoXuVIaP9Z0zdqGbb824IAnJMT36m7Mi2Rq5mNFlVAosf9A6TCcjomjD6vFqYwBg7dKPphRLISxWycj4MlPfsmh0IJEP24QFkhehKr2Nr5uiir0Jqv6JshygjKEulMtyiuwd3oytQfpjV-OFqceZbFWO1Q5tlQOfA6AXLWA4jTW3ucrXhSIkKJxHzkpV2AJlZCfGNzvolSbMWpuawHtXepxizEFFNRfYSdO4AW0FJ1hFZdA9R-YqXYbTqhtBaMG3CxfOO2wfga1nlVfzEaN04uYX4iTHDVt45GXufVRTls8UZSC1KdtpsbvlIyEHALlju2R6AxNDg6UCnnU8nyZhTPLLxhK6BetgDZNz_WUg0ObMf7GwXlYKfAaq4UQpVadl1yaMmO4VRIg8bkPrscgxDAajadu8168HNZ4YNUOJ4ucrnLV16sSmuIYbSL_acrECZD-O_wrl2M-bqFojb_YwH6DASjCIRdIXYRijCbcuG3uA-q2cWsNLLxzu3kMgK861gdYtEZA_qlo6lafAHIX16Vnfvl6g00FBAy1PouO_5qanLUH.wwIW58J2YrOrXgibDctcyQ'
    realmID = '4620816365221051280'

    client_id = 'ABsXVVAiyYYgiI6SvYDBz7AFsw5Rd4sn0PSmN6STlbWnlrkwgw'
    client_secret = 'Rioiq4ehbAZoDcbpHyrcoU2LsmL70yxzTSbSTYAS'

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

    file_name = 'data_from_qb_item_active_ac.json'
    fp = open(file_name,'a')
    startPosition = 1
    no_of_objects_fetched = 0
    flag = True
    while flag == True:
        selectQuery = f'select * from Item startPosition {startPosition}'
        sandbox_getURL = f"{sandboxURL}/v3/company/{realmID}/query?query={selectQuery}&minorversion=65"
        production_getURL = f"{productionURL}/v3/company/{realmID}/query?query={selectQuery}&minorversion=65"
        headers["Authorization"] = f"Bearer {access_token}"
        r = requests.get(sandbox_getURL,headers=headers)

        # print(r.status_code)
        if r.status_code == 200:
            parsed_data = r.json()

            if "QueryResponse" in parsed_data:
                if "Item" in parsed_data["QueryResponse"]:
                    for element in parsed_data["QueryResponse"]["Item"]:
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


def mapping_func(items_from_qb):

    null_value = None


    product_type = dict()
    product_type["Service"] = "service"
    product_type["NonInventory"] = "goods"
    product_type["Inventory"] = "goods"
    product_type["Category"] = "goods"

    account_dict = dict()
    account_dict["Deferred Tax Asset"] = "1208528000000058483"
    account_dict["Loan to Mr.Singavi"] = "1208528000000058369"
    account_dict["Loan to Pradip"] = "1208528000000058375"
    account_dict["Loan to Pratiksha distributors"] = "1208528000000058381"
    account_dict["Loan to Priyesh Jain"] = "1208528000000058387"
    account_dict["Loan to Sadhana Ostwal"] = "1208528000000058393"
    account_dict["Loan to Suvarna M Balai"] = "1208528000000058399"
    account_dict["Loans to Pushkraj Industries"] = "1208528000000058405"
    account_dict["Mr Priyesh Jain"] = "1208528000000058411"
    account_dict["Office Deposite"] = "1208528000000058417"
    account_dict["Pradip Lodha - Loan"] = "1208528000000058423"
    account_dict["Employee Advance"] = "1208528000000000570"
    account_dict["Prepaid Insurance"] = "1208528000000058429"
    account_dict["Rahul Yelwande"] = "1208528000000058435"
    account_dict["Ravinanda Ladmarks"] = "1208528000000058441"
    account_dict["Service Tax Refund"] = "1208528000000058447"
    account_dict["Advance To Narendra Bafna"] = "1208528000000058195"
    account_dict["Shree Harinath Cotton Industries"] = "1208528000000058453"
    account_dict["Deferred CGST"] = "1208528000000058201"
    account_dict["Staff Advance -Ashish Harale"] = "1208528000000058459"
    account_dict["Deferred GST Input Credit"] = "1208528000000058207"
    account_dict["Sales to Customers (Cash)"] = "1208528000000015200"
    account_dict["Sundry Debtors - Others"] = "1208528000000058465"
    account_dict["Deferred IGST"] = "1208528000000058213"
    account_dict["Suspense"] = "1208528000000058471"
    account_dict["Deferred Krishi Kalyan Cess Input Credit"] = "1208528000000058219"
    account_dict["Uncategorised Asset"] = "1208528000000058477"
    account_dict["Deferred Service Tax Input Credit"] = "1208528000000058225"
    account_dict["Deferred SGST"] = "1208528000000058231"
    account_dict["Deferred VAT Input Credit"] = "1208528000000058237"
    account_dict["Excess Short Credit on ITC"] = "1208528000000058243"
    account_dict["FD In Federal Bank  -35135"] = "1208528000000058249"
    account_dict["FD in Federal Bank - 24980"] = "1208528000000058255"
    account_dict["FD in Federal Bank - 25409"] = "1208528000000058261"
    account_dict["FD in Federal Bank -32462"] = "1208528000000058267"
    account_dict["Reverse Charge Tax Input but not due"] = "1208528000000016031"
    account_dict["Fixed Deposit 12102022"] = "1208528000000058273"
    account_dict["Prepaid Expenses"] = "1208528000000015012"
    account_dict["Fixed Deposit 20755"] = "1208528000000058279"
    account_dict["TDS Receivable"] = "1208528000000015016"
    account_dict["Fixed Deposit Federal Bank"] = "1208528000000058285"
    account_dict["Fixed Deposit-09052022"] = "1208528000000058291"
    account_dict["Input Tax Credits"] = "1208528000000016055"
    account_dict["Input IGST"] = "1208528000000016061"
    account_dict["Input CGST"] = "1208528000000016073"
    account_dict["Input SGST"] = "1208528000000016085"
    account_dict["Fixed Deposit-18190300040515"] = "1208528000000058297"
    account_dict["Fixed Deposite 14062022"] = "1208528000000058303"
    account_dict["GST Cash Ledger"] = "1208528000000058309"
    account_dict["GST Refund"] = "1208528000000058315"
    account_dict["Income Tat Refund FY 2019-2020"] = "1208528000000058321"
    account_dict["Advance Tax"] = "1208528000000000468"
    account_dict["Income Tax Refund FY 17-18"] = "1208528000000058327"
    account_dict["Income Tax Refund FY 18-19"] = "1208528000000058333"
    account_dict["Income Tax Refund FY 2020-21"] = "1208528000000058339"
    account_dict["Investments - Fixed Deposite"] = "1208528000000058345"
    account_dict["Krishi Kalyan Cess Refund"] = "1208528000000058351"
    account_dict["Loan to Devesh"] = "1208528000000058357"
    account_dict["Loan to Mr Sanjay Munot"] = "1208528000000058363"
    account_dict["Undeposited Funds"] = "1208528000000000456"
    account_dict["Petty Cash"] = "1208528000000000459"
    account_dict["Cash on hand"] = "1208528000000059013"
    account_dict["PAYRULE SERVICES PRIVATE LIMITED (3696)"] = "1208528000000059017"
    account_dict["Accounts Receivable"] = "1208528000000000462"
    account_dict["Leasehold Improvements"] = "1208528000000058627"
    account_dict["Microtek UPS & Power Max Battery"] = "1208528000000058633"
    account_dict["Mobile Handset"] = "1208528000000058639"
    account_dict["Vehicles"] = "1208528000000058645"
    account_dict["Wall Clocks -Seiko"] = "1208528000000058651"
    account_dict["Accumulated Depreciation"] = "1208528000000058561"
    account_dict["Apple MacBook AIR M1 8GB"] = "1208528000000058567"
    account_dict["Battery -Exide"] = "1208528000000058573"
    account_dict["Furniture and Equipment"] = "1208528000000000465"
    account_dict["Bionaire BT36R -Watt Tower Fan 36"] = "1208528000000058579"
    account_dict["Buildings and Improvements"] = "1208528000000058585"
    account_dict["Computer and Hardware"] = "1208528000000058591"
    account_dict["Dell Laptop -Dell 5450 i5/8gb Touch Screen"] = "1208528000000058597"
    account_dict["Digital clock Yale Black YDM"] = "1208528000000058603"
    account_dict["INVERTOR / UPS"] = "1208528000000058609"
    account_dict["Land"] = "1208528000000058615"
    account_dict["Laptop -Dell Vostro 3590"] = "1208528000000058621"
    account_dict["Pratik Cabletrey-Creditors"] = "1208528000000058117"
    account_dict["Professional Fees payable"] = "1208528000000058123"
    account_dict["Professional Tax on Salaries"] = "1208528000000058129"
    account_dict["Accounting Charges Payable"] = "1208528000000057877"
    account_dict["Professional Tax Payable"] = "1208528000000058135"
    account_dict["Audit Fees Payable"] = "1208528000000057883"
    account_dict["Salary Payable"] = "1208528000000058141"
    account_dict["Balai Darshan M (Creditors)"] = "1208528000000057889"
    account_dict["Service Tax Payable"] = "1208528000000058147"
    account_dict["CGST Payable"] = "1208528000000057895"
    account_dict["Service Tax Suspense"] = "1208528000000058153"
    account_dict["Client Payment of PF & ESIC"] = "1208528000000057901"
    account_dict["SGST Payable"] = "1208528000000058159"
    account_dict["CST Payable"] = "1208528000000057907"
    account_dict["Suryawanshi Ganesh L"] = "1208528000000058165"
    account_dict["CST Suspense"] = "1208528000000057913"
    account_dict["Swachh Bharat Cess Payable"] = "1208528000000058171"
    account_dict["Employee Reimbursements"] = "1208528000000000573"
    account_dict["Director Remuneration Payable"] = "1208528000000057919"
    account_dict["Swachh Bharat Cess Suspense"] = "1208528000000058177"
    account_dict["Drusti Mulay"] = "1208528000000057925"
    account_dict["VAT Payable"] = "1208528000000058183"
    account_dict["Duties and Taxes-Professional Tax on Salries"] = "1208528000000057931"
    account_dict["VAT Suspense"] = "1208528000000058189"
    account_dict["ESIC Payment -Payrule Services"] = "1208528000000057937"
    account_dict["GST Suspense"] = "1208528000000057943"
    account_dict["IGST Payable"] = "1208528000000057949"
    account_dict["Income Tax Payable"] = "1208528000000057955"
    account_dict["Opening Balance Adjustments"] = "1208528000000000615"
    account_dict["Unearned Revenue"] = "1208528000000000617"
    account_dict["Input CGST Tax RCM"] = "1208528000000057961"
    account_dict["Input IGST Tax RCM"] = "1208528000000057967"
    account_dict["Input Krishi Kalyan Cess"] = "1208528000000057973"
    account_dict["Input Krishi Kalyan Cess RCM"] = "1208528000000057979"
    account_dict["Input Service Tax"] = "1208528000000057985"
    account_dict["Input Service Tax RCM"] = "1208528000000057991"
    account_dict["Input SGST Tax RCM"] = "1208528000000057997"
    account_dict["Input VAT 14%"] = "1208528000000058003"
    account_dict["Input VAT 4%"] = "1208528000000058009"
    account_dict["Input VAT 5%"] = "1208528000000058015"
    account_dict["Krishi Kalyan Cess Payable"] = "1208528000000058021"
    account_dict["Reimbursements Payable"] = "1208528000000017319"
    account_dict["Payroll Tax Payable"] = "1208528000000017321"
    account_dict["GST Payable"] = "1208528000000016043"
    account_dict["Output IGST"] = "1208528000000016049"
    account_dict["Output CGST"] = "1208528000000016067"
    account_dict["Output SGST"] = "1208528000000016079"
    account_dict["Statutory Deductions Payable"] = "1208528000000017323"
    account_dict["Krishi Kalyan Cess Suspense"] = "1208528000000058027"
    account_dict["TDS Payable"] = "1208528000000015020"
    account_dict["Deductions Payable"] = "1208528000000017325"
    account_dict["Net Salary Payable"] = "1208528000000017327"
    account_dict["Hold Salary Payable"] = "1208528000000017329"
    account_dict["Output CGST Tax RCM"] = "1208528000000058033"
    account_dict["Output CST 2%"] = "1208528000000058039"
    account_dict["Output IGST Tax RCM"] = "1208528000000058045"
    account_dict["Output Krishi Kalyan Cess"] = "1208528000000058051"
    account_dict["Output Krishi Kalyan Cess RCM"] = "1208528000000058057"
    account_dict["Output Service Tax"] = "1208528000000058063"
    account_dict["Output Service Tax RCM"] = "1208528000000058069"
    account_dict["Tax Payable"] = "1208528000000000474"
    account_dict["Output SGST Tax RCM"] = "1208528000000058075"
    account_dict["Output VAT 14%"] = "1208528000000058081"
    account_dict["Output VAT 4%"] = "1208528000000058087"
    account_dict["Output VAT 5%"] = "1208528000000058093"
    account_dict["PAYRULE HR SOLUTIONS PVT LTD"] = "1208528000000058099"
    account_dict["Performance Incentive Payable"] = "1208528000000058105"
    account_dict["PF -Payrule Services"] = "1208528000000058111"
    account_dict["Accounts Payable"] = "1208528000000000471"
    account_dict["Mortgages"] = "1208528000000015052"
    account_dict["Construction Loans"] = "1208528000000015054"
    account_dict["Dimension Adjustments"] = "1208528000000000579"
    account_dict["Drawings"] = "1208528000000000561"
    account_dict["Opening Balance Equity"] = "1208528000000058957"
    account_dict["Share capital"] = "1208528000000058961"
    account_dict["Investments"] = "1208528000000015056"
    account_dict["Distributions"] = "1208528000000015058"
    account_dict["Capital Stock"] = "1208528000000015068"
    account_dict["Retained Earnings"] = "1208528000000000477"
    account_dict["Dividends Paid"] = "1208528000000015070"
    account_dict["Owner's Equity"] = "1208528000000000480"
    account_dict["Opening Balance Offset"] = "1208528000000000483"
    account_dict["Stability Certificate (deleted)"] = "1208528000000059139"
    account_dict["Other Charges"] = "1208528000000000619"
    account_dict["Shipping Charge"] = "1208528000000000622"
    account_dict["Billable Expense Income"] = "1208528000000058489"
    account_dict["BOCW license"] = "1208528000000058493"
    account_dict["Consulting Income"] = "1208528000000058497"
    account_dict["Contract Labour Registration Certificate"] = "1208528000000058501"
    account_dict["Discounts given"] = "1208528000000058505"
    account_dict["Interest Rec on FD 18190400020755"] = "1208528000000058509"
    account_dict["Interest Received FD"] = "1208528000000058513"
    account_dict["Labour Law Consultancy"] = "1208528000000058517"
    account_dict["PF Return Filling & Consultancy"] = "1208528000000058521"
    account_dict["Product Sales"] = "1208528000000058525"
    account_dict["Sales - Hardware"] = "1208528000000058529"
    account_dict["Sales - Software"] = "1208528000000058533"
    account_dict["Sales - Support and Maintenance"] = "1208528000000058537"
    account_dict["Sales Discounts"] = "1208528000000058541"
    account_dict["Sales of Product Income"] = "1208528000000058545"
    account_dict["Services"] = "1208528000000058549"
    account_dict["Unapplied Cash Payment Income"] = "1208528000000058553"
    account_dict["Uncategorised Income"] = "1208528000000058557"
    account_dict["ESIC Registration Charges (deleted)"] = "1208528000000059083"
    account_dict["ESIC Return Filling & Complince (deleted)"] = "1208528000000059087"
    account_dict["Factory License Processing (deleted)"] = "1208528000000059091"
    account_dict["HR & Online System set up onetime (deleted)"] = "1208528000000059095"
    account_dict["MLWF Insect & Registration (deleted)"] = "1208528000000059099"
    account_dict["Payroll Management (deleted)"] = "1208528000000059103"
    account_dict["Payroll Set up (deleted)"] = "1208528000000059107"
    account_dict["Sales"] = "1208528000000000486"
    account_dict["PF & ESIC Consultancy (deleted)"] = "1208528000000059111"
    account_dict["General Income"] = "1208528000000000489"
    account_dict["PF Registration Charges (deleted)"] = "1208528000000059115"
    account_dict["Interest Income"] = "1208528000000000492"
    account_dict["Late Fee Income"] = "1208528000000000495"
    account_dict["Professional Fees (deleted)"] = "1208528000000059119"
    account_dict["PT Return Filling & Challan (deleted)"] = "1208528000000059123"
    account_dict["PTRC Registration (deleted)"] = "1208528000000059127"
    account_dict["Discount"] = "1208528000000000504"
    account_dict["RC Certificate -Under Contract Act (deleted)"] = "1208528000000059131"
    account_dict["Shop Act License (deleted)"] = "1208528000000059135"
    account_dict["Finance Charge Income"] = "1208528000000057701"
    account_dict["Insurance Proceeds Received"] = "1208528000000057705"
    account_dict["Interest  Received  FD 20755"] = "1208528000000057709"
    account_dict["Interest Received on FD"] = "1208528000000057713"
    account_dict["Proceeds from Sale of Assets"] = "1208528000000057717"
    account_dict["Rounding off"] = "1208528000000057721"
    account_dict["Roundoff Income"] = "1208528000000057725"
    account_dict["Shipping and Delivery Income"] = "1208528000000057729"
    account_dict["Travel Expense"] = "1208528000000000516"
    account_dict["Repair and maintenance"] = "1208528000000058885"
    account_dict["Telephone Expense"] = "1208528000000000519"
    account_dict["Automobile Expense"] = "1208528000000000522"
    account_dict["Shipping Charges"] = "1208528000000058891"
    account_dict["IT and Internet Expenses"] = "1208528000000000525"
    account_dict["Rent Expense"] = "1208528000000000528"
    account_dict["Small Tools and Equipment"] = "1208528000000058897"
    account_dict["Janitorial Expense"] = "1208528000000000531"
    account_dict["Postage"] = "1208528000000000534"
    account_dict["Society Maintenance Charges"] = "1208528000000058903"
    account_dict["Bad Debt"] = "1208528000000000537"
    account_dict["Printing and Stationery"] = "1208528000000000540"
    account_dict["Software Charges -Tally"] = "1208528000000058909"
    account_dict["Salaries and Employee Wages"] = "1208528000000000543"
    account_dict["Admin Charges -PF"] = "1208528000000058657"
    account_dict["Meals and Entertainment"] = "1208528000000000546"
    account_dict["Staff Refreshment"] = "1208528000000058915"
    account_dict["Depreciation Expense"] = "1208528000000000549"
    account_dict["Advertising/Promotional"] = "1208528000000058663"
    account_dict["Consultant Expense"] = "1208528000000000552"
    account_dict["Swachh Bharat Cess Expense"] = "1208528000000058921"
    account_dict["Repairs and Maintenance"] = "1208528000000000555"
    account_dict["Annual function Expenses"] = "1208528000000058669"
    account_dict["Other Expenses"] = "1208528000000000558"
    account_dict["Taxes - Property"] = "1208528000000058927"
    account_dict["Annual Maintenance Charges -Computer"] = "1208528000000058675"
    account_dict["Lodging"] = "1208528000000000564"
    account_dict["Unapplied Cash Bill Payment Expense"] = "1208528000000058933"
    account_dict["Antivirus License & Internet Security Expenses"] = "1208528000000058681"
    account_dict["Uncategorised Expense"] = "1208528000000058939"
    account_dict["Audit Fees"] = "1208528000000058687"
    account_dict["Uncategorized"] = "1208528000000000576"
    account_dict["Utilities"] = "1208528000000058945"
    account_dict["Bank charges"] = "1208528000000058693"
    account_dict["Web side  Designing"] = "1208528000000058951"
    account_dict["Business Licenses and Permits"] = "1208528000000058699"
    account_dict["Business Tour Expenses"] = "1208528000000058705"
    account_dict["Staff Salaries"] = "1208528000000057683"
    account_dict["Gift For Staff -Entertainment"] = "1208528000000057689"
    account_dict["Performance Incentive"] = "1208528000000057695"
    account_dict["Charitable Contributions"] = "1208528000000058711"
    account_dict["Cloud Hosting Charges"] = "1208528000000058717"
    account_dict["Commissions and fees"] = "1208528000000058723"
    account_dict["Computer and Internet Expense"] = "1208528000000058729"
    account_dict["Continuing Education"] = "1208528000000058735"
    account_dict["Courier Expenses"] = "1208528000000058741"
    account_dict["Digital Marketing Expenses"] = "1208528000000058747"
    account_dict["Director Remuneration"] = "1208528000000058753"
    account_dict["Diwali Gifts Expenses"] = "1208528000000058759"
    account_dict["Dues and Subscriptions"] = "1208528000000058765"
    account_dict["Electricity Expenses"] = "1208528000000058771"
    account_dict["ESIC  Contribution -Employer"] = "1208528000000058777"
    account_dict["Fixed Asset Written off"] = "1208528000000058783"
    account_dict["Housekeeping Charges"] = "1208528000000058789"
    account_dict["Insurance Expense"] = "1208528000000058795"
    account_dict["Insurance Expense-General Liability Insurance"] = "1208528000000058801"
    account_dict["Insurance Expense-Health Insurance"] = "1208528000000058807"
    account_dict["Insurance Expense-Life and Disability Insurance"] = "1208528000000058813"
    account_dict["Insurance Expense-Professional Liability"] = "1208528000000058819"
    account_dict["Interest Expense"] = "1208528000000058825"
    account_dict["MLWF"] = "1208528000000058831"
    account_dict["Office/General Administrative Expenses"] = "1208528000000058837"
    account_dict["Online Software Charges"] = "1208528000000058843"
    account_dict["Raw Materials And Consumables"] = "1208528000000015072"
    account_dict["PF Contribution -Employer"] = "1208528000000058849"
    account_dict["Merchandise"] = "1208528000000015074"
    account_dict["Transportation Expense"] = "1208528000000015076"
    account_dict["Depreciation And Amortisation"] = "1208528000000015078"
    account_dict["Postage and Delivery"] = "1208528000000058855"
    account_dict["Contract Assets"] = "1208528000000015080"
    account_dict["Printing and Reproduction"] = "1208528000000058861"
    account_dict["Office Supplies"] = "1208528000000000498"
    account_dict["Professional Fees Paid"] = "1208528000000058867"
    account_dict["Advertising And Marketing"] = "1208528000000000501"
    account_dict["Purchase Discounts"] = "1208528000000011001"
    account_dict["Purchases"] = "1208528000000058873"
    account_dict["Bank Fees and Charges"] = "1208528000000000507"
    account_dict["Credit Card Charges"] = "1208528000000000510"
    account_dict["Rent or Lease of Buildings"] = "1208528000000058879"
    account_dict["Cost of Goods Sold"] = "1208528000000000567"
    account_dict["Cost of sales"] = "1208528000000058965"
    account_dict["Equipment Rental for Jobs"] = "1208528000000058971"
    account_dict["Freight and Shipping Costs"] = "1208528000000058977"
    account_dict["Merchant Account Fees"] = "1208528000000058983"
    account_dict["Purchases - Hardware for Resale"] = "1208528000000058989"
    account_dict["Purchases - Software for Resale"] = "1208528000000058995"
    account_dict["Subcontracted Services"] = "1208528000000059001"
    account_dict["Tools and Craft Supplies"] = "1208528000000059007"
    account_dict["Labor"] = "1208528000000015060"
    account_dict["Materials"] = "1208528000000015062"
    account_dict["Subcontractor"] = "1208528000000015064"
    account_dict["Job Costing"] = "1208528000000015066"
    account_dict["Exchange Gain or Loss"] = "1208528000000000513"
    account_dict["Tax Expenses"] = "1208528000000057859"
    account_dict["Tax write-off"] = "1208528000000057865"
    account_dict["Vehicle Expenses"] = "1208528000000057871"
    account_dict["Accounting Charges"] = "1208528000000057733"
    account_dict["Ask My Accountant"] = "1208528000000057739"
    account_dict["CGST write-off"] = "1208528000000057745"
    account_dict["Earlier Period Tax"] = "1208528000000057751"
    account_dict["GST write-off"] = "1208528000000057757"
    account_dict["IGST write-off"] = "1208528000000057763"
    account_dict["Income Tax Expenses"] = "1208528000000057769"
    account_dict["Ineligible ITC"] = "1208528000000057775"
    account_dict["Interest & Late on GST"] = "1208528000000057781"
    account_dict["Interest on GST"] = "1208528000000057787"
    account_dict["Interest On Income Tax"] = "1208528000000057793"
    account_dict["Interest on TDS Payable"] = "1208528000000057799"
    account_dict["Late Fees on GST"] = "1208528000000057805"
    account_dict["Late fees Paid"] = "1208528000000057811"
    account_dict["Miscellaneous Expense"] = "1208528000000057817"
    account_dict["Other Expense"] = "1208528000000057823"
    account_dict["Political Contributions"] = "1208528000000057829"
    account_dict["Provision for Income Tax"] = "1208528000000057835"
    account_dict["Reconciliation Discrepancies"] = "1208528000000057841"
    account_dict["Recruitment Expenses"] = "1208528000000057847"
    account_dict["SGST write-off"] = "1208528000000057853"
    account_dict["Inventory Asset"] = "1208528000000000626"





    mapping_dict = dict()

    # null_value = None

    if "Name" in items_from_qb:
        mapping_dict["name"] = items_from_qb["Name"]
    else:
        mapping_dict["name"] = null_value

    if "UnitPrice" in items_from_qb:
        mapping_dict["rate"] = items_from_qb["UnitPrice"]
    else:
        mapping_dict["rate"] = null_value

    description = ""
    if "Description" in items_from_qb:
        description = items_from_qb["Description"]

    if "TaxClassificationRef" in items_from_qb:
        mapping_dict["hsn_or_sac"] = items_from_qb["TaxClassificationRef"]["value"]
        description  += items_from_qb["TaxClassificationRef"]["name"]
    else:
        mapping_dict["hsn_or_sac"] = null_value
    
    if "Sku" in items_from_qb:
        mapping_dict["sku"] = items_from_qb["Sku"]
    else:
        mapping_dict["sku"] = null_value
    
    if "Type" in items_from_qb:
        mapping_dict["product_type"] = product_type[items_from_qb["Type"]]
    else:
        mapping_dict["product_type"] = null_value
    
    # if "Taxable" in items_from_qb:
    #     if items_from_qb["Taxable"]:
    #         mapping_dict["is_taxable"] = True
    #     else:
    #         mapping_dict["is_taxable"] = False

    is_item_type_sales = False
    is_item_type_purchases = False

    item_type = ""
    if "IncomeAccountRef" in items_from_qb:
        is_item_type_sales = True
    
    if "ExpenseAccountRef" in items_from_qb:
        is_item_type_purchases = True
    
    if is_item_type_sales and is_item_type_purchases:
        mapping_dict["item_type"] = "sales_and_purchases"

        # items_from_qb["IncomeAccountRef"]["value"] gives mapping_dict["account_id"]

        mapping_dict["account_id"] = account_dict[items_from_qb["IncomeAccountRef"]["name"]]
        # mapping_dict["account_name"] = 'We will get very soon ...'
        mapping_dict["account_name"] = items_from_qb["IncomeAccountRef"]["name"]

        mapping_dict["purchase_account_id"] = account_dict[items_from_qb["ExpenseAccountRef"]["name"]]
        # mapping_dict["purchase_account_name"] = 'We will get very soon ...'
        mapping_dict["purchase_account_name"] = items_from_qb["ExpenseAccountRef"]["name"]


    elif is_item_type_sales:
        mapping_dict["item_type"] = "sales"
        # items_from_qb["IncomeAccountRef"]["value"]
        mapping_dict["account_id"] = account_dict[items_from_qb["IncomeAccountRef"]["name"]]
        # mapping_dict["account_name"] = 'We will get very soon ...'

        mapping_dict["account_name"] = items_from_qb["IncomeAccountRef"]["name"]


    elif is_item_type_purchases:
        mapping_dict["item_type"] = "purchases"
        mapping_dict["purchase_account_id"] = account_dict[items_from_qb["ExpenseAccountRef"]["name"]]
        # mapping_dict["purchase_account_name"] = 'We will get very soon ...'

        mapping_dict["purchase_account_name"] = items_from_qb["ExpenseAccountRef"]["name"]


    else:
        # If is_item_type_sales and is_item_type_purchases are False
        mapping_dict["item_type"] = null_value

    # account_id we will get from the "IncomeAccountRef" and "ExpenseAccountRef"

    if "SalesTaxCodeRef" in items_from_qb:
        mapping_dict["taxability_type"] = items_from_qb["SalesTaxCodeRef"]["name"]

    mapping_dict["description"] = description


    return mapping_dict



def generate_post_json():

    # https://www.geeksforgeeks.org/read-json-file-using-python/
    # file_name = 'all_fetched_data_from_qb.json'
    # file_name = 'production_get.json'
    # file_name = 'excel/data_from_qb_items.json'
    file_name = 'data_from_qb_item_active_pr.json'



    f = open(file_name)
    parsed_data = json.load(f)

    # item_list = parsed_data["QueryResponse"]["Item"]
    my_item_list = list()
    for item in parsed_data:
        # my_item_dict = dict()
        # my_item_dict['name'] = item["Name"]
        # my_item_dict['rate'] = item["UnitPrice"]

        mapped_item = mapping_func(item)
        my_item_list.append(mapped_item)
    
    mapped_data = dict()
    mapped_data["Item"] = my_item_list

    mapped_json = json.dumps(mapped_data,indent=4)

    with open("mapped_item_PR.json", "w") as outfile:
        outfile.write(mapped_json)


# 'code' variable must be updated before running this function
def post_request_zoho():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # ZohoBooks.fullaccess.all
    # code = '1000.daac461adc23832519ccfdd0f40520af.8ced3ae8eb7d080c9cb2ca44fbebcbf3'
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
    
    refresh_token = '1000.af053ec9718b2c4619ff81c5265d18d2.2b09ce857e9089cc0f06b8d4a45444f1'
    access_token = '1000.630ae0ed181c1dfb95c746bf95bcac58.85d71867ad083d0c53d79016f84c8a9e'
    # expires_in = parsed_data["expires_in"]

    organization_id = '60019790139'
    post_url = f'https://books.zoho.in/api/v3/items?organization_id={organization_id}'

    f = open('../mapped_item_PR.json')
    parsed_data2 = json.load(f)
    items_list = parsed_data2["Item"]

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_item_PR.txt","a")

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
                response_save_file.write(f'{parsed_data3["item_id"]} : {item["name"]}\n')
                print(f'{item["name"]} is successfully pushed')
                # It means success
                break
            else:
                print(f'ERROR occurred: {item["name"]} was able to be pushed')
                print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                response_save_file.write(f'Failed to PUSH : {item["name"]} -> msg is {parsed_data3["message"]}\n')
                response_save_file.flush()
                break

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


# get_items_and_write_to_file()
# generate_post_json()
post_request_zoho()




        

