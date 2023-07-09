import json
from time import sleep
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime

def get_items_and_write_to_file():

    # These must be changed
    access_token = '1000.7003208ef0ee8d1cd5c84cd4b9eeec8e.5a2604e58976c1c7e348eb69e73280fd'
    refresh_token = '1000.c401e50034060a989765a87abd1f189d.65dc49ade635b0123577d77fcb56c384'
    organization_id = 60019301836

    client_id = '1000.D4O0MTFDO5CA3892KIOXRQ9FSTWDQE'
    client_secret = '397ea99bb60ec3dd586fc35a135691da4846824e88'

    # headers is used for GET
    headers = CaseInsensitiveDict()
    # headers["Accept"] = "application/json"

    file_name = 'data_from_zoho_items_zing.json'
    fp = open(file_name,'a')
    no_of_objects_fetched = 0
    flag = True
    page = 1
    while flag == True:
        getURL = f"https://www.zohoapis.in/books/v3/items?page={page}&organization_id={organization_id}"
        headers["Authorization"] = f"Zoho-oauthtoken {access_token}"
        r = requests.get(getURL,headers=headers)

        # print(r.status_code)
        if r.status_code == 200:
            parsed_data = r.json()

            if parsed_data["code"] == 0:
                contacts_list = parsed_data["items"]
                no_of_objects_fetched += len(contacts_list)
                page = page + 1,

                for element in contacts_list:
                    indented_data = json.dumps(element,indent=4)
                    fp.write(indented_data)
                    fp.write('\n,\n')

                has_more_page = parsed_data["page_context"]["has_more_page"]
                if not has_more_page:
                    print(f"Finished...Total fetched {no_of_objects_fetched}")
                    flag = False
            else:
                print("SOME ERROR OCCURRED... DUMPING.....")

                dumpfp = open('dumperror.json','w')
                autherror_parsed = json.dumps(parsed_data,indent=4)
                dumpfp.write(autherror_parsed)
                exit()
        else:
            print("RENEWING ACCESS TOKEN...")
            # print(f"SomeError occurred after fetching {no_of_objects_fetched} objects... dumping in error.json")
            # errorfp = open('error.json','w')
            # r_parsed = json.dumps(r.json(),indent=4)
            # errorfp.write(r_parsed)
            renew_URL = f"https://accounts.zoho.in/oauth/v2/token?refresh_token={refresh_token}&client_id={client_id}&client_secret={client_secret}&redirect_uri=http://www.zoho.in/books&grant_type=refresh_token"
            renew_access_token_reponse = requests.post(renew_URL)

            parsed_response = renew_access_token_reponse.json()

            if "error" in parsed_response:
                print("SOMEHTING INVALID HAPPENED DURING RENEWING....")
                errorfp = open('error.json','w')
                r_parsed = json.dumps(renew_access_token_reponse.json(),indent=4)
                errorfp.write(r_parsed)
                exit()
            else:
                # EVERYTHING IS OKAY
                """
                {
                    "access_token": "1000.d35310999e0dfe24ebe6b6a357c82216.9c16c5dd9a4153c9894df3202ec5ffea",
                    "api_domain": "https://www.zohoapis.in",
                    "token_type": "Bearer",
                    "expires_in": 3600
                }
                """
                print("ACCESS_TOKEN_RENEWED...")
                access_token = parsed_response["access_token"]
                print(access_token)
    
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

get_items_and_write_to_file()













