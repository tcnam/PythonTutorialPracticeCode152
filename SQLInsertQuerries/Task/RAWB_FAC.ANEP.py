import glob
import pandas as pd
from pathlib import Path
from datetime import datetime
import pprint
import os

def getTableName(currentName:str):
    result=currentName.split(".")[-1]
    result=result.split("_")[-1]
    return result

data2 =pd.read_excel(r'demo1.xlsx', engine='openpyxl')
df2=pd.DataFrame(data2)

#print(df2)

area_dict=df2.set_index('id')['filter'].to_dict()
pp=pprint.PrettyPrinter()
#pp.pprint(area_dict)

dir_path=os.path.dirname(os.path.realpath(__file__))
print(dir_path)
all_tsv_file_path=glob.glob(os.path.join(dir_path,"*.tsv"))
df_from_each_file=(pd.read_csv(f,sep='\t') for f in all_tsv_file_path)
concatenated_df=pd.concat(df_from_each_file, ignore_index=True)
print(concatenated_df)




# path2=str(Path(__file__).resolve())
# path2=path2.replace('.py','.tsv')
# print(path2)
#print(path);

# data =pd.read_csv(path, sep='\t')
# df=pd.DataFrame(data)

table_names=[]
for i in concatenated_df.index:

    table_name=concatenated_df.iloc[i][0]
    #print(table_name)
    if table_name not in table_names:
        table_names.append(table_name)
print(table_names)
index=0
# for table_name in table_names:
#     create_view_command='select\n\t'
#     for i in range(index,len(concatenated_df)):
#         table_name_2=concatenated_df.iloc[i][0]
#         collumn_name=concatenated_df.iloc[i][1]
#         owner=concatenated_df.iloc[i][2]
#         if table_name_2!=table_name:
#             print(table_name_2)
#             print('number of collumns:'+str(i-index))
#             index=i
#             print(index)
#             create_view_command=create_view_command+'from\n\t'+owner+'.'+table_name
#             print(getTableName(table_name))
#             print(create_view_command)
#             for key in area_dict.keys():
#                 if getTableName(table_name)==key:
#                     print(area_dict[key])
#             break
#         create_view_command=create_view_command+collumn_name+',\n\t'
#         if i+1==len(concatenated_df):
#             index=i+1
#             create_view_command=create_view_command+'from\n\t'+owner+'.'+table_name
#             print(getTableName(table_name))
#             print(create_view_command)
#             for key in area_dict.keys():
#                 if getTableName(table_name)==key:
#                     print(area_dict[key])
            


#     print('lenh da bi break tai vi tri '+str(index))




        


