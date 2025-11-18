#Câu 6: Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU

import random

N = int(input("Nhập số phần tử N: "))


lst = random.sample(range(1, 100), N)

print("Danh sách ngẫu nhiên:", lst)