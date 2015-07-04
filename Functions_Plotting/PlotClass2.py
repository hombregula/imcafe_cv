'''
Created on 15/11/2013

@author: hombregula
'''

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
from Funciones import minComparison , MAXComparison
import wx



class Pintar2:
    def __init__(self,Nodos,Bars,Skins,Figura):
        self.Nodes=Nodos
        self.Skin=Skins
        self.Bars=Bars
        self.ax=Figura
        
        self.LimX=(9999999999,-9999999999)
        self.LimY=(9999999999,-9999999999)
        self.LimZ=(9999999999,-9999999999)
        
        self.FactorLim=1.0
        
    def Plot000(self):
        self.ax.scatter (0,0,0,c='g')                        
            
    def PlotNodes(self):
        Indice=self.Nodes.keys()
        for i in Indice:
            self.ax.scatter (self.Nodes[i][0],self.Nodes[i][1],self.Nodes[i][2],c='g')                        
            self.LimX=(minComparison(self.LimX[0],self.Nodes[i][0]),MAXComparison(self.LimX[1],self.Nodes[i][0]))
            self.LimY=(minComparison(self.LimY[0],self.Nodes[i][1]),MAXComparison(self.LimY[1],self.Nodes[i][1]))
            self.LimZ=(minComparison(self.LimZ[0],self.Nodes[i][2]),MAXComparison(self.LimZ[1],self.Nodes[i][2]))
    def PlotBars(self):
        try:
            Indice=self.Bars.keys()
            self.ArrayBars=[]
            for i in Indice:
                x = np.linspace(self.Nodes[self.Bars[i][0]][0], self.Nodes[self.Bars[i][1]][0], 100)
                y = np.linspace(self.Nodes[self.Bars[i][0]][1], self.Nodes[self.Bars[i][1]][1], 100)
                z = np.linspace(self.Nodes[self.Bars[i][0]][2], self.Nodes[self.Bars[i][1]][2], 100)
                mylabel=str(i)+'_b'
                self.ArrayBars=self.ArrayBars + [self.ax.plot(x, y, z,'y',linewidth=2,picker=5,label=mylabel)]
                #self.ax.plot(x, y, z,'y',linewidth=1)
            self.PlotBarsLimits()
        except:
            print i
            print self.Nodes[self.Bars[i][3]][0] 
            print self.Nodes[self.Bars[i][3]][1]
            print self.Nodes[self.Bars[i][3]][2]
            raise
        
    def PlotBars_Clips(self, parent,axes):
        try:
            MisBarras= parent.Analysis.Analysis.keys()
            Indice=self.Bars.keys()
            self.axes=axes
            self.ArrayBars=[]
            self.ArrayBars0=[]
            self.ArrayBars1=[]
            self.ArrayBars2=[]
            for i in Indice:

                if (i in MisBarras)==False:

                    x = np.linspace(self.Nodes[self.Bars[i][0]][0], self.Nodes[self.Bars[i][1]][0], 100)
                    y = np.linspace(self.Nodes[self.Bars[i][0]][1], self.Nodes[self.Bars[i][1]][1], 100)
                    z = np.linspace(self.Nodes[self.Bars[i][0]][2], self.Nodes[self.Bars[i][1]][2], 100)
                    mylabel=str(i)+'_b'
                    self.ArrayBars=self.ArrayBars + [self.ax.plot(x, y, z,'y',linewidth=0.5,picker=5,label=mylabel)]
                    #self.ax.plot(x, y, z,'y',linewidth=1)
                else:

                    x = np.linspace(self.Nodes[self.Bars[i][0]][0], self.Nodes[self.Bars[i][1]][0], 100)
                    y = np.linspace(self.Nodes[self.Bars[i][0]][1], self.Nodes[self.Bars[i][1]][1], 100)
                    z = np.linspace(self.Nodes[self.Bars[i][0]][2], self.Nodes[self.Bars[i][1]][2], 100)                    

                    if float(parent.Analysis.Analysis[i].minimorum[0][1]) < 1.00001:
                        mylabel=str(i)+'_b_r' 
                        self.ArrayBars0=self.ArrayBars0 + [self.ax.plot(x, y, z, color=(1,0,0),linewidth=2,picker=5,label=mylabel)]
                    elif float(parent.Analysis.Analysis[i].minimorum[0][1]) > 1.10:
                        mylabel=str(i)+'_b_a'                      
                        self.ArrayBars2=self.ArrayBars2 + [self.ax.plot(x, y, z,color=(0,0.69,0.94),linewidth=2,picker=5,label=mylabel)]                        
                    else:
                        mylabel=str(i)+'_b_n'                         
                        self.ArrayBars1=self.ArrayBars1 + [self.ax.plot(x, y, z,color=(1,0.4,0),linewidth=2,picker=5,label=mylabel)]                          

                        
            self.PlotBarsLimits()
            '''
            yellow_proxy = plt.Rectangle((0, 0), 1, 1, fc="y") 
            red_proxy = plt.Rectangle((0, 0), 1, 1, fc="r")
            blue_proxy = plt.Rectangle((0, 0), 1, 1, fc="b")
            orange_proxy = plt.Rectangle((0, 0), 1, 1, fc="g")
            '''
            yellow_proxy = plt.Rectangle((0, 0), 1, 1, fc="y") 
            red_proxy = plt.Rectangle((0, 0), 1, 1, fc="r")
            orange_proxy = plt.Rectangle((0, 0), 1, 1, fc=(1,0.4,0))
            blue_proxy = plt.Rectangle((0, 0), 1, 1, fc=(0,0.69,0.94))
            #ax.legend([blue_proxy,red_proxy],['cars','bikes'])            
            
            #self.axes.legend([yellow_proxy,red_proxy,blue_proxy,green_proxy],['Not analized','RF < 1.10','RF < 3.00','RF > 3.00'],framealpha=0.5,frameon=None)
            self.axes.legend([yellow_proxy,red_proxy,orange_proxy,blue_proxy],['Not analized','RF < 1.00','RF < 1.10','RF > 1.10'],framealpha=0.5)
        except:
            raise        
    def PlotBars_Clips_Inputs(self, parent,axes):
        try:
            MisBarras= parent.Analysis.Analysis.keys()
            Indice=self.Bars.keys()
            self.axes=axes
            self.ArrayBars=[]
            self.ArrayBars0=[]
            self.ArrayBars1=[]
            self.ArrayBars2=[]
            for i in Indice:

                if (i in MisBarras)==False:

                    x = np.linspace(self.Nodes[self.Bars[i][0]][0], self.Nodes[self.Bars[i][1]][0], 100)
                    y = np.linspace(self.Nodes[self.Bars[i][0]][1], self.Nodes[self.Bars[i][1]][1], 100)
                    z = np.linspace(self.Nodes[self.Bars[i][0]][2], self.Nodes[self.Bars[i][1]][2], 100)
                    mylabel=str(i)+'_b'
                    self.ArrayBars=self.ArrayBars + [self.ax.plot(x, y, z,'y',linewidth=0.5,picker=5,label=mylabel)]
                    #self.ax.plot(x, y, z,'y',linewidth=1)
                else:

                    x = np.linspace(self.Nodes[self.Bars[i][0]][0], self.Nodes[self.Bars[i][1]][0], 100)
                    y = np.linspace(self.Nodes[self.Bars[i][0]][1], self.Nodes[self.Bars[i][1]][1], 100)
                    z = np.linspace(self.Nodes[self.Bars[i][0]][2], self.Nodes[self.Bars[i][1]][2], 100)                    

                    if (parent.Analysis.elementDict[i])=='TYPICAL':
                        mylabel=str(i)+'_b_r' 
                        self.ArrayBars0=self.ArrayBars0 + [self.ax.plot(x, y, z, color=(1,0,0),linewidth=2,picker=5,label=mylabel)]
                    elif (parent.Analysis.elementDict[i])=='CONTINUOUS':
                        mylabel=str(i)+'_b_a'                      
                        self.ArrayBars2=self.ArrayBars2 + [self.ax.plot(x, y, z,color=(0,0.69,0.94),linewidth=2,picker=5,label=mylabel)]                        
                    elif (parent.Analysis.elementDict[i])=='INTEGRAL':
                        mylabel=str(i)+'_b_n'                         
                        self.ArrayBars1=self.ArrayBars1 + [self.ax.plot(x, y, z,color=(1,0.4,0),linewidth=2,picker=5,label=mylabel)]                          

                        
            self.PlotBarsLimits()
            '''
            yellow_proxy = plt.Rectangle((0, 0), 1, 1, fc="y") 
            red_proxy = plt.Rectangle((0, 0), 1, 1, fc="r")
            blue_proxy = plt.Rectangle((0, 0), 1, 1, fc="b")
            orange_proxy = plt.Rectangle((0, 0), 1, 1, fc="g")
            '''
            yellow_proxy = plt.Rectangle((0, 0), 1, 1, fc="y") 
            red_proxy = plt.Rectangle((0, 0), 1, 1, fc="r")
            blue_proxy = plt.Rectangle((0, 0), 1, 1, fc=(0,0.69,0.94))
            orange_proxy = plt.Rectangle((0, 0), 1, 1, fc=(1,0.4,0))
            #ax.legend([blue_proxy,red_proxy],['cars','bikes'])            
            
            #self.axes.legend([yellow_proxy,red_proxy,blue_proxy,green_proxy],['Not analized','RF < 1.10','RF < 3.00','RF > 3.00'],framealpha=0.5,frameon=None)
            self.axes.legend([yellow_proxy,red_proxy,orange_proxy,blue_proxy],['Not analized','Typical','Integral','Continuous'],framealpha=0.5)
        except:
            raise           
    def PlotBarsLimits(self):
        try:
            Indice=self.Bars.keys()
            self.ArrayBars=[]
            for i in Indice:
                for t in (0,1):
                    self.LimX=(minComparison(self.LimX[0],self.Nodes[self.Bars[i][t]][0]),MAXComparison(self.LimX[1],self.Nodes[self.Bars[i][t]][0]))
                    self.LimY=(minComparison(self.LimY[0],self.Nodes[self.Bars[i][t]][1]),MAXComparison(self.LimY[1],self.Nodes[self.Bars[i][t]][1]))
                    self.LimZ=(minComparison(self.LimZ[0],self.Nodes[self.Bars[i][t]][2]),MAXComparison(self.LimZ[1],self.Nodes[self.Bars[i][t]][2]))
        except:
            dial = wx.MessageDialog(None, 'Error loading file. Nodes of ' + i + ' bar has not been located', 'Error', wx.OK | wx.ICON_ERROR)
            dial.ShowModal()
            print self.Nodes[self.Bars[i][3]][0] 
            print self.Nodes[self.Bars[i][3]][1]
            print self.Nodes[self.Bars[i][3]][2]
            raise                                                                                         
    def PlotShells(self):
        try:
            Indice=self.Skin.keys()
            self.ArrayShells=[]
            for i in Indice:                      
                N1 = (self.Nodes[self.Skin[i][0]][0], self.Nodes[self.Skin[i][0]][1], self.Nodes[self.Skin[i][0]][2])
                N2 = (self.Nodes[self.Skin[i][1]][0], self.Nodes[self.Skin[i][1]][1], self.Nodes[self.Skin[i][1]][2])
                N3 = (self.Nodes[self.Skin[i][2]][0], self.Nodes[self.Skin[i][2]][1], self.Nodes[self.Skin[i][2]][2])
                try:
                    N4 = (self.Nodes[self.Skin[i][3]][0], self.Nodes[self.Skin[i][3]][1], self.Nodes[self.Skin[i][3]][2]) 
                    verts=[[N1,N2,N3,N4]]
                except:
                    verts=[[N1,N2,N3]]                    
                codes=(1,2,2,2,79)
                mylabel=str(i)+'_s' 
                poligono=art3d.Poly3DCollection(verts,facecolor='b',alpha=0.4,picker=5,label=mylabel)  
                self.ArrayShells=self.ArrayShells+[self.ax.add_collection3d(poligono, zdir='y')]
                #self.ax.add_collection3d(poligono, zdir='y')      
                self.PlotShellsLimits()
        except:
            dial = wx.MessageDialog(None, 'Error loading file. Nodes of ' + i + ' shell has not been located', 'Error', wx.OK | wx.ICON_ERROR)
            dial.ShowModal()            
            raise 
    
    def PlotShellsLimits(self):
        try:
            Indice=self.Skin.keys()
            self.ArrayShells=[]
            for i in Indice:                         
                for t in (0,3):
                    self.LimX=(minComparison(self.LimX[0],self.Nodes[self.Skin[i][t]][0]),MAXComparison(self.LimX[1],self.Nodes[self.Skin[i][t]][0]))
                    self.LimY=(minComparison(self.LimY[0],self.Nodes[self.Skin[i][t]][1]),MAXComparison(self.LimY[1],self.Nodes[self.Skin[i][t]][1]))
                    self.LimZ=(minComparison(self.LimZ[0],self.Nodes[self.Skin[i][t]][2]),MAXComparison(self.LimZ[1],self.Nodes[self.Skin[i][t]][2]))
        except:
            print i

    def __Redifine_Nodes__(self,Xn,Yn,Zn):
        for i in self.Nodes.keys():
            self.Nodes[i]=[self.Nodes[i][0]-Xn,self.Nodes[i][1]-Yn,self.Nodes[i][2]-Zn]

    def Redifine_2_Zero(self):
        if self.LimX[1]<=0:
                Xn=-self.LimX[0]
        if self.LimX[0]>=0:
                Xn=-self.LimX[0]
        if self.LimX[0]<=0:
            if self.LimX[1]>=0:
                if self.LimX[1]*0.85 > abs(self.LimX[0]):
                    Xn=-self.LimX[0]
                else:
                    Xn=0

        if self.LimY[1]<=0:
                Yn=-self.LimY[0]
        if self.LimY[0]>=0:
                Yn=-self.LimY[0]
        if self.LimY[0]<=0:
            if self.LimY[1]>=0:
                if self.LimY[1]*0.85 > abs(self.LimY[0]):
                    Yn=-self.LimY[0]
                else:
                    Yn=0
        
        if self.LimZ[1]<=0:
            Zn=-self.LimZ[0]
        if self.LimZ[0]>=0:
                Zn=-self.LimZ[0]
        if self.LimZ[0]<=0:
            if self.LimZ[1]>=0:
                if self.LimZ[1]*0.95 > abs(self.LimZ[0]):
                    Zn=-self.LimZ[0]
                else:
                    Zn=0   
                     
        for i in self.Nodes.keys():
            self.Nodes[i]=[self.Nodes[i][0]+Xn,self.Nodes[i][1]+Yn,self.Nodes[i][2]+Zn]             
    
    def LimitesX(self,min,Max):
        self.ax.set_xlim3d(min,Max) 
    def LimitesY(self,min,Max):        
        self.ax.set_ylim3d(min,Max) 
    def LimitesZ(self,min,Max):        
        self.ax.set_zlim3d(min,Max)             
  
