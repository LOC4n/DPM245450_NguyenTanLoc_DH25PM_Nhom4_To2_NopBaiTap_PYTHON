#Câu 5: Hãy cho biết kết quả xuất ra màn hình

'''
Cho i, j, k là các con số và lệnh dưới đây:
Hãy cho biết kết quả xuất ra màn hình nếu tuần tự 3 biến trên có các giá trị sau:
(a) i = 3, j = 5, and k = 7
(b) i = 3, j = 7, and k = 5
(c) i = 5, j = 3, and k = 7
(d) i = 5, j = 7, and k =3
(e) i = 7, j = 3, and k = 5
(f) i =7, j = 5, and k = 3
'''


i=int(input("Nhap i:"))
j=int(input("Nhap j:"))
k=int(input("Nhap k:"))
if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        i=k
print("i=", i, "j=", j, "k=" ,k)