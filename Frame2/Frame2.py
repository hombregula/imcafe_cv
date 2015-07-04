'''
Created on 23/11/2013

@author: hombregula
'''

import wx
import gettext
from Tkinter import *
import tkFileDialog


from Functions_Plotting.Funciones import *
from Frame2_PlotGeometry import MyFrame2_PlotGeometry
from Frame2_ClipJoints import  *
from ClipJoints.Calculations import *

class MyFrame2(wx.Frame):
    def __init__(self, base, *args, **kwds):       
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, base, *args,style= wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)            
        self.base=base
        self.piel=''
        self.DicPieles={'Plot Geometry': MyFrame2_PlotGeometry(self), 'Frame Joints': MyFrame2_ClipJoints (self)}
        
        self.__set_properties()
        self.__do__layout__()            
        
    def __set_properties(self):
        self.SetTitle(_("Analysis Type & Geometry - ASC Software"))
        self.SetSize((520, 540))
        
    def __do__layout__(self):
        self.panel = wx.Panel(self,size=(500, 400))
        a1=30
        a2=110
        
        b1=50
        b2=b1+120
        b3=b2+30
        b4=b3+30
        
        s1=200
        s2=300
        
        self.textov1=wx.StaticText(self.panel, -1, 'Kind of analysis',(a1, b1+4))
        self.analysislist=['','Plot Geometry','Frame Joints']
        self.comboboxv1=wx.ComboBox(self.panel, -1, pos=(a2,b1), size=(s1, -1), choices=self.analysislist, style=wx.CB_READONLY)
        
        self.marco1=wx.StaticBox(self.panel, -1, '  Analysis  ', (5, 5), size=(500-10, b2-60)) 
        self.marco2=wx.StaticBox(self.panel, -1, '  Geometry  ', (5, b2-30), size=(500-10, 140) ) 
        self.marco3=wx.StaticBox(self.panel, -1, '  Data Input Files  ', (5, b2 +150), size=(500-10, 140 - 30) )
        
        self.button = wx.Button(self.panel, wx.ID_ANY, _("Apply"),pos=(200, b2 +150+150 - 10))      
        self.button.Enable(False) 
        self.Bind(wx.EVT_BUTTON, self.AccionarButton, self.button)
                
        self.Layout()
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)        
    
    def OnSelect(self, event):
        
        try:
            self.piel.__Destroy__()

        except AttributeError:
            ''' '''
        if self.comboboxv1.GetValue() <> '':
            self.button.Enable(True)
            #self.piel=self.DicPieles[self.comboboxAnalysis.GetValue()]
            if self.comboboxv1.GetValue()=='Plot Geometry':
                self.piel=self.DicPieles[self.comboboxv1.GetValue()]
                self.piel.do_layout__Geometry()
            if self.comboboxv1.GetValue()=='Frame Joints':
                self.piel=self.DicPieles[self.comboboxv1.GetValue()]
                self.piel.do_layout__ClipJoints()            
        else:
            self.button.Enable(False)            
  
    def AccionarButton(self,event):        
        if self.comboboxv1.GetValue()<> "":
            self.base.AnalysisType = self.comboboxv1.GetValue()
            
            self.base.NodosPath = self.display21.GetValue()
            self.base.BarsPath = self.display22.GetValue()
            self.base.ShellsPath = self.display23.GetValue()
            
            self.base.Nodos = NodosCapture(self.display21.GetValue(),4)
            
            if self.base.BarsPath<>"":
                self.base.Bars =BarsCapture(self.display22.GetValue(),3)
            print 'ruta'
            print self.base.ShellsPath
            if self.base.ShellsPath<>"":    
                self.base.Shells = ShellsCapture(self.display23.GetValue(),4)     
                    
            self.base.defaultpivotpoint=[0,0,0]
            self.base.pivotpoint=[0,0,0]    
            
            if self.comboboxv1.GetValue()=='Frame Joints':
                self.base.Analysis=Analysis_ClipJoints(self.display24.GetValue(),self.display25.GetValue())
                
            
            self.Hide()
            self.base.__do__layout_analysis()
                

        

