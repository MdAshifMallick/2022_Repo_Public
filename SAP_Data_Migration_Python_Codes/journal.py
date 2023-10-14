import pandas as pd
import numpy as np
import json

# Read the data from the Excel file into a pandas DataFrame
# df = pd.read_excel('NWW.xlsx')
# df = df[df['G/L Account'].notnull()]



# with open('coa_details_sapp.json', 'r') as f:
#     account_ids_data = json.load(f)


# with open('BRANCH.json', 'r') as f:
#     branch_ids_data = json.load(f)

# print(df)
# # Create a list to store the journal entries
# journal_entries = []

# # Group the DataFrame by continuous Document Numbers
# grouped = df.groupby((df['Document Number'] != df['Document Number'].shift()).cumsum())

# nm=1

# for _, group in grouped:
#     # Calculate the total debit amount for this group
#     total_debit = sum(row['Amount in local currency'] for _, row in group.iterrows() if row['Amount in local currency'] > 0)

#     # Create a list to store line items for this journal entry
#     line_items = []
#     for _, row in group.iterrows():
#         amount = abs(row['Amount in local currency'])
#         debit_or_credit = 'credit' if row['Amount in local currency'] < 0 else 'debit'
#         account_code = str(int(row['G/L Account']))
#         account_id = account_ids_data.get(account_code)
#         description = row["Text"]
#         branch_code = str(int(row['Profit Center']))
#         branch_id = branch_ids_data.get(branch_code)
        
#         if debit_or_credit == 'debit':
#             line_items.append({
#                 'amount': amount,
#                 'debit_or_credit': debit_or_credit,
#                 "description": description,
#                 'account_id': account_id
#             })

#     # Add the single credit entry with the total debit amount
#     line_items.append({
#         'amount': total_debit,
#         'debit_or_credit': 'credit',
#         "description": description,
#         'account_id': account_id
#     })

#     # Get journal_date, notes, and reference_number for this journal entry
#     journal_date = str(group['Document Date'].iloc[0].strftime('%Y-%m-%d'))
#     # notes = "."

#     # Create the journal entry for this group
#     journal_entry = {
#         "id_from_qb": str(nm),
#         "journal_number_prefix": str(row["Document Type"])+"-",
#         "journal_number_suffix": str(row["Document Number"]),
#         "journal_date": journal_date,
#         "branch_id": branch_id,
#         "line_items": line_items,
#         "custom_fields": [{
#                         "label" : "SAP Document No",
#                         "value" : row["Document Number"]
#                     },
#                     {
#                         "label" : "SAP Document Date",
#                         "value" : str(row["Document Date"])[ :10]
#                     }
#                     ],
#         # "notes": notes,
#     }

#     # Append the journal entry to the list of journal entries
#     journal_entries.append(journal_entry)
#     nm = nm + 1


# # Convert the result to a JSON string
# json_output = json.dumps(journal_entries, indent=4)

# # Print the JSON output
# # print(json_output)


# with open("mapped_journal_sapp_AA.json", "w") as outfile:
#     outfile.write(json_output)

############################################################################################

df = pd.read_excel('6012 2019-20_Output.xlsx', sheet_name='Full Output')
df = df[(df['G/L Account'].notnull())]
df['Document Number']=[int(float(i['Document Number'])) for _,i in df.iterrows()]
df=df[df['Interbranch'].str.contains("Regular")]
# df=df[df['Type']=="Creditors"]
df=df[df['Type']=="Debtors"]
df=df[df['Subtype']=="Debit/Credit Note"]
df['new_acc2'] = [str(5001) if 'Sundry Debtors' in j['G/L Acct Long Text'] else j['new_acc'] for i, j in df.iterrows()]
# df['new_acc2'] = [str(5001) if 'Sundry Creditors' in j['G/L Acct Long Text'] else j['new_acc'] for i, j in df.iterrows()]


with open('coa_details_CHIKHALI.json', 'r') as f:
    account_ids_data = json.load(f)


with open('BRANCH.json', 'r') as f:
    branch_ids_data = json.load(f)


# print(df)
# Create a list to store the journal entries
journal_entries = []

# Group the DataFrame by continuous Document Numbers
grouped = df.groupby((df['Document Number'] != df['Document Number'].shift()).cumsum())

nm=1
null_acc=[]
# Iterate through the groups and create the journal entries
for _, group in grouped:
    # Create a list to store line items for this journal entry
    line_items = []
    for _, row in group.iterrows():
        amount = abs(row['Amount in local currency'])
        debit_or_credit = 'credit' if row['Amount in local currency'] < 0 else 'debit'
        # account_code = str(int(row['new_acc']))
        account_code = str(int(row["new_acc2"]))
        account_id = account_ids_data.get(account_code)
        description = row["Text"]
        branch_code = str(int(row['Profit Center']))
        branch_id = branch_ids_data.get(branch_code)
        # print(account_id)
        if account_id == None:
            null_acc.append(account_code)
        line_items.append({ 
                'amount': amount,
                'debit_or_credit': debit_or_credit,
                "description": description,
                'account_id': account_id
        })

    # Get journal_date, notes, and reference_number for this journal entry
    journal_date = str(group['Posting Date'].iloc[0].strftime('%Y-%m-%d'))
    


    # Create the journal entry for this group
    journal_entry = {

        "id_from_qb": str(nm),
        "journal_number_prefix": "2019-",
        "journal_number_suffix": str(int(float(row["Document Number"]))),
        "journal_date": journal_date,
        "branch_id": branch_id,
        "notes": row["Text"],
        # "reference": row["Customer Name"],
        "reference_number": row["Reference"],
        "line_items": line_items,
        "custom_fields": [{
                        "label" : "SAP Document No",
                        "value" : str(int(float(row["Document Number"])))
                    },
                    {
                        "label" : "Document Date",
                        "value" : str(row["Document Date"])[ :10]
                    }
                    ],

    }

    # Append the journal entry to the list of journal entries
    journal_entries.append(journal_entry)
    nm=nm+1
# Convert the result to a JSON string
json_output = json.dumps(journal_entries, indent=4)

with open("mapped_journal_2019_D_C_note.json", "w") as outfile:
    outfile.write(json_output)

print(np.unique(null_acc))
# pd.DataFrame({"acc":null_acc}).to_csv('miss_coa_mbl.csv')