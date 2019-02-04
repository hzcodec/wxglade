#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0 on Mon Feb  4 08:36:33 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((532, 339))
        self.bitmap_button_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("start_grey.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("stop_grey.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Aerodrome control")
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.bitmap_button_2.SetSize(self.bitmap_button_2.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("aeroseum_logo_100x119.png", wx.BITMAP_TYPE_ANY))
        sizer_2.Add(bitmap_1, 0, wx.LEFT | wx.TOP, 15)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_2.Add(static_line_1, 0, wx.ALL | wx.EXPAND, 20)
        sizer_4.Add(self.bitmap_button_1, 0, wx.BOTTOM | wx.LEFT, 15)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Starting")
        label_1.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        sizer_4.Add(label_1, 0, wx.ALIGN_CENTER | wx.LEFT, 15)
        sizer_4.Add((0, 0), 0, 0, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.bitmap_button_2, 0, wx.LEFT, 15)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Stopping")
        label_2.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        sizer_5.Add(label_2, 0, wx.ALIGN_CENTER | wx.LEFT, 15)
        sizer_5.Add((0, 0), 0, 0, 0)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
