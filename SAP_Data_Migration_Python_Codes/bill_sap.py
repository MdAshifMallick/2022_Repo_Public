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

df=df[df['Interbranch'].str.contains("Regular")]
df=df[df['Type']=="Creditors"]
df=df[df['Subtype']=="Invoice/Bill"]
df['Document Number']=[int(float(i['Document Number'])) for _,i in df.iterrows()]
# df=df[df['Amount in local currency'] < 0]
# df=df[df['G/L Acct Long Text'].str.contains("Sundry Creditors")]

doc_num_count = {}

# Define a function to generate the "new_doc" value
def generate_new_doc(doc_num):
    count = doc_num_count.get(doc_num, 0) + 1
    doc_num_count[doc_num] = count
    return f"{doc_num}{chr(ord('a') + count - 1)}" if count > 1 else str(doc_num)

# Apply the function to create the "new_doc" column
df['new_doc'] = df['Document Number'].apply(generate_new_doc)


# df=df.groupby('Document Number').filter(lambda x: x['Profit Center'].nunique() == 1)
df1=df[~df['G/L Acct Long Text'].str.contains("Sundry Creditors")]
df2=df[df['G/L Acct Long Text'].str.contains("Sundry Creditors")]
# df=df[df['G/L Account']!=731720]
# df=df.groupby('Document Number').filter(lambda x: x['Profit Center'].nunique() == 1)



with open('coa_details_CHIKHALI.json', 'r') as f:
    account_ids_data = json.load(f)


with open('BRANCH.json', 'r') as f:
    branch_ids_data = json.load(f)

with open('contact_details_CHIKHALI.json', 'r') as f:
    vendor_ids_data = json.load(f)

vendor_code=[i['Vendor'] for _,i in df2.iterrows()]
doc_num=[i['Document Number'] for _,i in df2.iterrows()]
# print(df)
# Create a list to store the journal entries
journal_entries = []

# Group the DataFrame by continuous Document Numbers
# grouped = df1.groupby((df1['new_doc'] != df1['new_doc'].shift()).cumsum())
grouped = df1.groupby((df1['Document Number'] != df1['Document Number'].shift()).cumsum())

nm=1
null_acc=[]
# Iterate through the groups and create the journal entries
for _, group in grouped:
    # Create a list to store line items for this journal entry
    line_items = []
    # first_assignment = group.iloc[0]['Assignment']
    # skip_first_row = True
    # first_row_processed = False
    for _, row in group.iterrows():
        # if skip_first_row:
        #     skip_first_row = False
        #     continue
        # if first_row_processed:
        #     break
        print(row['Document Number'])
        amount =(row['Amount in local currency'])
        # debit_or_credit = 'credit' if row['Amount in local currency'] < 0 else 'debit'
        account_code = str(int(row['new_acc']))
        account_id = account_ids_data.get(account_code)
        description = row["new_acc_text"]
        notes = row["Text"]
        # name=row["new_acc_text"]
        branch_code = str(int(row['Profit Center']))
        branch_id = branch_ids_data.get(branch_code)
        # vendor_id=vendor_ids_data.get(str(int(row['Vendor'])))
        vendor_id=vendor_ids_data.get(str(int(vendor_code[doc_num.index(row['Document Number'])])))
        if vendor_id == None:
            null_acc.append(str(int(vendor_code[doc_num.index(row['Document Number'])])))
        # print(account_id)
        line_items.append({ 
                'rate': amount,
                # "name": name,
                # 'debit_or_credit': debit_or_credit,
                "description": description,
                'account_id': account_id,
                'gst_treatment_code': 'out_of_scope'
        })

    # Get journal_date, notes, and reference_number for this journal entry
    bill_date = str(group['Posting Date'].iloc[0].strftime('%Y-%m-%d'))
    
# for _, row in df.iterrows():

    # Create the journal entry for this group
    journal_entry = {

        "id_from_qb": str(nm),
        # "bill_number": "2017-"+str(row["new_doc"]),
        "bill_number": "2019-"+str(int(float(row["Document Number"]))),
        # "vendor_id": vendor_ids_data.get(str(int(row['Assignment']))),
        # "date": str(row['Posting Date'].strftime('%Y-%m-%d')),
        "vendor_id": vendor_id,
        "date": bill_date,
        "notes":notes,
        # "branch_id": branch_ids_data.get(str(int(row["Profit Center"]))),
        "branch_id": branch_id,
        "reference_number": row["Reference"],
        "line_items": line_items,
        # "line_items":[{'rate': abs(row["Amount in local currency"]),
        #         # "name": row['G/L Acct Long Text'],
        #         # 'debit_or_credit': debit_or_credit,
        #         "description": 'Sub-Contracting charges Road Work',
        #         'account_id': 1279300000000016874,
        #         'gst_treatment_code': 'out_of_scope'

        # }],
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
    # if vendor_ids_data.get(str(int(row["Assignment"]))) == None:
    #     null_acc.append(row["Assignment"])
    # Append the journal entry to the list of journal entries
    journal_entries.append(journal_entry)
    nm=nm+1

    # first_row_processed = True
# Convert the result to a JSON string
json_output = json.dumps(journal_entries, indent=4)

with open("mapped_bills_2019_Inv_Bill.json", "w") as outfile:
    outfile.write(json_output)

print(np.unique(null_acc))