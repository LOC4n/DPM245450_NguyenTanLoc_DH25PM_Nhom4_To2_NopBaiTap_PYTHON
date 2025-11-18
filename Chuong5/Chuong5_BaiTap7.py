#Câu 7: Tối ưu chuỗi danh từ
'''
Yêu cầu:
Viết chương trình tối ưu Chuỗi danh từ
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách
nhau bởi một khoảng trắng, Ký tự đầu tiên của các từ Viết Hoa
Ví dụ:
Input “ TRần duY thAnH ”
Output “Trần Duy Thanh”
'''
def toi_uu_chuoi(s):
   
    s = s.strip()
    
    words = s.split()
  
    s = ' '.join(words)
    
    s = s.title()
    return s


chuoi = input("Nhập vào chuỗi danh từ: ")
ket_qua = toi_uu_chuoi(chuoi)
print("Chuỗi sau khi tối ưu là:")
print(ket_qua)