# import wx
#
# class ImageToggleButton(wx.Frame):
#     def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
#                  size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
#         super(ImageToggleButton, self).__init__(parent, id, title, pos, size, style)
#
#         self.panel = wx.Panel(self)
#
#         self.image_paths = ["not_gou.png", "gou.png"]
#         self.current_image_index = 0
#
#         self.image_button = wx.BitmapButton(self.panel, wx.ID_ANY, wx.Bitmap(self.image_paths[0], wx.BITMAP_TYPE_ANY),style=wx.NO_BORDER)
#         self.image_button.Bind(wx.EVT_BUTTON, self.on_image_button_click)
#
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.image_button, 0, wx.ALL | wx.CENTER, 10)
#
#         self.panel.SetSizer(sizer)
#         self.Layout()
#
#     def on_image_button_click(self, event):
#         self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
#         self.image_button.SetBitmap(wx.Bitmap(self.image_paths[self.current_image_index], wx.BITMAP_TYPE_ANY))
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = ImageToggleButton(None, title="Image Toggle Button", size=(200, 100))
#     frame.Show()
#     app.MainLoop()
# import os
# import wx
# import wx.lib.buttons as buttons
# from PIL import Image, ImageOps
# import io
#
# class ImageConverterApp(wx.App):
#     def OnInit(self):
#         self.frame = MainFrame(None, title='Image Converter')
#         self.frame.Show()
#         return True
#
# class MainFrame(wx.Frame):
#     def __init__(self, *args, **kw):
#         super(MainFrame, self).__init__(*args, **kw,size=(800,400))
#
#
#         self.panel = wx.Panel(self)
#         self.SetMaxSize((800,500))
#         self.SetMaxSize((800,500))
#
#         self.images_folder = "./icon"  # Replace with the actual path to your images folder
#         self.image_paths = self.get_image_paths()
#
#         self.scroll_window = wx.ScrolledWindow(self.panel)
#         self.scroll_window.SetScrollRate(5, 5)  # Set scroll rate for smoother scrolling
#         self.sizer = wx.GridSizer(rows=0, cols=8, hgap=5, vgap=5)
#         self.load_images()
#
#         self.scroll_window.SetSizer(self.sizer)
#
#         main_sizer = wx.BoxSizer(wx.VERTICAL)
#         main_sizer.Add(self.scroll_window, 1, wx.EXPAND)
#         self.panel.SetSizer(main_sizer)
#
#         self.Center()
#
#     def get_image_paths(self):
#         image_paths = []
#         for filename in os.listdir(self.images_folder):
#             if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
#                 image_paths.append(os.path.join(self.images_folder, filename))
#         return image_paths
#
#     def convert_to_64x64(self, image_path):
#         img = Image.open(image_path).convert('RGBA')
#         img = ImageOps.fit(img, (64, 64), Image.LANCZOS, centering=(0.5, 0.5))
#         buffer = io.BytesIO()
#         img.save(buffer, format='PNG')
#         return buffer
#
#     def load_images(self):
#         for image_path in self.image_paths:
#             converted_image = self.convert_to_64x64(image_path)
#             wx_image = wx.Image(io.BytesIO(converted_image.getvalue()), wx.BITMAP_TYPE_PNG)
#             image_button = buttons.GenBitmapButton(self.scroll_window, bitmap=wx.Bitmap(wx_image.ConvertToBitmap()), style=wx.BORDER_NONE)
#             self.sizer.Add(image_button, 0, wx.EXPAND)
#
# if __name__ == '__main__':
#     app = ImageConverterApp()
#     app.MainLoop()

