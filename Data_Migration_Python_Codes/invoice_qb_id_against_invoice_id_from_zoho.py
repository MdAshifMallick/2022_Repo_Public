import json
def parse2():
	file_name1 = 'through_api_post_gst/saved_invoice_id_PR.txt'

	file_name1out = open(file_name1)

	final_dict = dict()
	for line in file_name1out:
		if line.startswith('NEW') or line.startswith('Failed') or line.startswith('ACCESS'):
			continue
		
		stripped_line_list = line.split(" : ")
		print(stripped_line_list)

		# final_dict[f"{stripped_line_list[0]}"] = f"{stripped_line_list[1].strip()}"
		final_dict[f"{stripped_line_list[1].strip()}"] = f"{stripped_line_list[0]}"


	mapped_json = json.dumps(final_dict,indent=4)
	with open("invoice_qb_id_against_invoice_id_from_zoho_PR.json", "w") as outfile:
		outfile.write(mapped_json)

	file_name1out.close()
parse2()