import pandas as pd
from pathlib import Path
from datetime import datetime

def DieuKien(sql_version:int):
    path=str(Path(__file__).resolve())
    path=path.replace('.py','.xlsx')
    print(path)

    data =pd.read_excel(path)
    df=pd.DataFrame(data)

    SQLQuerries=''

    for i in df.index:
        mamh=df.iloc[i][0]
        mamh_truoc=df.iloc[i][1]
        if sql_version==1:
            SQLQuerries=SQLQuerries + "insert into DIEUKIEN(MAMH, MAMH_TRUOC) values ('{}','{}')\n".format(mamh, mamh_truoc)
        elif sql_version==2:
            SQLQuerries=SQLQuerries + "insert into DIEUKIEN(ma_mh, ma_mh_truoc) values ('{}','{}');\n".format(mamh, mamh_truoc)

    print(SQLQuerries)
    return SQLQuerries





