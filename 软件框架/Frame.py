import wx,json,os,sys,io
from time import *
from PIL import Image, ImageOps
import wx.lib.buttons as buttons


################################################################################################
def uiread(name):
    with open('user_influence.json', "r",encoding="utf-8") as json_file:
        ret = json.load(json_file)
        data = ret[name]
        return data
def uirevise(name,zhi):
    with open('user_influence.json', "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    data[name] = zhi
    with open('user_influence.json', "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)
def all_color_set():
    ui_module = uiread("module")
    if ui_module == '默认模式':
        back_color = (248,248,245) #背景颜色
        l_color = (248,248,245) #lpanel颜色
        bt_color = (248,248,245) #按钮颜色
        dc_color = (102,178,255) #绘画及其他颜色
        kuang_color = (255,255,255) #文本框颜色
        txt_color = (0,0,0) #字体颜色

        bit_bt = './icon/gou_blue.png'

    elif ui_module == '夜间模式':
        back_color = (105,105,105)
        l_color = (139,126,102)
        bt_color = (169,169,169)
        dc_color = (139,126,102)
        kuang_color = (220,220,220)
        txt_color = (255,255,255)

        bit_bt = './icon/gou_brown.png'
    return back_color,l_color,bt_color,dc_color,kuang_color,txt_color,bit_bt,ui_module

back_color,l_color,bt_color,dc_color,kuang_color,txt_color,bit_bt,ui_module = all_color_set()

# print(ui_module)


################################################################################################
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
    with open('pwd.json', "r",encoding="utf-8") as json_file:
        ret = json.load(json_file)
        data = ret[name_first][name_second]
        return data
def revise_json(name_first,name_second,zhi):
    with open('pwd.json', "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    # 修改Python对象
    data[name_first][name_second] = zhi
    # 将修改后的对象写入JSON文件
    with open('pwd.json', "w", encoding="utf-8") as json_file:
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

def refrence_phone(phone_number,username,user_credentials):
    for user_id, user_info in user_credentials.items():
        if user_info.get("phone_id") == phone_number and user_info.get('name') == username:
            return True,user_id
    return False,user_id

def refrence_name(username, user_credentials):
    for user_id, user_info in user_credentials.items():
        if user_info.get('name') == username:
            return True
    return False

def refrence_password(password, user_credentials):
    for user_id, user_info in user_credentials.items():
        if user_info.get('pwd') == password:
            return True,user_id
    return False,user_id
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
def showFrame(name):
    frame = name(parent=None)
    frame.Show()
class MyTooltip(wx.PopupWindow):
    def __init__(self, parent, text):
        super(MyTooltip, self).__init__(parent)
        # self.SetBackgroundColour(wx.Colour(back_color))  # 设置背景颜色

        self.static_text = wx.StaticText(self, label=text, pos=(5, 5))
        self.static_text.Wrap(200)  # 设置文本控件的宽度限制

        # 获取文本控件的最佳大小，并设置气泡的尺寸
        text_width, text_height = self.static_text.GetBestSize()
        self.SetSize(text_width + 10, text_height + 10)
class LoginFace(wx.Frame):
    '登录界面'
    def __init__(self, parent):
        wx.Frame.__init__(self, parent,-1, size=(700, 605),title='登录界面')
        self.pnl = wx.Panel(self)
        self.color_get()
        self.pnl.SetBackgroundColour(wx.Colour(self.back_color))
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

        btn_exit.Bind(wx.EVT_BUTTON,self.OnclickCancel)
        btn_new_person.Bind(wx.EVT_BUTTON,self.OnclickZhuCe)
        btn_xiugai.Bind(wx.EVT_BUTTON,self.OnclickXiuGai)

        self.btn_warn.SetBackgroundColour(wx.Colour(self.back_color))
        btn_xiugai.SetBackgroundColour(wx.Colour(self.bt_color))
        btn_new_person.SetBackgroundColour(wx.Colour(self.bt_color))
        btn_exit.SetBackgroundColour(wx.Colour(self.bt_color))

        self.user_name.SetBackgroundColour(wx.Colour(self.kuang_color))
        self.user_password.SetBackgroundColour(wx.Colour(self.kuang_color))



        self.btn_warn.Bind(wx.EVT_ENTER_WINDOW, self.on_mouse_hover)
        self.btn_warn.Bind(wx.EVT_LEAVE_WINDOW, self.on_mouse_leave)


        self.tooltip = None
        self.logo_set()
    def color_get(self):
        self.back_color, self.l_color, self.bt_color, self.dc_color, self.kuang_color, self.txt_color, self.bit_bt, self.ui_module = all_color_set()
    def logo_set(self):
        icon = wx.Icon(".\icon\logo.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)
    def on_image_button_click(self,event):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.image_button.SetBitmap(wx.Bitmap(self.image_paths[self.current_image_index], wx.BITMAP_TYPE_ANY))

    def LoginInterface(self):
        # 创建垂直方向box布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        #################################################################################
        # 创建logo静态文本，设置字体属性
        logo = wx.StaticText(self.pnl, label="管 理 系 统")
        logo.SetForegroundColour(wx.Colour(self.txt_color))
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
        self.user_password = wx.TextCtrl(self.pnl, size=(210, 25),style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
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

        login_button.SetBackgroundColour(wx.Colour(self.bt_color))
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

        success,user_id = login(username, password, user_database)

        if username == "" or password == "":
            message = '用户名或密码不能为空'
            sleep(0.1)
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
        super(NewPerson, self).__init__(parent, -1, title='注册账号', size=(300, 310),
                                      style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)
        self.color_get()
        self.Center()
        self.pnl = wx.Panel(self)
        self.pnl.SetBackgroundColour(wx.Colour(self.back_color))
        self.LoginInterface()
        self.logo_set()
    def color_get(self):
        self.back_color, self.l_color, self.bt_color, self.dc_color, self.kuang_color, self.txt_color, self.bit_bt, self.ui_module = all_color_set()
    def logo_set(self):
        icon = wx.Icon(".\icon\logo.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)
    def LoginInterface(self):
        # 创建垂直方向box布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        #################################################################################
        # 创建logo静态文本，设置字体属性
        logo = wx.StaticText(self.pnl, label="注 册")
        logo.SetForegroundColour(wx.Colour(self.txt_color))
        font = logo.GetFont()
        font.PointSize += 10
        font = font.Bold()
        logo.SetFont(font)
        # 添加logo静态文本到vbox布局管理器
        vbox.Add(logo, proportion=0, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=20)
        #################################################################################
        # 创建静态框
        sb_username = wx.StaticBox(self.pnl, label="用户名")
        sb_password = wx.StaticBox(self.pnl, label="密  码")
        sb_phone = wx.StaticBox(self.pnl, label='手机号')
        # 创建水平方向box布局管理器
        hsbox_username = wx.StaticBoxSizer(sb_username, wx.HORIZONTAL)
        hsbox_password = wx.StaticBoxSizer(sb_password, wx.HORIZONTAL)
        hsbox_phone = wx.StaticBoxSizer(sb_phone, wx.HORIZONTAL)
        # 创建用户名、密码输入框
        self.user_name = wx.TextCtrl(self.pnl, size=(210, 25))
        self.user_password = wx.TextCtrl(self.pnl, size=(210, 25))
        self.user_phone = wx.TextCtrl(self.pnl, size=(210,25))

        self.user_name.SetBackgroundColour(wx.Colour(self.kuang_color))
        self.user_password.SetBackgroundColour(wx.Colour(self.kuang_color))
        self.user_phone.SetBackgroundColour(wx.Colour(self.kuang_color))
        # 添加用户名和密码输入框到hsbox布局管理器
        hsbox_username.Add(self.user_name, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_password.Add(self.user_password, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_phone.Add(self.user_phone, 0, wx.EXPAND | wx.BOTTOM, 5)
        # 将水平box添加到垂直box
        vbox.Add(hsbox_username, proportion=0, flag=wx.CENTER)
        vbox.Add(hsbox_password, proportion=0, flag=wx.CENTER)
        vbox.Add(hsbox_phone, proportion=0, flag= wx.CENTER)
        #################################################################################
        # 创建水平方向box布局管理器
        hbox = wx.BoxSizer()
        # 创建登录按钮、绑定事件处理
        login_button = wx.Button(self.pnl, label="确定", size=(80, 25))
        login_button.Bind(wx.EVT_BUTTON,self.OnclickQueding)
        login_button.SetBackgroundColour(wx.Colour(bt_color))
        # 添加登录按钮到hbox布局管理器
        hbox.Add(login_button, 0, flag=wx.EXPAND | wx.TOP, border=5)
        # 将水平box添加到垂直box
        vbox.Add(hbox, proportion=0, flag=wx.CENTER)
        #################################################################################
        # 设置面板的布局管理器vbox
        self.pnl.SetSizer(vbox)
    def OnclickQueding(self,event):
        "显示消息注册成功"
        message =""
        username = self.user_name.GetValue()
        password = self.user_password.GetValue()
        phonenumber = self.user_phone.GetValue()

        user_database = read_user_pwd('pwd.json')
        success_phone,user_id = refrence_phone(phonenumber,username, user_database)
        # success_name = refrence_name(username, user_database)

        if len(phonenumber)>= 11 and not success_phone:
            add_new_user('pwd.json', username, password, phonenumber)
            message = '注册成功'
            self.Destroy()
        elif success_phone:
            ''
            message = '手机号或用户名重复，请重新注册'
        else:
            self.user_phone.SetLabel('')
            message = '手机号格式错误，请重新注册'


        wx.MessageBox(message)
    def OnclickQuxiao(self,event):
        "直接退出"
        self.text_user.SetValue("")
        self.text_password.SetValue("")
        sleep(0.1)
        self.Destroy()


class XiuGai(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, title='密码修改', size=(300, 260))
        back_color, l_color, bt_color, dc_color, kuang_color, txt_color, bit_bt, ui_module = all_color_set()
        self.Center()  # 窗口居中
        self.color_get()
        self.pnl = wx.Panel(self)  # 创建面板，只需要在初始化时创建一次
        self.pnl.SetBackgroundColour(wx.Colour(back_color))
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        self.LoginInterface()
    def color_get(self):
        self.back_color, self.l_color, self.bt_color, self.dc_color, self.kuang_color, self.txt_color, self.bit_bt, self.ui_module = all_color_set()
    def logo_set(self):
        icon = wx.Icon(".\icon\logo.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

    def LoginInterface(self):
        logo = wx.StaticText(self.pnl, label="修改密码")
        logo.SetForegroundColour(wx.Colour(self.txt_color))
        font = logo.GetFont()
        font.PointSize += 10
        font = font.Bold()
        logo.SetFont(font)
        self.vbox.Add(logo, proportion=0, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=20)

        sb_username = wx.StaticBox(self.pnl, label="用户名")
        sb_phone = wx.StaticBox(self.pnl, label='手机号')
        hsbox_username = wx.StaticBoxSizer(sb_username, wx.HORIZONTAL)
        hsbox_phone = wx.StaticBoxSizer(sb_phone, wx.HORIZONTAL)
        self.user_name = wx.TextCtrl(self.pnl, size=(210, 25))
        self.user_phone = wx.TextCtrl(self.pnl, size=(210, 25))

        self.user_phone.SetBackgroundColour(wx.Colour(self.kuang_color))
        self.user_name.SetBackgroundColour(wx.Colour(self.kuang_color))

        hsbox_username.Add(self.user_name, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_phone.Add(self.user_phone, 0, wx.EXPAND | wx.BOTTOM, 5)
        self.vbox.Add(hsbox_username, proportion=0, flag=wx.CENTER)
        self.vbox.Add(hsbox_phone, proportion=0, flag=wx.CENTER)

        self.hbox = wx.BoxSizer()

        login_button = wx.Button(self.pnl, label="确定", size=(80, 25))
        login_button.Bind(wx.EVT_BUTTON, self.OnclickQueding)
        login_button.SetBackgroundColour(wx.Colour(bt_color))
        self.hbox.Add(login_button, 0, flag=wx.EXPAND | wx.TOP, border=5)
        self.vbox.Add(self.hbox, proportion=0, flag=wx.CENTER)
        self.pnl.SetSizer(self.vbox)

    def OnclickQueding(self, event):
        username = self.user_name.GetValue()
        phonenumber = self.user_phone.GetValue()
        if username == '' or phonenumber == '':
            message = '用户名或密码为空，请重新输入'
            wx.MessageBox(message)
        else:
            user_database = read_user_pwd('pwd.json')
            success_phone, self.the_user_id = refrence_phone(phonenumber,username, user_database)
            the_user_id = self.the_user_id
            # print(self.the_user_id)
            success_name = refrence_name(username, user_database)

            if success_name and success_phone:
                self.pnl.SetSizer(None)
                self.clear_panel()
                self.Layout()
                self.XGpassword()
            if not success_name or not success_phone:
                message = '用户名或手机号错误'
                wx.MessageBox(message)
    def XGpassword(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        logo = wx.StaticText(self.pnl, label="修改密码")
        logo.SetForegroundColour(wx.Colour(txt_color))
        font = logo.GetFont()
        font.PointSize += 10
        font = font.Bold()
        logo.SetFont(font)
        vbox.Add(logo, proportion=0, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=20)
        sb_old_pwd = wx.StaticBox(self.pnl, label="原密码")
        sb_new_pwd = wx.StaticBox(self.pnl, label='新密码')
        hsbox_old_pwd = wx.StaticBoxSizer(sb_old_pwd, wx.HORIZONTAL)
        hsbox_new_pwd = wx.StaticBoxSizer(sb_new_pwd, wx.HORIZONTAL)
        self.old_password = wx.TextCtrl(self.pnl, size=(210, 25))
        self.new_password = wx.TextCtrl(self.pnl, size=(210,25))

        self.old_password.SetBackgroundColour(wx.Colour(self.kuang_color))
        self.new_password.SetBackgroundColour(wx.Colour(self.kuang_color))

        hsbox_old_pwd.Add(self.old_password, 0, wx.EXPAND | wx.BOTTOM, 5)

        hsbox_new_pwd.Add(self.new_password, 0, wx.EXPAND | wx.BOTTOM, 5)
        vbox.Add(hsbox_old_pwd, proportion=0, flag=wx.CENTER)
        vbox.Add(hsbox_new_pwd, proportion=0, flag= wx.CENTER)
        hbox = wx.BoxSizer()

        login_button = wx.Button(self.pnl, label="确定", size=(80, 25))
        login_button.Bind(wx.EVT_BUTTON,self.OnclickQue)
        login_button.SetBackgroundColour(wx.Colour(self.bt_color))

        hbox.Add(login_button, 0, flag=wx.EXPAND | wx.TOP, border=5)
        vbox.Add(hbox, proportion=0, flag=wx.CENTER)
        self.pnl.SetSizer(vbox)
        self.pnl.Layout()
    def OnclickQue(self,event):
        ''
        # print('queding_2')
        old_password = self.old_password.GetValue()
        new_password = self.new_password.GetValue()
        # print(f'{self.the_user_id}hhhhhh')
        yuan_pwd = read_json(self.the_user_id,"pwd")
        # print(yuan_pwd)
        # print(self.the_user_id)
        if yuan_pwd == old_password:
            if old_password == new_password:
                message = '新密码不能与原密码一致'
            elif new_password != old_password:
                revise_json(self.the_user_id,"pwd",new_password)
                message='修改成功'
                self.Destroy()
            else:
                print('???')
        else:
            print(1111)
            message='原密码错误'
        wx.MessageBox(message)
    def clear_panel(self):
        for child in self.pnl.GetChildren():
            child.Destroy()

    def OnclickQuxiao(self,event):
        ''
        sleep(0.1)
        self.Destroy()

class MyFrame(wx.Frame):
    def __init__(self, parent):
        super(MyFrame, self).__init__(parent, -1, title='主界面', size=(700, 590),style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)
        self.color_get()
        self.Center()
        self.logo_set()
        self.font_cu = wx.Font(18,wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.font = wx.Font(12,wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.font_sys = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        self.SetMinSize((700,590))
        self.SetMaxSize((700,590))
        self.OperationInterface()
        self.Frame_Ui()
        self.tooltip = None
        self.tooltip_history = None
        self.Show()


    def color_get(self):
        self.back_color, self.l_color, self.bt_color, self.dc_color, self.kuang_color, self.txt_color, self.bit_bt, self.ui_module = all_color_set()
    def history_hover(self, event):
        if not self.tooltip_history:
            self.tooltip_history = MyTooltip(self, "查看历史头像")
        x, y = self.history_bt.GetScreenPosition()
        self.tooltip_history.SetPosition((x+self.history_bt.GetSize().width, y))
        self.tooltip_history.Show()

    def history_leave(self, event):
        if self.tooltip_history:
            self.tooltip_history.Destroy()
            self.tooltip_history = None
    def on_mouse_hover(self, event):
        if not self.tooltip:
            self.tooltip = MyTooltip(self, "  重启  ")
        x, y = self.apply.GetScreenPosition()
        self.tooltip.SetPosition((x+1, y-self.apply.GetSize().height ))
        self.tooltip.Show()

    def on_mouse_leave(self, event):
        if self.tooltip:
            self.tooltip.Destroy()
            self.tooltip = None
    def logo_set(self):
        icon = wx.Icon(".\icon\logo.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

        self.Show(True)
    def Frame_Ui(self):
        '主界面的ui设置'
        self.default_color = self.bt_color
        self.custom_color = wx.Colour(self.dc_color)


        icon_Home = wx.Bitmap(r".\icon\Home.png", wx.BITMAP_TYPE_PNG)
        self.btn_home = wx.BitmapButton(self.lpanel, wx.ID_ANY, icon_Home,pos=(0,0),size=(75,60))
        self.btn_home.Bind(wx.EVT_BUTTON, self.onbtn_home)

        self.btn_home.SetBackgroundColour(self.custom_color)

        icon_User = wx.Bitmap(r".\icon\user.png", wx.BITMAP_TYPE_PNG)
        self.btn_user = wx.BitmapButton(self.lpanel, wx.ID_ANY, icon_User,pos=(0,60),size=(75,60))
        self.btn_user.Bind(wx.EVT_BUTTON, self.onbtn_user)

        icon_Shezhi = wx.Bitmap(r".\icon\Shezhi.png", wx.BITMAP_TYPE_PNG)
        self.btn_shezhi = wx.BitmapButton(self.lpanel, wx.ID_ANY, icon_Shezhi,pos=(0,430),size=(75,60))
        self.btn_shezhi.Bind(wx.EVT_BUTTON, self.onbtn_shezhi)


        icon_Out = wx.Bitmap(r".\icon\out.png", wx.BITMAP_TYPE_PNG)
        self.btn_out = wx.BitmapButton(self.lpanel, wx.ID_ANY, icon_Out,pos=(0,490),size=(75,40))
        self.btn_out.Bind(wx.EVT_BUTTON, self.onbtn_out)
        writer_txt = wx.StaticText(self.lpanel,label='Beta_v0.1',pos=(5,530))

        hhh = wx.StaticText(self.rpanel,label='界面Home',pos=(5,10))
        self.current_button = self.btn_home

        self.btn_home.SetBackgroundColour(wx.Colour(self.bt_color))
        self.btn_user.SetBackgroundColour(wx.Colour(self.bt_color))
        self.btn_shezhi.SetBackgroundColour(wx.Colour(self.bt_color))
        self.btn_out.SetBackgroundColour(wx.Colour(self.bt_color))

    def onbtn_out(self,event):
        self.Destroy()
        showFrame(LoginFace)
    def onbtn_user(self,event):
        self.set_button_color(self.btn_user)
        self.yincang()
        self.clear_rpanel()
        hhh = wx.StaticText(self.rpanel, label=' 用 户', pos=(5, 14))
        hhh.SetFont(self.font_cu)
        hhh.SetForegroundColour(wx.Colour(self.txt_color))
        hhh.SetBackgroundColour(wx.Colour(self.dc_color))
        icon_user_image = wx.Bitmap(r".\user\user.png",wx.BITMAP_TYPE_PNG)

        self.image_button = wx.BitmapButton(self.rpanel, wx.ID_ANY, wx.Bitmap(r".\user\user.png"),pos=(490,5),size=(64,64))
        self.image_button.Bind(wx.EVT_BUTTON, self.on_image_button_click)

        self.history_bt = wx.Button(self.rpanel,pos=(555,50),size=(18,18),label='H')
        self.history_bt.Bind(wx.EVT_BUTTON,self.ShowPNG)
        self.history_bt.Bind(wx.EVT_ENTER_WINDOW,self.history_hover)
        self.history_bt.Bind(wx.EVT_LEAVE_WINDOW,self.history_leave)

        self.history_directory = "history"  # 历史图片保存目录
        if not os.path.exists(self.history_directory):
            os.makedirs(self.history_directory)

        self.image_count = self.get_image_count()  # 读取历史图片数量


        self.on_paint()
        self.rpanel.Layout()
    def ShowPNG(self,event):
        app = ImageConverterApp()
        app.MainLoop()
    def resize_image(self, image_path, target_size):
        image = Image.open(image_path)
        image = image.resize(target_size, Image.LANCZOS)
        return image

    def copy_image_to_target(self, image_path, target_directory, target_name):
        target_path = os.path.join(target_directory, target_name)
        image = Image.open(image_path)
        image.save(target_path)

    def get_image_count(self):
        count = 0
        for filename in os.listdir(self.history_directory):
            if filename.endswith(".png"):
                count += 1
        return count
    def on_image_button_click(self, event):
        wildcard = "图片文件 (*.png;*.jpg)|*.png;*.jpg|所有文件 (*.*)|*.*"
        dlg = wx.FileDialog(self, "选择图片文件", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dlg.ShowModal() == wx.ID_OK:
            file_path = dlg.GetPath()

            target_directory = "user"  # 用户头像保存目录
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            self.image_count += 1
            target_name = "user.png"
            target_path = os.path.join(target_directory, target_name)

            # 修改图片格式为64x64并替换按钮图像
            image = self.resize_image(file_path, (64, 64))
            image.save(target_path)

            wx_image = wx.Image(target_path, wx.BITMAP_TYPE_ANY)
            bitmap = wx.Bitmap(wx_image)
            self.image_button.SetBitmap(bitmap)

            # 复制原图片到history文件夹中，并按历史图片数量递增命名
            history_target_name = f"{self.image_count}.png"
            self.copy_image_to_target(file_path, self.history_directory, history_target_name)

        dlg.Destroy()
    def ex_user_image(self):
        '切换头像'
        print(1)
        showFrame(User_image)

    def onbtn_home(self,event):
        # 移除当前rpanel的内容
        self.set_button_color(self.btn_home)
        self.yincang()
        self.clear_rpanel()
        hhh = wx.StaticText(self.rpanel, label='界面Home', pos=(5, 10))
        self.rpanel.Layout()
    def onbtn_shezhi(self,event):
        ''
        self.set_button_color(self.btn_shezhi)
        self.yincang()
        self.clear_rpanel()
        hhh = wx.StaticText(self.rpanel, label=' 设 置', pos=(5, 14))
        hhh.SetFont(self.font_cu)
        hhh.SetForegroundColour(wx.Colour(self.txt_color))
        hhh.SetBackgroundColour(wx.Colour(self.dc_color))
        self.ui_shezi()
        self.on_paint()

        self.rpanel.Layout()
    def ui_shezi(self):
        self.image_paths = ["./icon/not_gou.png", self.bit_bt]
        self.current_image_index = [0,0,0]
        txt_1 = wx.StaticText(self.rpanel,pos=(10,65),label='主题颜色：')
        txt_1.SetFont(self.font)
        self.choice_color = ["默认模式","夜间模式"]
        self.choice_box = wx.ComboBox(self.rpanel,pos=(120,58),choices=self.choice_color, style=wx.CB_DROPDOWN,size=(80,35))
        self.choice_box.SetValue(self.ui_module)
        self.choice_box.SetBackgroundColour(wx.Colour(self.kuang_color))

        self.image_button_2 = wx.BitmapButton(self.rpanel, wx.ID_ANY, wx.Bitmap(self.image_paths[0], wx.BITMAP_TYPE_ANY),style=wx.NO_BORDER,pos=(135,85))
        self.image_button_2.Bind(wx.EVT_BUTTON,self.png_ex)

        self.image_button_3 = wx.BitmapButton(self.rpanel, wx.ID_ANY, wx.Bitmap(self.image_paths[0], wx.BITMAP_TYPE_ANY),style=wx.NO_BORDER,pos=(135,115))
        self.image_button_3.Bind(wx.EVT_BUTTON,self.png_ex)

        self.image_button_4 = wx.BitmapButton(self.rpanel, wx.ID_ANY, wx.Bitmap(self.image_paths[0], wx.BITMAP_TYPE_ANY),style=wx.NO_BORDER,pos=(135,145))
        self.image_button_4.Bind(wx.EVT_BUTTON,self.png_ex)

        self.image_button_2.SetBackgroundColour(wx.Colour(self.back_color))
        self.image_button_3.SetBackgroundColour(wx.Colour(self.back_color))
        self.image_button_4.SetBackgroundColour(wx.Colour(self.back_color))

        txt_2 = wx.StaticText(self.rpanel,pos=(10,95),label='开机自启:')
        txt_2.SetFont(self.font)
        txt_3 = wx.StaticText(self.rpanel,pos=(10,125),label='设置1：')
        txt_3.SetFont(self.font)
        txt_4 = wx.StaticText(self.rpanel,pos=(10,155),label='设置2：')
        txt_4.SetFont(self.font)

        # 颜色
        txt_1.SetForegroundColour(wx.Colour(self.txt_color))
        txt_2.SetForegroundColour(wx.Colour(self.txt_color))
        txt_3.SetForegroundColour(wx.Colour(self.txt_color))
        txt_4.SetForegroundColour(wx.Colour(self.txt_color))

        self.apply = wx.Button(self.rpanel,pos=(490,518),label='应用',size=(55,30))
        self.apply.Bind(wx.EVT_ENTER_WINDOW, self.on_mouse_hover)
        self.apply.Bind(wx.EVT_LEAVE_WINDOW, self.on_mouse_leave)
        self.cancel = wx.Button(self.rpanel,pos=(550,518),label='取消',size=(55,30))

        self.apply.Bind(wx.EVT_BUTTON,self.ReLoad)

        self.apply.SetBackgroundColour(wx.Colour(160,178,255))
        self.cancel.SetBackgroundColour(wx.Colour(160,178,255))

        self.apply.Refresh()
        self.cancel.Refresh()
        self.cancel.Bind(wx.EVT_BUTTON,self.onbtn_home)
    def ReLoad(self,event):
        the_module = self.choice_box.GetValue()
        self.Destroy()
        uirevise("module",the_module)
        showFrame(LoginFace)

    def png_ex(self,event):
        button = event.GetEventObject()
        if button == self.image_button_2:
            self.png_ex_num(number = 0,name=button)
        elif button == self.image_button_3:
            self.png_ex_num(number = 1,name=button)
        elif button == self.image_button_4:
            self.png_ex_num(number = 2,name=button)
        else:
            print('设置按钮不足')
    def png_ex_num(self,number,name):
        self.current_image_index[number] = (self.current_image_index[number] + 1) % len(self.image_paths)
        name.SetBitmap(wx.Bitmap(self.image_paths[self.current_image_index[number]], wx.BITMAP_TYPE_ANY))


    def set_button_color(self, button):
        if self.current_button is not None:
            self.current_button.SetBackgroundColour(self.default_color)
            self.current_button.Refresh()

        button.SetBackgroundColour(self.custom_color)
        button.Refresh()

        self.current_button = button
    def clear_rpanel(self):
        for child in self.rpanel.GetChildren():
            child.Destroy()

    def on_paint(self):
        # 在Panel上绘制蓝色矩形
        dc = wx.ClientDC(self.rpanel)
        gc = wx.GraphicsContext.Create(dc)

        # 蓝色矩形的边框颜色与背景颜色一致
        border_color = wx.Colour(255, 255, 255)  # 设置为白色
        gc.SetPen(wx.Pen(border_color, 1))

        # 蓝色矩形的填充颜色为蓝色
        fill_color = wx.Colour(self.dc_color)  # 设置为蓝色
        gc.SetBrush(wx.Brush(fill_color))

        # 画蓝色矩形
        gc.DrawRectangle(0, 0, 620, 50)


    def Paint_nomarl_d(self):
        # 在Panel上绘制蓝色矩形
        dc = wx.ClientDC(self.rpanel)
        gc = wx.GraphicsContext.Create(dc)

        # 蓝色矩形的边框颜色与背景颜色一致
        border_color = wx.Colour(255, 255, 255)  # 设置为白色
        gc.SetPen(wx.Pen(border_color, 1))

        # 蓝色矩形的填充颜色为蓝色
        fill_color = wx.Colour(self.dc_color)  # 设置为蓝色
        gc.SetBrush(wx.Brush(fill_color))

        # 画蓝色矩形
        gc.DrawRectangle(0, 0, 620, 50)

    def yincang(self):
        # 隐藏蓝色矩形
        dc = wx.ClientDC(self.rpanel)
        dc.Clear()


    def OperationInterface(self):
        self.split_mult = wx.SplitterWindow(self, style=wx.SP_LIVE_UPDATE | wx.SP_NOSASH, size=self.Size)
        self.lpanel = wx.Panel(self.split_mult, size=(100,self.split_mult.Size[1]), style=wx.SIMPLE_BORDER)
        self.rpanel = wx.ScrolledWindow(self.split_mult, style=wx.SIMPLE_BORDER, size=(607, self.split_mult.Size[1]))
        self.split_mult.SplitVertically(self.lpanel, self.rpanel)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.split_mult, 1, flag=wx.EXPAND)  # 自动缩放
        self.SetSizer(sizer)
        # self.lpanel.SetSize(wx.Size(50, self.lpanel.GetSize().GetHeight()))

        self.lpanel.SetBackgroundColour(wx.Colour(self.l_color))
        self.rpanel.SetBackgroundColour(wx.Colour(self.back_color))

        self.Layout()


    def Exit_all(self, event):
        ''
        os._exit(0)

class ImageConverterApp(wx.App):
    def OnInit(self):
        self.frame = PngFrame(None, title='历史头像')
        self.frame.Show()
        return True
class PngFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(PngFrame, self).__init__(*args, **kw, size=(800, 400),style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)
        back_color, l_color, bt_color, dc_color, kuang_color, txt_color, bit_bt, ui_module = all_color_set()

        self.panel = wx.Panel(self)
        self.SetMaxSize((800, 500))
        self.SetMaxSize((800, 500))

        self.images_folder = "./history"  # Replace with the actual path to your images folder
        self.image_paths = self.get_image_paths()

        self.scroll_window = wx.ScrolledWindow(self.panel)
        self.scroll_window.SetScrollRate(5, 5)  # Set scroll rate for smoother scrolling
        self.sizer = wx.GridSizer(rows=0, cols=8, hgap=5, vgap=5)
        self.load_images()

        self.scroll_window.SetSizer(self.sizer)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.scroll_window, 1, wx.EXPAND)
        self.panel.SetSizer(main_sizer)

        self.Center()

    def get_image_paths(self):
        image_paths = []
        for filename in os.listdir(self.images_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_paths.append(os.path.join(self.images_folder, filename))
        return image_paths

    def convert_to_64x64(self, image_path):
        img = Image.open(image_path).convert('RGBA')
        img = ImageOps.fit(img, (64, 64), Image.LANCZOS, centering=(0.5, 0.5))
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        return buffer

    def load_images(self):
        for image_path in self.image_paths:
            converted_image = self.convert_to_64x64(image_path)
            wx_image = wx.Image(io.BytesIO(converted_image.getvalue()), wx.BITMAP_TYPE_PNG)
            image_button = buttons.GenBitmapButton(self.scroll_window,
                                                   bitmap=wx.Bitmap(wx_image.ConvertToBitmap()),
                                                   style=wx.BORDER_NONE)
            self.sizer.Add(image_button, 0, wx.EXPAND)
        ''
if __name__ == '__main__':
    app = wx.App()
    # frame = MyFrame(parent=None)
    frame = LoginFace(parent=None)
    frame.Show()
    app.MainLoop()
    print('成功退出')