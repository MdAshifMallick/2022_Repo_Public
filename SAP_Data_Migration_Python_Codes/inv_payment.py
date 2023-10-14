import pandas as pd
import numpy as np
import json

import pandas as pd
import json

df = pd.read_excel('6012 2019-20_Output.xlsx', sheet_name='Full Output')
df = df[(df['G/L Account'].notnull())]
df['Document Number']=[int(float(i['Document Number'])) for _,i in df.iterrows()]
df=df[df['Interbranch'].str.contains("Regular")]
df=df[df['Type']=="Debtors"]
df=df[df['Subtype']=="Debit/Credit Note"]
df=df[df['Amount in local currency'] < 0]
# df=df[df['Partner Profit Ctr'].str.contains("ip")]
df1=df[df['G/L Acct Long Text'].str.contains("Sundry Debtors")]
df2=df[df['G/L Acct Long Text'].str.contains("Sundry Debtors")]
doc_num=[i['Document Number'] for _,i in df2.iterrows()]
acc=[i['new_acc'] for _,i in df2.iterrows()]

with open('contact_details_CHIKHALI.json', 'r') as f:
    contact_ids_data = json.load(f)

with open('coa_details_CHIKHALI.json', 'r') as f:
    account_ids_data = json.load(f)

with open('BRANCH.json', 'r') as f:
    branch_ids_data = json.load(f)

# Create a list to store the journal entries
journal_entries = []

# Group the DataFrame by continuous Document Numbers
grouped = df1.groupby((df1['Document Number'] != df1['Document Number'].shift()).cumsum())

nm = 1
null_acc = []

# Iterate through the groups and create the journal entries
# for _, group in grouped:
#     # Initialize a flag to track the first row
#     first_row_processed = False

#     for _, row in group.iterrows():
#         # If the first row has already been processed, skip the rest of the rows in this group
#         if first_row_processed:
#             break

#         amount = abs(row['Amount in local currency'])
#         account_code = str(int(row['G/L Account']))
#         account_id = account_ids_data.get(account_code)
#         vendor_id = contact_ids_data.get(str(int(row['Assignment'])))
#         description = row["Text"]
#         name = row["G/L Acct Long Text"]
#         branch_code = str(int(row['Profit Center']))
#         branch_id = branch_ids_data.get(branch_code)

#         if vendor_id is None:
#             null_acc.append(row['Assignment'])

#         line_items = [{
#             'rate': amount,
#             "name": name,
#             "description": description,
#             'account_id': account_id,
#             'gst_treatment_code': 'out_of_scope'
#         }]

#         # Get journal_date, notes, and reference_number for this journal entry
#         bill_date = str(group['Posting Date'].iloc[0].strftime('%Y-%m-%d'))
for _, row in df1.iterrows():
        # Create the journal entry for this group
        if contact_ids_data.get(str((row["Customer"]))) == None:
             null_acc.append(row["Customer"])
        print(row['Document Number'])
        journal_entry = {
            "id_from_qb": str(nm),
            "payment_number_prefix": "2019-",
            "payment_number_suffix": str(row["Document Number"]),
            "ignore_auto_number_generation": True,
            "payment_mode": "other",
            "customer_id": contact_ids_data.get(str((row["Customer"]))),
            "amount": abs(row["Amount in local currency"]),
            "description": row["Text"],
            "reference_number": (row["Reference"]),

            # "payment_number": "2021/"+str(nm)+"/"+ str(row["Document Number"]),
            "date": str(row['Posting Date'].strftime('%Y-%m-%d')),
            "branch_id": branch_ids_data.get(str(int(row["Profit Center"]))),
            'is_advance_payment': True,
            "account_id": 1497702000000028551,
            # "account_id": account_ids_data.get(str(int(acc[doc_num.index(row['Document Number'])]))),
            # "offset_account_id": 1279300000000016356,
            "custom_fields": [{
                "label": "SAP Document No",
                "value": row["Document Number"]
            },
            {
                "label": "Document Date",
                "value": str(row["Document Date"])[:10]
            }],
        }

        # Append the journal entry to the list of journal entries
        journal_entries.append(journal_entry)
        nm = nm + 1

        # Set the flag to indicate that the first row has been processed
        # first_row_processed = True

# Convert the result to a JSON string
json_output = json.dumps(journal_entries, indent=4)

with open("mapped_ip_2019_D_C_note.json", "w") as outfile:
    outfile.write(json_output)

print(np.unique(null_acc))
