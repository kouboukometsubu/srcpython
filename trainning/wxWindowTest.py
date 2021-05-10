import wx

class Window(wx.Frame):
    def __init__(self, parent, id = -1, title = None):
        wx.Frame.__init__(self, parent, id, title)
        panel = wx.Panel(self, wx.ID_ANY)
 
        # メニューバーの生成
        menu_bar = wx.MenuBar()
 
        file = wx.Menu()
        file.Append(1, "New")
        file.Append(2, "Quit")

        edit = wx.Menu()
        edit.Append(3, "Redu")
        edit.Append(4, "Undo")
 
        # メニューをメニューバーへ登録
        menu_bar.Append(file, 'File')
        menu_bar.Append(edit, 'Edit')
 
        # フレームにメニュバー登録
        self.SetMenuBar(menu_bar)
 
        # メニュークリック時のイベント登録
        self.Bind(wx.EVT_MENU, self.click_menu)

        self.text = wx.StaticText(panel, wx.ID_ANY, "押されたメニュー")
        self.Show(True)
 

    def click_menu(self, event):
        event_id = event.GetId()
        msg = ""
        if (event_id == 1):
            msg = "New"
        elif (event_id == 2):
            msg = "Quit"
            self.Close(True)
        elif (event_id == 3):
            msg = "Redu"
        elif (event_id == 4):
            msg = "Undo"
 
        self.text.SetLabel(msg)
 
if __name__ == "__main__":
    app = wx.App()
    Window(None, wx.ID_ANY, "menu-bar")
    app.MainLoop()
