import wx


class MyFrame(wx.Frame):
    def __init__(self, parent):
        super(MyFrame, self).__init__(parent, title='123', size=(300, 200))

        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Show()

    def on_paint(self, event):
        # 在Panel上绘制蓝色矩形
        dc = wx.ClientDC(self.panel)
        gc = wx.GraphicsContext.Create(dc)

        # 蓝色矩形的边框颜色与背景颜色一致
        border_color = wx.Colour(255, 255, 255)  # 设置为白色
        gc.SetPen(wx.Pen(border_color, 1))

        # 蓝色矩形的填充颜色为蓝色
        fill_color = wx.Colour(102, 178, 255)  # 设置为蓝色
        gc.SetBrush(wx.Brush(fill_color))

        # 画蓝色矩形
        gc.DrawRectangle(0, 0, 600, 50)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    app.MainLoop()
