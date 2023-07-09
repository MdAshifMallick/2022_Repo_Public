import json


def attachment_parsing():
	file_name1 = 'data_from_qb_attachable_mrj.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	final_parsed_data = parsed_data1

	null_value = None

	final_dict = dict()
	count = 0
	for item in final_parsed_data:
		if "AttachableRef" in item:
			attachable_ref_list = item["AttachableRef"]

			attachment_id = item["Id"]
			file_name = item["FileName"]
			content_type = item["ContentType"]

			for a_ref_item in attachable_ref_list:

				entity_value = a_ref_item["EntityRef"]["value"]
				entity_type = a_ref_item["EntityRef"]["type"]
				includeonsend  = a_ref_item["IncludeOnSend"]

				count = count+1

				key_string = f"{entity_value}#{entity_type}#{includeonsend}#{count}"

				final_dict[key_string] = [attachment_id,file_name,content_type]

	# mapped_data = dict()
	# mapped_data["Vendor"] = my_item_list

	mapped_json = json.dumps(final_dict,indent=4)

	with open("attachment_details.json", "w") as outfile:
	    outfile.write(mapped_json)


def extract_invoice():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "Invoice":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_invoice_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def extract_bill():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "Bill":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_bill_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def extract_creditMemo():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "CreditMemo":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_creditMemo_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def extract_journalEntry():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "JournalEntry":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_journalEntry_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def extract_estimate():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "Estimate":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_estimate_details.json", "w") as outfile:
	    outfile.write(mapped_json)


def extract_vendor_credit():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "VendorCredit":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_vendorCredit_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def extract_purchase():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "Purchase":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_purchase_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def extract_transfer():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "Transfer":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_transfer_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def extract_po():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "PurchaseOrder":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_po_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def extract_payment():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "Payment":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_payment_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def extract_billpayment():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "BillPayment":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_billpayment_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def extract_deposit():
	file_name1 = 'attachment_details.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	extracted_invoice_dict = dict()
	for key,value in parsed_data1.items():

		key_split_list = key.split('#')

		if key_split_list[1] == "Deposit":
			extracted_invoice_dict[key] = value

	mapped_json = json.dumps(extracted_invoice_dict,indent=4)

	with open("attachment_deposit_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing1():
	# file_name1 = '../invoice/excel/data_from_qb_2013_04_01_to_2017_06_30_invoice.json'
	# file_name1 = '../v2/v2/invoice/new_fetch_from_01_08_2022/through_api/data_from_qb_invoice.json'
	file_name1 = 'fatched_data/data_from_qb_invoice_mrj.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_invoice_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_invoice_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing2():
	# file_name1 = '../bill/data_from_qb_2013_04_01_to_2017_06_30_bill.json'
	file_name1 = 'fatched_data/data_from_qb_bill_mrj.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_bill_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	# 1449
	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_bill_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing3():
	file_name1 = '../creditMemo/new_fetch_from_01_08_2022/through_api/data_from_qb_creditMemo.json'
	# file_name1 = '../creditMemo/excel/data_from_qb_creditMemo_copy.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_creditMemo_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_creditMemo_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing4():
	file_name1 = 'fatched_data/data_from_qb_journal_entry_mrj.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_journalEntry_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	# 
	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_journalEntry_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing5():
	# file_name1 = '../estimates/new_fetch_from_01_08_2022/through_api/data_from_qb_estimate.json'
	# file_name1 = '../estimates/other_files/data_from_qb_2013_04_01_to_2017_06_30_estimate.json'
	file_name1 = 'fatched_data/data_from_qb_estimate_mrj.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_estimate_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	# 
	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_estimate_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing6():
	# file_name1 = '../vendorCredit/other_files/data_from_qb_2013_04_01_to_2017_06_30_vendor_credit.json'
	file_name1 = '../vendorCredit/new_fetch_from_01_08_2022/through_api/data_from_qb_vendor_credit.json'
	
	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_vendorCredit_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	# 
	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_vendorCredit_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing7():
	file_name1 = 'fatched_data/data_from_qb_purchase_mrj.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_purchase_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_purchase_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing8():
	file_name1 = '../purchase/through_api/vendor_payment_list.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_purchase_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_vp_using_purchase_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing9():
	# file_name1 = '../transfer/new_fetch_from_01_08_2022/through_api/data_from_qb_transfer.json'
	file_name1 = '../transfer/other_files/data_from_qb_2013_04_01_to_2017_06_30_transfer.json'
	file_name2= '../transfer/other_files/data_from_qb_2017_07_01_to_2022_07_31_transfer.json'

	f1 = open(file_name1)
	parsed_data1_1 = json.load(f1)
	f1.close()

	f1 = open(file_name2)
	parsed_data1_2 = json.load(f1)
	f1.close()

	parsed_data1 = parsed_data1_1 + parsed_data1_2

	file_name2 = 'attachment_transfer_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_transfer_details.json", "w") as outfile:
	    outfile.write(mapped_json)


def final_invoice_parsing10():
	# file_name1 = '../v2/v2/purchase_order/new_fetch_from_01_08_2022/through_api/data_from_qb_purchase_order.json'
	file_name1 = '../v2/v2/purchase_order/other_files/data_from_qb_2017_07_01_to_2022_07_31_purchase_order.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_po_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_po_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing11():
	# file_name1 = '../v2/v2/deposit/new_fetch_from_01_08_2022/through_api/data_from_qb_deposit.json'
	# file_name1 = '../v2/v2/deposit/other_files/data_from_qb_2013_04_01_to_2017_06_30_deposit.json'
	file_name1 = 'fatched_data/data_from_qb_transfer_mrj.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_transfer_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_transfer_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing12():
	file_name1 = 'fatched_data/data_from_qb_payment_mrj'
	# file_name1 = '../payment/new_fetch_from_01_08_2022/through_api/data_from_qb_payment.json'

	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_payment_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_payment_details.json", "w") as outfile:
	    outfile.write(mapped_json)

def final_invoice_parsing13():
	# file_name1 = '../bill_payment/other_files/all_bill_payment.json'
	file_name1 = 'fatched_data/data_from_qb_billpayment_mrj'
	
	f1 = open(file_name1)
	parsed_data1 = json.load(f1)

	file_name2 = 'attachment_billpayment_details.json'

	f2 = open(file_name2)
	parsed_data2 = json.load(f2)

	final_invoice_extracted_dict = dict()
	for pd1_item in parsed_data1:
		invoice_id = pd1_item["Id"]

		for key,value in parsed_data2.items():
			if invoice_id == key.split('#')[0]:
				final_invoice_extracted_dict[key] = value

	print(len(final_invoice_extracted_dict))

	mapped_json = json.dumps(final_invoice_extracted_dict,indent=4)

	with open("extracted_billpayment_details.json", "w") as outfile:
	    outfile.write(mapped_json)


# attachment_parsing()

# extract_invoice()
# final_invoice_parsing1()

# extract_bill()
# final_invoice_parsing2()

# extract_creditMemo()
# final_invoice_parsing3()

# extract_journalEntry()
# final_invoice_parsing4()

# extract_estimate()
# final_invoice_parsing5()

# extract_vendor_credit()
# final_invoice_parsing6()

# extract_purchase()
# final_invoice_parsing7()

# final_invoice_parsing8()

# extract_transfer()
# final_invoice_parsing9()

# extract_po()
# final_invoice_parsing10()

# extract_deposit()
final_invoice_parsing11()

# extract_payment()
# final_invoice_parsing12()

# extract_billpayment()
# final_invoice_parsing13()






