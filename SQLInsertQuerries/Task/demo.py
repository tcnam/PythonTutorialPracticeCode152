import glob
import pandas as pd
from pathlib import Path
from datetime import datetime
import pprint
import os

def getTableName(currentName:str):
    result=currentName.split("_")[-2]
    return result

def isHist(currentName:str):
    result=currentName.split("_")[1]
    if result=='HIST':
        return True
    else:
        return False

print(isHist('V_HIST_ANEK_G0'))
data2 =pd.read_excel(r'demo1.xlsx', engine='openpyxl')
df2=pd.DataFrame(data2)

#print(df2)

area_dict=df2.set_index('id')['filter'].to_dict()
pp=pprint.PrettyPrinter()
#pp.pprint(area_dict)

dir_path=os.path.dirname(os.path.realpath(__file__))
all_tsv_file_path=glob.glob(os.path.join(dir_path,"*.tsv"))
df_from_each_file=(pd.read_csv(f,sep='\t') for f in all_tsv_file_path)
concatenated_df=pd.concat(df_from_each_file, ignore_index=True)
#print(concatenated_df)


synonym_names=[]
for i in concatenated_df.index:
    synonym_name=concatenated_df.iloc[i][0]
    #print(synonym_name)
    if synonym_name not in synonym_names:
        synonym_names.append(synonym_name)

# for synonym_name in synonym_names:
#     print(getTableName(synonym_name))

f=open('Task.txt','a')
f.truncate(0)

index=0
for synonym_name in synonym_names:
    create_view_command='select\n\t'
    for i in range(index,len(concatenated_df)):
        synonym_name_2=concatenated_df.iloc[i][0]
        collumn_name=concatenated_df.iloc[i][1]
        owner=concatenated_df.iloc[i][2]
        if synonym_name_2!=synonym_name:
            #print(synonym_name_2)
            #print('number of collumns:'+str(i-index))
            index=i
            #print(index)
            create_view_command=create_view_command+'from\n\t'+owner+'.'+synonym_name
            #print(getTableName(synonym_name))
            for key in area_dict.keys():
                if getTableName(synonym_name)==key:
                    create_view_command=create_view_command+'\n where \n\t'+area_dict[key]
                    if isHist(synonym_name)==True:
                        create_view_command=create_view_command+"\n\t or tech_dml_flag = 'D'"
                    break
                
            print(create_view_command)
            f.write(create_view_command+'\n')
            break
        
        create_view_command=create_view_command+collumn_name+',\n\t'
        if i+1==len(concatenated_df):
            index=i+1
            create_view_command=create_view_command+'from\n\t'+owner+'.'+synonym_name
            #print(getTableName(synonym_name))           
            for key in area_dict.keys():
                if getTableName(synonym_name)==key:
                    create_view_command=create_view_command+'\n where \n\t'+area_dict[key]
                    if isHist(synonym_name)==True:
                        create_view_command=create_view_command+"\n\t or tech_dml_flag = 'D'"
                    break
            print(create_view_command)
            f.write(create_view_command+'\n')

f.close()
            
    #print('lenh da bi break tai vi tri '+str(index))




        


