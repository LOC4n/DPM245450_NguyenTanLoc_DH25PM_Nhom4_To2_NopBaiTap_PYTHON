#Câu 5: Màn hình đăng nhập
'''
Yêu cầu:
Thiết kế màn hình đăng nhập:
'''
import tkinter as tk
from tkinter import messagebox

def Enter_New_password():
    Old = entry_current.get()
    new = entry_new.get()
    Enter = entry_confirm.get()

    if Old != "123456": 
        messagebox.showerror("Error", "Old password is incorrect!")
        return
    
    if new != Enter:
        messagebox.showerror("Error", "New password and Enter password do not match!")
        return
    
    messagebox.showinfo("Success", "Password changed successfully!")
    entry_current.delete(0, tk.END)
    entry_new.delete(0, tk.END)
    entry_confirm.delete(0, tk.END)

root = tk.Tk()
root.title("Enter New Password")
root.resizable(False, False)

tk.Label(root, text="Old Passoword:").grid(row=0, column=0, padx=5, pady=5, sticky='w')     
entry_current = tk.Entry(root, show="*")
entry_current.grid(row=0, column=1, padx=5, pady=5)     


tk.Label(root, text="New Password:").grid(row=1, column=0, padx=5, pady=5, sticky='w')  
entry_new = tk.Entry(root, show="*")
entry_new.grid(row=1, column=1, padx=5, pady=5)     


tk.Label(root, text="Enter New Password Again:").grid(row=2, column=0, padx=5, pady=5, sticky='w')  
entry_confirm = tk.Entry(root, show="*")
entry_confirm.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Enter New Password", command=Enter_New_password).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()