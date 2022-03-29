from DieuKien import DieuKien
from GiangDay import GiangDay
from GiaoVien import GiaoVien
from HocVien import HocVien
from KetQuaThi import KetQuaThi
from Khoa import Khoa
from Lop import Lop
from MonHoc import MonHoc

f=open('QLGV.txt','a')
f.truncate(0)
f.write(Khoa()+'\n')
f.write(MonHoc()+'\n')
f.write(DieuKien()+'\n')
f.write(GiaoVien()+'\n')
f.write(Lop()+'\n')
f.write(HocVien()+'\n')
f.write(GiangDay()+'\n')
f.write(KetQuaThi()+'\n')



f.close()