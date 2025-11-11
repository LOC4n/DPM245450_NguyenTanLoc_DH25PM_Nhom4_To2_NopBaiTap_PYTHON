#Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
# (vd: n=35 => Ba mươi lăm, n=5 => năm). 

n = int(input("Nhập số n (0-99): "))

chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

if n < 0 or n > 99:
    print("Vui lòng nhập số có tối đa 2 chữ số (0-99).")
else:
    if n < 10:
        print(chu_so[n].capitalize())
    else:
        chuc = n // 10
        donvi = n % 10

        if chuc == 1:
            doc = "Mười"
        else:
            doc = chu_so[chuc].capitalize() + " mươi"

        if donvi == 0:
            pass  
        elif donvi == 1:
            if chuc == 1:
                doc += " một"
            else:
                doc += " mốt"
        elif donvi == 4 and chuc > 1:
            doc += " tư"
        elif donvi == 5 and chuc >= 1:
            doc += " lăm"
        else:
            doc += " " + chu_so[donvi]

        print(doc)
