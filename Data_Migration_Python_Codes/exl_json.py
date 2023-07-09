import pandas
import json
from datetime import datetime

# Read excel document


# read the CSV file with date parsing and format change

# excel_data_df = pandas.read_csv('ven_Credit_20.21.csv',encoding='latin',parse_dates=['Vendor Credit Date'])
excel_data_df = pandas.read_csv('expenses 1_download_19.05.23.csv',parse_dates=['Date','Due date'],dayfirst=True)
# excel_data_df = pandas.read_excel('expenses 1_download_19.05.23.xlsx',sheet_name='bill',parse_dates=['Date'])
excel_data_df['Date']=pandas.to_datetime(excel_data_df['Date']).dt.strftime('%Y-%m-%d')
excel_data_df['Due date']=pandas.to_datetime(excel_data_df['Due date']).dt.strftime('%Y-%m-%d')
# excel_data_df = pandas.read_csv('Vendor_Payment.csv')
# excel_data_df = pandas.read_excel('Vendor_Payment.xlsx',sheet_name='VendorPayments')
# Convert excel to string 
# (define orientation of document in this case from up to down)
thisisjson = excel_data_df.to_json(orient='records')

# Print out the result
print('Excel to JSON:\n', thisisjson)

# Make the string into a list to be able to input in to a JSON-file
thisisjson_dict = json.loads(thisisjson)

# Define file to write to and 'w' for write option -> json.dump() 
# defining the list to write from and file to write to
with open('bill_19.05.23.json', 'w') as json_file:
    json.dump(thisisjson_dict, json_file,indent=2)
