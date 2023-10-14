import pandas as pd
import numpy as np
import json




with open('contact_details_CHIKHALI.json', 'r') as f:
    contact_ids_data = json.load(f)

with open('coa_details_CHIKHALI.json', 'r') as f:
    account_ids_data = json.load(f)

with open('BRANCH.json', 'r') as f:
    branch_ids_data = json.load(f)

# Create a list to store the journal entries

df = pd.read_excel('6012 2018-19_Output.xlsx', sheet_name='Output')
df = df[df['G/L Account'].notnull()]
df=df[df['Interbranch'].str.contains("Regular")]
df=df[df['Type']=="Creditors"]
df=df[df['Subtype']=="Payment with Adj"]
df=df[df['Amount in local currency'] > 0]
df=df[df['G/L Acct Long Text'].str.contains("Sundry Creditors")]
df['Document Number']=[int(float(i['Document Number'])) for _,i in df.iterrows()]
doc_num_count = {}

# Define a function to generate the "new_doc" value
def generate_new_doc(doc_num):
    count = doc_num_count.get(doc_num, 0) + 1
    doc_num_count[doc_num] = count
    return f"{doc_num}{chr(ord('a') + count - 1)}" if count > 1 else str(doc_num)

# Apply the function to create the "new_doc" column
df['new_doc'] = df['Document Number'].apply(generate_new_doc)
# df=df.groupby('Document Number').filter(lambda x: x['Profit Center'].nunique() == 1)


# Filter rows where "G/L Acct Long Text" does not contain "Sundry Creditors"
# filtered_df = df[~df['G/L Acct Long Text'].str.contains("Sundry Creditors")]
# gl_acc=[i['G/L Account'] for _,i in filtered_df.iterrows()]
# doc_num=[i['Document Number'] for _,i in filtered_df.iterrows()]
# print(len(gl_acc))
# Get rows where "G/L Acct Long Text" contains "Sundry Creditors"
sundry_creditors_df = df[df['G/L Acct Long Text'].str.contains("Sundry Creditors")]

# Group by "Document Number" for the filtered DataFrame
grouped = sundry_creditors_df.groupby((sundry_creditors_df['new_doc'] != sundry_creditors_df['new_doc'].shift()).cumsum())

# Create a list to store the journal entries
journal_entries = []

nm = 1
null_acc = []

# Iterate through the groups and create the journal entries
for document_number, group in grouped:
    for _, row in group.iterrows():
        print(row['new_doc'])
        amount = abs(row['Amount in local currency'])
        account_code = str(int(row['new_acc']))
        # print(account_code)
        account_id = account_ids_data.get(account_code)
        vendor_id = contact_ids_data.get(str(int(row['Vendor'])))
        description = row["Text"]
        # document_number=int(row['new_doc'])
        name = row["G/L Acct Long Text"]
        branch_code = str(int(row['Profit Center']))
        branch_id = branch_ids_data.get(branch_code)

        if vendor_id is None:
            null_acc.append(row['Vendor'])

        line_items = [{
            'rate': amount,
            "name": name,
            "description": description,
            'account_id': account_id,
            'gst_treatment_code': 'out_of_scope'
        }]

        # Get journal_date, notes, and reference_number for this journal entry
        bill_date = str(group['Posting Date'].iloc[0].strftime('%Y-%m-%d'))

        # Create the journal entry for this group
        journal_entry = {
            "id_from_qb": str(nm),
            # "payment_number_prefix": "2017/"+str(nm)+"/",
            "payment_number_prefix": "2018-",
            "payment_number_suffix": str((row['new_doc'])),
            "ignore_auto_number_generation": True,
            "payment_mode": "other",
            "vendor_id": contact_ids_data.get(str(int(row['Vendor']))),
            "amount": abs(row['Amount in local currency']),
            "reference_number": (row['Reference']),
            # "payment_number": "2017" + str(document_number),
            "date": str(row['Posting Date'].strftime('%Y-%m-%d')),
            "branch_id": branch_ids_data.get(str(int(row['Profit Center']))),
            'is_advance_payment': True,
            # "paid_through_account_id": account_id,
            "paid_through_account_id": 1497702000000028551,
            "offset_account_id": 1497702000000028863,
            "custom_fields": [{
                "label": "SAP Document No",
                "value": str(int(float(row['Document Number'])))
            },
            {
                "label": "Document Date",
                "value": str(row["Document Date"])[:10]
            }],
        }

        # Append the journal entry to the list of journal entries
        journal_entries.append(journal_entry)
        nm = nm + 1

# Convert the result to a JSON string
json_output = json.dumps(journal_entries, indent=4)

with open("mapped_bp_2017_payment_adj.json", "w") as outfile:
    outfile.write(json_output)

print(np.unique(null_acc))


