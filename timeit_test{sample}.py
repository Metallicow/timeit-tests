#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports ---------------------------------------------------------------------
# -Python Imports.
import os
import sys
import timeit

# -wxPython Imports.
import wx
from wx.lib.embeddedimage import PyEmbeddedImage

clock16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABK0lEQVR4AaWTPWqEUBSFAwMp"
    "ZwsTsEk19fRuwZVkC2JnI9hZiUKwVCuF1LbWbiClYKFGlRu/QEAmczPFHLjwePeco/fnPV3h"
    "sMVxi9MW5y0uBGfuyP1wFDxv8WIYxptlWR+2bX8mSfJFcOaOHBy4t8Svpmm+B0HQNU0jbdtK"
    "XddSVZVM0yTckYMDd29ywJVEURQLwnVdBYRhKJ7nyTAMwh05OHDR/JZz5Ndwh7BHHMfi+75g"
    "AAAcuGjQYnCiPn6Rr9wzgAMXDVoMzjQJZ3DPAMBFgxaDC50ex1GuEUWRuK4rfd/LHnDRoP3X"
    "oCxLcRxH8jyXeZ41A70ExpdlGSaSpqksy3KrBL2JABFiRtp13Z8mKmNUoIxRXaQ99EXSV5lm"
    "EZy1VX78MT38nL8BuoU1fzYVzjQAAAAASUVORK5CYII=")


class TimeitPanel(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.BORDER_SUNKEN, name='panel'):
        wx.Panel.__init__(self, parent, id, pos, size, style, name)

        self.rb = wx.RadioBox(self, wx.ID_ANY, 'Number of times to test',
                              choices=('1', '10', '42', '100', '1000',
                                       '10000', '100000', '1000000'),
                              majorDimension=4,
                              style=wx.RA_SPECIFY_COLS)
        self.rb.SetSelection(2)

        self.b1 = wx.Button(self, wx.ID_ANY, 'timeit')
        self.b1.Bind(wx.EVT_BUTTON, self.OnRunTheTimeitTests)

        vbSizer = wx.BoxSizer(wx.VERTICAL)
        vbSizer.Add(self.rb, 1, wx.EXPAND | wx.ALL, 5)
        vbSizer.Add(self.b1, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(vbSizer)


    def OnRunTheTimeitTests(self, event=None):
        """
        Explain a bit about the tests being performed HERE.
        Ex: local vs. global access time, considering dots kill performance.
        """
        # - Add Some Tests. 1 or more tests supported.
        def Test1():
            pass
        def Test2():
            pass

        # - Prepare all the data for the Tests before testing.
        theLocals = locals()
        sortedLocals = sorted(list(theLocals.values()), key=str)
        allTestsTuple = tuple(sortedLocals)

        # - Define how many times we want to run the tests.
        timeitThisNumberTimes = int(self.rb.GetStringSelection())

        # - Do the actual testing and print out the individual results.
        print('')
        print('-' * 42)
        print('Timeit Test - %s times' % '{:,d}'.format(timeitThisNumberTimes))
        print(' '.join(['Python', sys.version, 'on', sys.platform]))
        print('wxPython %s' % wx.version())
        print('')

        testResultsDict = {}
        testResultsList = []
        for test in allTestsTuple:
            if not hasattr(test, '__call__'):
                continue
            testResults = timeit.repeat(test, number=timeitThisNumberTimes)
            print('%s:%s' % (test.__name__, testResults))
            testResultsList.append(testResults)
            testResultsDict['%s' % testResults] = test.__name__

        # Now that the testing is over, lets figure out the winners and losers.
        print('')
        winner = min(testResultsList)
        loser = max(testResultsList)
        print('Winner: %s' % testResultsDict['%s' % winner])
        print('Loser: %s' % testResultsDict['%s' % loser])


class TimeitFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP,
                 name='frame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)
        global gMainWin
        gMainWin = self
        panel = TimeitPanel(self)
        vbSizer = wx.BoxSizer(wx.VERTICAL)
        vbSizer.Add(panel, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizerAndFit(vbSizer)
        self.Centre()
        statusBar = self.CreateStatusBar()
        pyVER = '%d.%d.%d %s' % sys.version_info[:4]
        verInfo = 'wxPython %s running on Python %s' % (wx.version(), pyVER)
        statusBar.SetStatusText(verInfo, 0)
        self.Bind(wx.EVT_CLOSE, self.OnDestroy)


    def OnDestroy(self, event):
        self.Destroy()


class TimeitApp(wx.App):
    def OnInit(self):
        self.SetClassName('TimeitApp')
        self.SetAppName('TimeitApp')
        gMainWin = TimeitFrame(None)
        gMainWin.SetTitle('Timeit Test: ')
        gMainWin.SetIcon(clock16.GetIcon())
        self.SetTopWindow(gMainWin)
        gMainWin.Show()
        return True


if __name__ == '__main__':
    gApp = TimeitApp(redirect=False,
                     filename=None,
                     useBestVisual=False,
                     clearSigInt=True)

    gApp.MainLoop()

