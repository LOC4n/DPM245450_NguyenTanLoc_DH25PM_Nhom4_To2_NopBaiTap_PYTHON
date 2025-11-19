#Câu 8: Thiết kế màn hình chuyển độ F thành độ C
'''
Yêu cầu:
Thiết kế màn hình chuyển độ F thành độ C

'''
import tkinter as tk

def convert_f_to_c():
    """Lấy giá trị độ F từ ô nhập, tính toán và hiển thị độ C."""
    try:
        f_value_str = entry_f.get()
        if not f_value_str:
            lbl_ketqua.config(text="Chưa nhập!", fg="red")
            return

        f_value = float(f_value_str)
        
        c_value = (f_value - 32) * 5 / 9
        
        lbl_ketqua.config(text=f"{c_value:.2f}", fg="black")
        
    except ValueError:
        lbl_ketqua.config(text="Không hợp lệ!", fg="red")

window = tk.Tk()
window.title("Chuyển đổi F sang C")
window.resizable(False, False)

main_frame = tk.Frame(
    window, 
    bg="yellow", 
    padx=20, 
    pady=20, 
    highlightbackground="blue", 
    highlightthickness=2
)
main_frame.pack(padx=10, pady=10)

lbl_nhap = tk.Label(
    main_frame, 
    text="Nhập độ F", 
    bg="yellow", 
    font=("Arial", 12)
)
lbl_nhap.grid(row=0, column=0, padx=5, pady=10, sticky="e")

entry_f = tk.Entry(
    main_frame, 
    width=15, 
    font=("Arial", 12, "bold"), 
    fg="red", 
    justify="center"
)
entry_f.grid(row=0, column=1, padx=5, pady=10)
entry_f.insert(0, "350")

btn_chuyen = tk.Button(
    main_frame, 
    text="Chuyển", 
    font=("Arial", 11, "bold"), 
    width=10, 
    command=convert_f_to_c,
    bg="lightblue"
)
btn_chuyen.grid(row=1, column=1, pady=10)

lbl_c = tk.Label(
    main_frame, 
    text="Độ C", 
    bg="yellow", 
    font=("Arial", 12)
)
lbl_c.grid(row=2, column=0, padx=5, pady=10, sticky="e")

lbl_ketqua = tk.Label(
    main_frame, 
    text="Độ C ở đây", 
    bg="yellow", 
    font=("Arial", 12, "bold"),
    width=15
)
lbl_ketqua.grid(row=2, column=1, padx=5, pady=10, sticky="w")

window.mainloop()