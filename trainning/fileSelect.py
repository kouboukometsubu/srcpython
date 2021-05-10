# -*- coding: utf-8 -*-
import os, tkinter, tkinter.filedialog, tkinter.messagebox

class MyApp1(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.Button1 = tkinter.Button(self, bg='#000000', fg='#ffffff', width=12, height = 5)
        self.Button1["text"] = "SELECT FILE" #ボタンのテキスト
        self.Button1["command"] = self.Button1_Func #割り込み関数
        self.Button1.pack(side="top")
        
        self.ButtonQuit = tkinter.Button(self, bg='#000000', fg='#ffffff', width=12, height = 5)
        self.ButtonQuit["text"] = "QUIT"
        self.ButtonQuit["command"] = self.QuitApp
        self.ButtonQuit.pack(side="top")
        self.selected_file_path = ""
        
    def Button1_Func(self):
        fTyp = [("","*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        self.selected_file_path = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        print(self.selected_file_path)
        
    def QuitApp(self):
        print("quit this App")
        self.master.destroy()
        
        
root = tkinter.Tk()
root.geometry("100x200")
app = MyApp1(master=root)
app.mainloop()
