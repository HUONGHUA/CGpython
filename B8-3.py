# e = ''
a = 'My team is %s'%('Huong HUA')
print(a)
a1 = 'My nam is %s  Thanh Huong'%('HUA')
print(a1)
a2 = 'My Name is %s %s Huong'%('Hua' , 'Thanh')
print(a2)
s = '%s %s'
s1 = s %('D','2')
print(s1)
f = '%.0f' %(3.84219)
print(f)
#Chuoi F (f-string)
f1 =  f'HuaThanhHuong'
print(f1)
print(f'Hua\tThanh\tHuong')
HTH = 'HUA THANH HUONG'
result = f' {HTH} - Xin chao cacs ban'
# Timf bien HTH =
print(result)

Name = 'Tinh'
Adress = 'ĐÀ NẴNg'
Phone = '0935'
Level = '12'

THONGTIN = f'Student: {{Name}} \n Adress : {Adress} \n Phone :  {Phone} \n Level : {Level}'
print(THONGTIN)

# Hàm f = ' a:{a} , b: {b} ,.....'

# {{}} : Ham chua dinh dang
b = 'b1: {1},b2: {2},b3 : {0}' .format(1,2,3) 

print(b)
c = 'H:{1} , T: {2} , H2: {0}' . format(111,222,333)
print(c)
 

e = ' {:*>53}' .format('Hua Thanh Huong')
print(e)
print(e)
row1 = '+ {:-<8} + {:-^25} + {:->8} +' .format(' ',' ',' ')
print(row1)
row2 = '| {:^8} | {:^25} | {:^8} | ' . format ('STT' , 'Ho Va Ten ' ,'Nam Sinh' )
print(row2)
row3 = '| {:<8} | {:^25} | {:^8} | ' . format ('YD5869' , 'HUA THANH HUONG' , 'DA NANG')
print(row3)
row4 = '| {:<8} | {:^25} | {:^8} | ' . format ('1', 'Hua Lia' ,'1955')
print(row4)
row5 = '| {:<8} | {:^25} | {:^8} | ' . format ('2' , 'Nguyen Thi Buoi', '1956')
row6 = '| {:<8} | {:^25} | {:^8} | ' . format ('3' , 'Nguyen Thanh Toan', '1981')
row7 = '| {:<8} | {:^25} | {:^8} | ' . format ('4' , 'Hua Thi Nho' , ' 1983')
row8 = '| {:<8} | {:^25} | {:^8} | ' . format ('5' , 'Hua Thanh Huong' , ' 1990')
row9 = '| {:<8} | {:^25} | {:^8} | ' . format ('6' , 'Nguyen Thi Tinh' , ' 1991')
row10 = '| {:<8} | {:^25} | {:^8} | '. format ('7' , 'Nguyen Hua Huong Giang' , '2007')
row11 = '| {:<8} | {:^25} | {:^8} | ' . format ('8', 'Nguyen Hua Kieu Vy' , ' 2009' )
row12 = '| {:<8} | {:^25} | {:^8} | ' . format ('9', 'Hua Thanh Dung' , '2008')
row13 = '| {:<8} | {:^25} | {:^8} | ' . format ('10' ,' Hua Thanh Cuong' , '2013')
print(row5)
print(row6)
print(row7)
print(row8)
print(row9)
print(row10)
print(row11)
print(row12)
print(row13)
row14 = '+ {:-<8} + {:-^25} + {:->8} +' .format(' ',' ',' ')
print(row14)




