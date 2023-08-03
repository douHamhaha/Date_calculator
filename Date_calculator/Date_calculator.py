import wx
from time import *
import re
import datetime as dt

class Yemian(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, None, -1, title='日期计算器', size=(280, 350))
        self.Center()
        # 创建面板
        panel = wx.Panel(self)
        self.SetMinSize((280,350))
        self.SetMaxSize((280,350))
        # 创建文本框
        self.Nian = wx.TextCtrl(panel,id=14,pos=(10,0),size=(45,28),style=wx.TE_CENTER)
        self.text = wx.TextCtrl(panel, id=15, pos=(110, 0), size=(145, 28), style=wx.TE_LEFT)

        # 创建文字
        self.label = wx.StaticText(panel,pos=(75,5),label='年')
        self.label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.txt = wx.StaticText(panel,pos=(10,285),label='此计算机由Wu完成')
        # 创建按钮
        self.bt_shuaxin = wx.Button(panel, label='C', pos=(10, 30), size=(45, 45))
        # self.bt_nian = wx.Button(panel, label='年', pos=(60, 30), size=(45, 45))
        self.bt_yue = wx.Button(panel, label='月', pos=(60, 30), size=(95, 45))
        self.bt_ri = wx.Button(panel, label='日', pos=(160, 30), size=(95, 45))
        self.bt_7 = wx.Button(panel, label='7', pos=(10, 80), size=(45, 45))
        self.bt_8 = wx.Button(panel, label='8', pos=(60, 80), size=(45, 45))
        self.bt_9 = wx.Button(panel, label='9', pos=(110, 80), size=(45, 45))
        self.bt_4 = wx.Button(panel, label='4', pos=(10, 130), size=(45, 45))
        self.bt_5 = wx.Button(panel, label='5', pos=(60, 130), size=(45, 45))
        self.bt_6 = wx.Button(panel, label='6', pos=(110, 130), size=(45, 45))
        self.bt_1 = wx.Button(panel, label='1', pos=(10, 180), size=(45, 45))
        self.bt_2 = wx.Button(panel, label='2', pos=(60, 180), size=(45, 45))
        self.bt_3 = wx.Button(panel, label='3', pos=(110, 180), size=(45, 45))
        self.bt_jia = wx.Button(panel, label='➖', pos=(160, 80), size=(45, 95))
        self.bt_0 = wx.Button(panel, label='0', pos=(10, 230), size=(145, 45))
        self.bt_dengyu = wx.Button(panel, label='＝', pos=(210,180), size=(45, 95))

        self.bt_shan = wx.Button(panel, label='←',pos=(210,80),size=(45,95))
        self.bt_zhuan = wx.Button(panel, label='转换',pos=(160, 180),size=(45,95))

        # 绑定按钮
        self.bt_0.Bind(wx.EVT_BUTTON, self.Onzero)
        self.bt_1.Bind(wx.EVT_BUTTON, self.Onone)
        self.bt_2.Bind(wx.EVT_BUTTON, self.Ontwo)
        self.bt_3.Bind(wx.EVT_BUTTON, self.Onthree)
        self.bt_4.Bind(wx.EVT_BUTTON, self.Onfour)
        self.bt_5.Bind(wx.EVT_BUTTON, self.Onfive)
        self.bt_6.Bind(wx.EVT_BUTTON, self.Onsix)
        self.bt_7.Bind(wx.EVT_BUTTON, self.Onseven)
        self.bt_8.Bind(wx.EVT_BUTTON, self.Oneight)
        self.bt_9.Bind(wx.EVT_BUTTON, self.Onnine)
        self.bt_jia.Bind(wx.EVT_BUTTON, self.OnJia)
        self.bt_dengyu.Bind(wx.EVT_BUTTON, self.OnDeng)
        self.bt_shuaxin.Bind(wx.EVT_BUTTON, self.OnC)
        self.bt_yue.Bind(wx.EVT_BUTTON,self.OnYue)
        self.bt_ri.Bind(wx.EVT_BUTTON,self.OnRi)

        self.bt_shan.Bind(wx.EVT_BUTTON,self.Onshan)
        self.bt_zhuan.Bind(wx.EVT_BUTTON,self.Onzhuan)

        self.bt_zhuan.SetDefault()
        self.bt_zhuan.clicked_times = 0

        self.bt_jia.SetDefault()
        self.bt_jia.clicked_times = 0

        self.neir = ''
    def Onzhuan(self,event):
        ''
        self.bt_zhuan.clicked_times = self.bt_zhuan.clicked_times +1
        if self.bt_zhuan.clicked_times == 2:
            self.bt_zhuan.clicked_times = 0
    def Onzero(self, event):
        ''
        if self.bt_zhuan.clicked_times == 1:
            self.text.AppendText("0")
        else:
            self.Nian.AppendText('0')
    def Onone(self, event):
        ''
        if self.bt_zhuan.clicked_times == 1:
            self.text.AppendText("1")
        else:
            self.Nian.AppendText('1')
    def Ontwo(self, event):
        ''
        if self.bt_zhuan.clicked_times == 1:
            self.text.AppendText("2")
        else:
            self.Nian.AppendText('2')
    def Onthree(self, event):
        ''
        if self.bt_zhuan.clicked_times == 1:
            self.text.AppendText("3")
        else:
            self.Nian.AppendText('3')
    def Onfour(self, event):
        ''
        if self.bt_zhuan.clicked_times == 1:
            self.text.AppendText("4")
        else:
            self.Nian.AppendText('4')
    def Onfive(self, event):
        ''
        if self.bt_zhuan.clicked_times == 1:
            self.text.AppendText("5")
        else:
            self.Nian.AppendText('5')
    def Onsix(self, event):
        ''
        if self.bt_zhuan.clicked_times == 1:
            self.text.AppendText("6")
        else:
            self.Nian.AppendText('6')
    def Onseven(self, event):
        ''
        if self.bt_zhuan.clicked_times == 1:
            self.text.AppendText("7")
        else:
            self.Nian.AppendText('7')
    def Oneight(self, event):
        ''
        if self.bt_zhuan.clicked_times == 1:
            self.text.AppendText("8")
        else:
            self.Nian.AppendText('8')
    def Onnine(self, event):
        ''
        if self.bt_zhuan.clicked_times == 1:
            self.text.AppendText("9")
        else:
            self.Nian.AppendText('9')

    def OnYue(self, event):
        self.text.AppendText("月")
        text_Y=self.text.GetValue()
        data1 = '月'
        a={}
        all_index = re.findall('[\u4e00-\u9fa5]', text_Y)
        for i in all_index:
            if all_index.count(i) > 1:
                a[i] = all_index.count(i)
        if data1 in a.keys() and a[data1] >= 3:
            ''
            self.text.SetLabel('!Error!')
    def OnRi(self, event):
        ''
        self.text.AppendText("日")
        text_R=self.text.GetValue()
        data1 = '日'
        b={}
        all_index = re.findall('[\u4e00-\u9fa5]', text_R)
        for i in all_index:
            if all_index.count(i) > 1:
                b[i] = all_index.count(i)
        if data1 in b.keys() and b[data1] >= 3:
            ''
            self.text.SetLabel('!Error!')
    def Onshan(self,event):
        ''
        if self.bt_zhuan.clicked_times == 1:
            label = self.text.GetValue()
            fina = label[:-1]
            self.text.SetValue(fina)
        else:
            label = self.Nian.GetValue()
            fina = label[:-1]
            self.Nian.SetValue(fina)

    def OnC(self, event):
        ''
        self.bt_jia.clicked_times = 0
        self.bt_zhuan.clicked_times = 0
        self.neir = ''
        self.Nian.SetValue('')
        self.text.SetValue('')

    def OnJia(self, event):
        ''
        self.bt_jia.clicked_times = self.bt_jia.clicked_times + 1
        self.neir = self.text.GetValue()
        self.nian = self.Nian.GetValue()
        self.text.SetValue('')
        self.Nian.SetValue('')
        self.bt_zhuan.clicked_times = 0
        if self.bt_jia.clicked_times == 2:
            self.bt_jia.clicked_times = 0

    def OnDeng(self, event):
        ''
        # 加后
        nian2 = self.Nian.GetValue()
        Text2 = self.text.GetValue()
        yue2 = int(Text2.split("月")[0])
        yue_1 = Text2.split('月')[1]
        ri2 = int(yue_1.split('日')[0])

        nian1= str(self.nian)
        Text1 = self.neir
        yue1 = int(Text1.split("月")[0])
        yue_1 = Text1.split('月')[1]
        ri1 = int(yue_1.split('日')[0])
        # 判断日期格式是否正确
        # 加后
        if yue2 < 10 and ri2 < 10 :
            yue2 = str(yue2)
            ri2 = str(ri2)
            yue2 = yue2.zfill(2)
            ri2 = ri2.zfill(2)
            d2 = nian2+'-'+yue2+'-'+ri2
        elif yue2 < 10 and ri2 >=10:
            yue2 = str(yue2)
            ri2 = str(ri2)
            yue2 = yue2.zfill(2)
            d2 = nian2+'-'+yue2+'-'+ri2
        else:
            yue2 = str(yue2)
            ri2 = str(ri2)
            d2 = nian2 + '-' + yue2 + '-' + ri2
        d22 = d2
        # 加前
        if yue1 < 10 and ri1 < 10:
            yue1 = str(yue1)
            ri1 = str(ri1)
            yue1 = str(yue1.zfill(2))
            ri1 = str(ri1.zfill(2))
            d1 = nian1 + '-' + yue1 + '-' + ri1
        elif yue1 < 10 and ri1 >= 10:
            yue1 = str(yue1)
            ri1 = str(ri1)
            yue1 = str(yue1.zfill(2))
            d1 = nian1 + '-' + yue1 + '-' + ri1
        else:
            yue1 = str(yue1)
            ri1 = str(ri1)
            d1 = nian1 + '-' + yue1 + '-' + ri1
        d11 = d1

        # 结果报告
        try:
            date2 = dt.datetime.strptime(d11, "%Y-%m-%d").date()
            date1 = dt.datetime.strptime(d22, "%Y-%m-%d").date()
            Days = str((date2 - date1).days)
            wx.MessageBox('计算得出的天数差为:' + Days)
            self.bt_jia.clicked_times = 0
            self.bt_zhuan.clicked_times = 0
            self.neir = ''
            self.Nian.SetValue('')
            self.text.SetValue('')
        except:
            ''
            message = '日期格式错误，请重新输入'
            wx.MessageBox(message)
            self.bt_jia.clicked_times = 0
            self.bt_zhuan.clicked_times = 0
            self.neir = ''
            self.Nian.SetValue('')
            self.text.SetValue('')
if __name__ == '__main__':
    app = wx.App()
    Yemian(None).Show()
    app.MainLoop()