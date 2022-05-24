
import tkinter
from tkinter import messagebox


# clickイベント
def btn_click():
    messagebox.showwarning("title","hello")

frm = tkinter.Tk()

frm.geometry("300x200")

btn = tkinter.Button(frm,text="message", command=btn_click)
btn.place(x=140, y=170)




# 画面をそのまま表示
frm.mainloop()



