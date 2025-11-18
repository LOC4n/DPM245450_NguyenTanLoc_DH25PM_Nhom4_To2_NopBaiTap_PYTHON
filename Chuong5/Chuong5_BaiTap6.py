#Câu 6: Trích lọc số âm trong chuỗi
'''
Yêu cầu:
Viết một hàm đặt tên là NegativeNumberInStrings(str). Hàm này có đối số truyền vào
là một chuỗi bất kỳ, Hãy viết lệnh để xuất ra các số nguyên âm trong chuỗi.
Ví dụ: Nếu nhập vào chuỗi “abc-5xyz-12k9l--p” thì hàm phải xuất ra được 2 số nguyên
âm đó là -5 và -12
'''
import re

def NegativeNumberInStrings(s):
    negative_numbers = re.findall(r'-\d+', s)
    
    if negative_numbers:
        print("Các số nguyên âm trong chuỗi là:")
        for num in negative_numbers:
            print(num)
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

text = "Trong chuỗi này có -12, -7 và cả 45, -100."
NegativeNumberInStrings(text)