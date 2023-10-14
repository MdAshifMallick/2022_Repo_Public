import pandas as pd
import numpy as np
import json




df = pd.read_excel('6010_2018-19_Output.xlsx', sheet_name='Output')
df = df[(df['G/L Account'].notnull())]
df=df[df['Interbranch'].str.contains("Regular")]
df=df[df['Type']=="Debtors"]
df=df[df['Subtype']=="Debit/Credit Note"]
df=df[~df['G/L Acct Long Text'].str.contains("Sundry Debtors")]
# df=df[df['Partner Profit Ctr'].str.contains("inv")]

# df=df.groupby('Document Number').filter(lambda x: x['Profit Center'].nunique() == 1)



with open('coa_details_mbl.json', 'r') as f:
    account_ids_data = json.load(f)


with open('BRANCH.json', 'r') as f:
    branch_ids_data = json.load(f)

with open('contact_details_mbl.json', 'r') as f:
    cus_ids_data = json.load(f)


# print(df)
# Create a list to store the journal entries
journal_entries = []

# Group the DataFrame by continuous Document Numbers
grouped = df.groupby((df['Document Number'] != df['Document Number'].shift()).cumsum())

nm=1
null_acc=[]
null_cus=[]
# Iterate through the groups and create the journal entries
for _, group in grouped:
    # Create a list to store line items for this journal entry
    line_items = []
    for _, row in group.iterrows():
        amount = (row['Amount in local currency'])
        # debit_or_credit = 'credit' if row['Amount in local currency'] < 0 else 'debit'
        account_code = str(int(row['new_acc']))
        account_id = account_ids_data.get(account_code)
        notes = row["Text"]
        description=row["new_acc_text"]
        branch_code = str(int(row['Profit Center']))
        branch_id = branch_ids_data.get(branch_code)
        cus_code=str((row['Customer']))
        cus_id=cus_ids_data.get(cus_code)
        # print(account_id)
        if account_id == None:
            null_acc.append(account_code)
        if cus_id == None:
            null_cus.append(cus_code)
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
    


    # Create the journal entry for this group
    journal_entry = {

        "id_from_qb": str(nm),
        "customer_id": cus_id,
        "creditnote_number": "2018-"+str(row["Document Number"]),
        "reference_invoice_type": "registered",
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

with open("mapped_credit_2018_D_Debit_Credit Note.json", "w") as outfile:
    outfile.write(json_output)

print(np.unique(null_acc))
print(np.unique(null_cus))