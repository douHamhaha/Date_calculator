import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.panel = wx.Panel(self)
        self.CreateSizer()
        remove_button = wx.Button(self.panel, label="Remove Sizer",pos=(50,10))
        remove_button.Bind(wx.EVT_BUTTON, self.OnRemoveSizer)
    def CreateSizer(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 添加一些控件到vbox
        for i in range(3):
            label = wx.StaticText(self.panel, label=f"Label {i}")
            vbox.Add(label, 0, wx.ALL, 5)

        # 设置面板的Sizer为vbox
        self.panel.SetSizer(vbox)

    def RemoveSizer(self):
        # Remove the sizer from the panel
        self.panel.SetSizer(None)

    def OnRemoveSizer(self, event):
        self.RemoveSizer()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame(None, "BoxSizer Removal Example")
    frame.Show()
    app.MainLoop()
