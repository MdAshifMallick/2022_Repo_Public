import pandas as pd
import numpy as np
import json




df = pd.read_excel('6012 2019-20_Output.xlsx', sheet_name='Full Output')
df = df[(df['G/L Account'].notnull())]
df['Document Number']=[int(float(i['Document Number'])) for _,i in df.iterrows()]
df=df[df['Interbranch'].str.contains("Regular")]
df=df[df['Type']=="Debtors"]
df=df[df['Subtype']=="Debit/Credit Note"]
df=df[df['Amount in local currency'] > 0]
df1=df[df['G/L Acct Long Text'].str.contains("Sundry Debtors")]
df2=df[df['G/L Acct Long Text'].str.contains("Sundry Debtors")]
doc_num_count = {}

# Define a function to generate the "new_doc" value
def generate_new_doc(doc_num):
    count = doc_num_count.get(doc_num, 0) + 1
    doc_num_count[doc_num] = count
    return f"{doc_num}{chr(ord('a') + count - 1)}" if count > 1 else str(doc_num)

# Apply the function to create the "new_doc" column
df1['new_doc'] = df1['Document Number'].apply(generate_new_doc)
# df=df[df['Partner Profit Ctr'].str.contains("inv")]

# df=df.groupby('Document Number').filter(lambda x: x['Profit Center'].nunique() == 1)

customer_code=[i['Customer'] for _,i in df2.iterrows()]
doc_num=[i['Document Number'] for _,i in df2.iterrows()]

with open('coa_details_CHIKHALI.json', 'r') as f:
    account_ids_data = json.load(f)


with open('BRANCH.json', 'r') as f:
    branch_ids_data = json.load(f)

with open('contact_details_CHIKHALI.json', 'r') as f:
    cus_ids_data = json.load(f)


# print(df)
# Create a list to store the journal entries
journal_entries = []

# Group the DataFrame by continuous Document Numbers
# grouped = df1.groupby((df1['Document Number'] != df1['Document Number'].shift()).cumsum())
grouped = df1.groupby((df1['new_doc'] != df1['new_doc'].shift()).cumsum())

nm=1
null_acc=[]
null_acc2=[]
# Iterate through the groups and create the journal entries
for _, group in grouped:
    # Create a list to store line items for this journal entry
    line_items = []
    for _, row in group.iterrows():
        print(row['new_doc'],row['Document Number'])
        amount = abs(row['Amount in local currency'])
        # debit_or_credit = 'credit' if row['Amount in local currency'] < 0 else 'debit'
        account_code = str((row['new_acc']))
        account_id = account_ids_data.get(account_code)
        notes = row["Text"]
        description=row["new_acc_text"]
        branch_code = str(int(row['Profit Center']))
        branch_id = branch_ids_data.get(branch_code)
        cus_id=cus_ids_data.get(str(int(customer_code[doc_num.index(row['Document Number'])])))
        if cus_id == None:
            null_acc2.append(str(int(customer_code[doc_num.index(row['Document Number'])])))
        # print(account_id)
        if account_id == None:
            null_acc.append(account_code)
        line_items.append({ 
                'rate': amount,
                # "name": name,
                # 'debit_or_credit': debit_or_credit,
                "description": description,
                'account_id': 1497702000000028551,
                'gst_treatment_code': 'out_of_scope'
        })

    # Get journal_date, notes, and reference_number for this journal entry
    bill_date = str(group['Posting Date'].iloc[0].strftime('%Y-%m-%d'))
    


    # Create the journal entry for this group
    journal_entry = {

        "id_from_qb": str(nm),
        "customer_id": cus_id,
        # "invoice_number": "2019-"+str(row["Document Number"]),
        "invoice_number": "2019-"+str(row["new_doc"]),
        "date": bill_date,
        "branch_id": branch_id,
        "reference_number": row["Reference"],
        "notes": notes,
        "line_items": line_items,
        "custom_fields": [{
                        "label" : "SAP Document No",
                        "value" : row["Document Number"]
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

with open("mapped_inv_2019_D_C_note.json", "w") as outfile:
    outfile.write(json_output)

print(np.unique(null_acc))
print(np.unique(null_acc2))