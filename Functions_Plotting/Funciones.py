'''
Created on 03/11/2013

@author: hombregula
'''
def NodosCapture(Ruta,CampoEmpiezaCoord):
    #CampoEmpiezaCoord=4
    NFile=open(Ruta, 'r', 0)
    Nodos={}
    for line in NFile:
        Nodos[line[8:16].strip()]= [float(line[((CampoEmpiezaCoord-1)*8):((CampoEmpiezaCoord+0)*8)])]
        Nodos[line[8:16].strip()]= Nodos[line[8:16].strip()] + [float(line[((CampoEmpiezaCoord+0)*8):((CampoEmpiezaCoord+1)*8)])]
        if len(line)>=(8*(CampoEmpiezaCoord+2)):    
            Nodos[line[8:16].strip()]= Nodos[line[8:16].strip()] + [float(line[((CampoEmpiezaCoord+1)*8):((CampoEmpiezaCoord+2)*8)])]        
        else:
            Nodos[line[8:16].strip()]= Nodos[line[8:16].strip()] + [float(line[((CampoEmpiezaCoord+1)*8):])] 
    return Nodos

def ShellsCapture(Ruta,CampoEmpiezaCoord):
    #CampoEmpiezaCoord=4
    NFile=open(Ruta, 'r', 0)
    Quads={}
    for line in NFile:
        Quads[line[8:16].strip()]= [str(int(line[((CampoEmpiezaCoord-1)*8):((CampoEmpiezaCoord+0)*8)]))]
        Quads[line[8:16].strip()]= Quads[line[8:16].strip()] + [str(int(line[((CampoEmpiezaCoord+0)*8):((CampoEmpiezaCoord+1)*8)]))]
        Quads[line[8:16].strip()]= Quads[line[8:16].strip()] + [str(int(line[((CampoEmpiezaCoord+1)*8):((CampoEmpiezaCoord+2)*8)]))]
        if (len(line)>(8*(CampoEmpiezaCoord+2))) :
            try:   
                Quads[line[8:16].strip()]= Quads[line[8:16].strip()] + [str(int(line[((CampoEmpiezaCoord+2)*8):((CampoEmpiezaCoord+3)*8)]))]
            except:
                pass  
        ''' 
        else:
            Quads[line[8:16].strip()]= Quads[line[8:16].strip()] + [str(int(line[((CampoEmpiezaCoord+2)*8):]))]        
        '''
    return Quads

def BarsCapture(Ruta,CampoEmpiezaCoord):
#    CampoEmpiezaCoord=3
    NFile=open(Ruta, 'r', 0)
    Bars={}
    for line in NFile:
        Bars[line[8:16].strip()]=[str(int(line[((CampoEmpiezaCoord-1)*8):((CampoEmpiezaCoord+0)*8)]))]
        
        if len(line)>=(8*(CampoEmpiezaCoord+2)):    
            Bars[line[8:16].strip()]= Bars[line[8:16].strip()] + [str(int(line[((CampoEmpiezaCoord+0)*8):((CampoEmpiezaCoord+1)*8)]))]        
        else:
            #Bars[line[8:16].strip()]= Bars[line[8:16].strip()] + [str(line[((CampoEmpiezaCoord+1)*8):])]        
            Bars[line[8:16].strip()]= Bars[line[8:16].strip()] + [str(int(line[((CampoEmpiezaCoord+0)*8):((CampoEmpiezaCoord+1)*8)]))]
    NFile.close()
    return Bars
def minComparison(Ref,tmp):
    if Ref>tmp:
        return tmp
    else:
        return Ref
def MAXComparison(Ref,tmp):
    if Ref<tmp:
        return tmp
    else:
        return Ref  

