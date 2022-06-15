from DieuKien import DieuKien
from GiangDay import GiangDay
from GiaoVien import GiaoVien
from HocVien import HocVien
from KetQuaThi import KetQuaThi
from Khoa import Khoa
from Lop import Lop
from MonHoc import MonHoc
from numpy import array

valid_sql_version=array([1,2])
print(type(valid_sql_version[0]))
sql_version=0

f=open('QLGV.txt','a')
f.truncate(0)
while sql_version not in valid_sql_version:
    sql_version=input("Enter your sql management system: \n 1: SQLServer \n 2: Oracle \n")
    if (type(sql_version)!=int):
        sql_version=int(sql_version)

f.write(Khoa(sql_version)+'\n')
f.write(MonHoc(sql_version)+'\n')
f.write(DieuKien(sql_version)+'\n')
f.write(GiaoVien(sql_version)+'\n')
f.write(Lop(sql_version)+'\n')
f.write(HocVien(sql_version)+'\n')
f.write(GiangDay(sql_version)+'\n')
f.write(KetQuaThi(sql_version)+'\n')



f.close()