import time
import wx,json
import threading
from time import *
import os,sys
import datetime as dt

a = 0

user_info = {}
user_phonenumber = {}
user_text = {}
username = ''
phonenumber = ''
password = ''
def my_read_json(file,name_first,name_second):
    with open(file, "r",encoding="utf-8") as json_file:
        ret = json.load(json_file)
        data = ret[name_first][name_second]
        return data
def my_revise_json(file,name_first,name_second,zhi):
    with open(file,"r",encoding="utf-8") as json_file:
        data = json.load(json_file)
    # 修改Python对象
    data[name_first][name_second] = zhi
    # 将修改后的对象写入JSON文件
    with open(file, "w",encoding="utf-8") as json_file:
        json.dump(data, json_file)
#############################################################################################
def read_json(name_first,name_second):
    with open('数据.json', "r",encoding="utf-8") as json_file:
        ret = json.load(json_file)
        data = ret[name_first][name_second]
        return data
def revise_json(name_first,name_second,zhi):
    with open('pwd.json',"r",encoding="utf-8") as json_file:
        data = json.load(json_file)
    # 修改Python对象
    data[name_first][name_second] = zhi
    # 将修改后的对象写入JSON文件
    with open('pwd.json', "w",encoding="utf-8") as json_file:
        json.dump(data, json_file)
#############################################################################################
def read_user_pwd(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def login(username, password, user_credentials):
    for user_id, user_info in user_credentials.items():
        if user_info.get('name') == username and user_info.get('pwd') == password:
            return True, user_id
    return False, None
def refrence_phone(phone_number,user_credentials):
    for user_id, user_info in user_credentials.items():
        if user_info.get("phone_id") == phone_number:
            return True
    return False
def refrence_name(username, user_credentials):
    for user_id, user_info in user_credentials.items():
        if user_info.get('name') == username:
            return True
    return False
#############################################################################################
def add_new_user(file_path,name, pwd, phone_id):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # 获取当前最后一行数据的id_num的num值
    last_id = max([int(key.split('_')[1]) for key in data.keys()])

    # 构建新的id_num和数据
    new_id = "id_" + str(last_id + 1)
    new_entry = {"name": name, "pwd": pwd, "phone_id": phone_id}

    # 添加新的数据到JSON对象
    data[new_id] = new_entry

    # 写回到文件
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def opentxt(num):
    if num == 'info':
        txt_info = open('./info.txt', 'r')
        for line in txt_info.readlines():
            line = line.strip()
            k = line.split(' ')[0]
            l = line.split(' ')[1]
            user_info[k] = l

            txt_info.close()
    if num == 'phonenumber':
        txt_phonenumber = open('./phonenumber.txt','r')
        for line in txt_phonenumber.readlines():
            line = line.strip()
            k = line.split(' ')[0]
            j = line.split(' ')[1]
            user_phonenumber[k] = j

            txt_phonenumber.close()
    if num == 'text':
        ''
        txt_text = open('./text.txt','r')
        for line in txt_text.readlines():
            line = line.strip()
            k = line.split(' ')[0]
            j = line.split(' ')[1]
            user_text[k] = j

            txt_text.close()

def writetxt(num):
    if num == 'info':
        txt_info = open('./info.txt', 'a')
        for k, v in user_info.items():
            txt_info.write(str(k) + ' ' + str(v) + '\n')

        txt_info.close()
    if num == 'phonenumber':
        txt_phonenumber = open('./phonenumber.txt', 'a')
        for k, v in user_phonenumber.items():
            txt_phonenumber.write(str(k) + ' ' + str(v) + '\n')

        txt_phonenumber.close()
def writetxt_1(num):
    if num == 'info':
        txt_info = open('./info.txt', 'a')
        txt_info.write(str(username) + ' ' + str(password) + '\n')

        txt_info.close()
    if num == 'phonenumber':
        txt_phonenumber = open('./phonenumber.txt', 'a')
        txt_phonenumber.write(str(username) + ' ' + str(phonenumber) + '\n')


def showFrame(name):
    frame = name(parent=None)
    frame.Show()
class MyTooltip(wx.PopupWindow):
    def __init__(self, parent, text):
        super(MyTooltip, self).__init__(parent)
        self.SetBackgroundColour(wx.Colour('GhostWhite'))  # 设置背景颜色

        self.static_text = wx.StaticText(self, label=text, pos=(5, 5))
        self.static_text.Wrap(200)  # 设置文本控件的宽度限制

        # 获取文本控件的最佳大小，并设置气泡的尺寸
        text_width, text_height = self.static_text.GetBestSize()
        self.SetSize(text_width + 10, text_height + 10)
class Zhuce(wx.Frame):
    '登录界面'
    def __init__(self, parent):
        wx.Frame.__init__(self, parent,-1, size=(700, 605))
        self.pnl = wx.Panel(self)
        self.Center()
        self.SetMinSize((700,605))
        self.SetMaxSize((700,605))
        # 创建面板

        self.LoginInterface()


        icon_warn = wx.Bitmap(r".\icon\warning.png", wx.BITMAP_TYPE_PNG)
        self.btn_warn = wx.BitmapButton(self.pnl, wx.ID_ANY, icon_warn,pos=(0,0),size=(55,60),style=wx.NO_BORDER)
        icon_xiugai = wx.Bitmap(r".\icon\Xiugai.png", wx.BITMAP_TYPE_PNG)
        btn_xiugai = wx.BitmapButton(self.pnl, wx.ID_ANY, icon_xiugai,pos=(455,500),size=(75,60))
        icon_new_person = wx.Bitmap(r".\icon\new_person.png", wx.BITMAP_TYPE_PNG)
        btn_new_person = wx.BitmapButton(self.pnl, wx.ID_ANY, icon_new_person,pos=(530,500),size=(75,60))
        icon_exit = wx.Bitmap(r".\icon\exit.png", wx.BITMAP_TYPE_PNG)
        btn_exit = wx.BitmapButton(self.pnl, wx.ID_ANY, icon_exit,pos=(605,500),size=(75,60))

        self.btn_warn.Bind(wx.EVT_BUTTON,self.Warning)
        btn_exit.Bind(wx.EVT_BUTTON,self.OnclickCancel)
        btn_new_person.Bind(wx.EVT_BUTTON,self.OnclickZhuCe)
        btn_xiugai.Bind(wx.EVT_BUTTON,self.OnclickXiuGai)

        self.btn_warn.Bind(wx.EVT_ENTER_WINDOW, self.on_mouse_hover)
        self.btn_warn.Bind(wx.EVT_LEAVE_WINDOW, self.on_mouse_leave)


        self.tooltip = None
    def Warning(self,event):
        ''
        showFrame(Warning)
    def LoginInterface(self):
        # 创建垂直方向box布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        #################################################################################
        # 创建logo静态文本，设置字体属性
        logo = wx.StaticText(self.pnl, label="管 理 系 统")
        font = logo.GetFont()
        font.PointSize += 30
        font = font.Bold()
        logo.SetFont(font)
        # 添加logo静态文本到vbox布局管理器
        vbox.Add(logo, proportion=0, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=180)
        #################################################################################
        # 创建静态框
        sb_username = wx.StaticBox(self.pnl, label="用户名")
        sb_password = wx.StaticBox(self.pnl, label="密  码")
        # 创建水平方向box布局管理器
        hsbox_username = wx.StaticBoxSizer(sb_username, wx.HORIZONTAL)
        hsbox_password = wx.StaticBoxSizer(sb_password, wx.HORIZONTAL)
        # 创建用户名、密码输入框
        self.user_name = wx.TextCtrl(self.pnl, size=(210, 25))
        self.user_password = wx.TextCtrl(self.pnl, size=(210, 25))
        # 添加用户名和密码输入框到hsbox布局管理器
        hsbox_username.Add(self.user_name, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_password.Add(self.user_password, 0, wx.EXPAND | wx.BOTTOM, 5)
        # 将水平box添加到垂直box
        vbox.Add(hsbox_username, proportion=0, flag=wx.CENTER)
        vbox.Add(hsbox_password, proportion=0, flag=wx.CENTER)
        #################################################################################
        # 创建水平方向box布局管理器
        hbox = wx.BoxSizer()
        # 创建登录按钮、绑定事件处理
        login_button = wx.Button(self.pnl, label="登录", size=(80, 25))
        login_button.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        # 添加登录按钮到hbox布局管理器
        hbox.Add(login_button, 0, flag=wx.EXPAND | wx.TOP, border=5)
        # 将水平box添加到垂直box
        vbox.Add(hbox, proportion=0, flag=wx.CENTER)
        #################################################################################
        # 设置面板的布局管理器vbox
        self.pnl.SetSizer(vbox)

    def OnclickSubmit(self, event):
        "单击 “确定” 按钮， 执行方法"
        username = self.user_name.GetValue()
        password = self.user_password.GetValue()
        user_database = read_user_pwd('pwd.json')

        success = login(username, password, user_database)

        if username == "" or password == "":
            message = '用户名或密码不能为空'
            time.sleep(0.1)
            wx.MessageBox(message)
        elif success:
            showFrame(MyFrame)
            self.Destroy()
        else:
            message = '用户名或密码错误'
            wx.MessageBox(message)
    def OnclickCancel(self, event):
        "单机取消按钮，执行方法"
        self.user_name.SetValue("")
        self.user_password.SetValue("")
        os._exit(0)
    def OnclickXiuGai(self,event):
        ''
        showFrame(XiuGai)
    def OnclickZhuCe(self, event):
        ''
        showFrame(NewPerson)
    def on_mouse_hover(self, event):
        if not self.tooltip:
            self.tooltip = MyTooltip(self, "该版本为测试版本Beta-v0.1"+"\n"+"制作者:54行")
        x, y = self.btn_warn.GetScreenPosition()
        self.tooltip.SetPosition((x+self.btn_warn.GetSize().width, y ))
        self.tooltip.Show()

    def on_mouse_leave(self, event):
        if self.tooltip:
            self.tooltip.Destroy()
            self.tooltip = None
class Warning(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, title='警告', size=(400, 260))
        self.panel = wx.Panel(self)
class NewPerson(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, title='注册账号', size=(400, 260))
        self.Center()
        panel_zhuce = wx.Panel(self)

        self.title = wx.StaticText(panel_zhuce, label='注册账号', pos=(140, 20))
        self.label_user = wx.StaticText(panel_zhuce, label='用户名:', pos=(50, 50))
        self.text_user = wx.TextCtrl(panel_zhuce, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel_zhuce, pos=(50, 95), label='密   码:')
        self.text_password = wx.TextCtrl(panel_zhuce, pos=(100, 95), size=(235, 25), style=wx.TE_LEFT)
        self.label_phonenumber = wx.StaticText(panel_zhuce, label='手机号:', pos=(50, 140))
        self.text_phonenumber = wx.TextCtrl(panel_zhuce, pos=(100, 140), size=(235, 25), style=wx.TE_LEFT)


        self.bt_confirm = wx.Button(panel_zhuce, label="注册", pos=(100, 170))
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickQueding)
        self.bt_cancel = wx.Button(panel_zhuce, label='取消', pos=(190, 170))
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickQuxiao)

    def OnclickQueding(self,event):
        "显示消息注册成功"
        message =""
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()
        phonenumber = self.text_phonenumber.GetValue()

        user_database = read_user_pwd('pwd.json')
        success_phone = refrence_phone(phonenumber, user_database)
        success_name = refrence_name(username, user_database)

        if len(phonenumber)>= 11 and not success_phone and not success_name:
            add_new_user('pwd.json',username,password,phonenumber)
            message = '注册成功'
            self.Destroy()
        elif success_phone:
            ''
            message = '手机号重复，请重新注册'
        elif success_name:
            message = '用户名重复，请重新注册'
        else:
            self.text_user.SetLabel('')
            message = '手机号格式错误，请重新注册'


        wx.MessageBox(message)
    def OnclickQuxiao(self,event):
        "直接退出"
        self.text_user.SetValue("")
        self.text_password.SetValue("")
        sleep(0.1)
        self.Destroy()
class XiuGai(wx.Frame):
    ''
    def __init__(self, parent):

        wx.Frame.__init__(self, parent, -1, title='修改密码——1', size=(400, 260) )
        # 创建面板
        panel = wx.Panel(self)
        self.Center()
        self.title = wx.StaticText(panel, label='修改密码', pos=(50, 15))
        self.title.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.title.SetForegroundColour('blue')
        self.label_user = wx.StaticText(panel, label='用户名:', pos=(50, 50))
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, pos=(50, 95), label='密   码:')
        self.text_password = wx.TextCtrl(panel, pos=(100, 95), size=(235, 25), style=wx.TE_LEFT)
        self.label_phonenumber = wx.StaticText(panel, label='手机号:', pos=(50, 140))
        self.text_phonenumber = wx.TextCtrl(panel, pos=(100, 140), size=(235, 25), style=wx.TE_LEFT)

        self.bt_confirm = wx.Button(panel, label="确定", pos=(100, 170))
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickQueding)
        self.bt_cancel = wx.Button(panel, label='取消', pos=(190, 170))
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickQuxiao)

    def OnclickQueding(self,event):
        ''
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()
        phonenumber = self.text_phonenumber.GetValue()

        opentxt('info')
        opentxt('phonenumber')
        if username in user_info.keys() and password in user_info.values() and phonenumber in user_phonenumber.values():
            frame = XGpassword(parent=None, id=1)
            frame.Show()
        elif username == '' or password == '':
            message = '用户名或密码为空，请重新输入'
            wx.MessageBox(message)
        elif username not in user_info.keys() or password not in user_info.values():
            message = '用户名或密码错误'
            wx.MessageBox(message)
        elif phonenumber not in user_phonenumber.values():
            message = '手机号错误'
            wx.MessageBox(message)
    def OnclickQuxiao(self,event):
        ''
        time.sleep(0.1)
        self.Destroy()
class XGpassword(XiuGai):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, title='请确定您的新密码', size=(400, 260))
        self.Center()
        # 创建面板
        panel = wx.Panel(self)
        self.label_pwd1 = wx.StaticText(panel, label='原密码:', pos=(50, 50))
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)
        self.label_pwd2 = wx.StaticText(panel, pos=(50, 95), label='新密码:')
        self.text_password_1 = wx.TextCtrl(panel, pos=(100, 95), size=(235, 25), style=wx.TE_LEFT)

        self.bt_qued= wx.Button(panel, label="确定", pos=(100, 140))
        self.bt_qued.Bind(wx.EVT_BUTTON, self.OnclickQue)
        self.bt_qux = wx.Button(panel, label='取消', pos=(190, 140))
        self.bt_qux.Bind(wx.EVT_BUTTON, self.OnclickQu)

    def OnclickQue(self,event):
        ''
        print(username)
    def OnclickQu(self,event):
        ''
        time.sleep(0.1)
        self.Destroy()
class MuLu(wx.Frame):
    def __init__(self, parent, id):

        wx.Frame.__init__(self, parent, -1, title='目  录', size=(400, 220))
        self.Center()
        # 创建面板
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel,label="目  录",pos=(20,10))
        self.title.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.title.SetForegroundColour('Blue')
        self.bt_confirm = wx.Button(panel, label="备忘录",pos=(19,40),size=(80,60))
        self.bt_confirm.Bind(wx.EVT_BUTTON,self.OnclickBeiwang)
        self.bt_cancel = wx.Button(panel,label='密码管理',pos=(109,40),size=(80,60))
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickMiMa)
        # self.bt_zhuce = wx.Button(panel, label='标  签',pos=(199,40),size=(80,60))
        # self.bt_zhuce.Bind(wx.EVT_BUTTON,self.OnclickBiaoqian)
        # self.bt_zengjia = wx.Button(panel, label='➕',pos=(289,40),size=(80,60))
        # self.bt_zengjia.Bind(wx.EVT_BUTTON,self.OnclickZengjia)

    def OnclickBeiwang(self, event):
        ''
        showFrame(Beiw)

    def OnclickMiMa(self, event):
        ''
        showFrame(MiMa)
class MyFrame(wx.Frame):
    def __init__(self, parent):
        super(MyFrame, self).__init__(parent, -1, title='主界面', size=(700, 570),style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)
        self.Center()
        self.caidan_init_UI()
        self.SetMinSize((700,570))
        self.SetMaxSize((700,570))
        self.OperationInterface()
        self.Frame_Ui()
    def Frame_Ui(self):
        '主界面的ui设置'
        icon_Home = wx.Bitmap(r".\icon\Home.png", wx.BITMAP_TYPE_PNG)
        btn_icon = wx.BitmapButton(self.lpanel, wx.ID_ANY, icon_Home,pos=(0,0),size=(75,60))
        btn_icon.Bind(wx.EVT_BUTTON, self.panel_destory)
        icon_Shezhi = wx.Bitmap(r".\icon\Shezhi.png", wx.BITMAP_TYPE_PNG)
        btn_icon = wx.BitmapButton(self.lpanel, wx.ID_ANY, icon_Shezhi,pos=(0,430),size=(75,60))

        writer_txt = wx.StaticText(self.lpanel,label='Beta_v0.1',pos=(5,490))

        hhh = wx.StaticText(self.rpanel,label='界面1',pos=(5,10))


    def panel_destory(self,event):
        # 移除当前rpanel的内容
        for child in self.rpanel.GetChildren():
            child.Destroy()

        hhh = wx.StaticText(self.rpanel, label='界面2', pos=(5, 10))
        self.rpanel.Layout()

    def caidan_init_UI(self):
        """
        在这里添加控件
        """

        # 创建一个菜单
        menu_file = wx.Menu()

        # 创建一个菜单项
        menu_item_new = wx.MenuItem(menu_file, wx.ID_ANY, "新建\tCtrl+N", "新建一个便签")
        # 添加菜单项到菜单
        menu_file.Append(menu_item_new)

        # 也可以直接添加菜单项
        menu_item_re = menu_file.Append(wx.ID_ANY, "刷新","使窗口刷新")
        menu_item_open = menu_file.Append(wx.ID_ANY, "打开\tCtrl+O", "打开一个txt文件")
        menu_item_save = menu_file.Append(wx.ID_ANY, "保存\tCtrl+S", "保存txt文件")
        menu_item_saveas = menu_file.Append(wx.ID_ANY, "另存为\tCtrl+Shift+S", "保存txt文件")
        menu_file.AppendSeparator()
        menu_item_exit = menu_file.Append(wx.ID_ANY, "退出\tEsc", "退出程序")

        # 创建“查看”菜单
        menu_view = wx.Menu()
        menu_scale = wx.Menu()
        menu_item_zoomin = menu_scale.Append(wx.ID_ANY, "放大\tCtrl+加号")
        menu_item_zoomout = menu_scale.Append(wx.ID_ANY, "缩小\tCtrl+减号")
        menu_item_original = menu_scale.Append(wx.ID_ANY, "还原默认缩放\tCtrl+0")
        menu_item_scale = menu_view.AppendSubMenu(menu_scale, "缩放")
        menu_item_status = menu_view.AppendCheckItem(wx.ID_ANY, "状态栏")
        menu_item_wrap = menu_view.AppendCheckItem(wx.ID_ANY, "自动换行")
        menu_item_radio1 = menu_view.AppendRadioItem(wx.ID_ANY, "radio1")
        menu_item_radio2 = menu_view.AppendRadioItem(wx.ID_ANY, "radio2")

        # 创建"功能"菜单
        menu_daka = wx.Menu()
        menu_daka_zi = wx.Menu()
        menu_item_historyDaka = menu_daka.Append(wx.ID_ANY, "打卡记录","打开你的历史打卡记录")
        menu_item_beiwang = menu_daka.Append(wx.ID_ANY, "备忘录","打开备忘录（有提醒功能）")


        # 创建一个菜单栏
        self.menu_bar = wx.MenuBar()
        # 添加菜单到菜单栏
        self.menu_bar.Append(menu_file, "文件")
        self.menu_bar.Append(menu_view, "查看")
        self.menu_bar.Append(menu_daka, "功能")

        # 为窗框设置菜单栏
        self.SetMenuBar(self.menu_bar)
        # self.bind = self.Bind(wx.EVT_MENU, self.on_new, menu_item_new)
        self.bind = self.Bind(wx.EVT_MENU, self.Exit_all,menu_item_exit)
        # self.bind = self.Bind(wx.EVT_MENU, self.SetZhuangtai,menu_item_status)
        # self.Bind(wx.EVT_MENU, self.re,menu_item_re)
        # self.Bind(wx.EVT_MENU, self.NewBianqian ,menu_item_new)
    def OperationInterface(self):
        '创建分割窗口'
        self.split_mult = wx.SplitterWindow(self, style=wx.SP_LIVE_UPDATE, size=self.Size)
        self.lpanel = wx.Panel(self.split_mult, size=(200,self.split_mult.Size[1]), style=wx.SIMPLE_BORDER)
        self.rpanel = wx.ScrolledWindow(self.split_mult, style=wx.SIMPLE_BORDER, size=(602, self.split_mult.Size[1]))
        self.split_mult.SplitVertically(self.lpanel, self.rpanel, 160)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.split_mult, 1, flag=wx.EXPAND)  # 自动缩放
        self.SetSizer(sizer)
    def Exit_all(self, event):
        ''
        os._exit(0)
if __name__ == '__main__':
    app = wx.App()
    # frame = MyFrame(parent=None)
    frame = Zhuce(parent=None)
    frame.Show()

    app.MainLoop()
    print('成功退出')