'''
Created on 19/12/2013

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

from ClipJoints.Calculations import truncate

class ClipResults(wx.Frame):
    def __init__(self, base, *args, **kwds):       
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, base, *args,style= wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)            
        self.base=base
        self.__set_properties()
        self.__do_layout()
        
    def __set_properties(self):
        self.SetTitle(_(" Frame Joints - Results Exportation "))
        self.SetSize((420, 190))
        
    def __do_layout(self):      
        a1=30
        a2=110
        
        b1=35
        b2= b1+100
        b3=300
        b4=330
        
        s1=200
        s2=60          
        
        self.panel = wx.Panel(self,size=(190, 400))
        
        '''self.rb1 = wx.RadioButton(self.panel, -1, 'Minimum Minimorum', (10, 30), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(self.panel, -1, 'Minimum per analysis', (10, 50))
        self.rb3 = wx.RadioButton(self.panel, -1, 'Minimum per union', (10, 70))''' 
        
        self.chb1=wx.CheckBox(self.panel, -1 ,'  Minimum Minimorum', (15, 30))
        self.chb2=wx.CheckBox(self.panel, -1 ,'  Minimum per analysis', (15, 50))        
        self.chb3=wx.CheckBox(self.panel, -1 ,'  Minimum per union', (15, 70))
        
        self.marco1=wx.StaticBox(self.panel, -1, ' Data to export  ', (5, 5), size=(390, 95))         
        
        
        self.button0 = wx.Button(self.panel, wx.ID_ANY, _("Close"),pos=(320, 120))       
        self.button1 = wx.Button(self.panel, wx.ID_ANY, _("Acept"),pos=(240, 120))       
        self.Bind(wx.EVT_BUTTON, self.AccionarButton0, self.button0)
        self.Bind(wx.EVT_BUTTON, self.AccionarButton1, self.button1)
        self.Layout()  
                    

    def AccionarButton0(self,event):            
        self.Destroy()
        
    def AccionarButton1(self,event): 
        #print self.base.Analysis           
        #print self.base.Analysis.geo
        '''print self.base.Analysis.Analysis   
        print self.base.Analysis.Analysis.keys()
        a=self.base.Analysis.Analysis.keys()[0]
        print self.base.Analysis.Analysis[a]
        print self.base.Analysis.Analysis[a].minimorum'''
                              
        myfile= wx.FileDialog(self, " Save Frame Joints ", "", "","Result Files (*.RES.1)|*.RES.1", wx.FD_SAVE )
        if myfile.ShowModal() == wx.ID_CANCEL:
            return     # the user changed idea...
        f=open(myfile.GetPath(),'w')
        if self.chb1.GetValue():
            f.write('                          #### MINIMUM MINIMORUM #### \n')
            f.write('\n')
            minimo= self.base.Analysis.MinimoMinimorum[0]
            factor=''
            if self.base.Analysis.elementDict[self.base.Analysis.MinimoMinimorum[0]]=="TYPICAL":
                factor=" (" + str("%2f"% float(self.base.Analysis.Analysis[self.base.Analysis.MinimoMinimorum[0]].former_allw_factor)) + ")"
                print factor            
            f.write(' Element: ' + str(self.base.Analysis.MinimoMinimorum[0]) + '  --- ' 
                    + str(self.base.Analysis.geo[minimo][0][0]) + ': ' 
                    + str(self.base.Analysis.geo[minimo][0][1]) + '; '  
                    + str(self.base.Analysis.geo[minimo][0][2]) + '; ' 
                    + str(self.base.Analysis.geo[minimo][0][3]) + ': ' 
                    + str(self.base.Analysis.geo[minimo][0][4]) + ' and ' 
                     
                    + str(self.base.Analysis.geo[minimo][0][5])+'; ' + self.base.Analysis.elementDict[self.base.Analysis.MinimoMinimorum[0]] + factor + '\n') 
                    #+ str(self.base.Analyisis.geo[minimo][0][3]) + '\n')
                    
            f.write( '          ' + poner_espacios(str(self.base.Analysis.MinimoMinimorum[1][1][0]),10) + ' '
                    + poner_espacios('Mat. = ' + str(self.base.Analysis.MinimoMinimorum[1][1][2]),15) + ' '
                    + poner_espacios('Proc. = ' + str(self.base.Analysis.MinimoMinimorum[1][1][3]),15) + ' '
                    + poner_espacios('Rivet = ' + str(self.base.Analysis.MinimoMinimorum[1][1][5]),21) + ' '
                    + poner_espacios('Allw. = ' + str("%.1f" % self.base.Analysis.MinimoMinimorum[1][1][7]),18) + ' '
                    + poner_espacios('Lc = ' + str("%.1f" % self.base.Analysis.MinimoMinimorum[1][0][2]),17 ) + ' '               
                    + poner_espacios('LcId. = ' + str(self.base.Analysis.MinimoMinimorum[1][0][0]),17 ) + ' '                
                    + 'RF = ' + str(truncate(self.base.Analysis.MinimoMinimorum[1][0][1],2)) +'\n')                                           
            f.write('\n')
            f.write('\n')        
        if self.chb2.GetValue():
            f.write('                         #### MINIMUM PER ELEMENT #### \n')
            f.write('\n')        
            a=self.base.Analysis.Analysis
            g=self.base.Analysis.geo
            e=self.base.Analysis.elementList
            for i in e:
                factor=''
                if self.base.Analysis.elementDict[i]=="TYPICAL":
                    factor=" (" + str("%2f"% float(self.base.Analysis.Analysis[i].former_allw_factor)) + ")"
                    print factor
                at=a[i].minimorum
                gt=g[i]
                f.write(' Element: ' + str(i) + '  --- ' 
                        + str(gt[0][0]) + ': ' 
                        + str(gt[0][1]) + '; '  
                        + str(gt[0][2]) + '; ' 
                        + str(gt[0][3]) + ': ' 
                        + str(gt[0][4]) + ' and ' 
                        + str(gt[0][5])+'; ' + self.base.Analysis.elementDict[i]+factor+'\n') 
                        #+ str(self.base.Analyisis.geo[minimo][0][3]) + '\n')
                f.write( '          ' + poner_espacios(str(at[1][0]),10) + ' ' 
                        + poner_espacios('Mat. = '   + str(at[1][2]),15) + ' ' 
                        + poner_espacios('Proc. = '  + str(at[1][3]),15) + ' '  
                        + poner_espacios('Rivet = '  + str(at[1][5]),21) + ' ' 
                        + poner_espacios('Allw. = '  + str("%.1f" % at[1][7]),18) + ' ' 
                        + poner_espacios('Lc = '     + str("%.1f" % at[0][2]),17) + ' '                    
                        + poner_espacios('LcId. = '  + str(at[0][0]),17) + ' '                  
                        + 'RF = ' + str(truncate(at[0][1],2)) +'\n')
                f.write('\n')
                f.write('\n')
            if self.chb3.GetValue():
                f.write('                      #### MINIMUM PER ELEMENT JOINT #### \n')
                f.write('\n') 
            a=self.base.Analysis.Analysis
            g=self.base.Analysis.geo
            e=self.base.Analysis.elementList
            for i in e:
                factor=''
                if self.base.Analysis.elementDict[i]=="TYPICAL":
                    factor=" (" + str("%2f"% float(self.base.Analysis.Analysis[i].former_allw_factor)) + ")"
                    print factor                
                gt=g[i]
                f.write(' Element: ' + str(i) + '  --- ' 
                        + str(gt[0][0]) + ': ' 
                        + str(gt[0][1]) + '; '  
                        + str(gt[0][2]) + '; ' 
                        + str(gt[0][3]) + ': ' 
                        + str(gt[0][4]) + ' and ' 
                        + str(gt[0][5])+'; '+ factor + '\n')                
                if a[i].Skin<>[]:

                    atsk=a[i].minSkin
                    atclsk=a[i].minClipSk
                    minimo=[]
                    if float(atsk[0][1])>float(atclsk[0][1]):
                        minimo=[atclsk]
                    elif float(atsk[0][1])==float(atclsk[0][1]):
                        minimo=[atsk,atclsk]
                    else:
                        minimo=[atsk]
                    
                    for ii in minimo:
                        
                        f.write( '          ' +  poner_espacios(str(ii[1][0]),10) + ' '  
                                + poner_espacios('Mat. = '   + str(ii[1][2]),15) + ' ' 
                                + poner_espacios('Proc. = '  + str(ii[1][3]),15) + ' ' 
                                + poner_espacios('Rivet = '  + str(ii[1][5]),21) + ' '  
                                + poner_espacios('Allw. = '  + str("%.1f" % ii[1][7]),18) + ' '  
                                + poner_espacios('Lc = '     + str("%.1f" % ii[0][2]),17) + ' '                  
                                + poner_espacios('LcId. = '  + str(ii[0][0]),17) + ' '                  
                                + 'RF = '     + str(truncate(ii[0][1],2)) + '\n')   

                if a[i].Former<>[]:
                    atfr=a[i].minFormer
                    atclfr=a[i].minClipFr
                    
                    
                    minimo=[]
                    if float(atfr[0][1])>float(atclfr[0][1]):
                        minimo=[atclfr]
                    elif float(atfr[0][1])==float(atclfr[0][1]):
                        minimo=[atfr,atclfr]
                    else:
                        minimo=[atfr]
                    
                    for ii in minimo:
                        f.write( '          ' +  poner_espacios(str(ii[1][0]),10) + ' '  
                                +  poner_espacios('Mat. = '   + str(ii[1][2]),15) + ' '  
                                +  poner_espacios('Proc. = '  + str(ii[1][3]),15) + ' '   
                                +  poner_espacios('Rivet = '  + str(ii[1][5]),21) + ' '  
                                +  poner_espacios('Allw. = '  + str("%.1f" % ii[1][7]),18) + ' '  
                                +  poner_espacios('Lc = '     + str("%.1f" % ii[0][2]),17) + ' '                     
                                +  poner_espacios('LcId. = '  + str(ii[0][0]),17) + ' '                 
                                + 'RF = '     + str(truncate(ii[0][1],2)) +'\n') 
                f.write('\n')                                       
        f.close        
        
        self.Destroy()       
    
def poner_espacios(cadena,ocupacion):
    while (len(cadena)<ocupacion):
        cadena=cadena + ' '
    return cadena
     
  
        