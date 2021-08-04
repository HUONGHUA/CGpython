 # -*- coding: utf-8 -*-
# Chuỗi trần : Thêm chữ r trước chuỗi 

strA = "Hưa Thanh "
strB = " Hường"
strC = " 1990 "
strD = strA + "\t" + strB + "\t" + strC*5
print(r'Haizz, \nếu 1 ngày nào đó')
print(strD)
#in : Khi sử dụng bạn chỉ nhận được 1 trong 2 kết quả : True or False

strE = "g"
strG = strB in strB
print(strG)

# a b c _ x y z
# 0 1 2 3 4 5 6

# [] lay so thu tu trong o vuong / chi chap nhan so nguyen
strF = strC[2]
print(strF)
strH = strC[-2]
print(strH)

#ham  Len : lay ra phan tu cuoi cung cua chuoi
 
strK = strC[len(strC) - 3]
print(strK)

# Cắt chuỗi : strL = strC[a:b] Laays chuoi tu a to B
strL = strC[1:3]
strQ = strA[1:len(strA)]
strW = strA[1:None]

print(strQ)
print(strL)
print(strW)
# Cawts tu Phai? sang trai  strA = StrB[a:b:c] 
# a la tu dau , b la cuoi , c la buoc nhay
strR = strA[None:5:2]
print(strR)

# Biến chữ thành số / Số thành chữ
strA1 = "69" + "5"
strA2 = 69 + 5
print(strA1)
print(strA2)
# Ep kieu
strA3 = int("69") + 5
print(strA3)
strA4 = float("6.9")
print(strA4)
print(int(6.9))
# int(6.9) : Lay phan nguyen
# Số thành chuỗi 
strA5 = str(69) + "5"
print(strA5)

# THay đổi giá tri
strB1 = "HUATHANHHUONG"

strB1 = strB1[None:10] + "0" + strB1[11:None]
print(hash(strB1))

