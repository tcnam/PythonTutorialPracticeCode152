import pandas as pd
from pathlib import Path
from datetime import datetime

def Lop():
    path=str(Path(__file__).resolve())
    path=path.replace('.py','.xlsx')
    print(path)

    data =pd.read_excel(path)
    df=pd.DataFrame(data)

    SQLQuerries=''

    for i in df.index:
        malop=df.iloc[i][0]
        tenlop=df.iloc[i][1]
        trglop=df.iloc[i][2]
        siso=df.iloc[i][3]
        magvcn=df.iloc[i][4]
        SQLQuerries=SQLQuerries + "insert into LOP(MALOP, TENLOP, TRGLOP, SISO, MAGV) values ('{}','{}','{}', {},'{}')\n".format(malop, tenlop, trglop, siso,magvcn)

    print(SQLQuerries)
    return SQLQuerries

