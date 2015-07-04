'''
Created on 10/12/2013

@author: hombregula
'''

import wx
import gettext


class MyFrame2_PlotGeometry():
    def __init__(self, Frame2):  
        self.Frame2=Frame2
                 
    def do_layout__Geometry(self):            
        
        a1=30
        a2=110
        
        b1=50
        b2=b1+120
        b3=b2+30
        b4=b3+30
        
        s1=200
        s2=300
     
        self.Frame2.textov21=wx.StaticText(self.Frame2.panel, -1, 'Nodes File Path',(a1, b2+4))
        self.Frame2.display21 = wx.TextCtrl(self.Frame2.panel, -1, pos=(a2, b2), size=(s2, -1),  style=wx.TE_RIGHT)
        self.Frame2.bitmap_button_21 = wx.BitmapButton(self.Frame2.panel, wx.ID_ANY, wx.Bitmap("Icons\\Carpeta.png", wx.BITMAP_TYPE_ANY),size=(24,24), pos=(a2+s2+10, b2-1))
        self.Frame2.Bind(wx.EVT_BUTTON, self.AccionarButton_21, self.Frame2.bitmap_button_21)
     
        self.Frame2.textov22=wx.StaticText(self.Frame2.panel, 1, 'Bars File Path',(a1, b3+4))
        self.Frame2.display22 = wx.TextCtrl(self.Frame2.panel, 1, pos=(a2, b3), size=(s2, -1),  style=wx.TE_RIGHT)
        self.Frame2.bitmap_button_22 = wx.BitmapButton(self.Frame2.panel, wx.ID_ANY, wx.Bitmap("Icons\\Carpeta.png", wx.BITMAP_TYPE_ANY),size=(24,24), pos=(a2+s2+10, b3-1))
        self.Frame2.Bind(wx.EVT_BUTTON, self.AccionarButton_22, self.Frame2.bitmap_button_22)
   
        self.Frame2.textov23=wx.StaticText(self.Frame2.panel, 1, 'Shells File Path',(a1, b4+4))
        self.Frame2.display23 = wx.TextCtrl(self.Frame2.panel, 1, pos=(a2, b4), size=(s2, -1),  style=wx.TE_RIGHT)
        self.Frame2.bitmap_button_23 = wx.BitmapButton(self.Frame2.panel, wx.ID_ANY, wx.Bitmap("Icons\\Carpeta.png", wx.BITMAP_TYPE_ANY),size=(24,24), pos=(a2+s2+10, b4-1))
        self.Frame2.Bind(wx.EVT_BUTTON, self.AccionarButton_23, self.Frame2.bitmap_button_23)                          
        
        '''self.Frame2.marco1=wx.StaticBox(self.Frame2.panel, -1, '  Analysis  ', (5, 5), size=(500-10, b2-60)) 
        self.Frame2.marco2=wx.StaticBox(self.Frame2.panel, -1, '  Geometry  ', (5, b2-30), size=(500-10, 150) ) 
        
        self.button = wx.Button(self.panel, wx.ID_ANY, _("Apply"),pos=(200, b4+100))       
        self.Bind(wx.EVT_BUTTON, self.AccionarButton, self.button)'''
        
        self.Frame2.Layout()
        
        '''
        # S-18
        self.Frame2.display21.AppendText("E:\\Archivos\\S-18\\Grids-S18.txt")
        self.Frame2.display22.AppendText("E:\\Archivos\\S-18\\Bars.BLK")
        self.Frame2.display23.AppendText("E:\\Archivos\\S-18\\Panels.BLK")      
        '''
        '''
        # S-19.1
        self.Frame2.display21.AppendText("E:\\Archivos\\S-19\\s19-grids.txt")
        self.Frame2.display22.AppendText("E:\\Archivos\\S-19\\s19-1d.txt")
        self.Frame2.display23.AppendText("E:\\Archivos\\S-19\\003.11-CMEM.BLK")    
        '''       
    def __Destroy__ (self):
        self.Frame2.textov21.Destroy()
        self.Frame2.display21.Destroy()
        self.Frame2.bitmap_button_21.Destroy()
        
     
        self.Frame2.textov22.Destroy()
        self.Frame2.display22.Destroy()
        self.Frame2.bitmap_button_22.Destroy()
   
        self.Frame2.textov23.Destroy()
        self.Frame2.display23.Destroy()
        self.Frame2.bitmap_button_23.Destroy()               
        
        
        
    def AccionarButton_21(self,event):
        openFileDialog = wx.FileDialog(self.Frame2, "Open Nodes file", "", "","ascii files (*.*)|*.*", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed idea...
        self.Frame2.display21.Clear()
        self.Frame2.display21.AppendText(openFileDialog.GetPath())
        print openFileDialog.GetPath()
   
        
    def AccionarButton_22(self,event):
        openFileDialog = wx.FileDialog(self.Frame2, "Open 1d element file", "", "","ascii files (*.*)|*.*", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed idea...
        self.Frame2.display22.Clear()
        self.Frame2.display22.AppendText(openFileDialog.GetPath())
        print openFileDialog.GetPath()
        
    def AccionarButton_23(self,event):
        openFileDialog = wx.FileDialog(self.Frame2, "Open 2d element file", "", "","ascii files (*.*)|*.*", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed idea...
        self.Frame2.display23.Clear()
        self.Frame2.display23.AppendText(openFileDialog.GetPath())
        print openFileDialog.GetPath()
               
        