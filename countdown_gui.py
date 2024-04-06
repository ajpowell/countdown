# From https://realpython.com/python-gui-with-wxpython/#creating-a-skeleton-application
#
import wx
# import time
from datetime import datetime
import math


class MyFrame(wx.Frame):
    target_datetime = datetime.strptime('2024-04-29 09:00:00', '%Y-%m-%d %H:%M:%S')

    def __init__(self):
        super().__init__(parent=None, title='Countdown')

        self.SetSize((300, 100))

        panel = wx.Panel(self)
        # self.SetBackgroundColour((255, 0, 0))

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)

        """my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)"""

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer()

        # my_sizer = wx.BoxSizer(wx.VERTICAL)
        my_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.static_text = wx.StaticText(panel, label=self.CalcDeltaAsString(), style=wx.ALIGN_CENTER)
        font = wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.static_text.SetFont(font)
        # my_sizer.Add(self.static_text, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(self.static_text, 0, wx.ALL, 5)

        # my_btn = wx.Button(panel, label='Press Me')
        # my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        # my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        # self.static_text.SetLabel('foobar')
        sizer.Add(my_sizer, 0, wx.ALIGN_CENTER)
        sizer.AddStretchSpacer()
        panel.SetSizer(sizer)
        # panel.SetSizer(my_sizer)

        self.Show()

        self.timer.Start(1000)

    def on_press(self, event):
        self.ShowMessage()

    def ShowMessage(self):
        wx.MessageBox('Message box', 'Info',
                      wx.OK | wx.ICON_INFORMATION)

    def OnClose(self, event):
        self.Close()
        app.Destroy()

    def CalcDeltaAsString(self):
        now = datetime.now()

        delta = self.target_datetime - now
        weeks = delta.total_seconds()/3600/24/7
        delta_wk = math.floor(weeks)
        days = (weeks - delta_wk)*7
        delta_dy = math.floor(days)
        hours = (days - delta_dy)*24
        delta_hr = math.floor(hours)
        minutes = (hours - delta_hr)*60
        delta_mn = math.floor(minutes)

        print(f'full delta: {delta}')
        # print(f'delta_dy: {days} {delta_dy}')
        # print(f'delta_hr: {hours} {delta_hr}')
        # print(f'delta_mn: {minutes} {delta_mn}')

        wk = f'{delta_wk}w ' if delta_wk > 0 else ''
        dy = f'{delta_dy}d ' if delta_dy > 0 else ''
        hr = f'{delta_hr}h '
        mn = f'{delta_mn}m'

        delta_str = wk + dy + hr + mn

        return delta_str

    def update(self, event):
        # print('Updated: {} '. format(time.ctime()))

        self.static_text.SetLabel(self.CalcDeltaAsString())


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
