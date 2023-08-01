import wx
import threading
import time

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='超级功德箱', size=(600, 550))
        self.level = 0
        self.num_click = 0
        self.Center()
        self.auto_click = False

        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.level_text = wx.StaticText(panel, label='Lv.{}'.format(self.level))
        hbox1.Add(self.level_text, flag=wx.LEFT, border=10)
        self.name_input = wx.TextCtrl(panel)
        hbox1.Add(self.name_input, proportion=1, flag=wx.EXPAND|wx.RIGHT, border=10)
        self.merit_text = wx.StaticText(panel, label='功德：{}'.format(self.num_click))
        hbox1.Add(self.merit_text, flag=wx.RIGHT, border=10)
        vbox.Add(hbox1, proportion=1, flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.progress = wx.Gauge(panel, range=10, size=(300, 25))
        hbox2.Add(self.progress, proportion=1, flag=wx.ALIGN_CENTER)
        vbox.Add(hbox2, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        image = wx.StaticBitmap(panel, bitmap=wx.Bitmap('image.jpg'))
        hbox3.Add(image, proportion=1, flag=wx.ALIGN_CENTER)
        vbox.Add(hbox3, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        button2 = wx.Button(panel, label='敲木鱼')
        hbox4.Add(button2, flag=wx.LEFT|wx.RIGHT, border=10)
        button2.Bind(wx.EVT_BUTTON, self.on_click)
        button3 = wx.Button(panel, label='VIP自动敲木鱼')
        hbox4.Add(button3, flag=wx.LEFT|wx.RIGHT, border=10)
        button3.Bind(wx.EVT_BUTTON, self.on_auto_click)
        vbox.Add(hbox4, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

    def on_click(self, event):
        self.num_click += 1
        self.progress.SetValue(self.num_click%10)
        if self.num_click%10 == 0:
            self.level += 1
            self.progress.SetValue(0)
            self.progress.SetRange(10)
            self.level_text.SetLabel('Lv.{}'.format(self.level))
        self.merit_text.SetLabel('功德：{}'.format(self.num_click))

    def on_auto_click(self, event):
        if not self.auto_click:
            self.auto_click = True
            self.auto_click_thread = threading.Thread(target=self.auto_click_func)
            self.auto_click_thread.start()
            event.GetEventObject().SetLabel('停止自动敲木鱼')
        else:
            self.auto_click = False
            event.GetEventObject().SetLabel('VIP自动敲木鱼')

    def auto_click_func(self):
        while self.auto_click:
            self.num_click += 1
            self.progress.SetValue(self.num_click % 10)
            if self.num_click % 10 == 0:
                self.level += 1
                self.progress.SetRange(10)
                self.level_text.SetLabel('Lv.{}'.format(self.level))
            self.merit_text.SetLabel('功德：{}'.format(self.num_click))
            time.sleep(1)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
