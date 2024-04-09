#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we place a panel inside 
another panel.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        wx.Frame.SetIcon()

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)

        panel.SetBackgroundColour('#4f5049')
        vbox = wx.BoxSizer(wx.HORIZONTAL)

        midPan = wx.Panel(panel)
        midPan.SetBackgroundColour('#ededed')
        vbox.Add(midPan, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        midPan2 = wx.Panel(panel)
        midPan2.SetBackgroundColour('#aa0000')
        vbox.Add(midPan2, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        midPan3 = wx.Panel(panel)
        midPan3.SetBackgroundColour('#0000aa')
        vbox.Add(midPan3, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        panel.SetSizer(vbox)


def main():

    app = wx.App()
    ex = Example(None, title='Border')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
