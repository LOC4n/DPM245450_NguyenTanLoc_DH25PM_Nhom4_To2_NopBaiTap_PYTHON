#Câu 12: Hàm oscillat
'''
Yêu cầu:
Cho mã lệnh:
Hãy viết hàm oscillate để khi chạy phần mềm, nó ra kết quả:
-3 3 -2 2 -1 1 0 0 1 -1 2 -2 3 -3 4 -4
'''
def oscillate(start, stop):

  for i in range(start, stop):
    yield i
    yield -i


print("Kết quả chạy chương trình:")
for n in oscillate(-3, 5):
    print(n, end=' ')
print()