import wx
import os
from PIL import Image

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

        panel = wx.Panel(self)

        self.image_button = wx.BitmapButton(panel, wx.ID_ANY, wx.Bitmap(r".\user\user.png"))
        self.image_button.Bind(wx.EVT_BUTTON, self.on_image_button_click)


        self.history_directory = "history"  # 历史图片保存目录
        if not os.path.exists(self.history_directory):
            os.makedirs(self.history_directory)

        self.image_count = self.get_image_count()  # 读取历史图片数量

        self.Show()

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

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "图片文件选择示例")
    app.MainLoop()
