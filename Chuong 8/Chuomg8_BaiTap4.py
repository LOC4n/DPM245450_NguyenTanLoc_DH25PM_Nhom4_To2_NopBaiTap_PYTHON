#Câu 4: Phần mềm máy tính bỏ túi
'''
Yêu cầu:
Thiết kế Calculator đơn giản:
Phần mềm cho người sử dụng làm các phép toán cơ bản: +, - , *, / và xóa toàn bộ
phần mềm.
'''
from tkinter import *

def press(num):
    current = stringKQ.get()
    stringKQ.set(current + str(num))

def clear():
    stringKQ.set("")

def equal():
    try:
        result = eval(stringKQ.get())
        stringKQ.set(result)
    except:
        stringKQ.set("Error")


root = Tk()
root.title("Máy tính bỏ túi")
root.resizable(False, False)
stringKQ = StringVar()
Entry(root, textvariable=stringKQ, width=20, font=("tahoma", 14), justify="right").grid(row=0, column=0, columnspan=5, padx=5, pady=5)

Button(root, text='1', width=5, height=2, command=lambda: press('1')).grid(row=1, column=0, padx=2, pady=2)
Button(root, text='2', width=5, height=2, command=lambda: press('2')).grid(row=1, column=1, padx=2, pady=2)
Button(root, text='3', width=5, height=2, command=lambda: press('3')).grid(row=1, column=2, padx=2, pady=2)

Button(root, text='4', width=5, height=2, command=lambda: press('4')).grid(row=2, column=0, padx=2, pady=2)
Button(root, text='5', width=5, height=2, command=lambda: press('5')).grid(row=2, column=1, padx=2, pady=2)
Button(root, text='6', width=5, height=2, command=lambda: press('6')).grid(row=2, column=2, padx=2, pady=2)

Button(root, text='7', width=5, height=2, command=lambda: press('7')).grid(row=3, column=0, padx=2, pady=2)
Button(root, text='8', width=5, height=2, command=lambda: press('8')).grid(row=3, column=1, padx=2, pady=2)
Button(root, text='9', width=5, height=2, command=lambda: press('9')).grid(row=3, column=2, padx=2, pady=2)

Button(root, text='-', width=5, height=2, command=lambda: press('-')).grid(row=4, column=0, padx=2, pady=2)
Button(root, text='0', width=5, height=2, command=lambda: press('0')).grid(row=4, column=1, padx=2, pady=2)
Button(root, text='.', width=5, height=2, command=lambda: press('.')).grid(row=4, column=2, padx=2, pady=2)

Button(root, text='+', width=5, height=2, command=lambda: press('+')).grid(row=5, column=0, padx=2, pady=2)
Button(root, text='-', width=5, height=2, command=lambda: press('-')).grid(row=5, column=1, padx=2, pady=2)
Button(root, text='*', width=5, height=2, command=lambda: press('*')).grid(row=5, column=2, padx=2, pady=2)
Button(root, text='/', width=5, height=2, command=lambda: press('/')).grid(row=5, column=3, padx=2, pady=2)
Button(root, text='=', width=5, height=2, command=equal).grid(row=5, column=4, padx=2, pady=2)

Button(root, text='Clr', width=31, height=2, bg="#e6e6e6", command=clear).grid(row=6, column=0, columnspan=5, padx=5, pady=5)

root.mainloop()
