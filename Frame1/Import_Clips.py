'''
Created on 16/12/2013

@author: hombregula
'''
import wx
import gettext

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx as NavigationToolbar 
import matplotlib.pyplot as plt

from Functions_Plotting.PlotClass2 import *

from mpl_toolkits.mplot3d import Axes3D

import mpl_toolkits.mplot3d.art3d as art3d

# borrar ???
from Tkinter import *
import tkFileDialog
##

from Frame1.Import_Geometry import *

from ClipJoints.Calculations import truncate

class LeftPanel_Clips(LeftPanel):
    def __init__(self, parent, Nodos,Bars,Shells,base):
        super(LeftPanel_Clips,self).__init__(parent, Nodos,Bars,Shells,base,AnalysisList=["","Geometry Importation","Load Cases","Properties","Results"])
    
    def OnSelect(self, event):
        self.base.Freeze()
        if self.comboboxAnalysis.GetValue() == 'Geometry Importation':
            if self.tree:
                self.tree.Destroy()            
            self.tree = wx.TreeCtrl(self, 1, wx.DefaultPosition, (-1,-1), wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS)
            
            root = self.tree.AddRoot('Import Geometry')
           
            NodosBranch = self.tree.AppendItem(root, 'Nodes')
            BarsBranch = self.tree.AppendItem(root, 'Bars')
            ShellsBranch = self.tree.AppendItem(root, 'Shells')
            
            #self.tree.setItemTextColour(wx.GREEN)
            self.tree.AppendItem(NodosBranch,str(len(list(set(self.Nodos.keys()))))+ ' Nodes taken into accout')
            self.tree.AppendItem(BarsBranch, str(len(list(set(self.Bars.keys()))))+' Bars taken into accout')
            self.tree.AppendItem(ShellsBranch, str(len(list(set(self.Shells.keys()))))+' Shells taken into accout')
            
            
            self.ssizer.Add(self.tree, 1, wx.EXPAND)
            self.SetSizer(self.ssizer) 
            #self.comboboxAnalysis.SetValue('Import Geometry')  
            self.ssizer.Fit(self)
            #self.base.panel.SetSizer(self.base.sizer)

            self.base.sizer.Fit(self)    

            if self.base.IsMaximized():
                self.base.Restore()
                self.base.Maximize()
            else:
                self.base.Maximize()
                self.base.Restore()
                         
        elif self.comboboxAnalysis.GetValue() == 'Load Cases':
            if self.tree:
                self.tree.Destroy()            
            self.tree = wx.TreeCtrl(self, 1, wx.DefaultPosition, (-1,-1), wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS)
            
            root = self.tree.AddRoot('Load Cases')
            
            for i in self.base.Analysis.elementList:
                r = self.tree.AppendItem(root, str(i))
                for ii in self.base.Analysis.lcs[i]:
                    self.tree.AppendItem(r,str('Lc: ' + ii[0] + ' -- ' + ii[1]))
           
            self.ssizer.Add(self.tree, 1, wx.EXPAND)
            self.SetSizer(self.ssizer) 
            #self.comboboxAnalysis.SetValue('Import Geometry')  
            self.ssizer.Fit(self)
            #self.base.panel.SetSizer(self.base.sizer)

            self.base.sizer.Fit(self)    

            if self.base.IsMaximized():
                self.base.Restore()
                self.base.Maximize()
            else:
                self.base.Maximize()
                self.base.Restore()
        elif self.comboboxAnalysis.GetValue() == 'Properties':
            if self.tree:
                self.tree.Destroy()            
            self.tree = wx.TreeCtrl(self, 1, wx.DefaultPosition, (-1,-1), wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS)
            
            root = self.tree.AddRoot('Allowables')
            
            
            for i in self.base.Analysis.elementList:
                f=self.base.Analysis.Analysis[i]
                r = self.tree.AppendItem(root, str(i))
                if self.base.Analysis.elementDict[i]<>"TYPICAL":
                    self.tree.AppendItem(r,str(self.base.Analysis.elementDict[i]))
                else:
                    self.tree.AppendItem(r,str(self.base.Analysis.elementDict[i]+" (" + str(self.base.Analysis.Analysis[i].former_allw_factor) + ")"))
#                for ii in self.base.Analysis.Analysis[i]:
                if f.Skin<>[]:                    
                    for ii in f.Skin:
                        rr= self.tree.AppendItem(r,str('Skin'))
                        self.tree.AppendItem(rr,str('Thickness: '+ str(ii.thickness)))
                        self.tree.AppendItem(rr,str('Material: '+str(ii.material)))
                        self.tree.AppendItem(rr,str('Process: '+str(ii.process)))
                        self.tree.AppendItem(rr,str('Rivet: '+str(ii.rivet)))
                        self.tree.AppendItem(rr,str('Numb. of rivets: '+str(int(ii.nrivet))))
                        
                        self.tree.AppendItem(rr,str('Unit. Allowable: '+str(ii.allow)))
                        self.tree.AppendItem(rr,str('Allowable: '+ str(float(ii.allow) * float(ii.nrivet))))
                if f.ClipSk<>[]:                    
                    for ii in f.ClipSk:
                        rr= self.tree.AppendItem(r,str('ClipSk'))
                        self.tree.AppendItem(rr,str('Thickness: '+ str(ii.thickness)))
                        self.tree.AppendItem(rr,str('Material: '+str(ii.material)))
                        self.tree.AppendItem(rr,str('Process: '+str(ii.process)))
                        self.tree.AppendItem(rr,str('Rivet: '+str(ii.rivet)))
                        self.tree.AppendItem(rr,str('Numb. of rivets: '+str(int(ii.nrivet))))
                        
                        self.tree.AppendItem(rr,str('Unit. Allowable: '+str(ii.allow)))
                        self.tree.AppendItem(rr,str('Allowable: '+ str(float(ii.allow) * float(ii.nrivet))))
                if f.ClipFr<>[]:                    
                    for ii in f.ClipFr:
                        rr= self.tree.AppendItem(r,str('ClipFr'))
                        self.tree.AppendItem(rr,str('Thickness: '+ str(ii.thickness)))
                        self.tree.AppendItem(rr,str('Material: '+str(ii.material)))
                        self.tree.AppendItem(rr,str('Process: '+str(ii.process)))
                        self.tree.AppendItem(rr,str('Rivet: '+str(ii.rivet)))
                        self.tree.AppendItem(rr,str('Numb. of rivets: '+str(int(ii.nrivet))))
                        
                        self.tree.AppendItem(rr,str('Unit. Allowable: '+str(ii.allow)))
                        if self.base.Analysis.elementDict[i]<>"TYPICAL":
                            self.tree.AppendItem(rr,str('Allowable: '+ str(float(ii.allow) * float(ii.nrivet))))
                        else:
                            self.tree.AppendItem(rr,str('Allowable: '+ str("%.2f"%(float(ii.allow) /self.base.Analysis.Analysis[i].former_allw_factor))))
                if f.Former<>[]:                    
                    for ii in f.Former:
                        rr= self.tree.AppendItem(r,str('Former'))
                        self.tree.AppendItem(rr,str('Thickness: '+ str(ii.thickness)))
                        self.tree.AppendItem(rr,str('Material: '+str(ii.material)))
                        self.tree.AppendItem(rr,str('Process: '+str(ii.process)))
                        self.tree.AppendItem(rr,str('Rivet: '+str(ii.rivet)))
                        self.tree.AppendItem(rr,str('Numb. of rivets: '+str(int(ii.nrivet))))
                        
                        self.tree.AppendItem(rr,str('Unit. Allowable: '+str(ii.allow)))
                        if self.base.Analysis.elementDict[i]<>"TYPICAL":
                            self.tree.AppendItem(rr,str('Allowable: '+ str(float(ii.allow) * float(ii.nrivet))))
                        else:
                            self.tree.AppendItem(rr,str('Allowable: '+ str("%.2f"%(float(ii.allow) / self.base.Analysis.Analysis[i].former_allw_factor))))
            self.ssizer.Add(self.tree, 1, wx.EXPAND)
            self.SetSizer(self.ssizer) 
            #self.comboboxAnalysis.SetValue('Import Geometry')  
            self.ssizer.Fit(self)
            #self.base.panel.SetSizer(self.base.sizer)

            self.base.sizer.Fit(self)    

            if self.base.IsMaximized():
                self.base.Restore()
                self.base.Maximize()
            else:
                self.base.Maximize()
                self.base.Restore()                
        elif self.comboboxAnalysis.GetValue() == 'Results':
            if self.tree:
                self.tree.Destroy()            
            self.tree = wx.TreeCtrl(self, 1, wx.DefaultPosition, (-1,-1), wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS)
            
            root = self.tree.AddRoot('Allowables')
            

            
            for i in self.base.Analysis.elementList:
                f=self.base.Analysis.Analysis[i]
                r = self.tree.AppendItem(root, str(i))
#                for ii in self.base.Analysis.Analysis[i]:
                if f.Skin<>[]:                 
                        rr= self.tree.AppendItem(r,str('Skin'))
                        self.tree.AppendItem(rr,str('RF: '+ str(truncate(f.minSkin[0][1],2))))
                        self.tree.AppendItem(rr,str('Load Case Id.: '+ str(f.minSkin[0][0])))
                        self.tree.AppendItem(rr,str('Load Case Val.: '+ str(f.minSkin[0][2])))
                if f.ClipSk<>[]:                        
                        rr= self.tree.AppendItem(r,str('ClipSk'))
                        self.tree.AppendItem(rr,str('RF: '+ str(truncate(f.minClipSk[0][1],2))))
                        self.tree.AppendItem(rr,str('Load Case Id.: '+ str(f.minClipSk[0][0])))
                        self.tree.AppendItem(rr,str('Load Case Val.: '+ str(f.minClipSk[0][2])))                    
                    
                if f.ClipFr<>[]:                
                        rr= self.tree.AppendItem(r,str('ClipFr'))
                        self.tree.AppendItem(rr,str('RF: '+ str(truncate(f.minClipFr[0][1],2))))
                        self.tree.AppendItem(rr,str('Load Case Id.: '+ str(f.minClipFr[0][0])))
                        self.tree.AppendItem(rr,str('Load Case Val.: '+ str(f.minClipFr[0][2])))                    
                if f.Former<>[]:                        
                        rr= self.tree.AppendItem(r,str('Former'))
                        self.tree.AppendItem(rr,str('RF: '+ str(truncate(f.minFormer[0][1],2))))
                        self.tree.AppendItem(rr,str('Load Case Id.: '+ str(f.minFormer[0][0])))
                        self.tree.AppendItem(rr,str('Load Case Val.: '+ str(f.minFormer[0][2])))                                       
                               
            self.ssizer.Add(self.tree, 1, wx.EXPAND)
            self.SetSizer(self.ssizer) 
            #self.comboboxAnalysis.SetValue('Import Geometry')  
            self.ssizer.Fit(self)
            #self.base.panel.SetSizer(self.base.sizer)

            self.base.sizer.Fit(self)    

            if self.base.IsMaximized():
                self.base.Restore()
                self.base.Maximize()
            else:
                self.base.Maximize()
                self.base.Restore()      
        else:
            if self.tree:
                self.tree.Destroy()  
        self.base.Thaw() 

class RightPanelUp_Clips(RightPanelUp):
    def __init__(self, parent,Nodos,Bars,Shells,papa):
        super(RightPanelUp_Clips,self).__init__(parent,Nodos,Bars,Shells,papa)
        
        self.TextToolBar2 = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        self.TextToolBar2.AddSimpleTool(3, wx.Image('Icons\Input-Results.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Change Visualitation - Input 2 Output', '')
        self.TextToolBar2.AddSimpleTool(5, wx.Image('Icons\Input-Results_2.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Change Visualitation - Input', '')
        self.TextToolBar2.Realize()
        self.Bind(wx.EVT_TOOL, self.OnChangeVisualitation, id=3)
        self.Bind(wx.EVT_TOOL, self.OnChangeVisualitation2, id=5)
        self.hboxi.Add(self.TextToolBar2, 0,wx.EXPAND|wx.ALIGN_LEFT)
        
        self.vboxi.Add(self.hboxi, 0,wx.EXPAND |wx.ALIGN_TOP)
        
        self.SetSizer(self.vboxi)
        self.vboxi.Fit(self)     
        self.pantalla='inputs'
        self.pantallainput=1
        self.base=papa
    def OnChangeVisualitation (self,event):
        #self.base.Freeze()
        self.__Remove_Figure__()
        
        if self.pantalla=='results':
            if self.pantallainput==1:
                self.__New_Figure__(Xn=0, Yn=0, Zn=0)
            elif self.pantallainput==2:
                self.__New_Figure__Clips_Input(0, 0, 0,self.base)
            
            self.pantalla='inputs'
            
            #self.base.Restauracion()
        elif self.pantalla=='inputs':
            self.__New_Figure__Clips(0, 0, 0,self.base)
            self.pantalla='results'
            #self.base.Restauracion()
            
        if self.base.IsMaximized():
            self.base.Restore()
            self.base.Maximize()
        else:
            self.base.Maximize()
            self.base.Restore()        
        #self.base.Thaw() 

    def OnChangeVisualitation2 (self,event):
        #self.base.Freeze()
        self.__Remove_Figure__()
        
        if self.pantallainput==1:
            self.__New_Figure__Clips_Input(0, 0, 0,self.base)
            self.pantallainput=2
            
            #self.base.Restauracion()
        elif self.pantallainput==2:
            self.__New_Figure__(Xn=0, Yn=0, Zn=0)
            self.pantallainput=1
            #self.base.Restauracion()
            
        if self.base.IsMaximized():
            self.base.Restore()
            self.base.Maximize()
        else:
            self.base.Maximize()
            self.base.Restore()        
        #self.base.Thaw() 
                
    def __plot_Bars__Clips__(self,parent,axes):
        if self.Bars<>"":    
            self.Dibujo2.PlotBars_Clips(parent,axes)  
    
    def __plot_Bars__Clips__Input__(self,parent,axes):
        if self.Bars<>"":    
            self.Dibujo2.PlotBars_Clips_Inputs(parent,axes)              

    def __plot_Shells__(self):
        if self.Shells<>"":    
            self.Dibujo2.PlotShells() 
                       
    def __New_Figure__Clips(self,Xn,Yn,Zn,parent):        
        #self.axes = self.fig.add_subplot(111, projection='3d')
        self.axes = self.fig.gca(projection='3d')
        self.Dibujo2 = Pintar2(self.Nodos,self.Bars,self.Shells,self.axes)

        
        self.Dibujo2.__Redifine_Nodes__(Xn,Yn,Zn)
                
        '''self.__plot_Shells__()'''
        self.__plot_Bars__Clips__(parent,self.axes)
        #self.Dibujo2.Plot000()
        
        Factor=1.0
        self.Dibujo2.LimitesX(self.Dibujo2.LimX[0]*Factor,self.Dibujo2.LimX[1]*Factor)
        self.Dibujo2.LimitesY(self.Dibujo2.LimY[0]*Factor,self.Dibujo2.LimY[1]*Factor)
        self.Dibujo2.LimitesZ(self.Dibujo2.LimZ[0]*Factor,self.Dibujo2.LimZ[1]*Factor)
        
        self.axes.set_axis_off()
        
        plt.subplots_adjust(left=0,bottom=0,right=1,top=1)          
        self.axes.set_axis_bgcolor(self.bgcolor)         
        #self.canvas.draw() 
    def __New_Figure__Clips_Input(self,Xn,Yn,Zn,parent):        
        #self.axes = self.fig.add_subplot(111, projection='3d')
        self.axes = self.fig.gca(projection='3d')
        self.Dibujo2 = Pintar2(self.Nodos,self.Bars,self.Shells,self.axes)

        
        self.Dibujo2.__Redifine_Nodes__(Xn,Yn,Zn)
                
        '''self.__plot_Shells__()'''
        self.__plot_Bars__Clips__Input__(parent,self.axes)
        #self.Dibujo2.Plot000()
        
        Factor=1.0
        self.Dibujo2.LimitesX(self.Dibujo2.LimX[0]*Factor,self.Dibujo2.LimX[1]*Factor)
        self.Dibujo2.LimitesY(self.Dibujo2.LimY[0]*Factor,self.Dibujo2.LimY[1]*Factor)
        self.Dibujo2.LimitesZ(self.Dibujo2.LimZ[0]*Factor,self.Dibujo2.LimZ[1]*Factor)
        
        self.axes.set_axis_off()
        
        plt.subplots_adjust(left=0,bottom=0,right=1,top=1)          
        self.axes.set_axis_bgcolor(self.bgcolor)         
        #self.canvas.draw()                     
class RightPanelDown_Clips(RightPanelDown):
    def __init__(self, parent,Nodos,Bars,Shells,NodosPath,BarsPath,ShellsPath,base):
        super(RightPanelDown_Clips,self).__init__( parent,Nodos,Bars,Shells,NodosPath,BarsPath,ShellsPath)     
        self.base=base
        self.display.SetDefaultStyle(wx.TextAttr(wx.GREEN))
        self.display.AppendText('Frame Joints Input Data Dictionary: ' +  " \n")
        self.display.SetDefaultStyle(wx.TextAttr(wx.BLUE))
        self.display.AppendText(str(self.base.Analysis.geo) +  " \n")
        
        self.display.SetDefaultStyle(wx.TextAttr(wx.GREEN))
        self.display.AppendText('Frame Joints Input Load Dictionary: ' +  " \n")
        self.display.SetDefaultStyle(wx.TextAttr(wx.BLUE))
        self.display.AppendText(str(self.base.Analysis.lcs) +  " \n")        
        self.display.SetDefaultStyle(wx.TextAttr(wx.RED))

        print self.base.Analysis.MinimoMinimorum[1][0][1]
        print self.base.Analysis.MinimoMinimorum[0]
        print self.base.Analysis.MinimoMinimorum[1][1][0]
        
        self.display.AppendText("RF min = " + str(truncate(self.base.Analysis.MinimoMinimorum[1][0][1],2)) + ' at ' + str(self.base.Analysis.MinimoMinimorum [0]) 
        + ' ' + self.base.Analysis.MinimoMinimorum [1][1][0] )                     
        self.display.Refresh()
        #self.sizer.Add(self.display,1, wx.EXPAND, 40)
        self.SetSizer(self.sizer) 
          
        self.sizer.Fit(self)           
