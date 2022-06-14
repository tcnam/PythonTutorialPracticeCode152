import pandas as pd
from pathlib import Path
from datetime import datetime
import pprint

data2 =pd.read_excel(r'demo1.xlsx', engine='openpyxl')
df2=pd.DataFrame(data2)

print(df2)

area_dict=df2.set_index('id')['filter'].to_dict()
pp=pprint.PrettyPrinter()
pp.pprint(area_dict)


# path=str(Path(__file__).resolve())
# path=path.replace('.py','.tsv')
# #print(path);

# data =pd.read_csv(path, sep='\t');
# df=pd.DataFrame(data)

# table_names=[]
# for i in df.index:

#     table_name=df.iloc[i][0]
#     #print(table_name)
#     if table_name not in table_names:
#         table_names.append(table_name)

# index=0
# for table_name in table_names:
#     create_view_command='select\n\t'
#     for i in range(index,len(df)):
#         table_name_2=df.iloc[i][0]
#         collumn_name=df.iloc[i][1]
#         owner=df.iloc[i][2]
#         if table_name_2!=table_name:
#             #print(table_name_2)
#             #print('number of collumns:'+str(i-index))
#             index=i
#             print(index)
#             create_view_command=create_view_command+'from\n\t'+owner+'.'+table_name
#             print(create_view_command)
#             break
#         create_view_command=create_view_command+collumn_name+',\n\t'
#         if i+1==len(df):
#             index=i+1
#             create_view_command=create_view_command+'from\n\t'+owner+'.'+table_name
#             print(create_view_command)


#     #print('lenh da bi break tai vi tri '+str(index))

        


