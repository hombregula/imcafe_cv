'''
Created on 13/12/2013

@author: hombregula
'''
import os
import math

def truncate(x, d):
    return int(x)+(int((x-int(x))*(10.0**d)))/(10.0**d)

class Analysis_ClipJoints():
    def __init__(self, GeometryFilePath,LoadsFilePath):
        ####
        self.geo_file=GeometryFilePath
        ####
        
        ####
        self.lcs_file = LoadsFilePath
        ####
        
        self.all_file=''
        self.Analysis={}
    
    ## GEO DICTIONARY & ELEMENTS LIST ##        
        f=open(self.geo_file,'r').read().split('\n')
        self.geo={}
        self.elementList=[]
        self.elementDict={}
        for i in f:        
            i= i.split(' ')
            while (('' in i)==True):
                i.remove('')                
            if len(i)>0:
                ''' si es dos id y Type
                si es X, datos de allow
                si es X+2, es geometri
                '''
                if len(i)==2:
                    self.geo[i[1]]=[]
                    self.elementList= self.elementList + [i[1]]
                    self.elementDict[i[1]]=i[0]
                else:
                    self.geo[ self.elementList [-1+len(self.elementList)]] = self.geo[ self.elementList [-1+len(self.elementList) ] ] + [i]             

    ## LCS LIST ##       
                
        f=open(self.lcs_file,'r').read().split('\n')
        self.lcs={}
        for i in f:
            i= i.split(' ')
            while (('' in i)==True):
                i.remove('')                
            if len(i)>0:
                LLaves=self.lcs.keys()
                if ((i[0]in LLaves)==True):
                    self.lcs[i[0]]=self.lcs[i[0]] + [(i[1],i[2])]
                else:
                    self.lcs[i[0]]=[]
                    self.lcs[i[0]]=self.lcs[i[0]] + [(i[1],i[2])]               

        self.SingleAnalysisGeneration()
        self.MinimoMinimorum=self.MinimoMinimorum()
    def SingleAnalysisGeneration(self):                 
        for i in self.elementList:

            self.Analysis[i]= AnalisisElemento(self.geo[i],self.lcs[i],i,self.elementDict)
    def MinimoMinimorum(self):
        minRF=9999
        minimo=()
        for i in self.elementList:
            if float(self.Analysis[i].minimorum[0][1])<float(minRF):
                minimo=(i,self.Analysis[i].minimorum)
                minRF=self.Analysis[i].minimorum[0][1]
        return minimo

class AnalisisElemento():
    def __init__ (self, geo, lcs, elemento,elementDict):
        self.Frame=geo[0][1]
        self.Stringers=geo[0][2]
        self.Grids=(geo[0][4],geo[0][5])

        self.Skin=[]
        self.ClipSk=[]
        self.ClipFr=[]
        self.Former=[]
        
        self.former_allw_factor= 0
        
        if (elementDict[elemento]=='INTEGRAL') or   (elementDict[elemento]=='CONTINUOUS'):             
            for i in geo:
                if i[0]=='Skin':
                    self.Skin= self.Skin + [dataline_and_allowable(i)]
                elif i[0]=='Clip-sk':
                    self.ClipSk= self.ClipSk + [dataline_and_allowable(i)]
                if elementDict[elemento]=='CONTINUOUS':
                    if   i[0]=='Clip-fr':
                        self.ClipFr= self.ClipFr + [dataline_and_allowable(i)]
                    elif i[0]=='Former':
                        self.Former= self.Former + [dataline_and_allowable(i)]   
        elif (elementDict[elemento]=='TYPICAL'):
            
            for i in geo:
                if i[0]=='Skin':
                    self.Skin= self.Skin + [dataline_and_allowable(i)]
                elif i[0]=='Clip-sk':
                    self.ClipSk= self.ClipSk + [dataline_and_allowable(i)]
    
                elif   i[0]=='Clip-fr':
                    self.ClipFr= self.ClipFr + [dataline_and_allowable(i)]
                elif i[0]=='Former':
                    self.Former= self.Former + [dataline_and_allowable(i)] 
                

                if len(i)>=9:                    
                    if self.former_allw_factor < float(i[8]):
                        self.former_allw_factor = float(i[8])

        else:
            print ' This kind of element is no known '                      
                           
        if self.Skin<>[]:
            self.minSkin=self.minimoZona(self.Skin,lcs,elementDict[elemento],self.former_allw_factor,'Skin')
        if self.ClipSk<>[]:
            self.minClipSk=self.minimoZona(self.ClipSk,lcs,elementDict[elemento],self.former_allw_factor,'Skin-fr')
        if self.ClipFr<>[]:
            self.minClipFr=self.minimoZona(self.ClipFr,lcs,elementDict[elemento],self.former_allw_factor,'Clip-fr')
        if self.Former<>[]:
            self.minFormer=self.minimoZona(self.Former,lcs,elementDict[elemento],self.former_allw_factor,'Former')
        
        self.minimorum=self.minimo()
    def minimoZona(self,ListZone,lcs,type,former_allw_factor,kind_element):
        element=ListZone[0].element
        thickness=ListZone[0].thickness
        material=ListZone[0].material
        process=ListZone[0].process
        
        minallw=999999
        allwAbs=0
        nrivet=0
        rivet=""
        
        minRF=99999
        
        for i in ListZone:

            
            if float(minallw)>float(i.allow):

                minallw=i.allow
                rivet=i.rivet  
          

            nrivet=nrivet + float(i.nrivet)
            allwAbs=allwAbs+float(i.nrivet)*float(i.allow)

        if type=='TYPICAL':      
                #allwAbs=allwAbs+float(i.nrivet)*float(i.allow)
                if (kind_element=='Clip-fr')or(kind_element=='Former'):
                    #allwAbs= "%.2f" %  (float(minallw)/float(former_allw_factor))
                    allwAbs=  (float(minallw)/float(former_allw_factor))
                    
       
        
        minRFs=self.Calc_All_RFs(allwAbs,lcs)

        
        Adevolver=[minRFs,[element,thickness,material,process,nrivet,rivet,minallw,allwAbs]]   

        return Adevolver
    def minimo(self):
        minimom=''
        minRF=9999
        if self.Skin<>[]:   
            if float(self.minSkin[0][1])<float(minRF):
                minRF=self.minSkin[0][1]
                minimom=self.minSkin
        if self.ClipSk<>[]:   
            if float(self.minClipSk[0][1])<float(minRF):
                minRF=self.minClipSk[0][1]          
                minimom=self.minClipSk
        if self.ClipFr<>[]:      
            if float(self.minClipFr[0][1])<float(minRF):
                minRF=self.minClipFr[0][1]        
                minimom=self.minClipFr
        if self.Former<>[]:                
            if float(self.minFormer[0][1])<float(minRF):
                minRF=self.minFormer[0][1]          
                minimom=self.minFormer 
        return minimom
    def Calc_All_RFs(self,allw,lcs):
        RFs=[]
        RFmin=9999
        RFsmin=()
        for i in lcs:
            try:
                RFs=RFs + [(i[0],truncate(float(allw)/float(i[1]),5)   )]
                
                if float(allw)/float(i[1]) < float(RFmin):
                    RFmin=float(allw)/float(i[1])
                    #RFsmin=(i[0], "%.2f" % float(truncate(RFmin,2)),"%.2f" % float(i[1]))
                    RFsmin=(i[0],  float(truncate(RFmin,5)),float(i[1]))
                
            except ZeroDivisionError:
                
                a=2
                RFs=RFs + [(i[0],9999)]
                #raise
        return RFsmin
        #return RFs,RFsmin    
    
#class SingleAnalysis():
class dataline_and_allowable():
    def __init__(self,data): 
        self.data=data
        self.allow=self.Calc_Allowable(data)
    
    def Calc_Allowable(self,data):
        self.element=self.data[0]
        self.thickness=self.data[1]
        self.material=self.data[2]
        self.process=self.data[3]
        self.nrivet=self.data[4]
        self.rivet=self.data[5]
        
        ###
        file=r'BBDD\Allowables.txt'
        ###
        
        f=open(file,'r').read().split('\n')    
        for i in f:   
            
            i=i.split(' ')

            while (('' in i)==True):
                i.remove('')  
            
            if len(i)>0:
                if ("%.5f" % float(i[0]))==("%.5f" % float(self.thickness)):
                    if (i[1])==(self.material):
                        if (i[2])==(self.process):
                                if (i[3])==(self.rivet):
                                    return (i[4])
        return False
    
class dataline_and_allowable_typical(dataline_and_allowable):                
    def __init__(self,data): 
        self.data=data
        self.allow=self.Calc_Allowable(data)
