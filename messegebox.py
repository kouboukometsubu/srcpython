import sys
from tkinter import messagebox



# メッセージボックス（情報） 
messagebox.showinfo("Title", "メッセージ内容")

# メッセージボックス（警告） 
messagebox.showwarning("タイトル", "メッセージ内容")

# メッセージボックス（エラー） 
messagebox.showerror("タイトル", "メッセージ内容")

# メッセージボックス（はい・いいえ） 
messagebox.askyesno("タイトル", "メッセージ内容")

# メッセージボックス（はい・いいえ） 
messagebox.askquestion("タイトル", "メッセージ内容")

# メッセージボックス（OK・キャンセル） 
messagebox.askokcancel("タイトル", "メッセージ内容")

# メッセージボックス（再試行・キャンセル） 
messagebox.askretrycancel("タイトル", "メッセージ内容")


# メッセージボックス（はい・いいえ） 
ret = messagebox.askyesno('確認', 'ウィンドウを閉じますか？')
#if ret == True:
#    //sys.exit()
