import tkinter

class MyApp1(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.Button1 = tkinter.Button(self)
        self.Button1["text"] = "Click here!" #ボタンのテキスト
        self.Button1["command"] = self.Button1_Func #割り込み関数
        self.Button1.pack(side="top")
        
        self.ButtonQuit = tkinter.Button(self, bg='#000000', fg='#ffffff', width=30, height = 10)
        self.ButtonQuit["text"] = "QUIT"
        self.ButtonQuit["command"] = self.QuitApp
        self.ButtonQuit.pack(side="top")

    def Button1_Func(self):
        print("Hello, World!")
        
    def QuitApp(self):
        print("quit this App")
        self.master.destroy()
        
root = tkinter.Tk()
root.geometry("400x300")
app = MyApp1(master=root)
app.mainloop()
