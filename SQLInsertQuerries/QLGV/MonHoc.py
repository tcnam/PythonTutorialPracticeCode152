import pandas as pd
from pathlib import Path
from datetime import datetime

def MonHoc(sql_version:int):
    path=str(Path(__file__).resolve())
    path=path.replace('.py','.xlsx')
    print(path)

    data =pd.read_excel(path)
    df=pd.DataFrame(data)

    SQLQuerries=''

    for i in df.index:
        mamh=df.iloc[i][0]
        tenmh=df.iloc[i][1]
        tclt=df.iloc[i][2]
        tcth=df.iloc[i][3]
        makhoa=df.iloc[i][4]
        if sql_version==1:
            SQLQuerries=SQLQuerries + "insert into MONHOC(MAMH, TENMH, TCLT, TCTH, MAKHOA) values ('{}','{}',{} , {},'{}')\n".format(mamh, tenmh, tclt, tcth,makhoa)
        elif sql_version==2:
            SQLQuerries=SQLQuerries + "insert into MONHOC(ma_mh, ten_mh, tclt, tcth, ma_khoa) values ('{}','{}',{} , {},'{}');\n".format(mamh, tenmh, tclt, tcth,makhoa)

    print(SQLQuerries)
    return SQLQuerries

