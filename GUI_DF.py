from tkinter import *
from tkinter.ttk import Treeview
#import ControladorCalculos as CCal
import ControladorCualculosXForm as CCal
#from tkinter.ttk import *

#from sympy import rootof
root = Tk()


LblLnBS = Label(root, text=" ")
LblLnBS.grid(row=0,column=0)
Lbl = Label(root, text="Datos separados por ;")
Lbl.grid(row=1,column=0)
ent = Entry(root)
ent.grid(row=1,column=1)
LblLnB = Label(root, text=" ")
LblLnB.grid(row=3,column=0)
LblNDatos = Label(root, text="El número de datos es: ")
LblNDatos.grid(row=4,column=0)
LblNDatosS = Label(root, text=" ")
LblNDatosS.grid(row=4,column=1)
LblRango = Label(root, text="El rango (R) es : ")
LblRango.grid(row=5,column=0)
LblRangoS = Label(root, text=" ")
LblRangoS.grid(row=5,column=1)
LblNIntervalos = Label(root, text="El número de intervalos (m) es: ")
LblNIntervalos.grid(row=6,column=0)
LblNIntervalosS = Label(root, text=" ")
LblNIntervalosS.grid(row=6,column=1)
LblAmplitud = Label(root, text="La amplitud del intervalo (C) es: ")
LblAmplitud.grid(row=7,column=0)
LblAmplitudS = Label(root, text=" ")
LblAmplitudS.grid(row=7,column=1)
LblRR = Label(root, text="El rango real (RR) es: ")
LblRR.grid(row=8,column=0)
LblRRS = Label(root, text=" ")
LblRRS.grid(row=8,column=1)
LblVmaxVmin = Label(root, text="El rango máximo es: \nEl Rango mínimo es: ")
LblVmaxVmin.grid(row=9,column=0)
LblVmaxVminS = Label(root, text=" ")
LblVmaxVminS.grid(row=9,column=1)
LblLnBT = Label(root, text=" ")
LblLnBT.grid(row=10,column=0)

TblCTallo = Treeview(root,columns=11)
TblCTallo['columns'] = ["Tallo","0","1","2","3","4","5","6","7","8","9"]
TblCTallo['show'] = "headings"
TblCTallo.heading("Tallo",text="Tallo")
TblCTallo.heading("0",text="0")
TblCTallo.heading("1",text="1")
TblCTallo.heading("2",text="2")
TblCTallo.heading("3",text="3")
TblCTallo.heading("4",text="4")
TblCTallo.heading("5",text="5")
TblCTallo.heading("6",text="6")
TblCTallo.heading("7",text="7")
TblCTallo.heading("8",text="8")
TblCTallo.heading("9",text="9")
TblCTallo.column("Tallo",minwidth=0,width=40, stretch=NO)
TblCTallo.column("0",minwidth=0,width=20, stretch=NO)
TblCTallo.column("1",minwidth=0,width=20, stretch=NO)
TblCTallo.column("2",minwidth=0,width=20, stretch=NO)
TblCTallo.column("3",minwidth=0,width=20, stretch=NO)
TblCTallo.column("4",minwidth=0,width=20, stretch=NO)
TblCTallo.column("5",minwidth=0,width=20, stretch=NO)
TblCTallo.column("6",minwidth=0,width=20, stretch=NO)
TblCTallo.column("7",minwidth=0,width=20, stretch=NO)
TblCTallo.column("8",minwidth=0,width=20, stretch=NO)
TblCTallo.column("9",minwidth=0,width=20, stretch=NO)
#TblCTallo.place(x=35,y=200)
TblCTallo.place(x=320,y=10)

TblCDN = Treeview(root,columns=11)
TblCDN['columns'] = ["I.A.C","F","F.A.A","F.A.D","%'FR","%'F.R.A","MarcaC"]
TblCDN['show'] = "headings"
TblCDN.heading("I.A.C",text="I.A.C")
TblCDN.heading("F",text="F")
TblCDN.heading("F.A.A",text="F.A.A")
TblCDN.heading("F.A.D",text="F.A.D")
TblCDN.heading("%'FR",text="%'FR")
TblCDN.heading("%'F.R.A",text="%'F.R.A")
TblCDN.heading("MarcaC",text="Marca de\nClase")
TblCDN.column("I.A.C",minwidth=0,width=60, stretch=NO)
TblCDN.column("F",minwidth=0,width=60, stretch=NO)
TblCDN.column("F.A.A",minwidth=0,width=60, stretch=NO)
TblCDN.column("F.A.D",minwidth=0,width=60, stretch=NO)
TblCDN.column("%'FR",minwidth=0,width=60, stretch=NO)
TblCDN.column("%'F.R.A",minwidth=0,width=60, stretch=NO)
TblCDN.column("MarcaC",minwidth=0,width=70, stretch=NO)
#TblCTallo.place(x=35,y=200)
TblCDN.place(x=130,y=260)

def LlenarTablaTallo(DicDat):
    NFil = 0
    NCol = 0
    FilDat = TblCTallo.get_children()
    #print(x)
    if len(FilDat) > 0:
        for item in FilDat:
            TblCTallo.delete(item)
    for Tal,Dat in DicDat.items():
        LDat = []
        LDat.append(Tal[1:])
        #print(Dat)
        if Dat["exist"] == "Yes":
            for key,Val in Dat.items():
                if key != "exist":
                    LDat.append(Val) 
            TblCTallo.insert('',NFil,NCol,values=LDat)
            NFil += 1
            NCol += 1

def LlenarTablaDN(DicDat):
    NFil = 0
    NCol = 0
    FilDat = TblCDN.get_children()
    #print(x)
    if len(FilDat) > 0:
        for item in FilDat:
            TblCDN.delete(item)
    for Tal,Dat in DicDat["Valu"].items():
        LDat = []
        #LDat.append(Tal[1:])
        #print(Dat)
        for key,Val in DicDat.items():
            if key != "Valu":
                LDat.append(Val[Tal]) 
        TblCDN.insert('',NFil,NCol,values=LDat)
        NFil += 1
        NCol += 1


def PDT():
    #LblRango['text'] = f"El rango es: {ent.get()}"
    VarR = str(ent.get())
    ListVR = VarR.split(';')
    ListINT = [int(ND) for ND in ListVR]
    #DicDT = CCal.FirstFormule(ListINT)
    DicDT = CCal.DictFormule(ListINT)
    LblNDatosS['text'] = f"{DicDT['Ndat']}"
    LblRangoS['text'] = f"{DicDT['Rango']}"
    LblNIntervalosS['text'] = f"{DicDT['Vm']}"
    LblAmplitudS['text'] = f"{DicDT['VC']}"
    LblRRS['text'] = f"{DicDT['VRR']}"
    LblVmaxVminS['text'] = f"{DicDT['Rmax']}\n{DicDT['Rmin']}"
    #print(ent.get())
    LlenarTablaTallo(DicDT['Tallo'])
    LlenarTablaDN(DicDT['TDF'])     
        

    

BtnCalc = Button(root, text="Hacer cálculos", command=PDT)
#BtnCalc.grid(row=11,column=0)
BtnCalc.place(x=15,y=270)



"""
boton1 = Button(root,
                text="No puedes presionar el botón rojo ;)",
                bg="red",
                padx=100,
                pady=25,
                state=DISABLED).grid(row=1, column=2)
"""

root.geometry("600x500")
root.title("Análisis de distribución de la normal (13 fórmulas)")
root.mainloop()