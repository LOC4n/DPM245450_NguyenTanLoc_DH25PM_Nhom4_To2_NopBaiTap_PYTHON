#Câu 8: Tách lấy tên bài hát
'''
Yêu cầu:
Cho một chuỗi là đường dẫn của 1 file nhạc, ví dụ: d:\\music\muabui.mp3
Hãy viết 2 hàm để:
- Lấy ra muabui.mp3
- Lấy ra muabui
Lưu ý đường dẫn bài hát là bất kỳ. Nên khi truyền vào bài hát nào thì lấy chính xác theo
bài hát đó.
'''
import os

def lay_ten_file(path):
    return os.path.basename(path) 

def lay_ten_bai_hat(path):
    file_name = os.path.basename(path)       
    ten_bai = os.path.splitext(file_name)[0] 
    return ten_bai

duong_dan = input("Nhập đường dẫn file nhạc: ")

print("Tên file là:", lay_ten_file(duong_dan))
print("Tên bài hát là:", lay_ten_bai_hat(duong_dan))