#Câu 8: Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp.


n = int(input("Nhập số phần tử n: "))

M = []
for i in range(n):
    x = float(input(f"Nhập M[{i}]: "))
    M.append(x)

M.sort(reverse=True)

print("Dãy sau khi sắp xếp giảm dần:")
for x in M:
    print(x, end=" ")