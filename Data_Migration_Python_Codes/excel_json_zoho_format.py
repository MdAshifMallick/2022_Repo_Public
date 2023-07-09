import pandas
import json

data=pandas.read_excel('sample_contacts_new_VENDOR.xlsx', sheet_name='sample_contacts_new (5)')
data[' Rate ']=int(data[' Rate '])

# dic={'contact_name':data['Party Name'].to_list(),'email':data['Email Id'].to_list(),'phone':data['Phone'].to_list(),
#      'gst_treatment':data['GST Treatment'].to_list(),'gst_no':data['GSTIN'].to_list(),
#      'billing_address':{'address':data['Billing Address'].to_list(),'city':data['Billing City'].to_list(),
#                         'state':data['Billing State'].to_list(),'country':data['Billing Country'].to_list(),
#                         'zip':data['Billing Code'].to_list()},
#      'shipping_address':{'address':data['Shipping Address'].to_list(),'city':data['Shipping City'].to_list(),
#                         'state':data['Shipping State'].to_list(),'country':data['Shipping Code'].to_list(),
#                         'zip':data['Shipping Code.1'].to_list()}}

# zoho customer json format for data pushing
def zoho_json_format_customer():
    emp_list=[]
    for i in range(data.shape[0]):
        emp_list.append({'contact_name':data['Party Name'][i],'contact_type': "customer",'email':data['Email Id'][i],'phone':data['Phone'][i],
                         'gst_treatment':data['GST Treatment'][i],'gst_no':data['GSTIN'][i],
                         'billing_address':{'address':data['Billing Address'][i],'city':data['Billing City'][i],
                         'state':data['Billing State'][i],'country':data['Billing Country'][i],
                         'zip':data['Billing Code'][i]},
                         'shipping_address':{'address':data['Shipping Address'][i],'city':data['Shipping City'][i],
                         'state':data['Shipping State'][i],'country':data['Shipping Code'][i],
                         'zip':data['Shipping Code.1'][i]}})
    with open("sample_contacts_new_VENDOR.json", "w") as final:
        json.dump(emp_list, final,indent=2)


# zoho vendor json format for data pushing

def zoho_json_format_vendor():
    emp_list=[]
    for i in range(data.shape[0]):
        emp_list.append({'contact_name':data['Party Name'][i],'contact_type': "vendor",'email':data['Email Id'][i],'phone':data['Phone'][i],
                         'gst_treatment':data['GST Treatment'][i],'gst_no':data['GSTIN'][i],
                         'billing_address':{'address':data['Billing Address'][i],'city':data['Billing City'][i],
                         'state':data['Billing State'][i],'country':data['Billing Country'][i],
                         'zip':data['Billing Code'][i]},
                         'shipping_address':{'address':data['Shipping Address'][i],'city':data['Shipping City'][i],
                         'state':data['Shipping State'][i],'country':data['Shipping Code'][i],
                         'zip':data['Shipping Code.1'][i]}})
    with open("sample_contacts_new_VENDOR.json", "w") as final:
        json.dump(emp_list, final,indent=2)

# zoho_json_format_customer()
# zoho_json_format_vendor()