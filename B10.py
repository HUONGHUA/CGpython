# -*- coding : utf-8 -*-

a = 'hua Thanh huong'

print(type(a))
a1 = a.capitalize()
print(a1)
# capitalize() Viet Hoa dauf tien cua tu
a2 = a.upper()
#upper la Viet Hoa ca cau
print(a2)
a3 = a.lower()
#lower : viet thuong ca cau
#swapcase : viet thuong thanh hoa , hoa thanh thuong
#title : Viet Hoa dau tien cuar tuwf

a4 = a.title()
print(a4)
#center(width,[fillchar]) : Nam giua cac o hien thi
#rjust(,) : Cang phai
#ljust(,) cang trai
a5 = a.center(50 , '*')
print(a5)
b = a.encode(encoding='utf-8' , errors='strict')
print(b)
# Encode : mã hoá
d = a.join(['1','2','3'])
print(d)
e = a.replace('hua',"NGUYEN")
print(e)
#REPLAYCE : thay the chuoi 
f = a.strip('g')
# Cat 2 dau co trong nội dung
# rstrip : cắt phải
# lstrip : Căt trái

print(f)

