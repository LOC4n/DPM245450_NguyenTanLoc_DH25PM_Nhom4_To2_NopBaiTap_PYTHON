#Câu 7: Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong 

while True:
    try:
        
        lst = list(map(int, input("Nhập dãy số theo thứ tự tăng (cách nhau bằng dấu cách): ").split()))
        
 
        is_increasing = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
        
        if is_increasing:
            print("Dãy số hợp lệ:", lst)
            break
        else:
            print(" Dãy không tăng dần, vui lòng nhập lại!")
    except ValueError:
        print(" Vui lòng chỉ nhập số nguyên, cách nhau bằng dấu cách!")