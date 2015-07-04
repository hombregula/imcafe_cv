'''
Created on 24/11/2013

@author: hombregula
'''
'''
Created on 24/11/2013

@author: hombregula
'''
import wx
import gettext
from wx import ColourDatabase as Database
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx as NavigationToolbar 
import matplotlib.pyplot as plt

from Functions_Plotting.PlotClass2 import *

from mpl_toolkits.mplot3d import Axes3D

import mpl_toolkits.mplot3d.art3d as art3d

from Tkinter import *
import tkFileDialog
class LeftPanel(wx.Panel):
    def __init__(self, parent, Nodos,Bars,Shells,base,AnalysisList=["","Geometry Importation"]):
        """Constructor"""
        
        self.Nodos=Nodos
        self.Bars=Bars
        self.Shells=Shells
        self.base=base
        wx.Panel.__init__(self, parent=parent)

        #AnalysisList=["","Geometry Importation"]

        self.ssizer = wx.BoxSizer(wx.VERTICAL)
        
        self.comboboxAnalysis=wx.ComboBox(self, -1, choices=AnalysisList, style=wx.CB_READONLY)
        
        '''Initialize our tree
        '''
        #self.tree = wx.TreeCtrl(self, 1, wx.DefaultPosition, (-1,-1), wx.TR_HAS_BUTTONS |wx.TR_FULL_ROW_HIGHLIGHT )
        
        self.tree = wx.TreeCtrl(self, 1, wx.DefaultPosition, (-1,-1), wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS)
        
        root = self.tree.AddRoot('Import Geometry')
       
        NodosBranch = self.tree.AppendItem(root, 'Nodes')
        BarsBranch = self.tree.AppendItem(root, 'Bars')
        ShellsBranch = self.tree.AppendItem(root, 'Shells')
        
        #self.tree.setItemTextColour(wx.GREEN)
        self.tree.AppendItem(NodosBranch,str(len(list(set(self.Nodos.keys()))))+ ' Nodes taken into accout')
        
        try:
            self.tree.AppendItem(BarsBranch, str(len(list(set(self.Bars.keys()))))+' Bars taken into accout')
        except:
            print 'No 1d element file has been selected'
                        
        try:
            self.tree.AppendItem(ShellsBranch, str(len(list(set(self.Shells.keys()))))+' Shells taken into accout')
        except:
            print 'No 2d element file has been selected'
        self.ssizer.Add(self.comboboxAnalysis,0, wx.EXPAND |wx.ALIGN_TOP)
        self.ssizer.Add(self.tree, 1, wx.EXPAND)
        self.SetSizer(self.ssizer) 
        self.comboboxAnalysis.SetValue('Geometry Importation')  
        self.ssizer.Fit(self)            
########################################################################
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)        
    
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
                         
        else:
            if self.tree:
                self.tree.Destroy()  
        self.base.Thaw() 
        
            
            
class RightPanelUp(wx.Panel):
    def __init__(self, parent,Nodos,Bars,Shells,papa):

        """Constructor"""
        self.base=parent
        self.Nodos=Nodos
        self.Shells=Shells
        self.Bars=Bars
        self.papa=papa
        wx.Panel.__init__(self, parent=parent)
        
        # PLOT FIGURE
        self.bgcolor='black'
        self.__init_Figure__()
        self.__plot_figure__()
        
        self.toolbar = NavigationToolbar(self.canvas)
        
        self.vboxi = wx.BoxSizer(wx.VERTICAL)
        self.vboxi.Add(self.canvas, 1,wx.EXPAND )
        
        self.hboxi= wx.BoxSizer(wx.HORIZONTAL)
        self.hboxi.Add(self.toolbar, 0,wx.EXPAND |wx.ALIGN_LEFT)
        
        self.TextToolBar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        self.TextToolBar.AddSimpleTool(1, wx.Image('Icons\\1386563260_download_2.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'TextImportation', '')
        self.TextToolBar.AddSimpleTool(2, wx.Image('Icons\Blanco.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Backcolor White', '')
        self.TextToolBar.Realize()
        
        self.Bind(wx.EVT_TOOL, self.OnTextImportation, id=1)
        self.Bind(wx.EVT_TOOL, self.BackGroundColor, id=2)
        
        self.hboxi.Add(self.TextToolBar, 0,wx.EXPAND|wx.ALIGN_LEFT)
        
        self.vboxi.Add(self.hboxi, 0,wx.EXPAND |wx.ALIGN_TOP)
        
        self.SetSizer(self.vboxi)
        self.vboxi.Fit(self)
        
    def on_pick(self,event):
        #print event
        thisline = event.artist
        #print thisline
        #print thisline
        #print dir(thisline)
         
        self.papa.rightPd.plot_elm_clicked(thisline.get_label())
    def __init_Figure__(self):
        self.dpi = 100
        self.fig = plt.figure( dpi=self.dpi)
        #self.fig.tight_layout(pad=0.5)
        self.canvas = FigureCanvas(self,  wx.ID_ANY, self.fig)
        #self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.canvas.mpl_connect('pick_event', self.on_pick)
    def __plot_figure__(self):
        #self.axes = self.fig.add_subplot(111, projection='3d')         
        self.axes = self.fig.gca(projection='3d')
        self.Dibujo2 = Pintar2(self.Nodos,self.Bars,self.Shells,self.axes)
        
        if self.Bars<>"":
            self.Dibujo2.PlotBarsLimits()

        if self.Shells<>"":
            self.Dibujo2.PlotShellsLimits()
        #self.Dibujo2.Redifine_2_Zero()
        self.__plot_Shells__()
        self.__plot_Bars__()
        #self.Dibujo2.PlotNodes()
        #self.Dibujo2.Plot000()
        
        Factor=1.0
        self.Dibujo2.LimitesX(self.Dibujo2.LimX[0]*Factor,self.Dibujo2.LimX[1]*Factor)
        self.Dibujo2.LimitesY(self.Dibujo2.LimY[0]*Factor,self.Dibujo2.LimY[1]*Factor)
        self.Dibujo2.LimitesZ(self.Dibujo2.LimZ[0]*Factor,self.Dibujo2.LimZ[1]*Factor)
        
        self.axes.set_axis_off()
        
        plt.subplots_adjust(left=0,bottom=0,right=1,top=1)
        #plt.subplots_adjust(left=-a,right=a ,top=a,bottom=-a)           
        self.axes.set_axis_bgcolor(self.bgcolor) 


        '''Dibujo = Pintar(Nodos,Skins,Stringers,Frames)
        
        #GEOMETRIA
        #Dibujo.PlotNodes()
        Dibujo.Nuevos_Nodos()
        Dibujo.PlotQuads()
        Dibujo.PlotStringers()
        
        #LIMITES
        Dibujo.LimitesX(Dibujo.LimX[0]*1.15,Dibujo.LimX[1]*1.15)
        Dibujo.LimitesY(Dibujo.LimY[0]*1.15,Dibujo.LimY[1]*1.15)
        Dibujo.LimitesZ(Dibujo.LimZ[0]*1.15,Dibujo.LimZ[1]*1.15)
        
        #PLOTEAR
        Dibujo.Plotear()'''

    def __plot_Bars__(self):
        if self.Bars<>"":    
            self.Dibujo2.PlotBars()  
             
    def __plot_Shells__(self):
        if self.Shells<>"":    
            self.Dibujo2.PlotShells()          
                 
    
    def __Remove_Bars__(self):        

        t=-1
        while t!=0:
            t=0

            for i in self.axes.lines:
                self.axes.lines.pop()
                t=t+1

    
    '''def __Remove_Bars__(self):        
    
    '''
           
    def __Remove_Figure__(self):        
        self.axes.cla()
        self.axes = self.fig.add_subplot(111, projection='3d')              
        self.axes.set_axis_bgcolor(self.bgcolor)    
        self.axes.set_axis_off()  
    
    def __New_Figure__(self,Xn,Yn,Zn):        
        #self.axes = self.fig.add_subplot(111, projection='3d')
        self.axes = self.fig.gca(projection='3d')
        self.Dibujo2 = Pintar2(self.Nodos,self.Bars,self.Shells,self.axes)

        
        self.Dibujo2.__Redifine_Nodes__(Xn,Yn,Zn)
                
        self.__plot_Shells__()
        self.__plot_Bars__()
        #self.Dibujo2.Plot000()
        
        Factor=1.0
        self.Dibujo2.LimitesX(self.Dibujo2.LimX[0]*Factor,self.Dibujo2.LimX[1]*Factor)
        self.Dibujo2.LimitesY(self.Dibujo2.LimY[0]*Factor,self.Dibujo2.LimY[1]*Factor)
        self.Dibujo2.LimitesZ(self.Dibujo2.LimZ[0]*Factor,self.Dibujo2.LimZ[1]*Factor)
        
        self.axes.set_axis_off()
        
        plt.subplots_adjust(left=0,bottom=0,right=1,top=1)          
        self.axes.set_axis_bgcolor(self.bgcolor)         
        #self.canvas.draw() 
    def OnTextImportation (self,event):
        root = Tk()
        root.withdraw()
        file_path_string = tkFileDialog.asksaveasfile()   

        self.papa.rightPd.display.SaveFile(file=file_path_string.name,fileType=0)
    def BackGroundColor (self,event):
        self.papa.Freeze()
        if self.bgcolor=='black':
            self.axes.set_axis_bgcolor('white')
            self.TextToolBar.RemoveTool(2)
            self.TextToolBar.AddSimpleTool(2, wx.Image('Icons\\Negro.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Backcolor black', '')
            self.bgcolor='white'
            
        elif self.bgcolor=='white':
            self.axes.set_axis_bgcolor('black')
            self.TextToolBar.RemoveTool(2)
            self.TextToolBar.AddSimpleTool(2, wx.Image('Icons\\Blanco.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Backcolor white', '')            
            self.bgcolor='black'         
        self.TextToolBar.Realize()
        self.Bind(wx.EVT_TOOL, self.BackGroundColor, id=2)
        
        if self.papa.IsMaximized():
            self.papa.Restore()
            self.papa.Maximize()
        else:
            self.papa.Maximize()
            self.papa.Restore() 
        self.papa.Thaw()
class RightPanelDown(wx.Panel):
    def __init__(self, parent,Nodos,Bars,Shells,NodosPath,BarsPath,ShellsPath):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)  
        self.sizer = wx.BoxSizer(wx.VERTICAL)      

        #self.display =wx.TextCtrl(self, -1, style=wx.TE_MULTILINE | wx.TE_READONLY| wx.SUNKEN_BORDER | wx.TE_RICH2)
        self.display =wx.TextCtrl(self, -1, style= wx.TE_MULTILINE | wx.TE_READONLY|wx.TE_RICH |wx.TE_DONTWRAP)
        
        Sort=["Nodes","Bars","Shells"]
        Elements=[Nodos,Bars,Shells]
        Paths=[NodosPath,BarsPath,ShellsPath]
        for i in range(0,3):
            
            self.display.SetDefaultStyle(wx.TextAttr(wx.GREEN))
            self.display.AppendText(Sort[i] + " Path: " + Paths[i] +  " \n")
            self.display.SetDefaultStyle(wx.TextAttr(wx.BLUE))
            self.display.AppendText("Imported " + Sort[i] + " dictionary: " + str(Elements[i]) ) 
            if i<>2:
                self.display.AppendText( " \n"    )    
        self.display.Refresh()
        self.sizer.Add(self.display,1, wx.EXPAND, 40)
        self.SetSizer(self.sizer) 
          
        self.sizer.Fit(self)      
        self.Show(True)
    def plot_elm_clicked(self,element):
        element= element.split('_')
        self.display.AppendText(" \n")  
        if element[1]=='b':
            if len(element)==2:
                self.display.SetDefaultStyle(wx.TextAttr((1,0,0)))
                self.display.AppendText("Bar:" + element[0])    
            elif len(element)==3:
                if element[2]=='a':
                    self.display.AppendText("Bar:" + element[0])  
                    self.display.SetDefaultStyle(wx.TextAttr(wx.BLUE))
                    
                
                elif element[2]=='r':
                    self.display.SetDefaultStyle(wx.TextAttr(wx.RED))
                    self.display.AppendText("Bar:" + element[0])  
                elif element[2]=='n':
                    self.display.SetDefaultStyle(wx.TextAttr('orange'))
                    self.display.AppendText("Bar:" + element[0]) 
                                     
        elif element[1]=='s':
            self.display.SetDefaultStyle(wx.TextAttr(wx.BLUE))
            self.display.AppendText("Shell:" + element[0])   
            
        
        