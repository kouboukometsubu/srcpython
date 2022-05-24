import os
from tkinter import filedialog
from tkinter import messagebox


fileType = [('テキストファイル','*.txt')] 
dir = 'd:\\'
filename = filedialog.askopenfilename(filetypes = fileType, initialdir = dir) 
print(filename)

readstr = "" 

f = open(filename)

readstr = f.read()

f.close()

messagebox.showinfo("title", readstr)
 #messagebox.showinfo("readstr", "readstr")