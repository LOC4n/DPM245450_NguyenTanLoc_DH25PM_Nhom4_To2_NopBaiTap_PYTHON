#Câu 10: Tính dãy số

'''
Yêu cầu:
Cho biểu thức toán học sau:
Tinh S (x, n)= x + x*x/2! + x*x*x/3!+...+x*n/n!
Viết chương trình cho phép nhập x, n và xuất ra kết quả của biểu thức.
'''


x=int(input("Nhập x:"))
n=int(input("Nhập N:"))
s=0
for i in range(1,n+1):
 tu=x**i
 mau=1
 for j in range(1,i+1):
    mau=mau*j
 s=s+(tu/mau)
print("s({0},{1})={2}".format(x,n,s))
