import pandas as pd
from pathlib import Path
from datetime import datetime

def HocVien(sql_version:int):
    path=str(Path(__file__).resolve())
    path=path.replace('.py','.xlsx')
    print(path)

    data =pd.read_excel(path)
    df=pd.DataFrame(data)

    SQLQuerries=''

    for i in df.index:
        mahv=df.iloc[i][0]
        ho=df.iloc[i][1]
        ten=df.iloc[i][2]
        ngsinh=df.iloc[i][3]
        if type(ngsinh)==str:
            ngsinh=datetime.strptime(ngsinh, '%d/%m/%Y')
        gioitinh=df.iloc[i][4]
        noisinh=df.iloc[i][5]
        malop=df.iloc[i][6]
        if sql_version==1:
            SQLQuerries=SQLQuerries + "insert into HOCVIEN(MAHV, HO, TEN, NGSINH, GIOITINH, NOISINH, MALOP) values ('{}','{}','{}','{}','{}','{}','{}')\n".format(mahv, ho, ten, ngsinh.date(),gioitinh, noisinh, malop )
        elif sql_version==2:
            SQLQuerries=SQLQuerries + "insert into HOCVIEN(ma_hv, ho, ten, ng_sinh, gioi_tinh, noi_sinh, ma_lop) values ('{}','{}','{}','{}','{}','{}','{}');\n".format(mahv, ho, ten, ngsinh.date(),gioitinh, noisinh, malop )

    print(SQLQuerries)
    return SQLQuerries
