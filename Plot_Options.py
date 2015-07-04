'''
Created on 30/11/2013

@author: hombregula
'''
import wx
import gettext


from Functions_Plotting.Funciones import *
import matplotlib.pyplot as plt

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
#from matplotlib.backends.backend_wx import NavigationToolbar2Wx as NavigationToolbar 
import matplotlib.pyplot as plt

from Functions_Plotting.PlotClass2 import *

class MyFrameCoord(wx.Frame):
    def __init__(self, base, *args, **kwds):       
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, base, *args,style= wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)            
        self.base=base
        self.__set_properties()
        self.__do_layout()
        
    def __set_properties(self):
        self.SetTitle(_(" Figure location "))
        #self.SetSize((120))
        
    def __do_layout(self):      
        a1=30
        a2=110
        
        b1=35
        b2= b1+100
        b3=300
        b4=330
        
        s1=200
        s2=60          
        
        self.panel = wx.Panel(self,size=(500, 400))
        print 1
        print self.base.pivotpoint[0]
        print 2
        print self.base.pivotpoint[1]
        print 3
        print self.base.pivotpoint[2]

        self.texto11=wx.StaticText(self.panel, -1, 'Current Coord. [x,y,z] = [' + str(self.base.pivotpoint[0]) +','+ str(self.base.pivotpoint[1]) +','+ str(self.base.pivotpoint[2]) +']',(a1, b1))        
        self.texto12=wx.StaticText(self.panel, -1, 'Default Coord. [x,y,z] = [' + str(self.base.defaultpivotpoint[0]) +','+str(self.base.defaultpivotpoint[1]) +','+ str(self.base.defaultpivotpoint[2]) +']',(a1, b1+ 30))   
        
        self.marco1=wx.StaticBox(self.panel, -1, '  Coordinates Info  ', (5, 5), size=(500-10, b1+60))         
        self.marco2=wx.StaticBox(self.panel, -1, '  Modify Coordinates  ', (5, b1+80), size=(500-10, 120) ) 
        
        self.texto21=wx.StaticText(self.panel, -1, 'X',(a1, b2+4))
        self.display21 = wx.TextCtrl(self.panel, -1, pos=(a1 + 30, b2), size=(s2, -1),  style=wx.TE_RIGHT)
        self.display21.AppendText(str(self.base.pivotpoint[0]))
        self.texto22=wx.StaticText(self.panel, -1, 'Y',(a1, b2+4+30))
        self.display22 = wx.TextCtrl(self.panel, -1, pos=(a1 + 30, b2 + 30), size=(s2, -1),  style=wx.TE_RIGHT)
        self.display22.AppendText(str(self.base.pivotpoint[1]))
        self.texto23=wx.StaticText(self.panel, -1, 'Z',(a1, b2+4 +30+30))
        self.display23 = wx.TextCtrl(self.panel, -1, pos=(a1 + 30, b2+30+30), size=(s2, -1),  style=wx.TE_RIGHT)        
        self.display23.AppendText(str(self.base.pivotpoint[2]))

        self.button21 = wx.Button(self.panel, wx.ID_ANY, _("Apply"),pos=(400, b2))       
        self.Bind(wx.EVT_BUTTON, self.AccionarButton21, self.button21)
        self.button22 = wx.Button(self.panel, wx.ID_ANY, _("Default"),pos=(400, b2+30))       
        self.Bind(wx.EVT_BUTTON, self.AccionarButton22, self.button22)

        
        self.button0 = wx.Button(self.panel, wx.ID_ANY, _("Close"),pos=(420, 250))       
        self.Bind(wx.EVT_BUTTON, self.AccionarButton0, self.button0)
        
        self.Layout()  

    def AccionarButton21(self,event):  
        self.base.pivotpoint=[float(self.display21.GetValue()),float(self.display22.GetValue()),float(self.display23.GetValue())]
        print self.base.pivotpoint
        
        '''self.base.rightPu.__Remove_Figure__()
        self.base.rightPu.__New_Figure__(self.base.pivotpoint[0],self.base.pivotpoint[1],self.base.pivotpoint[2])'''
        self.base.rightPu.__Remove_Figure__()
        self.base.Restauracion()
        self.base.rightPu.__New_Figure__(self.base.pivotpoint[0],self.base.pivotpoint[1],self.base.pivotpoint[2])
        
    def AccionarButton22(self,event):            
        self.display21.Clear()
        self.display22.Clear()
        self.display23.Clear()
        self.display21.AppendText(str(self.base.defaultpivotpoint[0]))
        self.display22.AppendText(str(self.base.defaultpivotpoint[1]))
        self.display23.AppendText(str(self.base.defaultpivotpoint[2]))                    

    def AccionarButton0(self,event):            
        self.Destroy()
  
        