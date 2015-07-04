'''
Created on 22/11/2013

@author: hombregula
'''
import wx

import gettext
import os
from Frame2 import *

from Frame1.Import_Geometry  import *
from Frame1.Import_Clips import *

from Plot_Options import *
from MySplashScreen import *

import time
from Frame2.Frame2 import *

from Frame2.Frame2 import *
from ClipsResults import *
import win32com.client

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)            
        self.statusbar = self.CreateStatusBar()
        self.__set_properties()
        self.__do_layout()
        #self.create_toolbar
        self.create_menu()
        
        self.ruta='Icons\\' 
        ruta='Icons\\'
        self.toolbar = self.CreateToolBar()
        
        #self.toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        
        self.toolbar.AddSimpleTool(2, wx.Image(ruta + 'stock_exit - 24.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Exit', '')
        self.toolbar.AddSimpleTool(1, wx.Image(ruta + 'Close - 24.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Close', '')
        self.toolbar.AddSeparator()
        self.toolbar.AddSimpleTool(3, wx.Image(ruta + 'Picture - 24.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Picture', '')
        self.toolbar.AddSeparator()
        self.toolbar.AddSimpleTool(4, wx.Image(ruta + 'NewAnalysis - 24.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'New Analysis', '')
        self.toolbar.AddSeparator()
        self.toolbar.AddSimpleTool(5, wx.Image(ruta + 'documentation - 24.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Open documentation', '')
        self.toolbar.AddSimpleTool(7, wx.Image(ruta + 'About - 24.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'About', '')
        
        self.toolbar.Realize()

        self.Centre()
        
        self.Bind(wx.EVT_TOOL, self.on_close_2, id=1)

        self.Bind(wx.EVT_TOOL, self.on_exit, id=2)
        self.Bind(wx.EVT_TOOL, self.on_save_plot, id=3)
        self.Bind(wx.EVT_TOOL, self.on_m_analysis, id=4)
        self.Bind(wx.EVT_TOOL, self.on_documentation, id=5) 
        self.Bind(wx.EVT_TOOL, self.on_about, id=7)                
        
        self.AnalysisType = None
        self.Analysis=None
        self.NodosPath = ""
        self.BarsPath = ""
        self.ShellsPath = ""
        
        self.Nodos=""
        self.Bars=""
        self.Shells=""
        
        self.Maximize()
        self.desenable()
    def desenable (self):

        self.toolbar.EnableTool(1, False)
        self.toolbar.EnableTool(3, False)
        #self.toolbar.EnableTool(5, False)
        
        self.menu_file.Enable(11,False)
        self.menu_edit.Enable(13,False)
        #self.menu_analysis.Enable(15,False)
        self.menu_analysis.Enable(16,False) 

    def enable (self):
        self.toolbar.EnableTool(1, True)
        self.toolbar.EnableTool(3, True)
        #self.toolbar.EnableTool(5, True)  
        
        self.menu_file.Enable(11,True)
        self.menu_edit.Enable(13,True)
        #self.menu_analysis.Enable(15,True)
        
        if self.AnalysisType=='Frame Joints':
            self.menu_analysis.Enable(16,True)

        
    def __set_properties(self):

        self.statusbar.SetStatusText('Ready to Start')
        
        self.headline="Imcafe v1.0b "
        self.SetTitle(_(self.headline + "-- ASC Software"))
    
         
    def __do_layout(self):
        self.panel = wx.Panel(self)   
        #self.vboxi = wx.BoxSizer(wx.VERTICAL)   
           
    def create_menu(self):
        self.menubar = wx.MenuBar()
     # Menu File 
        self.menu_file = wx.Menu()
        
        #m_close = self.menu_file.Append(11, "Close")
        self.m_close = self.menu_file.Append(11, "&Close\tCtrl-L", "Close")
        self.Bind(wx.EVT_MENU, self.on_close, self.m_close) 
         
        self.menu_file.AppendSeparator()
        #m_exit = self.menu_file.Append(-1, "E&xit\tCtrl-X", "Exit")
        m_exit = self.menu_file.Append(12, "E&xit\tCtrl-X", "Exit")
        self.Bind(wx.EVT_MENU, self.on_exit, m_exit)
        
   # Menu Edit        
        self.menu_edit = wx.Menu()
        m_save = self.menu_edit.Append(13, "&Save plot\tCtrl-S", "Save plot to file")
        #m_save = self.menu_edit.Append(3, "&Save plot\tCtrl-S", "Save plot to file")
        self.Bind(wx.EVT_MENU, self.on_save_plot, m_save)
           
   # Menu Tools
        self.menu_analysis = wx.Menu()     
        m_analysis=self.menu_analysis.Append(14, "&New Analysis\tCtrl-A", "New analysis")        
        #m_analysis=self.menu_analysis.Append(4, "&New Analysis\tCtrl-A", "New analysis")
        self.Bind(wx.EVT_MENU, self.on_m_analysis, m_analysis)    

        
        #m_fullscreen=self.menu_analysis.Append(15, "&Full Screen\tCtrl-F", "Full Screen")
                
        #m_fullscreen=self.menu_analysis.Append(5, "&Full Screen\tCtrl-F", "Full Screen")
         
        
        m_Sresults=self.menu_analysis.Append(16, "&Save results\tCtrl-R", "Save results")        
        #m_Sresults=self.menu_analysis.Append(6, "&Save results\tCtrl-R", "Save results")  
        self.Bind(wx.EVT_MENU, self.on_m_Sresults, m_Sresults)  
                     
   # Menu Help      
        self.menu_help = wx.Menu()
        m_documentation=self.menu_help.Append(15, "&Documentation\tF1", "Open documentation")
        self.Bind(wx.EVT_MENU, self.on_documentation, m_documentation)
        m_about = self.menu_help.Append(17, "&About\tCtrl-F", "About the demo")
        #m_about = self.menu_help.Append(7, "&About\tF1", "About the demo")
        self.Bind(wx.EVT_MENU, self.on_about, m_about)
        
   # Integration Menu             
        self.menubar.Append(self.menu_file, "&File")
        self.menubar.Append(self.menu_edit, "&Edit")
        self.menubar.Append(self.menu_analysis, "&Tools")
        self.menubar.Append(self.menu_help, "&Help")
        self.SetMenuBar(self.menubar)   
#EVENTS
    def on_save_plot(self, event,id=3):
        
        file_choices = "PNG (*.png)|*.png"
        
        dlg = wx.FileDialog(
            self, 
            message="Save plot as...",
            defaultDir=os.getcwd(),
            defaultFile="plot.png",
            wildcard=file_choices,
            style=wx.SAVE)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.rightPu.canvas.print_figure(path, dpi=self.rightPu.dpi)
            self.flash_status_message("Saved to %s" % path)
            
    def on_close_2(self, event):
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys("^l")
        
        self.Refresh()
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys("^l")        
        


    def on_close(self,event):     
        try:    
            print 'aa'
            self.panel.Destroy()

            print 'aa'
            self.__do_layout() 
            
            self.AnalysisType = ""
                  
            self.NodosPath = ""
            self.BarsPath = ""
            self.ShellsPath = ""
            
            self.Nodos=""
            self.Bars=""
            self.Shells=""

            self.__set_properties()
            self.desenable()
            self.Restauracion()
            
            
        except AttributeError:
            print 'bb' 

    def on_exit_2(self):
        try:
            self.frame_2.Destroy()
            self.Destroy()
        except AttributeError:
            self.Destroy()
    def on_exit(self, event,id=1):
        try:
            self.frame_2.Destroy()
            self.Destroy()
        except AttributeError:
            self.Destroy()
    def on_m_analysis(self, event,id=4):
        try:
            self.frame_2.Show()
        except AttributeError:
            gettext.install("app") # replace with the appropriate catalog name
            app2 = wx.PySimpleApp(0)
            wx.InitAllImageHandlers()
            self.frame_2 = MyFrame2(self)
            ico = wx.Icon(self.ruta +'Ico-Init.ico', wx.BITMAP_TYPE_ICO)
            self.frame_2.SetIcon(ico)            
            app.SetTopWindow(self.frame_2)
            self.frame_2.Show()
            app.MainLoop()
    '''    
    def on_m_fullscreen(self, event,id=5):
        try:
            self.MyFrameCoord.Show()
        except AttributeError:
            gettext.install("app") # replace with the appropriate catalog name
            app3 = wx.PySimpleApp(0)
            wx.InitAllImageHandlers()
            self.MyFrameCoord = MyFrameCoord(self)
            app.SetTopWindow(self.MyFrameCoord)
            self.MyFrameCoord.Show()
            app.MainLoop()
    '''
    def on_documentation(self, event,id=5):
        try: 
            #subprocess.Popen([file],shell=True)
            os.startfile('BBDD\\Manual.pdf')
        except AttributeError:
            print ' Documentation has not been found '
            
    def on_m_Sresults(self, event,id=5):
        try:
            self.ClipResults.Show()
        except AttributeError:
            gettext.install("app") # replace with the appropriate catalog name
            app4 = wx.PySimpleApp(0)
            wx.InitAllImageHandlers()
            self.ClipResults = ClipResults(self)
            app.SetTopWindow(self.ClipResults)
            self.ClipResults.Show()
            app.MainLoop()
          
            
        
    def on_about(self, event,id=6):
        msg=""" A Python software whose aim is to validate and check the performance of different structural joints through its different modules :
        
         * Plot Geometry
         * Frame Joints
           
        """
        dlg = wx.MessageDialog(self, msg, "About", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def _MyFrame2__do__layout_analysis(self):
        if self.AnalysisType=='Plot Geometry':
            self.statusbar.SetStatusText('Loading .... Plot Geometry')
            self.panel.Destroy()
            self.panel = wx.Panel(self)  
            
            self.splitter=wx.SplitterWindow(self.panel, -1, style=wx.SP_3D)
            self.splitterRight=wx.SplitterWindow(self.splitter)
            
            self.leftP = LeftPanel(self.splitter,self.Nodos,self.Bars,self.Shells,self)
            self.rightPu = RightPanelUp(self.splitterRight,self.Nodos,self.Bars,self.Shells,self)
            self.rightPd = RightPanelDown(self.splitterRight,self.Nodos,self.Bars,self.Shells,self.NodosPath,self.BarsPath,self.ShellsPath)
            
            # split the window
            self.splitterRight.SplitHorizontally(self.rightPu, self.rightPd,-1000)
            self.splitterRight.SetSashGravity(0.9)
            self.splitter.SplitVertically(self.leftP, self.splitterRight)
            self.splitter.SetSashGravity(0.001)
            self.sizer = wx.BoxSizer(wx.VERTICAL)
            self .sizer.Add(self.splitter, 1, wx.EXPAND)
            self.panel.SetSizer(self.sizer)
            self.sizer.Fit(self)
            self.SetTitle(_(self.headline + "-- Plot Geometry Analysis"))
            self.statusbar.SetStatusText('Ready - 3d structure correctly loaded')
            self.rightPd.display.Refresh()
            self.enable()
            self.Restauracion()
            
        if self.AnalysisType=='Frame Joints':
            self.statusbar.SetStatusText('Loading .... Frame Joints Results')
            self.panel.Destroy()
            self.panel = wx.Panel(self)  
            
            self.splitter=wx.SplitterWindow(self.panel, -1, style=wx.SP_3D)
            self.splitterRight=wx.SplitterWindow(self.splitter)
            
            self.leftP = LeftPanel_Clips(self.splitter,self.Nodos,self.Bars,self.Shells,self)
            self.rightPu = RightPanelUp_Clips(self.splitterRight,self.Nodos,self.Bars,self.Shells,self)
            self.rightPd = RightPanelDown_Clips(self.splitterRight,self.Nodos,self.Bars,self.Shells,self.NodosPath,self.BarsPath,self.ShellsPath,self)
            
            # split the window
            self.splitterRight.SplitHorizontally(self.rightPu, self.rightPd,-1000)
            self.splitterRight.SetSashGravity(0.9)
            self.splitter.SplitVertically(self.leftP, self.splitterRight)
            self.splitter.SetSashGravity(0.001)
            self.sizer = wx.BoxSizer(wx.VERTICAL)
            self .sizer.Add(self.splitter, 1, wx.EXPAND)
            self.panel.SetSizer(self.sizer)
            self.sizer.Fit(self)
            self.SetTitle(_(self.headline + "-- Frame Joints Analysis"))
            self.statusbar.SetStatusText('Ready - Frame Joints Results correctly calculated')
            self.rightPd.display.Refresh()
            self.enable()
            self.Restauracion()            

    def Restauracion(self):
        self.Freeze()
        if self.IsMaximized():
            self.Restore()
            self.Maximize()
        else:
            self.Maximize()
            self.Restore()
        self.Thaw()   

 

                  
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    Milisegundos=3000
    
    
    MySplash = MySplashScreen(Milisegundos)
    MySplash.Show()
    
    frame_1 = MyFrame(None, wx.ID_ANY, "")
    ico = wx.Icon('Icons\Ico-Init.ico', wx.BITMAP_TYPE_ICO)
    frame_1.SetIcon(ico)
    
    app.SetTopWindow(frame_1)
    
    time.sleep(Milisegundos/1000) 
    MySplash.Destroy()
    frame_1.Show()
   
    app.MainLoop()
