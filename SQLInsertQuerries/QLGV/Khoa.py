import pandas as pd
from pathlib import Path
from datetime import datetime

def Khoa(sql_version:int):
    path=str(Path(__file__).resolve())
    path=path.replace('.py','.xlsx')
    print(path)

    data =pd.read_excel(path)
    df=pd.DataFrame(data)

    SQLQuerries=''

    for i in df.index:
        makhoa=df.iloc[i][0]
        tenkhoa=df.iloc[i][1]
        ngtlap=df.iloc[i][2]
        if type(ngtlap)==str:
            ngtlap=datetime.strptime(ngtlap, '%d/%m/%Y')
        print (ngtlap)
        trgkhoa=df.iloc[i][3]
        if sql_version==1:
            SQLQuerries=SQLQuerries + "insert into KHOA(MAKHOA, TENKHOA, NGTLAP, TRGKHOA) values ('{}','{}','{}','{}')\n".format(makhoa, tenkhoa, ngtlap.date(), trgkhoa)
        elif sql_version==2:
            SQLQuerries=SQLQuerries + "insert into KHOA(ma_khoa, ten_khoa, ng_tlap, tr_khoa) values ('{}','{}','{}','{}');\n".format(makhoa, tenkhoa, ngtlap.date(), trgkhoa)

    print(SQLQuerries)
    return SQLQuerries
