import pandas as pd
from pathlib import Path
from datetime import datetime

def GiaoVien():
    path=str(Path(__file__).resolve())
    path=path.replace('.py','.xlsx')
    print(path)

    data =pd.read_excel(path)
    df=pd.DataFrame(data)

    SQLQuerries=''

    for i in df.index:
        magv=df.iloc[i][0]
        hoten=df.iloc[i][1]
        hocvi=df.iloc[i][2]
        hocham=df.iloc[i][3]
        gioitinh=df.iloc[i][4]
        ngsinh=df.iloc[i][5]
        if type(ngsinh)==str:
            ngsinh=datetime.strptime(ngsinh, '%d/%m/%Y')
        ngvl=df.iloc[i][6]
        if type(ngvl)==str:
            ngvl=datetime.strptime(ngvl, '%d/%m/%Y')
        heso=df.iloc[i][7]
        mucluong=df.iloc[i][8]
        makhoa=df.iloc[i][9]
        SQLQuerries=SQLQuerries + "insert into GIAOVIEN(MAGV, HOTEN, HOCVI, HOCHAM, GIOITINH, NGSINH, NGVL, HESO, MUCLUONG, MAKHOA) values ('{}','{}','{}','{}','{}','{}','{}',{},{},'{}')\n".format(magv, hoten, hocvi, hocham,gioitinh, ngsinh.date(), ngvl.date() ,heso, mucluong, makhoa)

    print(SQLQuerries)
    return SQLQuerries

