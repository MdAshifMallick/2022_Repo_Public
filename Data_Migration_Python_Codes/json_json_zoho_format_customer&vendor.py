import json

# converting json to dictionary

def js_r(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)

if __name__ == "__main__":
    my_data = js_r('vvgydccy.json')
    

# iterating dictionary

print(len(my_data))

contact_name=[]
email=[]
phone=[]
gst_treatment=[]
gst_no=[]
bill_add=[]
bill_city=[]
bill_state=[]
bill_country=[]
bill_zip=[]
ship_add=[]
ship_city=[]
ship_state=[]
ship_country=[]
ship_zip=[]
currency=[]
term=[]

for i in range(len(my_data)):
    contact_name.append(my_data[i]['contact_name'])
    email.append(my_data[i]['email'])
    phone.append(my_data[i]['phone'])
    gst_treatment.append(my_data[i]['gst_treatment'])
    gst_no.append(my_data[i]['gst_no'])
    bill_add.append(my_data[i]['billing_address']['address'])
    bill_city.append(my_data[i]['billing_address']['city'])
    bill_state.append(my_data[i]['billing_address']['state'])
    bill_country.append(my_data[i]['billing_address']['country'])
    bill_zip.append(my_data[i]['billing_address']['zip'])
    ship_add.append(my_data[i]['shipping_address']['address'])
    ship_city.append(my_data[i]['shipping_address']['city'])
    ship_state.append(my_data[i]['shipping_address']['state'])
    ship_country.append(my_data[i]['shipping_address']['country'])
    ship_zip.append(my_data[i]['shipping_address']['zip'])

# gst_registration_type

for j in range(len(gst_treatment)):
    if gst_treatment[j] == 'GST_REG_REG':
        gst_treatment[j] = 'business_gst'
    elif gst_treatment[j] == 'GST_UNREG':
        gst_treatment[j] = 'business_none'
    elif gst_treatment[j] == 'GST_REG_COMP':
        gst_treatment[j] = 'business_registered_composition'
    elif gst_treatment[j] == 'CONSUMER':
        gst_treatment[j] = 'consumer'
    elif gst_treatment[j] == 'OVERSEAS':
        gst_treatment[j] = 'overseas'
    elif gst_treatment[j] == 'SEZ':
        gst_treatment[j] = 'sez_developer'
    elif gst_treatment[j] == 'SEZ':
        gst_treatment[j] = 'DEEMED'

# currency type

for k in range(len(currency)):
    if currency[k] == 'AED':
        currency[k] = '951651000000014183'
    elif currency[k] == 'AUD':
        currency[k] = '951651000000000073'
    elif currency[k] == 'CAD':
        currency[k] = '951651000000000067'
    elif currency[k] == 'CNY':
        currency[k] = '951651000000000085'
    elif currency[k] == 'EUR':
        currency[k] = '951651000000000079'
    elif currency[k] == 'GBP':
        currency[k] = '951651000000000070'
    elif currency[k] == 'INR':
        currency[k] = '951651000000000064'
    elif currency[k] == 'JPY':
        currency[k] = '951651000000000082'
    elif currency[k] == 'SAR':
        currency[k] = '951651000000014181'
    elif currency[k] == 'USD':
        currency[k] = '951651000000000061'
    elif currency[k] == 'ZAR':
        currency[k] = '951651000000000076'

# term type 1

# for l in range(len(term)):
#     if term[l] == '0':
#         term[l] = 'By 5th'
#     elif term[l] == '1':
#         term[l] = 'Due on receipt'
#     elif term[l] == '2':
#         term[l] = 'Immediate'
#     elif term[l] == '3':
#         term[l] = 'Net'
#     elif term[l] == '4':
#         term[l] = 'Net 10'
#     elif term[l] == '5':
#         term[l] = 'Net 30'
#     elif term[l] == '6':
#         term[l] = 'Net 45'
#     elif term[l] == '7':
#         term[l] = 'Net 45 Days'
#     elif term[l] == '8':
#         term[l] = 'Net 5'
#     elif term[l] == '9':
#         term[l] = 'Net 60'
#     elif term[l] == '10':
#         term[l] = 'Net 75'
#     elif term[l] == '11':
#         term[l] = 'Net 90'
#     elif term[l] == '12':
#         term[l] = 'quarterly'
#     elif term[l] == '13':
#         term[l] = 'nothingfor13'
#     elif term[l] == '14':
#         term[l] = 'nothingfor14'
#     elif term[l] == '15':
#         term[l] = 'nothingfor15'
#     elif term[l] == '16':
#         term[l] = 'nothingfor16'
    


# term type 2

for l in range(len(term)):
    if term[l] == '6':
        term[l] = 'By 5th'
    elif term[l] == '1':
        term[l] = 'Due on receipt'
    elif term[l] == '12':
        term[l] = 'Immediate'
    elif term[l] == '7':
        term[l] = 'Net'
    elif term[l] == '9':
        term[l] = 'Net 10'
    elif term[l] == '2':
        term[l] = 'Net 15'
    elif term[l] == '3':
        term[l] = 'Net 30'
    elif term[l] == '14':
        term[l] = 'Net 45'
    elif term[l] == '8':
        term[l] = 'Net 45 Days'
    elif term[l] == '15':
        term[l] = 'Net 5'
    elif term[l] == '4':
        term[l] = 'Net 60'
    elif term[l] == '5':
        term[l] = 'Net 7'
    elif term[l] == '13':
        term[l] = 'Net 75'
    elif term[l] == '11':
        term[l] = 'Net 90'
    elif term[l] == '10':
        term[l] = 'quarterly'
    
    
# converting to zoho json format

# zoho customer json format for data pushing
def zoho_json_format_customer():
    emp_list=[]
    for i in range(mydata.shape[0]):
        emp_list.append({'contact_name':contact_name[i],'contact_type': "customer",'email':email[i],'phone':phone[i],
                         'gst_treatment':gst_treatment[i],'gst_no':gst_no[i],
                         'billing_address':{'address':bill_add[i],'city':bill_city[i],
                         'state':bill_state[i],'country':bill_country[i],
                         'zip':bill_zip[i]},
                         'shipping_address':{'address':ship_add[i],'city':ship_city[i],
                         'state':ship_state[i],'country':ship_country[i],
                         'zip':ship_zip[i]}})
    with open("sample_contacts_new_VENDOR.json", "w") as final:
        json.dump(emp_list, final,indent=2)

# zoho vendor json format for data pushing
def zoho_json_format_vendor():
    emp_list=[]
    for i in range(data.shape[0]):
        emp_list.append({'contact_name':contact_name[i],'contact_type': "vendor",'email':email[i],'phone':phone[i],
                         'gst_treatment':gst_treatment[i],'gst_no':gst_no[i],
                         'billing_address':{'address':bill_add[i],'city':bill_city[i],
                         'state':bill_state[i],'country':bill_country[i],
                         'zip':bill_zip[i]},
                         'shipping_address':{'address':ship_add[i],'city':ship_city[i],
                         'state':ship_state[i],'country':ship_country[i],
                         'zip':ship_zip[i]}})
    with open("sample_contacts_new_VENDOR.json", "w") as final:
        json.dump(emp_list, final,indent=2)

# zoho_json_format_customer()
# zoho_json_format_vendor()