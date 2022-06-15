import pandas as pd
from pathlib import Path
from datetime import datetime

def KetQuaThi(sql_version:int):
    path=str(Path(__file__).resolve())
    path=path.replace('.py','.xlsx')
    print(path)

    data =pd.read_excel(path)
    df=pd.DataFrame(data)

    SQLQuerries=''

    for i in df.index:
        mahv=df.iloc[i][0]
        mamh=df.iloc[i][1]
        lt=df.iloc[i][2]
        ngthi=df.iloc[i][3]
        if type(ngthi)==str:
            ngthi=datetime.strptime(ngthi, '%d/%m/%Y')
        diem=df.iloc[i][4]
        ketqua=df.iloc[i][5]
        if sql_version==1:
            SQLQuerries=SQLQuerries + "insert into KETQUATHI(MAHV, MAMH, LANTHI, NGTHI, DIEM, KQUA) values ('{}','{}',{} , '{}',{},'{}')\n".format(mahv, mamh, lt, ngthi.date(),diem, ketqua)
        elif sql_version==2:
            SQLQuerries=SQLQuerries + "insert into KETQUATHI(ma_hv, ma_mh, lan_thi, ng_thi, diem, kqua) values ('{}','{}',{} , '{}',{},'{}');\n".format(mahv, mamh, lt, ngthi.date(),diem, ketqua)

    print(SQLQuerries)
    return SQLQuerries


