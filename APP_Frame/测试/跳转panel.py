# import wx
#
#
# class MyFrame(wx.Frame):
#     def __init__(self, *args, **kw):
#         super(MyFrame, self).__init__(*args, **kw)
#
#         self.panel = wx.Panel(self)
#
#         self.splitter = wx.SplitterWindow(self.panel)
#         self.lpanel = wx.Panel(self.splitter, style=wx.SUNKEN_BORDER)
#         self.rpanel = wx.Panel(self.splitter, style=wx.SUNKEN_BORDER)
#         self.splitter.SplitVertically(self.lpanel, self.rpanel, sashPosition=150)
#
#         self.button = wx.Button(self.panel, label="切换面板")
#         self.button.Bind(wx.EVT_BUTTON, self.on_button_click)
#
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.splitter, 1, wx.EXPAND)
#         sizer.Add(self.button, 0, wx.ALIGN_CENTER)
#         self.panel.SetSizer(sizer)
#
#     def on_button_click(self, event):
#         # 移除当前rpanel的内容
#         for child in self.rpanel.GetChildren():
#             child.Destroy()
#
#         # 添加新的内容到rpanel
#         new_content = wx.StaticText(self.rpanel, label="新的面板内容")
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(new_content, 0, wx.ALIGN_CENTER)
#         self.rpanel.SetSizer(s