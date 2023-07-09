import json

file_name = 'data_from_qb_taxcode_PR.json'

f = open(file_name)
parsed_data = json.load(f)
f1 = open("parsed_taxcode_PR.txt","w")

# def mapping_func(taxcode):
#     taxcodename  = taxcode["Name"]
#     taxcodeid  = taxcode["Id"]

#     return [taxcodeid,taxcodename]

my_item_list = list()
for taxcode in parsed_data:
    # my_item_dict = dict()
    # my_item_dict['name'] = item["Name"]
    # my_item_dict['rate'] = item["UnitPrice"]

    # mapped_customer = mapping_func(item)

    tax_rate_dict = dict()

    taxCodeName = taxcode["Name"]
    taxCodeId = taxcode["Id"]

    final_string = f'taxcode_dict["{taxCodeId}"] = "{taxCodeName}"\n'

    f1.write(final_string)

    # my_item_list.append(mapped_customer)

# mapped_data = dict()
# mapped_data["Vendor"] = my_item_list

# mapped_json = json.dumps(mapped_data,indent=4)

# with open("parsed.txt", "w") as outfile:
#     outfile.write(mapped_json)
