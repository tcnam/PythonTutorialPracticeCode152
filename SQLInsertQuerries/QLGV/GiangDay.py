import pandas as pd
from pathlib import Path
from datetime import datetime

def GiangDay():
    path=str(Path(__file__).resolve())
    path=path.replace('.py','.xlsx')
    print(path)

    data =pd.read_excel(path)
    df=pd.DataFrame(data)

    SQLQuerries=''

    for i in df.index:
        malop=df.iloc[i][0]
        mamh=df.iloc[i][1]
        magv=df.iloc[i][2]
        hocky=df.iloc[i][3]
        nam=df.iloc[i][4]
        tungay=df.iloc[i][5]
        if type(tungay)==str:
            tungay=datetime.strptime(tungay, '%d/%m/%Y')
        denngay=df.iloc[i][6]
        if type(denngay)==str:
            denngay=datetime.strptime(denngay, '%d/%m/%Y')
        SQLQuerries=SQLQuerries + "insert into GIANGDAY(MALOP, MAMH, MAGV, HOCKY, NAM, TUNGAY, DENNGAY) values ('{}','{}','{}',{},{}, '{}','{}')\n".format(malop, mamh, magv, hocky,nam, tungay.date(), denngay.date())

    print(SQLQuerries)
    return SQLQuerries


