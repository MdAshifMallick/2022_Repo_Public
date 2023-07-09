# Realm ID : 4620816365221051280
# Refresh Token : AB11669005834yy7f3vM3AbtxyhN0GPpZohd2ppGf5h2MDb9XV expires in 101 days
# Access Token : eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..0p2dc3enERLQynKRXAPjMg.BmeLQQaZhlwL4DhQCS6iC25NFi3NU3AA3BfatKvrNq0iXBMzXEXufpRcfS9iPY8yqNLRCAu_BW7O5NaqADZEXcO1aNtK26HYcOTXAI9asgOw2Lp5leUhudtBzKb6y3wF8Buzq5UaM1BNX12dn4Mk0HijqQ3Lo4lPLc5MM_8MOr4-4uOWFdiQizGknNUgGqiqcqjvVpWZCp8i5xcOW_bf7O0EKJpQx6Wf5surj01X1f6tWX9NKftq_LQ58LfD_fB9uVirB9zdOkmcCCJ4aokBSMV47pWhB8R81QCBLFYd35RQObeU5hkIB21_nYc09covmy4P4bPA61OON6nH9hV2ofVT_FguRiuVhiuIb3Ubakl3FiSlnKuenw5Xd73GAAQRHm4kM_IlVQoc2Zun1UdSUE36fJnzx1LCCBmtZ04tDr0E6qghSfYlCECoX90MuD6qPc_EtGmkoS2b_wkIwSCeZQ3PTI4dS9Mhq878NeUo7Joek_gCmsKc0_3UbTZqaPef0kK8yEFCGCutTCBm6cuGwGa8kyQnLQyFGEulzIm7oULn0hEi8UHPBR92-lKo1Gmsq9EzYnGdkQ3img5kf6cOgE01Bqlb2Ek4VwPjaOYgtUBGg8SCwfEZdEjQRaMx3y7A9k7oEIUO8SmVWtKtvH3m3CzqNzn9PMv5zXNi1xSWaMFSbJU8RlD3i9B8Y-i1KqvXz9UNjHlR3uFvEvs7W2Y9K90S5dkW61OVptOT-rncxmuJgGNIF9wj1zcpgQsMdXp3.VOLnrFPCYY0T2xxdUl97Rw
# expires in 60 minutes

import base64
import json
from time import sleep
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime
import os

# 'access_token' variable must be updated before running this function
def get_items_and_write_to_file():
    # Sandbox URL
    sandboxURL = 'https://sandbox-quickbooks.api.intuit.com'
    productionURL = 'https://quickbooks.api.intuit.com'
    auth_URL = 'https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer'

    # These must be changed
    refresh_token = 'AB11690448827CtSBoD5b0xxpOscInT6FGRrDmHiC97H9HJ7OK'
    access_token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..JPZ-JMePCyDM0DgYmzk4Og.Aysz1X4vRGCZQhPVeTGSd6XJXDPYrBSJGgmX7u61pPOPwayiHHY7s-cI8eRuVKimBfJmKF0XOWxkAPUQSglsdnt1YNGt1ADwkvLYfg5UugXQ6v3D5FiKOWAdNd4wafEH05Qf1x1pte1WK9HEZAivLnM-9782A4teN0wAG9YyU6jTxh2bVtbFgD8PEIPi5LYkYaJMHbLKHBPa3hC6h4bqq2k85qRT5mjLn2x9XrRVYEebjJjOLiHb8s8GrBUaS03DLy5EArSwcQhx8PSTwBvhTVsdWtAV4cCBQV8BeJIZIgxTyDiOXhPVRjyh7AC7g9Fkqrf8HONT8-ff5fXst6T0SD9pByfWFZxnZM4mjuvPv2yXvky6L-YUVkOofRk1qasHxQmbRL_rms-HJo9neucaBK5HfKtqhRq-Qt2Hc4z5ai-C2F0fJzO-Wtm9tZjfQaIwWon59dnOIZEID-5qj0BUqu-L_e7VRzevRSeyUsOBUu-2vylSizv-MvpuZvws3LQr2ksEKn-OVSop0KiKPtcDy3iqkXr3d3kpqfqu4SlycnS50fQQQahd5OwY39IpZ5ehT5IsAIteGCAgFfL39SO4zEXRfQpWNY4MiDRA-Lnt4hLdVEfP93JSntwI_Bkee6RbWvSvmKy7J4raw4Jju4-uBViD32YSzEbh_jh6nBPSZSrjG4aHXUBAyOw3Gmyb7h628UvAvwpJzgq01jRbpd7FhluzfpAPUF2QhNKHLWmLhQk.0nwVbn3L7ob7ItSjMNjYIA'
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

    file_name = 'data_from_qb_attachable_payrule.json'
    fp = open(file_name,'a')
    startPosition = 1
    # startPosition = 32901
    no_of_objects_fetched = 0
    # no_of_objects_fetched = 32900
    flag = True
    while flag == True:
        selectQuery = f'select * from Attachable startPosition {startPosition}'
        sandbox_getURL = f"{sandboxURL}/v3/company/{realmID}/query?query={selectQuery}&minorversion=65"
        production_getURL = f"{productionURL}/v3/company/{realmID}/query?query={selectQuery}&minorversion=65"
        headers["Authorization"] = f"Bearer {access_token}"
        # r = requests.get(sandbox_getURL,headers=headers)
        r = requests.get(production_getURL,headers=headers)


        # print(r.status_code)
        # if r.status_code == 200:
        #     parsed_data = r.json()

        #     if "QueryResponse" in parsed_data:
        #         if "Attachable" in parsed_data["QueryResponse"]:
        #             for element in parsed_data["QueryResponse"]["Attachable"]:
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

        #         if "error" in auth_response:
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
        #             print("GENERATING ACCESS TOKEN .....")
        # else:
        #     print(f"SomeError occurred after fetching {no_of_objects_fetched} objects... dumping in error.json")
        #     errorfp = open('error.json','w')
        #     r_parsed = json.dumps(r.json(),indent=4)
        #     errorfp.write(r_parsed)
        #     exit()

        parsed_data = r.json()
        if "QueryResponse" in parsed_data:
            if "Attachable" in parsed_data["QueryResponse"]:
                for element in parsed_data["QueryResponse"]["Attachable"]:
                    indented_data = json.dumps(element,indent=4)
                    fp.write(indented_data)
                    fp.write('\n,\n')

                maxResults = parsed_data["QueryResponse"]["maxResults"]
                print(f"Fetched {maxResults} Objects")
                no_of_objects_fetched += maxResults

                print(f"startPosition currently fetched upto: {startPosition}")
                print(f"maxResults fetched: {maxResults}")
                print(f"No.of objects fetched: {no_of_objects_fetched}")

                startPosition = no_of_objects_fetched + 1

                print(f"startPosition to be fetched: {startPosition}\n")
            else:
                print(f"Finished...Total fetched {no_of_objects_fetched}")
                flag = False
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
                print("GENERATING ACCESS TOKEN.....")
                print(access_token)


def mapping_func(customer_from_qb):
    mapping_dict = dict()

    return mapping_dict

# clean out 'file_download.txt'
def download_all_attachable_at_once():

    file = 'data_from_qb.json'

    file_qb = open(file)
    parsed_data = json.load(file_qb)

    details_file = open('file_download.txt','a')

    for item in parsed_data:
        filename = item["FileName"]
        file_id = item["Id"]
        download_url = item["TempDownloadUri"]
        r = requests.get(download_url)

        # change for windows
        final_filename = f"download_folder/{file_id}#{filename}"

        file_download_count = 0
        with open(final_filename,'wb') as f:
            f.write(r.content)
            file_download_count = file_download_count + 1
            print(f"{final_filename} downloaded. File Downloaded is {file_download_count}")
        
        final_string = ""
        if "AttachableRef" in item:
            attachable_ref = item["AttachableRef"]

            write_string = f"{file_id}##"
            for ref in attachable_ref:
                value = ref["EntityRef"]["value"]
                type = ref["EntityRef"]["type"]
                includeonsend = ref["IncludeOnSend"]

                write_string += f"{value}##{type}##{includeonsend}&&"

            final_string = f"{write_string}\n"
        else:
            final_string = f"{file_id}##No AttachableRef present\n"

        details_file.write(final_string)

# clean out 'file_download.txt'
def download_all_attachable_in_chunks():

    file = 'data_from_qb.json'

    file_qb = open(file)
    parsed_data = json.load(file_qb)

    details_file = open('file_download.txt','a')

    for item in parsed_data:
        filename = item["FileName"]
        file_id = item["Id"]
        download_url = item["TempDownloadUri"]
        r = requests.get(download_url,stream=True)

        # change for windows
        final_filename = f"download_folder/{file_id}#{filename}"

        file_download_count = 0
        with open(final_filename,'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
            file_download_count = file_download_count + 1
            print(f"{final_filename} downloaded. File Downloaded is {file_download_count}")
        
        final_string = ""
        if "AttachableRef" in item:
            attachable_ref = item["AttachableRef"]

            write_string = f"{file_id}##"
            for ref in attachable_ref:
                value = ref["EntityRef"]["value"]
                type = ref["EntityRef"]["type"]
                includeonsend = ref["IncludeOnSend"]

                write_string += f"{value}##{type}##{includeonsend}&&"

            final_string = f"{write_string}\n"
        else:
            final_string = f"{file_id}##No AttachableRef present\n"

        details_file.write(final_string)


def download_attachable_at_once():
    file = 'data_from_qb.json'
    file_qb = open(file)
    parsed_data = json.load(file_qb)
    details_file = open('file_download.txt','a')

    # Sandbox URL
    sandboxURL = 'https://sandbox-quickbooks.api.intuit.com'
    productionURL = 'https://quickbooks.api.intuit.com'
    auth_URL = 'https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer'

    # These must be changed
    refresh_token = 'AB116704252382vkLwLIxyffpcMTvMupBrTBQDaZGf8DltUcIX'
    access_token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..n4XdpXSEau31iegKxFyDMw.gQ8Q208aHrENWmedQr2BpD56Xmo3JXVrV933LAo0VVD_LXwB3UoCUPy_qV6kiCC3YP4pLBAfbxOSPGGFp4T2SvBfnnWsHHWaYQ_I-n0P1d8nMJ4vi0dvrIPhUEZ7ulFGXUkJSeEFrYq3cM4xIc6194DuSp-hRaCy1TGVHV07tDT0_qkfHrX-ZWDpu07Q9r6kH7V41mEMoIJGUejqh7BjDYIbSf4gDoyHHrXmZemchZcmmVKNjZZctHJCfKvzKzBAmCK9OD5SncVjFWHCXnPabN6JiIiyHj9q4xqmg5Ibg0iXhnC6KsZ4agzYdMw2sQpRaiLq6ugD62hnqS3TZjShkVT3Bqi44AxjQzNU1PYGCuT1rNWK4LQUOBO2lOIvJbbPr_eUjBnNcl_pIcFtzScb5V5WXW88S65zut8oL9v_J_-ef8L-88gwEeE0qnl1tG0iNEWb9Mdd5jrUzZQyRetK2Wa4qyIAgS7kiIXKHInhPOuBYHxcIyUHKozPHCW-Viiogs_erLHxwDxYrlW2pE6cEsuEbciH0OOgDAlpFWhW0ihCN4Cw6h4mNrzpeTL7vy6LYakPFqU8MSdYnzUaKooTQs72bgzsGEzdhYvc_d9VfA_IkGfg8lAIO6UIIpUTgTpMMDxlHDv1sQ3yaXyrCka41SlXhpPRvwFeOSog3RWHdgeoTt4ojVjHh5Aer5jXgsR0k4VbF0B86J-li9q1Yl4vrUATkRjhwxHcTugrPLVan0YlsgsH3kr8oEWAn4NSYGBd.tRbShcnufa8YDG7MDSx41A'
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

    headers = CaseInsensitiveDict()

    file_downloaded_count = 0
    for item in parsed_data:
        filename = item["FileName"]
        file_id = item["Id"]
        # download_url = item["TempDownloadUri"]
        
        final_string = ""
        if "AttachableRef" in item:
            attachable_ref = item["AttachableRef"]

            write_string = f"{file_id}##"
            for ref in attachable_ref:
                value = ref["EntityRef"]["value"]
                type = ref["EntityRef"]["type"]
                includeonsend = ref["IncludeOnSend"]

                write_string += f"{value}##{type}##{includeonsend}&&"

            final_string = f"{write_string}\n"
        else:
            final_string = f"{file_id}##No AttachableRef present\n"


        while True:

            headers["Authorization"] = f"Bearer {access_token}"

            url_r = requests.get(f"{sandboxURL}/v3/company/{realmID}/download/{file_id}?minorversion=65",headers=headers)
            # url_r = requests.get(f"{productionURL}/v3/company/{realmID}/download/{file_id}?minorversion=65",headers=headers)

            if url_r.status_code == 200:
                # Returns a download_url
                # Download URL is valid for 15 minutes. We are downloading right away

                download_url = url_r.content
                download_r = requests.get(download_url)

                # change for windows
                final_filename = f"download_folder/{file_id}#{filename}"

                with open(final_filename,'wb') as f:
                    f.write(download_r.content)
                    file_downloaded_count = file_downloaded_count + 1
                    print(f"{final_filename} downloaded. File Downloaded is {file_downloaded_count}")
                
                details_file.write(final_string)
                break
            else:
                # Status Code returned may be 401 unauthorized access access token expired
                # get new access_token
                auth_response = requests.post(auth_URL,data=payload,headers=auth_headers)
                if "error" in auth_response:
                    """"
                    {
                        "error_description": "Incorrect or invalid refresh token",
                        "error": "invalid_grant"
                    }
                    """
                    print(f"SomeError occurred at getting new access_token after fetching {file_downloaded_count} objects... dumping in error.json")
                    autherrorfp = open('autherror.json','w')
                    autherror_parsed = json.dumps(auth_response.json(),indent=4)
                    autherrorfp.write(autherror_parsed)
                    exit()
                else:
                    """{"access_token":"..","token_type":"bearer","x_refresh_token_expires_in":8725268,"refresh_token":"...","expires_in":3600}"""
                    parsed_auth_response = auth_response.json()
                    access_token = parsed_auth_response["access_token"]
                    print("NEW ACCESS TOKEN IS GENERATED")


def download_attachable_in_chunks():
    file = 'data_from_qb.json'
    file_qb = open(file)
    parsed_data = json.load(file_qb)
    details_file_json = open('file_download_details.json','a')
    # details_file_txt = open('file_download.txt','a')

    # Sandbox URL
    sandboxURL = 'https://sandbox-quickbooks.api.intuit.com'
    productionURL = 'https://quickbooks.api.intuit.com'
    auth_URL = 'https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer'

    # These must be changed
    refresh_token = 'AB116704252382vkLwLIxyffpcMTvMupBrTBQDaZGf8DltUcIX'
    access_token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..6MRlk44MfVxsjmti8JvHHA.xcfci7FHCpOwjCX4jiM9cX4xc3DzCwZKTFpBi33XrkTHJsGLvgzm7jp2kkdh6UeSbcYK8ZinWHnR9MmuqNU5ki1J2jgf2_Xc6MY9Q2OWbKcdqZdADgG_mGYijbG-J03Mm1ddVY4_xsIJ2lUnC6LiAZkxIqvCZKjmS8uZxoCGH1SYR-zgurD54ykJXT8ulDQ6fPUU6ST0X0odpMA9khO-3cyDvu--7AG2Zw2xphA1qkR1rd2dPBZ5GAQ8-0vGJzP7NzfzkDc4lp9pFPcY1bK66QFFGA2-lINc_TGClqVJllq3enqE1FOnjvWpYsmRvdHNbYbw6wbv-Ez2xvo3Fgp1vrxHyR_1fEDwOYz_kds5qKcQpKDZ1HCSCWzybAfCZxJ5vtbe45hBkJkPMXQduqt-beqzU3E_k0ML6Vp9j9qli9EdtWOrACGRjePhyxppQ_znjwwDQ62uEOo3IHCCpklWsSDoLHZ4xFSow8F2FAJ0xYkCTkHafuJI75vuvq2ddqAisu7fjpgrrsmsCu_PC-uU_oXWx-ZYc0woRSAwFYMVTKxlXbDzZan3nChpvYZnRYNYUEyDwlCBwN5RY6jdMK7Rzi9ih4Loif6kEFXNq6sfiNQVKJHveXKcsBFeXxbUFJCbgEYcbQakGNxrKDPrFX8V8cp7xPPyXV7FBuvW_oiKDULLbIbv_3s2FGtUBpiWNlTkI_HfUQ-566_hBauxS_DXq51B7-ooOzVca8x5aKkchMLfsno-GuLlar58fGvCbGJz.jKJiXk6p5QM1PysNOhnzyA'
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

    headers = CaseInsensitiveDict()

    file_download_details_dict = dict()

    file_downloaded_count = 0
    for item in parsed_data:
        filename = item["FileName"]
        file_id = item["Id"]
        # download_url = item["TempDownloadUri"]
        final_string = ""
        if "AttachableRef" in item:
            attachable_ref = item["AttachableRef"]

            # write_string = f"{file_id}##"
            write_string = ""
            for ref in attachable_ref:
                value = ref["EntityRef"]["value"]
                type = ref["EntityRef"]["type"]
                includeonsend = ref["IncludeOnSend"]

                write_string += f"{value}##{type}##{includeonsend}&&"

            # final_string = f"{write_string}\n"
            final_string = f"{write_string}"
        else:
            # final_string = f"{file_id}##No AttachableRef present\n"
            final_string = f"NAP"

        while True:

            headers["Authorization"] = f"Bearer {access_token}"

            url_r = requests.get(f"{sandboxURL}/v3/company/{realmID}/download/{file_id}?minorversion=65",headers=headers)
            # url_r = requests.get(f"{productionURL}/v3/company/{realmID}/download/{file_id}?minorversion=65",headers=headers)

            if url_r.status_code == 200:
                # Returns a download_url
                # Download URL is valid for 15 minutes. We are downloading right away

                download_url = url_r.content
                download_r = requests.get(download_url,stream=True)

                # change for windows
                final_filename = f"download_folder/{file_id}#{filename}"

                with open(final_filename,'wb') as f:
                    for chunk in download_r.iter_content(chunk_size=1024):
                        f.write(chunk)
                    
                    file_download_details_dict[file_id] = final_string
                    file_downloaded_count = file_downloaded_count + 1
                    print(f"{final_filename} downloaded. File Downloaded is {file_downloaded_count}")
                    
                
                # details_file_txt.write(final_string)
                break
            else:
                # Status Code returned may be 401 unauthorized access access token expired
                # get new access_token
                auth_response = requests.post(auth_URL,data=payload,headers=auth_headers)
                if "error" in auth_response:
                    """"
                    {
                        "error_description": "Incorrect or invalid refresh token",
                        "error": "invalid_grant"
                    }
                    """
                    print(f"SomeError occurred at getting new access_token after fetching {file_downloaded_count} objects... dumping in error.json")
                    autherrorfp = open('autherror.json','w')
                    autherror_parsed = json.dumps(auth_response.json(),indent=4)
                    autherrorfp.write(autherror_parsed)
                    exit()
                else:
                    """{"access_token":"..","token_type":"bearer","x_refresh_token_expires_in":8725268,"refresh_token":"...","expires_in":3600}"""
                    parsed_auth_response = auth_response.json()
                    access_token = parsed_auth_response["access_token"]
                    print("NEW ACCESS TOKEN IS GENERATED")

    indented_data = json.dumps(file_download_details_dict,indent=4)
    details_file_json.write(indented_data)

def download_attachable_in_chunks_v2():
    # file = 'splitted_invoice/ext_invoice0_copy.json'
    # file = 'splitted_invoice/ext_invoice0.json'
    
    # file = 'splitted_invoice/ext_invoice1.json'
    # file = 'splitted_invoice/ext_invoice2_copy.json'
    # file = 'splitted_invoice/ext_invoice3_copy.json'
    # file = 'splitted_invoice/ext_invoice4_copy.json'
    # file = 'splitted_invoice/ext_invoice5.json'
    # file = 'splitted_invoice/ext_invoice6_copy.json'
    # file = 'splitted_invoice/ext_invoice7.json'
    # file = 'splitted_invoice/ext_invoice8.json'
    # file = 'splitted_invoice/ext_invoice9_copy.json'
    # file = 'splitted_invoice/ext_invoice10.json'
    # file = 'splitted_invoice/ext_invoice11.json'
    # file = 'splitted_invoice/ext_invoice12_copy.json'
    # file = 'splitted_invoice/ext_invoice13_copy.json'
    # file = 'splitted_invoice/ext_invoice14_copy.json'
    # file = 'splitted_invoice/ext_invoice15.json'

    # file = 'splitted_bill/ext_bill0.json'
    # file = 'splitted_bill/ext_bill1.json'
    # file = 'splitted_bill/ext_bill2.json'
    # file = 'splitted_bill/ext_bill3.json'
    # file = 'splitted_bill/ext_bill4.json'
    # file = 'splitted_bill/ext_bill5.json'
    # file = 'splitted_bill/ext_bill6.json'
    # file = 'splitted_bill/ext_bill7.json'
    # file = 'splitted_bill/ext_bill8.json'
    # file = 'splitted_bill/ext_bill9.json'
    # file = 'splitted_bill/ext_bill10.json'
    # file = 'splitted_bill/ext_bill11.json'
    # file = 'splitted_bill/ext_bill12.json'
    
    # file = 'extracted_journalEntry_details.json'
    file = 'extracted_invoice_details.json'
    # file = 'extracted_bill_details.json'
    # file = 'extracted_creditMemo_details.json'
    # file = 'extracted_journalEntry_details.json'
    # file = 'extracted_estimate_details.json'
    # file = 'extracted_vendorCredit_details.json'
    # file = 'extracted_purchase_details.json'
    # file = 'extracted_po_details.json'
    # file = 'extracted_transfer_details.json'
    # file = 'extracted_deposit_details.json'
    # file = 'extracted_payment_details.json'
    # file = 'extracted_bill_payment_details.json'

    file_qb = open(file)
    parsed_data = json.load(file_qb)

    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext0.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext1.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext2.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext3.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext4.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext5.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext6.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext7.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext8.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext9.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext10.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext11.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext12.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext13.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext14.txt','a')
    # invoice_console_output_file_fout = open('invoice_saved_response/invoice_2017_to_2022_console_output_ext15.txt','a')

    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext0.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext1.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext2.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext3.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext4.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext5.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext6.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext7.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext8.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext9.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext10.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext11.txt','a')
    # invoice_console_output_file_fout = open('bill_saved_response/bill_2017_to_2022_console_output_ext12.txt','a')
    # invoice_console_output_file_fout = open('journal_saved_response/journal_2017_to_2022_console_output_okay.txt','a')
    
    invoice_console_output_file_fout = open('saved_response/invoice_saved_response.txt','a')
    # invoice_console_output_file_fout = open('saved_response/bill_saved_response.txt','a')
    # invoice_console_output_file_fout = open('saved_response/creditMemo_saved_response.txt','a')
    # invoice_console_output_file_fout = open('saved_response/journalEntry_saved_response.txt','a')
    # invoice_console_output_file_fout = open('saved_response/estimate_saved_response.txt','a')
    # invoice_console_output_file_fout = open('saved_response/vendor_credit_saved_response.txt','a')
    # invoice_console_output_file_fout = open('saved_response/purchase_saved_response.txt','a')
    # invoice_console_output_file_fout = open('saved_response/transfer_saved_response.txt','a')
    # invoice_console_output_file_fout = open('saved_response/deposit_saved_response.txt','a')
    # invoice_console_output_file_fout = open('saved_response/payment_saved_response.txt','a')
    # invoice_console_output_file_fout = open('saved_response/bill_payment_saved_response.txt','a')



    # Sandbox URL
    sandboxURL = 'https://sandbox-quickbooks.api.intuit.com'
    productionURL = 'https://quickbooks.api.intuit.com'
    auth_URL = 'https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer'

    # These must be changed
    refresh_token = 'AB11685644074Jp4kXNBY3JPQ6LNRIXIzIGN4ZVLmc1x00H12h'
    access_token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..FSBmXjAUNW-3naoIaK1frA.AgNHWOBXAeZF6fdw5OH_Kh-HU-KgkBAR6It0wXxxgYxiDxWerY1rFGKq-U0sxbgWe6gS9SGJwNVRM7hASYBgNsEJbwOjqa1SHOC9u2JlHDLSO1MlgTf8w0ia3pydY6dWQ9m1uI_4xcbi8qyrBLuBAc80hBJOFwk7sMXo16KkI2_Sc4z8bAB2gXGwUv1VJTR9idEEXWXXfro6Rk6_4WG4I-vO0dCjGNrawbnCd5C1uZFFHLrmlMri_rb5cQ0Jimj8tJLXL7gyczzk5Dn40lgv0UK1YCyg1qM-Hyfbv3u7Da3dg_BAFUAlknKHNY4ntddLdH_Fw7rdswUNrejFazo_lV5nIDKnbgLCpndILXSPUw-6YAWiwmKxO5kdbOgCoJcbXMnSvf6v6sizBOy23efnadrLwJN4Q2G_HREErGSutoq36l8GGW1C2I0p0FVD42EExJcpKr2hbujBZc-2WKGQCd20vIWvu7HEy1WUX6EU_2-1YPP8CpR2JOU8ClUe4xU4qJITsvoE-fBmlydyjmh7gBM84EAwRkuSmAtzhtkXEVcV3UHHzeKCedpyZXuHcr8RSbPsWPFO5mDJsodUJYMYEnms8cKlogts-iIUV_yEV6-eGT1_HFvmQXX-W4hdea_vYIae_9OIje5ae6-kj5putqnKjjTRFU3LrwENnI8F8aMbTmRfPShzeLcGQXrCVAFn2ZDbpwSEgA18CK9wI-J7izKF-aNldqGQbtPK5ovRXdM.xtJmk-g5EirkY1wHMJm7JweyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..FSBmXjAUNW-3naoIaK1frA.AgNHWOBXAeZF6fdw5OH_Kh-HU-KgkBAR6It0wXxxgYxiDxWerY1rFGKq-U0sxbgWe6gS9SGJwNVRM7hASYBgNsEJbwOjqa1SHOC9u2JlHDLSO1MlgTf8w0ia3pydY6dWQ9m1uI_4xcbi8qyrBLuBAc80hBJOFwk7sMXo16KkI2_Sc4z8bAB2gXGwUv1VJTR9idEEXWXXfro6Rk6_4WG4I-vO0dCjGNrawbnCd5C1uZFFHLrmlMri_rb5cQ0Jimj8tJLXL7gyczzk5Dn40lgv0UK1YCyg1qM-Hyfbv3u7Da3dg_BAFUAlknKHNY4ntddLdH_Fw7rdswUNrejFazo_lV5nIDKnbgLCpndILXSPUw-6YAWiwmKxO5kdbOgCoJcbXMnSvf6v6sizBOy23efnadrLwJN4Q2G_HREErGSutoq36l8GGW1C2I0p0FVD42EExJcpKr2hbujBZc-2WKGQCd20vIWvu7HEy1WUX6EU_2-1YPP8CpR2JOU8ClUe4xU4qJITsvoE-fBmlydyjmh7gBM84EAwRkuSmAtzhtkXEVcV3UHHzeKCedpyZXuHcr8RSbPsWPFO5mDJsodUJYMYEnms8cKlogts-iIUV_yEV6-eGT1_HFvmQXX-W4hdea_vYIae_9OIje5ae6-kj5putqnKjjTRFU3LrwENnI8F8aMbTmRfPShzeLcGQXrCVAFn2ZDbpwSEgA18CK9wI-J7izKF-aNldqGQbtPK5ovRXdM.xtJmk-g5EirkY1wHMJm7JweyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..FSBmXjAUNW-3naoIaK1frA.AgNHWOBXAeZF6fdw5OH_Kh-HU-KgkBAR6It0wXxxgYxiDxWerY1rFGKq-U0sxbgWe6gS9SGJwNVRM7hASYBgNsEJbwOjqa1SHOC9u2JlHDLSO1MlgTf8w0ia3pydY6dWQ9m1uI_4xcbi8qyrBLuBAc80hBJOFwk7sMXo16KkI2_Sc4z8bAB2gXGwUv1VJTR9idEEXWXXfro6Rk6_4WG4I-vO0dCjGNrawbnCd5C1uZFFHLrmlMri_rb5cQ0Jimj8tJLXL7gyczzk5Dn40lgv0UK1YCyg1qM-Hyfbv3u7Da3dg_BAFUAlknKHNY4ntddLdH_Fw7rdswUNrejFazo_lV5nIDKnbgLCpndILXSPUw-6YAWiwmKxO5kdbOgCoJcbXMnSvf6v6sizBOy23efnadrLwJN4Q2G_HREErGSutoq36l8GGW1C2I0p0FVD42EExJcpKr2hbujBZc-2WKGQCd20vIWvu7HEy1WUX6EU_2-1YPP8CpR2JOU8ClUe4xU4qJITsvoE-fBmlydyjmh7gBM84EAwRkuSmAtzhtkXEVcV3UHHzeKCedpyZXuHcr8RSbPsWPFO5mDJsodUJYMYEnms8cKlogts-iIUV_yEV6-eGT1_HFvmQXX-W4hdea_vYIae_9OIje5ae6-kj5putqnKjjTRFU3LrwENnI8F8aMbTmRfPShzeLcGQXrCVAFn2ZDbpwSEgA18CK9wI-J7izKF-aNldqGQbtPK5ovRXdM.xtJmk-g5EirkY1wHMJm7JweyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..FSBmXjAUNW-3naoIaK1frA.AgNHWOBXAeZF6fdw5OH_Kh-HU-KgkBAR6It0wXxxgYxiDxWerY1rFGKq-U0sxbgWe6gS9SGJwNVRM7hASYBgNsEJbwOjqa1SHOC9u2JlHDLSO1MlgTf8w0ia3pydY6dWQ9m1uI_4xcbi8qyrBLuBAc80hBJOFwk7sMXo16KkI2_Sc4z8bAB2gXGwUv1VJTR9idEEXWXXfro6Rk6_4WG4I-vO0dCjGNrawbnCd5C1uZFFHLrmlMri_rb5cQ0Jimj8tJLXL7gyczzk5Dn40lgv0UK1YCyg1qM-Hyfbv3u7Da3dg_BAFUAlknKHNY4ntddLdH_Fw7rdswUNrejFazo_lV5nIDKnbgLCpndILXSPUw-6YAWiwmKxO5kdbOgCoJcbXMnSvf6v6sizBOy23efnadrLwJN4Q2G_HREErGSutoq36l8GGW1C2I0p0FVD42EExJcpKr2hbujBZc-2WKGQCd20vIWvu7HEy1WUX6EU_2-1YPP8CpR2JOU8ClUe4xU4qJITsvoE-fBmlydyjmh7gBM84EAwRkuSmAtzhtkXEVcV3UHHzeKCedpyZXuHcr8RSbPsWPFO5mDJsodUJYMYEnms8cKlogts-iIUV_yEV6-eGT1_HFvmQXX-W4hdea_vYIae_9OIje5ae6-kj5putqnKjjTRFU3LrwENnI8F8aMbTmRfPShzeLcGQXrCVAFn2ZDbpwSEgA18CK9wI-J7izKF-aNldqGQbtPK5ovRXdM.xtJmk-g5EirkY1wHMJm7Jw'
    
    realmID = '508030115'

    client_id = 'AB7TLSmTPE1BWkhOB33zXDSLdFZJbYwjiwoY44mQtXN8KD1REp'
    client_secret = 'C8uMr29rU887zmbcYnUG8ym3XbSQ9cDg58MObdrO'

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

    headers = CaseInsensitiveDict()

    # file_download_details_dict = dict()
    file_downloaded_count = 0
    for key,value in parsed_data.items():
        # filename = item["FileName"]
        # file_id = item["Id"]
        # # download_url = item["TempDownloadUri"]
        # final_string = ""
        # if "AttachableRef" in item:
        #     attachable_ref = item["AttachableRef"]

        #     # write_string = f"{file_id}##"
        #     write_string = ""
        #     for ref in attachable_ref:
        #         value = ref["EntityRef"]["value"]
        #         type = ref["EntityRef"]["type"]
        #         includeonsend = ref["IncludeOnSend"]

        #         write_string += f"{value}##{type}##{includeonsend}&&"

        #     # final_string = f"{write_string}\n"
        #     final_string = f"{write_string}"
        # else:
        #     # final_string = f"{file_id}##No AttachableRef present\n"
        #     final_string = f"NAP"

        while True:

            headers["Authorization"] = f"Bearer {access_token}"

            sleep(0.3)
            # url_r = requests.get(f"{sandboxURL}/v3/company/{realmID}/download/{file_id}?minorversion=65",headers=headers)
            url_r = requests.get(f"{productionURL}/v3/company/{realmID}/download/{value[0]}?minorversion=65",headers=headers)

            if url_r.status_code == 200:
                # Returns a download_url
                # Download URL is valid for 15 minutes. We are downloading right away

                download_url = url_r.content
                download_r = requests.get(download_url,stream=True)

                key_splitted = key.split('#')  
                final_filename = f"{key_splitted[0]}#{value[1]}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext0/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext1/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext2/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext3/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext4/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext5/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext6/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext7/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext8/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext9/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext10/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext11/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext12/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext13/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext14/{final_filename}"
                # final_folder_filename = f"downloaded_invoice_folder_2017_to_2022_ext15/{final_filename}"

                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext0/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext1/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext2/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext3/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext4/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext5/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext6/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext7/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext8/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext9/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext10/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext11/{final_filename}"
                # final_folder_filename = f"downloaded_bill_folder_2017_to_2022_ext12/{final_filename}"
                # final_folder_filename = f"downloaded_journalEntry_folder/{final_filename}"

                final_folder_filename = f"downloaded_invoice_folder/{final_filename}"
                # final_folder_filename = f"downloaded_Purchase_folder/{final_filename}"


                with open(final_folder_filename,'wb') as f:
                    for chunk in download_r.iter_content(chunk_size=1024):
                        f.write(chunk)
                    
                    # file_download_details_dict[file_id] = final_string
                    file_downloaded_count = file_downloaded_count + 1
                    console_output = f"{final_filename} downloaded. File Downloaded is {file_downloaded_count}"
                    print(console_output)
                    invoice_console_output_file_fout.write(console_output+'\n')

                    invoice_console_output_file_fout.flush()
                # details_file_txt.write(final_string)
                break
            else:
                # Status Code returned may be 401 unauthorized access access token expired
                # get new access_token
                auth_response = requests.post(auth_URL,data=payload,headers=auth_headers)
                if "error" in auth_response.json():
                    """"
                    {
                        "error_description": "Incorrect or invalid refresh token",
                        "error": "invalid_grant"
                    }
                    """
                    print(f"SomeError occurred at getting new access_token after fetching {file_downloaded_count} objects... dumping in error.json")
                    autherrorfp = open('autherror.json','w')
                    autherror_parsed = json.dumps(auth_response.json(),indent=4)
                    autherrorfp.write(autherror_parsed)
                    exit()
                else:
                    """{"access_token":"..","token_type":"bearer","x_refresh_token_expires_in":8725268,"refresh_token":"...","expires_in":3600}"""
                    parsed_auth_response = auth_response.json()
                    access_token = parsed_auth_response["access_token"]
                    print("NEW ACCESS TOKEN IS GENERATED")
                    print(access_token)

    # indented_data = json.dumps(file_download_details_dict,indent=4)
    # details_file_json.write(indented_data)


def upload_attachment_to_invoice():
    code = '1000.45f6e1ea786f95c49ff4d7761d8f98f2.b38bced0d13295fa7c392d3f35ef3309'
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
    
    # refresh_token = parsed_data1["refresh_token"]
    # access_token = parsed_data1["access_token"]
    refresh_token = '1000.4fe7b2b285387b4b129d2f5377c6eb75.9e44fe8b2a0bc5e460a9152ac51cdb3b'
    access_token = '1000.5e005e089c30dd81dbdd1412a1d4af43.d4263b7e95d4418da5102fd6c5af8539'
    # expires_in = parsed_data["expires_in"]

    organization_id = '60018491680'
    # post_url = f'https://books.zoho.in/api/v3/invoices?organization_id={organization_id}'
    # post_url = f"https://books.zoho.com/api/v3/invoices/{:invoice_id}/attachment?organization_id={organization_id}"

    extractedfout = open('extracted_invoice_details.json')

    # extractedfout = open('splitted_invoice/ext_invoice0_copy.json')
    # extractedfout = open('splitted_invoice/ext_invoice0.json')
    # extractedfout = open('splitted_invoice/ext_invoice1.json')
    # extractedfout = open('splitted_invoice/ext_invoice2_copy.json')
    # extractedfout = open('splitted_invoice/ext_invoice3_copy.json')
    # extractedfout = open('splitted_invoice/ext_invoice4_copy.json')
    # extractedfout = open('splitted_invoice/ext_invoice5.json')
    # extractedfout = open('splitted_invoice/ext_invoice6_copy.json')
    # extractedfout = open('splitted_invoice/ext_invoice7.json')
    # extractedfout = open('splitted_invoice/ext_invoice8.json')
    # extractedfout = open('splitted_invoice/ext_invoice9_copy.json')
    # extractedfout = open('splitted_invoice/ext_invoice10.json')
    # extractedfout = open('splitted_invoice/ext_invoice11.json')
    # extractedfout = open('splitted_invoice/ext_invoice12_copy.json')
    # extractedfout = open('splitted_invoice/ext_invoice13_copy.json')
    # extractedfout = open('splitted_invoice/ext_invoice14_copy.json')
    # extractedfout = open('splitted_invoice/ext_invoice15.json')

    
    
    parsed_data2 = json.load(extractedfout)
    # items_list = parsed_data2

    # parsedout_fout = open('parsed_out_for_upload/parsed_out_mapped_for_payment_adv_after.json')
    # parsedout_fout = open('parsed_out_for_upload/parsed_out_mapped_for_payment_adv_before.json')
    # parsedout_fout = open('parsed_out_for_upload/parsed_out_mapped_for_payment_before.json')
    parsedout_fout = open('parsed_out_mapped_for_invoice.json')

    qb_id_against_zoho_id = json.load(parsedout_fout)

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    # response_save_file = open("saved_response_id/saved_response_payment_after.txt","a")
    # response_save_file = open("saved_response_id/saved_response_payment_adv_before.txt","a")
    # response_save_file = open("saved_response_id/saved_response_payment_before.txt","a")
    response_save_file = open("saved_response_id/saved_response_invoice_push.txt","a")

    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")

    for key,value in parsed_data2.items():
        while True:
            stripped_key_list = key.split('#')
            print(f"Processing for name: {stripped_key_list[0]}....")
            # invoice_id_from_zoho = qb_id_against_zoho_id[stripped_key_list[0]]
            invoice_id_from_zoho = qb_id_against_zoho_id.get(stripped_key_list[0])
            if not invoice_id_from_zoho:
                print(f'KEY ERROR occurred: {stripped_key_list[0]} does not have any corresponding ZOHO ID')
                response_save_file.write(f'KEY ERROR occurred: {stripped_key_list[0]} does not have any corresponding ZOHO ID\n')
                break

            post_url = f"https://books.zoho.in/api/v3/invoices/{invoice_id_from_zoho}/attachment?organization_id={organization_id}"
            # post_url = f"https://books.zoho.in/api/v3/creditnotes/{invoice_id_from_zoho}/attachment?organization_id={organization_id}"
            # post_url = f"https://books.zoho.in/api/v3/purchaseorders/{invoice_id_from_zoho}/attachment?organization_id={organization_id}"
            # post_url = f"https://books.zoho.in/api/v3/estimates/{invoice_id_from_zoho}/attachment?organization_id={organization_id}"
            # post_url = f"https://books.zoho.in/api/v3/expenses/{invoice_id_from_zoho}/attachment?organization_id={organization_id}"
            # post_url = f"https://books.zoho.in/api/v3/journals/{invoice_id_from_zoho}/attachment?organization_id={organization_id}"
            # post_url = f"https://books.zoho.in/api/v3/customerpayments/{invoice_id_from_zoho}/attachment?organization_id={organization_id}"

            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(0.4)

            # param = dict()
            # param['JSONString'] = item
            # r2 = requests.post(post_url,headers=headers,data=param)
            # try:
            #     files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext0/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext1/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext2/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext3/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext4/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext5/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext6/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext7/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext8/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext9/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext10/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext11/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext12/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext13/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext14/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext15/{stripped_key_list[0]}#{value[1]}','rb')}
            # except:
            #     my_str = f"FILE ERROR for {stripped_key_list[0]}#{value[1]}"
            #     print(my_str+'\n')
            #     response_save_file.write(f'{my_str}\n')
            #     response_save_file.flush()
            #     break

            files = {'attachment': open(f'downloaded_invoice_folder/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext1/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext2/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext3/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext4/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext5/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext6/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext7/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext8/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext9/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext10/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext11/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext12/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext13/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext14/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext15/{stripped_key_list[0]}#{value[1]}','rb')}

            r2 = requests.post(post_url,headers=headers,files=files)

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
                response_save_file.write(f'ACCESS TOKEN : {access_token}\n')
                response_save_file.flush()
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
                response_save_file.write(f'{key} : {value[1]}\n')
                print(f'{stripped_key_list[0]}#{value[1]} is successfully pushed')
                response_save_file.flush()
                # It means success
                break
            else:
                # print(f'ERROR occurred: {key} was able to be pushed')
                print(f'ERROR occurred: {key} was not able to be pushed....error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                response_save_file.write(f'ERROR occurred: {key} was able to not be pushed....error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}\n')
                response_save_file.flush()
                break
        
        # print(f'Successfully created item named: {item["name"]}')

def upload_attachment_to_bills():
    # code = '1000.82fd1342dade44b59e1fc9e31f3026cd.790d25b3974aad9395f52916fa092f7f'
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
    refresh_token = '1000.44b261b92b9479bcfb981d1b7a37c241.a2dcc94750c80ec33d9386dbe2d2ce53'
    access_token = '1000.261d8b83585aa8e8d724c550f1e2a7be.2e83abf38f274c82f140f3e42e1e165d'
    # expires_in = parsed_data["expires_in"]

    organization_id = '60001574931'
    # post_url = f'https://books.zoho.in/api/v3/invoices?organization_id={organization_id}'
    # post_url = f"https://books.zoho.com/api/v3/invoices/{:invoice_id}/attachment?organization_id={organization_id}"

    extractedfout = open('extracted_bill_details.json')
    # extractedfout = open('splitted_bill/ext_bill0.json')
    # extractedfout = open('splitted_bill/ext_bill1_copy.json')
    # extractedfout = open('splitted_bill/ext_bill2_copy.json')
    # extractedfout = open('splitted_bill/ext_bill2.json')
    # extractedfout = open('splitted_bill/ext_bill3.json')
    # extractedfout = open('splitted_bill/ext_bill4_copy.json')
    # extractedfout = open('splitted_bill/ext_bill4.json')
    # extractedfout = open('splitted_bill/ext_bill5_copy.json')
    # extractedfout = open('splitted_bill/ext_bill6_copy.json')
    # extractedfout = open('splitted_bill/ext_bill7_copy.json')
    # extractedfout = open('splitted_bill/ext_bill8_copy.json')
    # extractedfout = open('splitted_bill/ext_bill8.json')
    # extractedfout = open('splitted_bill/ext_bill9.json')
    # extractedfout = open('splitted_bill/ext_bill10_copy.json')
    # extractedfout = open('splitted_bill/ext_bill11_copy.json')
    # extractedfout = open('splitted_bill/ext_bill12_copy.json')

    
    
    parsed_data2 = json.load(extractedfout)
    # items_list = parsed_data2

    parsedout_fout = open('parsed_out_for_upload/parsed_out_mapped_for_bill.json')
    qb_id_against_zoho_id = json.load(parsedout_fout)

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    # response_save_file = open("saved_response_bill4.txt","a")
    # response_save_file = open("saved_response_bill5.txt","a")
    # response_save_file = open("saved_response_bill6.txt","a")
    # response_save_file = open("saved_response_bill7.txt","a")
    # response_save_file = open("saved_response_bill8.txt","a")
    # response_save_file = open("saved_response_bill9.txt","a")
    # response_save_file = open("saved_response_bill10.txt","a")
    # response_save_file = open("saved_response_bill11.txt","a")
    response_save_file = open("saved_response_id/saved_response_bill.txt","a")


    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")

    for key,value in parsed_data2.items():
        while True:
            stripped_key_list = key.split('#')
            print(f"Processing for name: {stripped_key_list[0]}....")
            # invoice_id_from_zoho = qb_id_against_zoho_id[stripped_key_list[0]]
            invoice_id_from_zoho = qb_id_against_zoho_id.get(stripped_key_list[0])
            if not invoice_id_from_zoho:
                print(f'KEY ERROR occurred: {stripped_key_list[0]} does not have any corresponding ZOHO ID')
                response_save_file.write(f'KEY ERROR occurred: {stripped_key_list[0]} does not have any corresponding ZOHO ID\n')
                break

            post_url = f"https://books.zoho.in/api/v3/bills/{invoice_id_from_zoho}/attachment?organization_id={organization_id}"

            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(0.6)

            # param = dict()
            # param['JSONString'] = item
            # r2 = requests.post(post_url,headers=headers,data=param)
            # try:
            #     files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext0/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': opepost_url = f"https://books.zoho.inn(f'downloaded_invoice_folder_2017_to_2022_ext1/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext2/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext3/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext4/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext5/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext6/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext7/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext8/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext9/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext10/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext11/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext12/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext13/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext14/{stripped_key_list[0]}#{value[1]}','rb')}
            #     # files = {'attachment': open(f'downloaded_invoice_folder_2017_to_2022_ext15/{stripped_key_list[0]}#{value[1]}','rb')}
            # except:
            #     my_str = f"FILE ERROR for {stripped_key_list[0]}#{value[1]}"
            #     print(my_str+'\n')
            #     response_save_file.write(f'{my_str}\n')
            #     response_save_file.flush()
            #     break

            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext0/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext1/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext2/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext3/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext4/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext5/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext6/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext7/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext8/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext9/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext10/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext11/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext12/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext13/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext14/{stripped_key_list[0]}#{value[1]}','rb')}
            # files = {'attachment': open(f'downloaded_bill_folder_2017_to_2022_ext15/{stripped_key_list[0]}#{value[1]}','rb')}
            files = {'attachment': open(f'downloaded_bill_folder/{stripped_key_list[0]}#{value[1]}','rb')}

            r2 = requests.post(post_url,headers=headers,files=files)

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
                response_save_file.write(f'ACCESS TOKEN : {access_token}\n')
                response_save_file.flush()
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
                response_save_file.write(f'{key} : {value[1]}\n')
                print(f'{stripped_key_list[0]}#{value[1]} is successfully pushed')
                response_save_file.flush()
                # It means success
                break
            else:
                # print(f'ERROR occurred: {key} was able to be pushed')
                print(f'ERROR occurred: {key} was not able to be pushed....error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                response_save_file.write(f'ERROR occurred: {key} was able to not be pushed....error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}\n')
                response_save_file.flush()
                break
        
        # print(f'Successfully created item named: {item["name"]}')


def upload_attachment_to_journalEntrys():
    # code = '1000.28cc7b3faf90801be2f406156453dfdd.a3f1951dba09d58b811b48020c86a848'
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
    
    refresh_token = '1000.74431251c0987fafd427242961a1dfef.505eda1559d6bec5d8afaa0b48750efa'
    access_token = '1000.3211c6b396e8dddaeb7b6bb114368055.5ff11a74944b24bd3e78a257caadee90'

    # refresh_token = parsed_data1["refresh_token"]
    # access_token = parsed_data1["access_token"]
    # expires_in = parsed_data["expires_in"]
    # print(refresh_token)
    # print(access_token)

    # refresh_token = ''
    # access_token = ''

    organization_id = '60001574931'
    # post_url = f'https://books.zoho.in/api/v3/invoices?organization_id={organization_id}'
    # post_url = f"https://books.zoho.com/api/v3/invoices/{:invoice_id}/attachment?organization_id={organization_id}"

    extractedfout = open('extracted_journalEntry_details.json')
    # extractedfout = open('extracted_journalEntry_details_failed_ones.json')
    # extractedfout = open('failed_bill_attachment.json')

    parsed_data2 = json.load(extractedfout)
    # items_list = parsed_data2

    parsedout_fout = open('parsed_out_mapped_for_journalEntry.json')
    qb_id_against_zoho_id = json.load(parsedout_fout)

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_response_for_journalEntry.txt","a")

    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")

    for key,value in parsed_data2.items():
        while True:
            stripped_key_list = key.split('#')
            print(f"Processing for name: {stripped_key_list[0]}....")
            je_id_against_qb = qb_id_against_zoho_id.get(stripped_key_list[0])
            if je_id_against_qb:
                invoice_id_from_zoho = je_id_against_qb
                # print(f"DONE FOR {stripped_key_list[0]}")
                # break
            else:
                key_error_str = f"KEY ERROR FOR {stripped_key_list[0]}"
                print(key_error_str)
                response_save_file.write(key_error_str+'\n')
                response_save_file.flush()
                break
            post_url = f"https://books.zoho.in/api/v3/journals/{invoice_id_from_zoho}/attachment?organization_id={organization_id}"

            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(0.3)

            # param = dict()
            # param['JSONString'] = item
            # r2 = requests.post(post_url,headers=headers,data=param)
            files = {'attachment': open(f'downloaded_journalEntry_folder_2013_to_2017/{stripped_key_list[0]}#{value[1]}','rb')}
            r2 = requests.post(post_url,headers=headers,files=files)

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
                response_save_file.write(f'{key} : {value[1]}\n')
                print(f'{stripped_key_list[0]}#{value[1]} is successfully pushed')
                response_save_file.flush()
                # It means success
                break
            else:
                # print(f'ERROR occurred: {key} was able to be pushed')
                print(f'ERROR occurred: {key} was able to be pushed....error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
                response_save_file.write(f'ERROR occurred: {key} was able to be pushed....error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}\n')
                response_save_file.flush()
                break
        
        # print(f'Successfully created item named: {item["name"]}')
    
    response_save_file.close()
    extractedfout.close()

def generate_post_json():

    # https://www.geeksforgeeks.org/read-json-file-using-python/
    # file_name = 'all_fetched_data_from_qb.json'
    file_name = 'excel/data_from_qb_vendor.json'

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
    mapped_data["Vendor"] = my_item_list

    mapped_json = json.dumps(mapped_data,indent=4)

    with open("mapped.json", "w") as outfile:
        outfile.write(mapped_json)


# 'code' variable must be updated before running this function
# def post_request_zoho():
#     # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

#     # ZohoBooks.fullaccess.all
#     code = '1000.aaa9c909edbfc63081d0a7af4d3562ff.788dd88975c13d53e8e80323be51c0d9'
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
#     post_url = f'https://books.zoho.in/api/v3/items?organization_id={organization_id}'

#     f = open('mapped.json')
#     parsed_data2 = json.load(f)
#     # items_list = parsed_data2["Item"]

#     headers = CaseInsensitiveDict()
#     headers["Accept"] = "application/json"

#     # response_save_dict = dict()
#     response_save_file = open("saved_customer_id.txt","a")

#     # dd/mm/YY H:M:S
#     now = datetime.now()
#     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#     # print("date and time =", dt_string)
#     response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")

#     for item in parsed_data2["Item"]:
#         while True:
#             print(f'Processing for name: {item["name"]}....')
#             # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
#             headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
#             # access token expires in 3600 seconds (60 minutes)
#             sleep(2)

#             # param = dict()
#             # param['JSONString'] = item
#             # r2 = requests.post(post_url,headers=headers,data=param)

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
#                 response_save_file.write(f'{parsed_data3["contact"]["contact_id"]} : {item["name"]}\n')
#                 print(f'{item["name"]} is successfully pushed')
#                 # It means success
#                 break
#             else:
#                 print(f'ERROR occurred: {item["name"]} was able to be pushed')
#                 print(f'error code returned in json is {parsed_data3["code"]} and msg is {parsed_data3["message"]}')
            

#         print(f'Successfully created item named: {item["name"]}')

def put_request_bill_vendor_zoho():
    # https://accounts.zoho.in/oauth/v2/token?code=..&client_id=..&client_secret=..&redirect_uri=http://www.zoho.in/books&grant_type=authorization_code

    # output_file_name = 'console_output_2013_to_2017.txt'
    # output_file_name_fout = open(output_file_name)

    # ZohoBooks.fullaccess.all
    # code = '1000.3f2187fa12c1465d48fab99ab199f937.619ab209c92d1634e7764f1c5b6ce6e7'
    # client_id = '1000.UR9FCNRIBAJ11TLABY8K4C0UAW14BP'
    # client_secret = 'e72b1a3f32e16117b3287974149f066ed1f13f0822'

    # code = '1000.47cf7788be746f4c544b7725fe9b8490.5e228429002f2291c7ce4e2c9412b313'
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
    access_token = '1000.0b376db984e80e18a8bd768347cf806e.7f68a00bb74bd80c86fb18f2b7d97e27'
    # expires_in = parsed_data["expires_in"]

    print(refresh_token)
    print(access_token)

    organization_id = '60001574931'
    # organization_id = '60015983411'
    # post_url = f'https://books.zoho.in/api/v3/expenses?organization_id={organization_id}'

    # f = open('mapped.json')
    # f = open('failed_mapped.json')
    # f = open('to_again_mapped.json')
    # f = open('mapped_expense_list.json')
    # f = open('failed_mapped.json')
    # f = open('failed_mapped_expense.json')
    # f = open('mapped_expense_list_for_PUT.json')
    f = open('mapped_saved_details.json')

    parsed_data2 = json.load(f)
    # items_list = parsed_data2["JournalEntry"]
    items_list = parsed_data2


    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    # response_save_dict = dict()
    response_save_file = open("saved_bill_vendor_put_id.txt","a")
    error_response_save_file = open("error_console_for_failed_invoice.txt","a")


    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    response_save_file.write(f"NEW WRITE STARTED : {dt_string}\n")
    # error_response_save_file.write(f"NEW WRITE STARTED: {dt_string}\n")

    for item in items_list:
        post_url = f'https://books.zoho.in/api/v3/contacts/{item["for_my_use"]}?organization_id={organization_id}'

        while True:
            print(f'Processing for entry_number: {item["for_my_use"]}....')
            # Zoho-oauthtoken 1000.a43e3a6b304f8ffb600387c4502054d0.5d80657681be79cf9b70154e2b4fe5a0
            headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
            # access token expires in 3600 seconds (60 minutes)
            sleep(0.5)
            # 500ms
            # param = dict()
            # param['JSONString'] = item
            # r2 = requests.post(post_url,headers=headers,data=param)

            id_from_qb = item["for_my_use"]

            # if "id_from_qb" in item:
            #     del item["id_from_qb"]

            r2 = requests.put(post_url,headers=headers,json=item)

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
                response_save_file.write(f"ACCESS_TOKEN IS : {access_token} and REFRESH_TOKEN IS : {refresh_token}")
                response_save_file.flush()
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
                response_save_file.write(f'{parsed_data3["contact"]["contact_id"]} : {id_from_qb}\n')

                print(f'{id_from_qb} is successfully updated')
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
                print(f'ERROR occurred: {item["for_my_use"]} was not able to be pushed')
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
    
    if r.status_code == 200:
        parsed_json = r.json()
        access_token = parsed_json["access_token"]
        return access_token

    print('refresh_token is expired')
    exit()

get_items_and_write_to_file()

# download_all_attachable_at_once() # Links get expired, so possible and also incase file is large then also it fails
# download_all_attachable_in_chunks() # Links get expired
# download_attachable_at_once() # Does not work if file is large
# download_attachable_in_chunks()

# download_attachable_in_chunks_v2()
# upload_attachment_to_invoice()
# upload_attachment_to_bills()
# upload_attachment_to_journalEntrys()
# generate_post_json()
# post_request_zoho()
# put_request_bill_vendor_zoho()


        

