import json

def parse1():
    fileout = open('data_from_zoho_currency_geo.json')

    parsed_data1 = json.load(fileout)

    final_dict = dict()
    for item in parsed_data1:
        final_dict[item["currency_code"]] = item["currency_id"] 

    mapped_json = json.dumps(final_dict,indent=4)
    with open('currency_details_geo.json','w') as f:
        f.write(mapped_json)
    fileout.close()

def parse2():
    fileout = open('data_from_zoho_po_detailed.json')

    parsed_data1 = json.load(fileout)

    final_dict = dict()
    for item in parsed_data1:
        final_dict[item["purchaseorder_number"]] = item["purchaseorder_id"] 

    mapped_json = json.dumps(final_dict,indent=4)
    with open('po_details.json','w') as f:
        f.write(mapped_json)
    fileout.close()

def parse3():
    parsed_data_old_id = json.load(open('../getData/purchaseorders/po_details.json'))
    parsed_data_new_id = json.load(open('po_details.json'))

    final_dict = dict()
    for oldk,oldv in parsed_data_old_id.items():
        for newk,newv in parsed_data_new_id.items():
            if oldk == newk:
                final_dict[oldv] = newv

    mapped_json = json.dumps(final_dict,indent=4)
    with open('final_po_details.json','w') as f:
        f.write(mapped_json)

def parse4():
    fileout = open('data_from_zoho_contacts_geo.json')

    parsed_data1 = json.load(fileout)

    final_dict = dict()
    for item in parsed_data1:
        final_dict[item["contact_name"]] = item["contact_id"] 

    mapped_json = json.dumps(final_dict,indent=4)
    with open('contact_details_geo.json','w') as f:
        f.write(mapped_json)
    fileout.close()

def parse5():
    parsed_data_old_id = json.load(open('../fromOldZoho/coa_details.json'))
    parsed_data_new_id = json.load(open('coa_details.json'))

    final_dict = dict()
    for oldk,oldv in parsed_data_old_id.items():
        for newk,newv in parsed_data_new_id.items():
            if oldk == newk:
                final_dict[oldv] = newv

    print(len(final_dict))
    mapped_json = json.dumps(final_dict,indent=4)
    with open('final_coa_details.json','w') as f:
        f.write(mapped_json)

def parse6():
    fileout = open('data_from_zoho_tax_global.json')

    parsed_data1 = json.load(fileout)

    final_dict = dict()
    for item in parsed_data1:
        final_dict[item["tax_name"]] = item["tax_id"] 

    mapped_json = json.dumps(final_dict,indent=4)
    with open('tax_details_global.json','w') as f:
        f.write(mapped_json)
    fileout.close()

def parse7():
    fileout = open('data_from_zoho_coa_geowale.json')

    parsed_data1 = json.load(fileout)

    final_dict = dict()
    for item in parsed_data1:
        final_dict[item["account_name"]] = item["account_id"] 

    mapped_json = json.dumps(final_dict,indent=4)
    with open('coa_details_geo5.json','w') as f:
        f.write(mapped_json)
    fileout.close()

def parse8():
    parsed_data_old_id = json.load(open('../fromOldZoho/warehouse_details.json'))
    parsed_data_new_id = json.load(open('warehouse_details.json'))

    final_dict = dict()
    for oldk,oldv in parsed_data_old_id.items():
        for newk,newv in parsed_data_new_id.items():
            if oldk == newk:
                final_dict[oldv] = newv

    print(len(final_dict))
    mapped_json = json.dumps(final_dict,indent=4)
    with open('final_warehouse_details.json','w') as f:
        f.write(mapped_json)

def parse9():
    fileout = open('data_from_zoho_invoices_zing.json')

    parsed_data1 = json.load(fileout)

    final_dict = dict()
    for item in parsed_data1:
        final_dict[item["invoice_number"]] = item["invoice_id"] 

    mapped_json = json.dumps(final_dict,indent=4)
    with open('invoice_id.json','w') as f:
        f.write(mapped_json)
    fileout.close()

def parse10():
    fileout = open('data_from_zoho_items_global.json')

    parsed_data1 = json.load(fileout)

    final_dict = dict()
    for item in parsed_data1:
        final_dict[item["item_name"]] = item["item_id"] 

    mapped_json = json.dumps(final_dict,indent=4)
    with open('item_details_global.json','w') as f:
        f.write(mapped_json)
    fileout.close()

# parse1()
# parse2()
# parse3()
# parse4()
# parse5()
# parse6()
parse7()
# parse8()
# parse9()
# parse10()
