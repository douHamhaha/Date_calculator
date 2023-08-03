# import wx
#
# class MyFrame(wx.Frame):
#     def __init__(self, parent, title):
#         super(MyFrame, self).__init__(parent, title=title, size=(400, 300))
#
#         panel = wx.Panel(self)
#
#         self.image_button = wx.BitmapButton(panel, wx.ID_ANY, wx.Bitmap(r"..\icon\user.png"))
#         self.image_button.Bind(wx.EVT_BUTTON, self.on_image_button_click)
#
#         self.file_path_text = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_READONLY)
#
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.image_button, proportion=0, flag=wx.ALL, border=10)
#         sizer.Add(self.file_path_text, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)
#
#         panel.SetSizerAndFit(sizer)
#
#         self.Show()
#
#     def on_image_button_click(self, event):
#         wildcard = "图片文件 (*.png;*.jpg)|*.png;*.jpg|所有文件 (*.*)|*.*"
#         dlg = wx.FileDialog(self, "选择图片文件", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
#
#         if dlg.ShowModal() == wx.ID_OK:
#             file_path = dlg.GetPath()
#             self.file_path_text.SetValue(file_path)
#             image = wx.Image(file_path, wx.BITMAP_TYPE_ANY)
#             bitmap = wx.Bitmap(image)
#             self.image_button.SetBitmap(bitmap)
#
#         dlg.Destroy()
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MyFrame(None, "图片文件选择示例")
#     app.MainLoop()
# import wx
# from PIL import Image
#
# class MyFrame(wx.Frame):
#     def __init__(self, parent, title):
#         super(MyFrame, self).__init__(parent, title=title, size=(400, 300))
#
#         panel = wx.Panel(self)
#
#         self.image_button = wx.BitmapButton(panel, wx.ID_ANY, wx.Bitmap(r"..\icon\user.png"))
#         self.image_button.Bind(wx.EVT_BUTTON, self.on_image_button_click)
#
#         # self.file_path_text = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_READONLY)
#
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.image_button, proportion=0, flag=wx.ALL, border=10)
#         # sizer.Add(self.file_path_text, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)
#
#         panel.SetSizerAndFit(sizer)
#
#         self.Show()
#
#
#     def resize_image(self, image_path, target_size):
#         image = Image.open(image_path)
#         image = image.resize(target_size, Image.LANCZOS)
#         return image
#     def on_image_button_click(self, event):
#         wildcard = "图片文件 (*.png;*.jpg)|*.png;*.jpg|所有文件 (*.*)|*.*"
#         dlg = wx.FileDialog(self, "选择图片文件", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
#
#         if dlg.ShowModal() == wx.ID_OK:
#             file_path = dlg.GetPath()
#             # self.file_path_text.SetValue(file_path)
#
#             target_size = (64, 64)
#             resized_image = self.resize_image(file_path, target_size)
#             wx_image = wx.Image(resized_image.size[0], resized_image.size[1])
#             wx_image.SetData(resized_image.tobytes())
#             bitmap = wx.Bitmap(wx_image)
#             self.image_button.SetBitmap(bitmap)
#
#         dlg.Destroy()
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MyFrame(None, "图片文件选择示例")
#     app.MainLoop()
import wx
import os
from PIL import Image

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

        panel = wx.Panel(self)

        self.image_button = wx.BitmapButton(panel, wx.ID_ANY, wx.Bitmap(r".\user\user.png"))
        self.image_button.Bind(wx.EVT_BUTTON, self.on_image_button_click)

        self.file_path_text = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_READONLY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.image_button, proportion=0, flag=wx.ALL, border=10)
        sizer.Add(self.file_path_text, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)

        panel.SetSizerAndFit(sizer)

        self.Show()

    def resize_image(self, image_path, target_size):
        image = Image.open(image_path)
        image = image.resize(target_size, Image.LANCZOS)
        return image

    def copy_image_to_target(self, image_path, target_directory, target_name):
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        target_path = os.path.join(target_directory, target_name)
        image = Image.open(image_path)
        image.save(target_path)

        return target_path

    def on_image_button_click(self, event):
        wildcard = "图片文件 (*.png;*.jpg)|*.png;*.jpg|所有文件 (*.*)|*.*"
        dlg = wx.FileDialog(self, "选择图片文件", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dlg.ShowModal() == wx.ID_OK:
            file_path = dlg.GetPath()
            self.file_path_text.SetValue(file_path)

            target_directory = "user"
            target_name = "user.png"
            target_path = self.copy_image_to_target(file_path, target_directory, target_name)

            wx_image = wx.Image(target_path, wx.BITMAP_TYPE_ANY)
            bitmap = wx.Bitmap(wx_image)
            self.image_button.SetBitmap(bitmap)

        dlg.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "图片文件选择示例")
    app.MainLoop()
