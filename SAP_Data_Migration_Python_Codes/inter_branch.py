import pandas as pd
import numpy as np
import json


# Read the Excel file into a DataFrame
df = pd.read_excel('6010 - 2017-18 Breakup 1.xlsx', sheet_name='JV')
df = df[df['G/L Account'].notnull()]
# print(df[['Assignment']])
# Group the DataFrame by 'document number' and filter groups with unequal 'profit center' values
filtered_df = df.groupby('Document Number').filter(lambda x: x['Profit Center'].nunique() > 1)

# Print the filtered DataFrame
filtered_df['Document Number'].to_excel('MBL_2017-18_JV_Branch.xlsx')