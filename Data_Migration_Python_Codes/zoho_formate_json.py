import pandas as pd 
import json

map = {
        

        # "Invoice Number" : "Invoice_number",
        # "Seller Gstin" : "GST Identification Number(GSTIN)",
        # "Invoice Date" : "date",
        # "Order Id":"PurchaseOrder",
        # "Shipment Id":"Shipment ID_AMZ",
        # "Shipment Date":"Shipment Date_AMZ_SIM",
        # "Item Description":"Item Desc",
        # "Ship From City":"Ship To City_AMZ",
        # "Ship To Postal Code":"Ship To Postal Code_C",
        # "Tax Exclusive Gross":"Item Price",
        # "Cgst Rate":"CGST",
        # "Sgat Rate":"SGST",
        # "Igst Rate":"IGST",
        # "Product Tax Code":"Product Tax Code_AMZ_FK",
        # "SKU as per ZOHO":"SKU"
    }


def mapping():
    fin = open("data.json")
    parsed_data = json.load(fin)

    mapping_json = []
    for this_json in parsed_data:
        tmp_dict = {"custom_fields" : []}
        for i in this_json:
            if i in list(map.keys()):
                tmp_dict[map[i]] = this_json[i]
            else:
                tmp_dict['custom_fields'].append({"label": i , "value" : this_json[i]})
        tmp_dict['Principal Amount'] = round((1 + this_json['Igst Rate']) * this_json['Tax Exclusive Gross'])        
        mapping_json.append(tmp_dict)
    
    mapped_json = json.dumps(mapping_json,indent=4)
    with open("mapped11.json", "w") as outfile:
        outfile.write(mapped_json)
    # pass


mapping()



# def mapped():
    
#     fin = open("data.json")
#     parsed_data = json.load(fin)

#     #null_value = None
     
#     invoice_list = list()
   
#     for i in parsed_data:
#         mapping_dict = dict()
#         if "Seller Gstin" in i:
#             mapping_dict['GST Identification Number(GSTIN)'] = i['c']
#         else:
#             mapping_dict['GST Identification Number(GSTIN)'] = None
            
#         if "Invoice Number" in i:
#             mapping_dict['Invoice Number'] = i['Invoice Number']
#         else:
#             mapping_dict['Invoice Number'] = None
#         if "Invoice Date" in i:
#             mapping_dict['Invoice Date'] = i['Invoice Date']
#         else:
#             mapping_dict['Invoice Date'] = None
#         if "Order Id" in i:
#             mapping_dict['PurchaseOrder'] = i['Order Id']
#         else:
#             mapping_dict['PurchaseOrder'] = None 
#         if "Shipment Id" in i:
#             mapping_dict['Shipment ID_AMZ'] = i['Shipment Id']
#         else:
#             mapping_dict['Shipment ID_AMZ'] = None         
#         if "Quantity" in i:
#             mapping_dict['Quantity'] = i['Quantity']
#         else:
#             mapping_dict['Quantity'] = None 

#         if "Shipment Date" in i:
#             mapping_dict['Shipment Date_AMZ_SIM'] = i['Shipment Date']
#         else:
#             mapping_dict['Shipment Date_AMZ_SIM'] = None 

#         #if "ccc" in i:
#             #mapping_dict['Item Desc'] = i['Item Description']
#         #else:
#            # mapping_dict['Item Desc'] = None 
#         if "Asin" in i:
#             mapping_dict['Asin_AMZ'] = i['Asin']
#         else:
#             mapping_dict['Asin_AMZ'] = None
#         if "Ship From City" in i:
#             mapping_dict['Ship To City_AMZ'] = i['Ship From City']
#         else:
#             mapping_dict['Ship To City_AMZ'] = None  

#         if "Ship From Postal Code" in i:
#             mapping_dict['Ship From Postal Code_AMZ'] = i['Ship From Postal Code']
#         else:
#             mapping_dict['Ship From Postal Code_AMZ'] = None


#         if "c" in i:
#             mapping_dict['Ship To Postal Code_C'] = i['Ship To Postal Code']
#         else:
#             mapping_dict['Ship To Postal Code_C'] = None 
#         if "Tax Exclusive Gross" in i:
#             mapping_dict['Item Price'] = i['Tax Exclusive Gross']
#         else:
#             mapping_dict['Item Price'] = None     

    
#         # if "Invoice Amount" in i:
#         #     mapping_dict['Principle Amount'] = i['Invoice Amount']
#         # else:
#         #     mapping_dict['Principle Amount'] = None   
#         if "Cgst Rate"in i:
#             mapping_dict['CGST'] = i['Cgst Rate']
#         else:
#             mapping_dict['CGST'] = None  
            
#         if "Sgst Rate" in i:
#             mapping_dict['SGST'] = i['Sgst Rate']
#         else:
#             mapping_dict['SGST'] = None   
#         if "Igst Rate" in i:
#             mapping_dict['IGST'] = i['Igst Rate']
#         else:
#             mapping_dict['IGST'] = None  

#         if "Product Tax Code" in i:
#             mapping_dict['Product Tax Code_AMZ_FK'] = i['Product Tax Code']
#         else:
#             mapping_dict['Product Tax Code_AMZ_FK'] = None      
#         if "SKU as per ZOHO" in i:
#             mapping_dict['SKU'] = i['SKU as per ZOHO']
#         else:
#             mapping_dict['SKU'] = None  

#          # here we done calculation
        
#         # mapping_dict['Principal Amount'] = round(1.18*i["Tax Exclusive Gross"])
#         #mapping_dict['Principal Amount'] = round((1 + i['Igst Rate']) * i['Tax Exclusive Gross'])
#         #mapping_dict['Principal Amount'] = round( i['Igst Rate'] * i['Tax Exclusive Gross']+i['Tax Exclusive Gross'])
#         mapping_dict['Principal Amount'] = round(( i['Igst Rate']+i["Sgst Rate"]+i["Cgst Rate"]) * i['Tax Exclusive Gross']+i['Tax Exclusive Gross'])
#         invoice_list.append(mapping_dict)  

#     mapped_data = dict()
#     mapped_data["Invoice"] = invoice_list

#     mapped_json = json.dumps(mapped_data,indent=4)

#     with open("mapped11.json", "w") as outfile:
#         outfile.write(mapped_json)

           
        
   


#     #mapped_data = dict()
    

#     # mapped_json = json.dumps(invoice_list,indent=2)

#     # with open("mapped6.json", "w") as outfile:
#     #     outfile.write(mapped_json)




# #generate_post_json()

# mapped()    