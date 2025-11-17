#Câu 19: Tính giá trị biểu thức S
import math

def giaithua(a):
    for l in range(1, a):
        a = a * l
    return a

x = float(input("Nhap x: "))
n = int(input("Nhap n: "))

S = 0

for i in range(n + 1):
    k = 2 * i + 1
    S += x**k / giaithua(k)

print("S(x,n) =", S)