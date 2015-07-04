'''
Created on 11/12/2013

@author: hombregula
'''
import wx
import gettext

from Frame2_PlotGeometry import *
class MyFrame2_ClipJoints (MyFrame2_PlotGeometry):
    def do_layout__ClipJoints(self):            
        self.do_layout__Geometry()
        a1=30
        a2=110
        
        b1=50
        b2=b1+120
        b3=b2+30
        b4=b3+30
        
        s1=200
        s2=300
     
        self.Frame2.textov24=wx.StaticText(self.Frame2.panel, -1, 'Geo. File Path',(a1, b2 + 150 + 30 +4))
        self.Frame2.display24 = wx.TextCtrl(self.Frame2.panel, -1, pos=(a2,b2 + 150 + 30), size=(s2, -1),  style=wx.TE_RIGHT) 
        self.Frame2.bitmap_button_24 = wx.BitmapButton(self.Frame2.panel, wx.ID_ANY, wx.Bitmap("Icons\\Carpeta.png", wx.BITMAP_TYPE_ANY),size=(24,24), pos=(a2+s2+10, b2 + 150 + 30 -1))
        self.Frame2.Bind(wx.EVT_BUTTON, self.AccionarButton_24, self.Frame2.bitmap_button_24)
     
        self.Frame2.textov25=wx.StaticText(self.Frame2.panel, 1, 'Loads File Path',(a1, b2 + 150 + 60 +4))
        self.Frame2.display25 = wx.TextCtrl(self.Frame2.panel, 1, pos=(a2,b2 + 150 + 60), size=(s2, -1),  style=wx.TE_RIGHT)
        self.Frame2.bitmap_button_25 = wx.BitmapButton(self.Frame2.panel, wx.ID_ANY, wx.Bitmap("Icons\\Carpeta.png", wx.BITMAP_TYPE_ANY),size=(24,24), pos=(a2+s2+10, b2 + 150 + 60 -1))
        self.Frame2.Bind(wx.EVT_BUTTON, self.AccionarButton_25, self.Frame2.bitmap_button_25)
                       
        self.Frame2.Layout()
        '''
        # S-18
        self.Frame2.display24.AppendText("E:\\Archivos\\S-18\\DATOSREMACHADO.DAT")
        self.Frame2.display25.AppendText("E:\\Archivos\\S-18\\M-CLIPALL.FORCE")        
        '''
        '''
        # S-19.1
        self.Frame2.display24.AppendText("E:\\Archivos\\S-19\\DATOSREM.DAT")
        self.Frame2.display25.AppendText("E:\\Archivos\\S-19\\M-CLIPALL.FORCE.modif")   
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
        
        self.Frame2.textov24.Destroy()
        self.Frame2.display24.Destroy() 
        self.Frame2.bitmap_button_24.Destroy()
    
        self.Frame2.textov25.Destroy()
        self.Frame2.display25.Destroy()
        self.Frame2.bitmap_button_25.Destroy()

    def AccionarButton_24(self,event):
        '''root = Tk()
        root.withdraw()
        file_path_string = tkFileDialog.askopenfilename()
        self.Frame2.display24.Clear()
        file_path_string= file_path_string.replace('/', '\\')
        self.Frame2.display24.AppendText(file_path_string)'''
        
        openFileDialog = wx.FileDialog(self.Frame2, "Open 1d element file", "", "","ascii files (*.*)|*.*", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed idea...
        self.Frame2.display24.Clear()
        self.Frame2.display24.AppendText(openFileDialog.GetPath())
     
        
    def AccionarButton_25(self,event):
        '''root = Tk()
        root.withdraw()
        file_path_string = tkFileDialog.askopenfilename()
        self.Frame2.display25.Clear()
        file_path_string= file_path_string.replace('/', '\\')
        self.Frame2.display25.AppendText(file_path_string)'''
        openFileDialog = wx.FileDialog(self.Frame2, "Open 1d element file", "", "","ascii files (*.*)|*.*", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed idea...
        self.Frame2.display25.Clear()
        self.Frame2.display25.AppendText(openFileDialog.GetPath())
  
        
        
        