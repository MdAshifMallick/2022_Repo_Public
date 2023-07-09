import json
import random
import string
def parse3():
    # filename = 'mapped.json'
    # filename = '../all_bill_payment.json'
    # parsed_data = json.load(open(filename))

    fout = open('saved_payment_newcom.txt')

    # str1 = "msg is Some of the bills for which you've chosen to record payments do not exist. Please check and try again."
    # str2 = "msg is The Vendor field can neither be blank nor be incorrect. Please enter a correct vendor name."
    # str3 = "msg is The amount entered is more than the balance due for the selected bills."
    # str4 = "msg is Please enter valid expense account"
    str5 = "msg is The amount entered is more than the balance due for the selected invoices."
    # str6 = "msg is Reverse charge should be applied on import of services or purchases from unregistered vendors."

    final_list = list()
    for line in fout:
        if line.startswith('Failed'):
            # print(line)
            splitted_line = line.split(' -> ')
            stripped_line1 = splitted_line[1].strip()
            stripped_line0 = splitted_line[0].strip()
            if stripped_line1 == str5: # and stripped_line1 == str5:
                item_id = stripped_line0.split(' : ')[1]
                if str(item_id) not in final_list:
                    final_list.append(str(item_id))


    print(len(final_list))
    mapped_data = json.dumps(final_list,indent=4)
    with open('list_newcom.json','w') as f:
        f.write(mapped_data)

def parse4():
    # to_find_list = ["4417","4433","4412","4074","4431","4426","4407","4410","4408","4399","4081","4405",
                    # "4090","4084","4082","4075","97","152"]
    to_find_list = json.load(open('list_newcom.json'))
    filename = 'data_from_qb_payment_newcom.json'
    parsed_data = json.load(open(filename))

    final_list = list()
    for item in parsed_data:
        if item["Id"] in to_find_list:
            final_list.append(item)

    print(final_list[:10])
    # alphanumeric_chars = string.ascii_letters + string.digits
    # alphanumeric_chars = string.digits
    # unique_values = [''.join(random.choices(alphanumeric_chars, k=3)) for i in range(38)]
    # print(len(unique_values))
    # for i,j in zip(final_list,unique_values):
    #     i['bill_number'] += j
    # print(final_list[:10])
    
    mapped_data = json.dumps(final_list,indent=4)
    with open('err_newcom.json','w') as f:
        f.write(mapped_data)
# parse3()
parse4()