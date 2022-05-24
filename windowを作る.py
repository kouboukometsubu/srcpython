import tkinter
from tkinter import filedialog



# メニューから呼び出される関数
def open_file():
    pass
fileType = [('テキストファイル','*.txt')] 
dir = 'C:\\pg'
fle = filedialog.askopenfilename(filetypes = fileType, initialdir = dir) 
print(fle)



def close_disp():
    pass






# Tkクラス生成
frm = tkinter.Tk()
# 画面サイズ
frm.geometry('600x400')
# 画面タイトル
frm.title('サンプル画面')

#メニューバー作成 
men = tkinter.Menu(frm) 

#メニューバーを画面にセット 
frm.config(menu=men) 

#メニューに親メニュー（ファイル）を作成する 
menu_file = tkinter.Menu(frm) 
men.add_cascade(label='ファイル', menu=menu_file) 

#親メニューに子メニュー（開く・閉じる）を追加する 
menu_file.add_command(label='開く', command=open_file) 
menu_file.add_separator() 
menu_file.add_command(label='閉じる', command=close_disp)

# ボタン
btn = tkinter.Button(frm, text='計算',fg="blue",bg="white",width=5)
btn.place(x=140, y=170)

#閉じるボタン
btnClose = tkinter.Button(frm,text = "閉じる",fg="red",bg="white",width=5)
btnClose.place(x=250,y=170)









# 画面をそのまま表示
frm.mainloop()


