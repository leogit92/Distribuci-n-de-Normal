import math

def FirstFormule(NMax,NMin):
    Result = NMax-NMin
    return Result

def SecondFormule(ND):
    Vm = math.log(int(ND),10)
    Vm = 3.3 * float(Vm)
    Vm = 1 + float(Vm)
    #Vm = int(Vm)+1
    return math.ceil(Vm)

def ThirdFormule(VR,Vm):
    VC = VR/Vm
    #VC = int(VC)+1
    return math.ceil(VC)

def FourthFormule(VC,Vm,VR):
    VRR = VC*Vm
    VRR = VRR - VR
    VRR = VRR/2
    return VRR

def FivethFormule(NMax,NMin,RR):
    ResultMax = NMax+RR
    ResultMin = NMin-RR
    return (ResultMax,ResultMin)

def SixthFormule(Dt):
    Tallo = {}
    for tll in range(0,201,10):
        Tallo["F"+str(tll)] = {"exist":"No","C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
    for Num in Dt:
        for NX in range(0,201,10):
            if int(Num) >= NX and int(Num) < NX+10:
                VarSt = str(Num)
                if int(Num) < 10:
                    VarStC = "C"+VarSt[0:]
                elif int(Num) >= 10 and int(Num) < 100:
                    VarStC = "C"+VarSt[1:]
                #print(VarStC)
                Tallo["F"+str(NX)]["exist"] = "Yes"
                Tallo["F"+str(NX)][str(VarStC)] += 1
                break
    return Tallo

def SeventhFormule(RMax,RMin,NI,AI,LDT):
    TDF = {}
    TDF["Valu"] =  {}
    TDF["IAC"] = {}
    TDF["F"] = {}
    TDF["FAA"] = {}
    TDF["FAD"] = {}
    TDF["FR"] = {}
    TDF["FRA"] = {}
    TDF["MC"] = {}
    DI = RMin
    DNN = RMin-1
    for NV in range(1,NI+1):
        TDF["Valu"]["V"+str(NV)] = NV
        TDF["IAC"]["V"+str(NV)] = str(DI)+" - "+str(DI+AI)
        TDF["F"]["V"+str(NV)] = 0
        for x in range(int(math.ceil(DI))+1,(int(math.ceil(DI))+AI)+1):
            if x == RMin+1:
                TDF["F"]["V"+str(NV)] += LDT.count(RMin)
            TDF["F"]["V"+str(NV)] += LDT.count(x)
        TDF["FR"]["V"+str(NV)] = round((TDF["F"]["V"+str(NV)]/len(LDT))*100,3)
        if NV == 1:
            TDF["FAA"]["V"+str(NV)] = TDF["F"]["V"+str(NV)]
            TDF["FAD"]["V"+str(NV)] = len(LDT)
            TDF["FRA"]["V"+str(NV)] = TDF["FR"]["V"+str(NV)]
        else:
            TDF["FAA"]["V"+str(NV)] = TDF["FAA"]["V"+str(NV-1)]+TDF["F"]["V"+str(NV)]
            TDF["FAD"]["V"+str(NV)] = TDF["FAD"]["V"+str(NV-1)]-TDF["F"]["V"+str(NV-1)]
            TDF["FRA"]["V"+str(NV)] = round(TDF["FRA"]["V"+str(NV-1)]+TDF["FR"]["V"+str(NV)],3)
        TDF["MC"]["V"+str(NV)] = round((DI + (DI+AI))/2,2)
        DI = DI+AI
    #print(TDF)
    return TDF
    #print(LDT.count(-1))
    




def DictFormule(Datos: list):
    DictDatosR = dict()
    DictDatosR['Ndat'] = len(Datos)
    NumMenor = int(100)
    NumMayor = int(0)
    for ND in Datos:
        if int(ND) < NumMenor:
            NumMenor = ND
        elif int(ND) > NumMayor:
            NumMayor = ND
    DictDatosR['Rango'] = FirstFormule(NumMayor,NumMenor)
    Datos.sort()    
    DictDatosR['Vm'] = SecondFormule(DictDatosR['Ndat'])    
    DictDatosR['VC'] = ThirdFormule(DictDatosR['Rango'],DictDatosR['Vm'])
    #DictDatosR['VRR'] = int(FourthFormule(DictDatosR['VC'],DictDatosR['Vm'],DictDatosR['Rango']))
    #DictDatosR['VRR'] = FourthFormule(DictDatosR['VC'],DictDatosR['Vm'],DictDatosR['Rango'])
    V_RR = FourthFormule(DictDatosR['VC'],DictDatosR['Vm'],DictDatosR['Rango'])
    if V_RR > int(V_RR):
        DictDatosR['VRR'] = V_RR
    else:
        DictDatosR['VRR'] = int(V_RR)
        
    RMN = FivethFormule(NumMayor,NumMenor,DictDatosR['VRR'])
    #DictDatosR['Rmax'] = int(RMN[0])
    #DictDatosR['Rmin'] = int(RMN[1])
    if RMN[0] > 0:
        if RMN[0] > int(RMN[0]):
            DictDatosR['Rmax'] = RMN[0]
        else:
            DictDatosR['Rmax'] = int(RMN[0])
    else:
        if RMN[0] < int(RMN[0]):
            DictDatosR['Rmax'] = RMN[0]
        else:
            DictDatosR['Rmax'] = int(RMN[0])

    if RMN[1] > 0:
        if RMN[1] > int(RMN[1]):
            DictDatosR['Rmin'] = RMN[1]
        else:
            DictDatosR['Rmin'] = int(RMN[1])
    else:
        if RMN[1] < int(RMN[1]):
            DictDatosR['Rmin'] = RMN[1]
        else:
            DictDatosR['Rmin'] = int(RMN[1])
    DictDatosR['Tallo'] = SixthFormule(Datos)
    DictDatosR["TDF"] = SeventhFormule(DictDatosR['Rmax'],DictDatosR['Rmin'],DictDatosR['Vm'],DictDatosR['VC'],Datos)
    #print(DictDatosR['Tallo'])
    return DictDatosR





"""

antigua fórmula 6

def SixthFormule(Dt):
    Tallo = {}
    Tallo["F0"] = {"exist":"No","C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
    Tallo["F10"] = {"exist":"No","C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
    Tallo["F20"] = {"exist":"No","C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
    Tallo["F30"] = {"exist":"No","C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
    Tallo["F40"] = {"exist":"No","C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
    Tallo["F50"] = {"exist":"No","C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
    for Num in Dt:
        if int(Num) >= 0 and int(Num) < 10:
            #Tallo["F0"] = {"C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
            VarSt = str(Num)
            VarStC = "C"+VarSt[0:]
            #print(VarStC)
            Tallo["F0"]["exist"] = "Yes"
            Tallo["F0"][str(VarStC)] += 1
        elif Num >= 10 and Num < 20:
            #Tallo["F10"] = {"C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
            VarSt = str(Num)
            VarStC = "C"+VarSt[1:]
            Tallo["F10"]["exist"] = "Yes"
            Tallo["F10"][VarStC] += 1
        elif Num >= 20 and Num < 30:
            #Tallo["F20"] = {"C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
            VarSt = str(Num)
            VarStC = "C"+VarSt[1:]
            Tallo["F20"]["exist"] = "Yes"
            Tallo["F20"][VarStC] += 1
        elif Num >= 30 and Num < 40:
            #Tallo["F30"] = {"C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
            VarSt = str(Num)
            VarStC = "C"+VarSt[1:]
            Tallo["F30"]["exist"] = "Yes"
            Tallo["F30"][VarStC] += 1
        elif Num >= 40 and Num < 50:
            #Tallo["F40"] = {"C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
            VarSt = str(Num)
            VarStC = "C"+VarSt[1:]
            Tallo["F40"]["exist"] = "Yes"
            Tallo["F40"][VarStC] += 1
        elif Num >= 50 and Num < 60:
            #Tallo["F50"] = {"C0":0,"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0}
            VarSt = str(Num)
            VarStC = "C"+VarSt[1:]
            Tallo["F50"]["exist"] = "Yes"
            Tallo["F50"][VarStC] += 1
    """