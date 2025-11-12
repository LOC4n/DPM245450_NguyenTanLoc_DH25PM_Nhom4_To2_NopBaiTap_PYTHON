#Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).
# Hàm kiểm tra năm nhuận
def nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

# Nhập ngày tháng năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Số ngày trong từng tháng
ngay_thang = [31, 28 + nam_nhuan(nam), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Tăng ngày
ngay += 1

# Kiểm tra nếu quá ngày trong tháng
if ngay > ngay_thang[thang - 1]:
    ngay = 1
    thang += 1

# Kiểm tra nếu quá tháng 12
if thang > 12:
    thang = 1
    nam += 1

print("Ngày kế tiếp là: {}/{}/{}".format(ngay, thang, nam))
