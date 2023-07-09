# import pandas
# import json

# def js_r(filename: str):
#     with open(filename) as f_in:
#         return json.load(f_in)

# if __name__ == "__main__":
#     my_data = js_r('mapped_active_geo111.json')

# dis_itr=[]
# for i in my_data['Customer']:
    
#     dis_itr.append(i['contact_name'])

# # print(dis_itr)
# print(len(my_data['Customer']))
# print(len(dis_itr))
# df=pandas.read_csv('Contacts (5).csv')

# for val in dis_itr:
#     if val in df['Display Name'].values:
#         del my_data['Customer'][dis_itr.index(val)]
#     else:
#         print(val)

# print(len(my_data['Customer']))

import pandas
import json

def js_r(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)

if __name__ == "__main__":
    my_data = js_r('mapped_active_geo111.json')

dis_itr=[]
for i in my_data['Customer']:
    
    dis_itr.append(i['contact_name'])

# print(dis_itr)
print(len(my_data['Customer']))
print(len(dis_itr))
df=pandas.read_csv('Contacts (5).csv')

# emp=[]
# for j in df['Display Name'].values:
#     if j in dis_itr:
#         emp.append(j)
# print(len(emp))

for m,n in enumerate(my_data['Customer']):
    print(n['contact_name'])
    if n['contact_name'] in df['Display Name'].values:
        del my_data['Customer'][m]
    else:
        print(m)

print(len(my_data['Customer']))
