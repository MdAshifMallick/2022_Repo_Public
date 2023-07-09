import json

def parse1():
	# file_name1 = '../v2/v2/invoice/through_api_post_gst/saved_invoice_id.txt'
	# file_name1 = '../v2/v2/invoice/new_fetch_from_01_08_2022/through_api/saved_invoice_id.txt'

	file_name1 = 'saved_bill_id.txt'
	# file_name1 = '../v2/v2/bill/new_fetch_from_01_08_2022/through_api/saved_bill_id.txt'

	# file_name1 = '../creditMemo/through_api_post_gst/saved_creditMemo_id.txt'
	# file_name1 = '../creditMemo/new_fetch_from_01_08_2022/through_api/saved_creditMemo_id.txt'

	# file_name1 = '../v3/purchase_order/through_api_post_gst/saved_po_id.txt'
	# file_name1 = '../v2/v2/purchase_order/new_fetch_from_01_08_2022/through_api/saved_po_id.txt'

	# file_name1 = '../vendorCredit/new_fetch_from_01_08_2022/through_api/saved_vendorcredits_id.txt'

	# file_name1 = '../estimates/new_fetch_from_01_08_2022/through_api/saved_estimate_id.txt'
	# file_name1 = '../estimates/through_api_post_gst/saved_estimate_id.txt'

	# file_name1 = '../purchase/new_fetch_from_01_08_2022/through_api/saved_customer_id.txt'
	# file_name1 = '../journal_entry/new_fetch_from_01_08_2022/through_api/saved_journal_id.txt'

	# file_name1 = '../payment/through_api/saved_payment_customer_advance_id.txt'
	# file_name1 = '../payment/through_api/saved_payment_id.txt'
	# file_name1 = '../payment/new_fetch_from_01_08_2022/through_api/saved_payment_customer_advance_id.txt'


	file_name1out = open(file_name1)

	final_dict = dict()
	for line in file_name1out:
		if line.startswith('NEW') or line.startswith('Failed') or line.startswith('ACCESS') or line.startswith('SKIPPED_B2COTHERS') or line.startswith('SKIPPED_EXPORTWITHOUTPAYMENT') or line.startswith('SKIPPED_TO_PUSH_1'):
			continue
		
		stripped_line_list = line.split(" : ")
		# print(stripped_line_list)

		# print(line)
		# final_dict[f"{stripped_line_list[0]}"] = f"{stripped_line_list[1].strip()}"
		final_dict[f"{stripped_line_list[1].strip()}"] = f"{stripped_line_list[0]}"


	mapped_json = json.dumps(final_dict,indent=4)
	with open("parsed_out_mapped_for_payment_1.json", "w") as outfile:
		outfile.write(mapped_json)

	file_name1out.close()

def parse2():
	file_name1 = 'saved_invoice_id_final_aq.txt'

	file_name1out = open(file_name1)

	final_dict = dict()
	for line in file_name1out:
		if line.startswith('NEW') or line.startswith('Failed') or line.startswith('ACCESS'):
			continue
		
		stripped_line_list = line.split(" : ")
		# print(stripped_line_list)

		# final_dict[f"{stripped_line_list[0]}"] = f"{stripped_line_list[1].strip()}"
		final_dict[f"{stripped_line_list[1].strip()}"] = f"{stripped_line_list[0]}"


	mapped_json = json.dumps(final_dict,indent=4)
	with open("mapped_for_invoice.json", "w") as outfile:
		outfile.write(mapped_json)

	file_name1out.close()

def parse3():
	file_name1 = '../purchase/through_api/saved_purchase_expense_id.txt'

	file_name1out = open(file_name1)

	final_dict = dict()
	for line in file_name1out:
		if line.startswith('NEW') or line.startswith('Failed') or line.startswith('ACCESS') or line.startswith('SKIPPED_B2COTHERS'):
			continue
		
		stripped_line_list = line.split(" : ")
		# print(stripped_line_list)

		# final_dict[f"{stripped_line_list[0]}"] = f"{stripped_line_list[1].strip()}"
		print(line)
		final_dict[f"{stripped_line_list[1].strip()}"] = f"{stripped_line_list[0]}"


	mapped_json = json.dumps(final_dict,indent=4)
	with open("parsed_out_mapped_for_purchase_expense.json", "w") as outfile:
		outfile.write(mapped_json)

	file_name1out.close()

# parse1()
parse2()
# parse3()