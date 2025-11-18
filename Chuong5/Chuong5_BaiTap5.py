#Câu 5: Xử lý chuỗi với các hàm cơ bản
'''
Yêu cầu:
Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
- Bao nhiêu chữ IN HOA
- Bao nhiêu chữ in thường
- Bao nhiêu chữ là chữ số
- Bao nhiêu chữ là ký tự đặc biệt
- Bao nhiêu chữ là khoảng trắng
- Bao nhiêu chữ là Nguyên Âm
- Bao nhiêu chữ là Phụ âm

'''
s = input("Nhập vào một chuỗi: ")

hoa = thuong = so = dac_biet = khoang_trang = nguyen_am = phu_am = 0

nguyen_am_set = "aeiouAEIOU"

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    elif ch.isdigit():
        so += 1
    elif ch.isspace():
        khoang_trang += 1
    else:
        dac_biet += 1

    if ch.isalpha():  
        if ch in nguyen_am_set:
            nguyen_am += 1
        else:
            phu_am += 1


print("Số chữ IN HOA: ", hoa)
print("Số chữ in thường: ", thuong)
print("Số chữ là chữ số: ", so)
print("Số ký tự đặc biệt: ", dac_biet)
print("Số ký tự khoảng trắng: ", khoang_trang)
print("Số nguyên âm: ", nguyen_am)
print("Số phụ âm: ", phu_am)