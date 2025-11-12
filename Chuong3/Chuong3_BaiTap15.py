#Câu 15: Giải thích cách chạy các dòng lệnh rang


'''
Yêu cầu:
(a) range(5)-> sẽ chạy từ 0 đến 4
(b) range(5, 10)-> sẽ chạy từ 5 đến 9
(c) range(5, 20, 3) -> sẽ chạy từ 5 đến 20, bước nhảy là 3
(d) range(20, 5, -1)-> sẽ chạy từ 20 đén 6, bước nhảy là -1
(e) range(20, 5, -3)-> sẽ chạy từ 20 đến 6, bước nhảy là -3
(f) range(10, 5)-> không chạy vì giá trị bắt đầu lớn hơn giá trị kết thúc và không có bước nhảy âm
(g) range(0)-> không chạy vì không có giá trị nào để lặp
(h) range(10, 101, 10)-> sẽ chạy từ 10 đến 100, bước nhảy là 10
(i) range(10, -1, -1)-> sẽ chạy từ 10 đến 0, bước nhảy là -1
(j) range(-3, 4)-> sẽ chạy từ -3 đến 3, bước nhảy là 1
(k) range(0, 10, 1)-> sẽ chạy từ 0 đến 9,bước nhảy là 1
'''

for i in range(0, 10, 1):
    print(i)