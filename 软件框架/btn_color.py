# import wx
#
# class MyPanel(wx.Panel):
#     def __init__(self, parent):
#         super(MyPanel, self).__init__(parent)
#         self.SetBackgroundColour(wx.Colour(255, 255, 255))  # 设置面板的背景颜色为白色
#         self.Bind(wx.EVT_PAINT, self.OnPaint)  # 绑定绘制事件
#
#     def OnPaint(self, event):
#         dc = wx.PaintDC(self)
#         dc.Clear()  # 清空绘制区域
#         dc.SetBrush(wx.Brush(wx.Colour(0, 0, 255)))  # 设置蓝色画刷
#         dc.DrawRectangle(50, 100, 100, 500)  # 绘制矩形
#
#
# if __name__ == '__main__':
#     app = wx.App(False)
#     frame = wx.Frame(None, title="蓝色矩形示例", size=(300, 200))
#     panel = MyPanel(frame)
#     frame.Show()
#     app.MainLoop()
# import wx
#
# class MyFrame(wx.Frame):
#     def __init__(self, parent, title):
#         super(MyFrame, self).__init__(parent, title=title, size=(200, 150))
#
#         # 创建一个无边框Panel用于显示蓝色矩形
#         self.panel = wx.Panel(self, style=wx.SIMPLE_BORDER)
#         self.panel.SetBackgroundColour(wx.WHITE)  # 设置Panel的背景颜色为白色
#
#         # 设置Panel的尺寸为长10宽5
#         self.panel.SetSize(10, 5)
#
#         # 在Panel上绘制蓝色矩形
#         self.panel.Bind(wx.EVT_PAINT, self.on_paint)
#
#     def on_paint(self, event):
#         dc = wx.PaintDC(self.panel)
#         gc = wx.GraphicsContext.Create(dc)
#
#         # 设置蓝色矩形的边框颜色与背景颜色一致
#         border_color = wx.Colour(255, 255, 255)  # 设置为白色
#         gc.SetPen(wx.Pen(border_color, 1))
#
#         # 设置蓝色矩形的填充颜色为蓝色
#         fill_color = wx.Colour(0, 0, 255)  # 设置为蓝色
#         gc.SetBrush(wx.Brush(fill_color))
#
#         # 绘制蓝色矩形
#         gc.DrawRectangle(0, 0, 100, 150)
#
# if __name__ == '__main__':
#     app = wx.App(False)
#     frame = MyFrame(None, '蓝色矩形示例')
#     frame.Show()
#     app.MainLoop()
#

# import wx
#
# class MyFrame(wx.Frame):
#     def __init__(self, parent, title):
#         super(MyFrame, self).__init__(parent, title=title, size=(200, 150))
#
#         # 创建一个无边框Panel用于显示蓝色矩形
#         self.panel = wx.Panel(self, style=wx.SIMPLE_BORDER)
#         self.panel.SetBackgroundColour(wx.WHITE)  # 设置Panel的背景颜色为白色
#
#         # 设置Panel的尺寸为长10宽5
#         self.panel.SetSize(10, 5)
#
#         # 创建显示蓝色矩形的按钮
#         self.show_button = wx.Button(self, label="显示蓝色矩形")
#         self.show_button.Bind(wx.EVT_BUTTON, self.on_show_button_click)
#
#         # 创建隐藏蓝色矩形的按钮
#         self.hide_button = wx.Button(self, label="隐藏蓝色矩形")
#         self.hide_button.Bind(wx.EVT_BUTTON, self.on_hide_button_click)
#
#         # 设置水平布局
#         sizer = wx.BoxSizer(wx.HORIZONTAL)
#         sizer.Add(self.show_button, 0, wx.ALL, 5)
#         sizer.Add(self.hide_button, 0, wx.ALL, 5)
#         self.SetSizer(sizer)
#
#         # 初始状态下隐藏蓝色矩形
#         self.hide_blue_rectangle()
#
#     def on_show_button_click(self, event):
#         # 显示蓝色矩形
#         self.show_blue_rectangle()
#
#     def on_hide_button_click(self, event):
#         # 隐藏蓝色矩形
#         self.hide_blue_rectangle()
#
#     def show_blue_rectangle(self):
#         # 在Panel上绘制蓝色矩形
#         dc = wx.ClientDC(self.panel)
#         gc = wx.GraphicsContext.Create(dc)
#
#         # 设置蓝色矩形的边框颜色与背景颜色一致
#         border_color = wx.Colour(255, 255, 255)  # 设置为白色
#         gc.SetPen(wx.Pen(border_color, 1))
#
#         # 设置蓝色矩形的填充颜色为蓝色
#         fill_color = wx.Colour(0, 0, 255)  # 设置为蓝色
#         gc.SetBrush(wx.Brush(fill_color))
#
#         # 绘制蓝色矩形
#         gc.DrawRectangle(0, 0, 10, 5)
#
#     def hide_blue_rectangle(self):
#         # 清空Panel上的内容，即隐藏蓝色矩形
#         dc = wx.ClientDC(self.panel)
#         dc.Clear()
#
# if __name__ == '__main__':
#     app = wx.App(False)
#     frame = MyFrame(None, '蓝色矩形示例')
#     frame.Show()
#     app.MainLoop()
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        panel = wx.Panel(self)
        self.file_picker_btn = wx.Button(panel, label="选择文件", pos=(10, 10))
        self.file_picker_btn.Bind(wx.EVT_BUTTON, self.on_file_picker_btn)

        self.Show()

    def on_file_picker_btn(self, event):
        wildcard = "文本文件 (*.txt)|*.txt|所有文件 (*.*)|*.*"
        dlg = wx.FileDialog(self, "选择文件", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            print("选择的文件路径：", path)

        dlg.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "文件选择界面示例")
    app.MainLoop()


# import wx
#
# class MyFrame(wx.Frame):
#     def __init__(self, parent, title):
#         super(MyFrame, self).__init__(parent, title=title, size=(300, 200))
#
#         panel = wx.Panel(self)
#
#         # 加载图片
#         image = wx.Image(r".\icon\oucome.png", wx.BITMAP_TYPE_ANY)
#
#         # 调整图片大小为 64x64 像素
#         image = image.Scale(64, 64, wx.IMAGE_QUALITY_HIGH)
#
#         # 将图片转换为位图对象
#         bitmap = wx.Bitmap(image)
#
#         # 创建一个静态图片控件
#         static_bitmap = wx.StaticBitmap(panel, wx.ID_ANY, bitmap, pos=(10, 10))
#
#         self.Center()
#         self.Show()
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MyFrame(None, "显示固定大小图片示例")
#     app.MainLoop()

# import wx
#
# class MyFrame(wx.Frame):
#     def __init__(self, parent, title):
#         super(MyFrame, self).__init__(parent, title=title, size=(300, 200))
#
#         panel = wx.Panel(self)
#
#         # 加载图片
#         image = wx.Image(r".\icon\tou.jpg", wx.BITMAP_TYPE_ANY)
#
#         # 将图片转换为位图对象
#         bitmap = wx.Bitmap(image)
#
#         # 创建一个静态图片控件
#         static_bitmap = wx.StaticBitmap(panel, wx.ID_ANY, bitmap, pos=(10, 10))
#
#         self.Center()
#         self.Show()
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MyFrame(None, "显示图片示例")
#     app.MainLoop()
#

