
from encodings import utf_8
from fileinput import close
from operator import contains
from tkinter import *
from tkinter import font
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

from scipy import signal
import scipy
from control.matlab import *
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import *


DataValue = ["1"]
TFs = [""]
pantalla = "1"
Parameters = [""]

class APP:
    def __init__(self,master = None):
        super().__init__()
        self.master = master
        self.master.geometry("920x720")
        self.master.configure(bg = "#253132")
        
        MainWindow(self.master)

class MainWindow:
    def __init__(self,master):
        super().__init__()
        self.master = master   
        self.bg1()
        self.mainBtn()

    def bg1(self):
        self.master.geometry("920x720")
        self.master.configure(bg = "#253132")
        self.MainW = Canvas(self.master,bg = "#253132", height = 720, width = 920, bd = 0, highlightthickness = 0, relief = "ridge")
        self.MainW.place(x = 0, y = 0)
        # Define Background
        self.background_img = ImageTk.PhotoImage(file = f"background.png")
        background = self.MainW.create_image(475.0, 204.0, image=self.background_img)
    
    def mainBtn(self):       
        # image for buttons
        self.New = ImageTk.PhotoImage(file = f"New.png")
        self.Load = ImageTk.PhotoImage(file = f"Load.png")
        self.ImgHelp = ImageTk.PhotoImage(file = f"Help.png")
        
        # create button
        self.NewDesign = Button( image = self.New, borderwidth=0, highlightthickness=0, command=self.btnNew, relief = "flat",bg = "#303F40")
        self.LoadDesign = Button( image = self.Load, borderwidth=0, highlightthickness=0, command=self.btnLoad, relief = "flat",bg = "#303F40")
        self.Help = Button( image = self.ImgHelp, borderwidth=0, highlightthickness=0, command=self.btnHelp, relief = "flat",bg = "#303F40")
        # set place
        self.NewDesign.place(x = 335, y = 405, width= 280, height=70)
        self.LoadDesign.place(x = 335, y = 505, width= 280, height=70)
        self.Help.place(x = 335, y = 605, width= 280, height=70)
        

    def btnNew(self):
        self.MainW.destroy()
        MainBackgraound(self.master,"1")
        

    def btnLoad(self):
        global DataValue
        namepath = filedialog.askopenfile()
        if namepath.name.__contains__(".txt"):
            f = open(namepath.name,'r',encoding = 'utf-8') 
            DataValue = f.readline().split()
            print(f.readlines())
            f.close()
            MainBackgraound(self.master,DataValue[0])
        else:
            messagebox.showwarning(title = "Warning", message="Escoger un archivo correcto")   
    def btnHelp(self):
        pass     

class MainBackgraound:
    def __init__(self,master,window):
        super().__init__()
        self.master = master
        global pantalla
        global DataValue
        self.Ventanas(window)
        #ConverterWindow(self.master,self.MainBG)
    def Ventanas(self,value):
        bg2 = self.bg2()
        self.BgButtons()
        if value == "1":
            ConverterWindow(self.master,bg2)
            self.ConvDes['state'] = DISABLED
            self.ElemSpec['state'] = NORMAL
            self.CtrlDes['state'] = NORMAL
            self.CtrlImp['state'] = NORMAL
            self.Summary['state'] = NORMAL
        if value == "2":
            ElementWindow(self.master,bg2)
            self.ElemSpec['state'] = DISABLED
            self.ConvDes['state'] = NORMAL
            self.CtrlDes['state'] = NORMAL
            self.CtrlImp['state'] = NORMAL
            self.Summary['state'] = NORMAL
        if value == "3":
            DesignWindow(self.master,bg2)
            self.CtrlDes['state'] = DISABLED
            self.ConvDes['state'] = NORMAL
            self.ElemSpec['state'] = NORMAL
            self.CtrlImp['state'] = NORMAL
            self.Summary['state'] = NORMAL  
        if value == "4":
            ImplementWindow(self.master,bg2)
            self.CtrlImp['state'] = DISABLED
            self.ElemSpec['state'] = NORMAL
            self.ConvDes['state'] = NORMAL
            self.CtrlDes['state'] = NORMAL
            self.Summary['state'] = NORMAL
        if value == "5":
            SummaryWindow(self.master,bg2)
            self.Summary['state'] = DISABLED
            self.CtrlImp['state'] = NORMAL
            self.ElemSpec['state'] = NORMAL
            self.ConvDes['state'] = NORMAL
            self.CtrlDes['state'] = NORMAL
    
    def bg2(self):
        self.master.geometry("1280x720")
        self.master.configure(bg = "#253132")
        self.MainBG = Canvas(self.master,bg = "#253132", height = 720, width = 1280, bd = 0, highlightthickness = 0, relief = "ridge")
        self.MainBG.place(x = 0, y = 0)
        return self.MainBG
      
    def btn_click(self,value):
        self.value = value
        print(self.value)
        self.Ventanas(self.value)
    #actiones del menu principal
    def btn_action(self,value): 
        global DataValue
        if value == "1":
            #menu button New Design
            Action = messagebox.askyesno(title = "", message= "Do you want to save the previous design?")
            if Action == True:
                self.saveArchive()
            print(DataValue)
            DataValue = ["1"]    
            self.Ventanas("1")
        if value == "2":
            #menu button Save
            self.saveArchive()
        if value == "3":
            #menu button open
            Action = messagebox.askyesno(title = "", message= "Do you want to save the previous design?")
            if Action == True:
                self.saveArchive()
                pantalla = DataValue[0]
                self.Ventanas(pantalla)
            else:
                pantalla = self.openArchive()
                self.Ventanas(pantalla)
        if value == "4":
            #menu button Help
            pass
    def openArchive(self):
        global DataValue
        namepath = filedialog.askopenfile()
        try :
            print(namepath.name)
            if namepath.name.__contains__(".txt"):
                f = open(namepath.name,'r',encoding = 'utf-8') 
                DataValue = f.readline().split()
                print(f.readlines())
                f.close()
                return DataValue[0]
            else:
                messagebox.showwarning(title="file",message="select a correct file")
                return "1"
        except:
            return "1"
    def saveArchive(self):
        global DataValue
        aux = ""
        for i in DataValue:
            aux += i + " " 
        fname = filedialog.asksaveasfilename()
        try:
            if fname.__contains__(".txt"):
                pass
            else:
                fname = fname + ".txt"
            f = open(fname,'w',encoding = 'utf-8') 
            f.write(aux)
            #print(f.readline())
            f.close()
        except:
            pass

    def BgButtons(self):         
        # image button
        self.ConvDesImg = ImageTk.PhotoImage(file = f"ConvDes.png")
        self.ElemSpecImg = ImageTk.PhotoImage(file = f"ElemSpec.png")
        self.CtrlDesImg = ImageTk.PhotoImage(file = f"CtrlDes.png")
        self.CtrlImpImg = ImageTk.PhotoImage(file = f"CtrlImp.png")
        self.SummaryImg = ImageTk.PhotoImage(file = f"Summary.png")
        
        self.ImgNewD = ImageTk.PhotoImage(file = f"NewD.png")
        self.ImgSave = ImageTk.PhotoImage(file = f"Save.png")
        self.ImgOpen = ImageTk.PhotoImage(file = f"Open.png")
        self.ImgHelp2 = ImageTk.PhotoImage(file = f"Help2.png")
        # create button
        self.ConvDes = Button( image = self.ConvDesImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_click("1"), relief = "flat",bg = "#3A4C4E")
        self.ElemSpec = Button( image = self.ElemSpecImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_click("2"), relief = "flat",bg = "#3A4C4E")
        self.CtrlDes = Button( image = self.CtrlDesImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_click("3"), relief = "flat",bg = "#3A4C4E")
        self.CtrlImp = Button( image = self.CtrlImpImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_click("4"), relief = "flat",bg = "#3A4C4E")
        self.Summary = Button( image = self.SummaryImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_click("5"), relief = "flat",bg = "#3A4C4E")
        
        self.NweD = Button( image = self.ImgNewD, borderwidth=0, highlightthickness=0, command=lambda:self.btn_action("1"), relief = "flat",bg = "#303F40")
        self.Save = Button( image = self.ImgSave, borderwidth=0, highlightthickness=0, command=lambda:self.btn_action("2"), relief = "flat",bg = "#303F40")
        self.Open = Button( image = self.ImgOpen, borderwidth=0, highlightthickness=0, command=lambda:self.btn_action("3"), relief = "flat",bg = "#303F40")
        self.Help2 = Button( image = self.ImgHelp2, borderwidth=0, highlightthickness=0, command=lambda:self.btn_action("4"), relief = "flat",bg = "#303F40")

        #set button place
        self.ConvDes.place(x = 6, y = 90, width = 70, height = 61)  
        self.ElemSpec.place(x = 6, y = 171, width = 70, height = 61)
        self.CtrlDes.place(x = 6, y = 252, width = 70, height = 61)
        self.CtrlImp.place(x = 6, y = 333, width = 70, height = 61)
        self.Summary.place(x = 6, y = 414, width = 70, height = 61)

        self.NweD.place(x = 94, y = 0, width = 106, height = 40)
        self.Save.place(x = 293, y = 0, width = 77, height = 40)
        self.Open.place(x = 208, y = 0, width = 77, height = 40)
        self.Help2.place(x = 378, y = 0, width = 77, height = 40)
     
    
class ConverterWindow:
    def __init__(self,master,canva):
        super().__init__()
        self.master = master
        self.canva = canva
        self.typesC = StringVar()
        
        global DataValue
        global pantalla
        pantalla = "1"
        
        self.bg2_img = ImageTk.PhotoImage(file = f"background2.png")
        background = self.canva.create_image(640.0, 366.0, image=self.bg2_img)
        
        self.ConverterBtn()
        self.entryBox1()
        self.typesC.trace('w',self.infobox)
        self.previousVal()
    
    def ConverterBtn(self):       
        #image Button
        self.ApplyImg = ImageTk.PhotoImage(file = f"Apply.png")
        self.DiscardImg = ImageTk.PhotoImage(file = f"Discard.png")
        # create button
        self.Apply = Button( image = self.ApplyImg, borderwidth = 0, highlightthickness = 0, command = self.btn_Apply, relief = "flat",bg = "#303F40")
        self.Discard = Button( image = self.DiscardImg, borderwidth = 0, highlightthickness = 0, command = self.btn_Discard, relief = "flat",bg = "#303F40")
        #set button place
        self.Apply.place(x = 96, y = 360, width = 109, height = 26)
        self.Discard.place(x = 229, y = 360, width = 109, height = 26)

    def btn_Apply(self):
        global TFs
        DataValue[0] = pantalla
        aux = [self.Vin.get(), self.Vo.get(), self.Po.get(), self.Vripple.get(), self.Cripple.get(), self.Topology.get(), self.Fs.get()]
        if aux.__contains__(""):
            messagebox.showwarning(title = "Warning", message="Fill all parameters values")
        else:
            DataValue[1:] = aux
            if str(self.Topology.get()) == "Buck":
                val = self.buckDesign(float(aux[0]),float(aux[1]),float(aux[2]),float(aux[3]),float(aux[4]),float(aux[6]))
                self.DisplayConverter(val,"1")
            if str(self.Topology.get()) == "Boost":
                val = self.boostDesign(float(aux[0]),float(aux[1]),float(aux[2]),float(aux[3]),float(aux[4]),float(aux[6]))
                self.DisplayConverter(val,"2")
            TFs = val
            print(type(DataValue),DataValue,"\n",val)
    def btn_Discard(self):
        self.Vin.delete(0,END) 
        self.Vo.delete(0,END)
        self.Po.delete(0,END)
        self.Vripple.delete(0,END)
        self.Cripple.delete(0,END)
        self.Fs.delete(0,END)
        DataValue[1:] = [self.Vin.get(), self.Vo.get(), self.Po.get(), self.Vripple.get(), self.Cripple.get(), self.Topology.get(),  self.Fs.get()]
        print(type(DataValue),DataValue)   
        if self.newCanva:
            self.newCanva.destroy()
    def DisplayConverter(self,val,typeC):
        self.newCanva = Canvas(self.master, bg = "#3A4C4E",height = 520, width = 829, bd = 0, highlightthickness = 0, relief = "ridge")
        self.newCanva.place(x = "402", y = "135")
        
        #internal labels
        self.R = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = str(val[2]),highlightthickness = 0, anchor= "e")
        self.L = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = str(val[0]),highlightthickness = 0, anchor= "e")
        self.C = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = str(val[1]),highlightthickness = 0, anchor= "e")
        self.D = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = str(val[3]),highlightthickness = 0, anchor= "e")
        
        self.R.place(x = 690, y = 60, width = 105, height = 15)
        self.L.place(x = 690, y = 95, width = 105, height = 15)
        self.C.place(x = 690, y = 130, width = 105, height = 15)
        self.D.place(x = 690, y = 165, width = 105, height = 15)

        # creacion textos
        self.newCanva.create_text( 630.0, 66, text = "R("+ chr(937)+")          =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.newCanva.create_text( 630.0, 101, text = "L(H)          =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.newCanva.create_text( 630.0, 136, text = "C(F)          =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.newCanva.create_text( 630.0, 171, text = "Duty          =", fill = "#ffffff", font = ("Calibri", int(12.0)))

        if typeC == "1":           
            self.buckimg = ImageTk.PhotoImage(file = f"buck.png")
            self.newCanva.create_image(300.0, 200.0, image=self.buckimg) 

            self.newCanva.create_text(650.0, 250, text = str(val[8]), fill = "#ffffff", font = ("Calibri", int(12.0)))
        if typeC == "2":
            self.buckimg = ImageTk.PhotoImage(file = f"buck.png")
            self.newCanva.create_image(300.0, 200.0, image=self.buckimg) 

            self.newCanva.create_text(650.0, 250, text = str(val[8]), fill = "#ffffff", font = ("Calibri", int(12.0)))

    def buckDesign(self,Vi,Vo,Po,deltaVo,deltaIl,Fsw):
    #Funcion BUCK DESIGN
    #Entradas: Vi, Vo, Po, deltaVo, deltaIl, Fsw
    #Salidas: L, C, R, D, Iout, Lcrit, iL_avg, TF, TFDisplay
        D=Vo/Vi
        L=Vo*(1-D)/(deltaIl*Fsw)
        C=deltaIl/(8*Fsw*deltaVo)
        R=Vo*Vo/Po
        Iout=Po/Vo
        Lcrit=(1-D)*R/(2*Fsw)
        iL_avg=Vo/R
        #print(L, C, R, D, Iout, Lcrit, iL_avg)
        Gp1=tf([R*Vi],[C*L*R, L, R])
        Gp=Gp1
        [Gmu,Pmu,G_0u,Stabilityu]=self.margins(Gp1)
        return(L, C, R, D, Iout, Lcrit, iL_avg, Gp1, Gp,Gmu,Pmu,G_0u,Stabilityu)
    def boostDesign(self, Vi,Vo,Po,deltaVo,deltaIl,Fsw):
        #Funcion BOOST DESIGN
        #Entradas: Vi, Vo, Po, deltaVo, deltaIl, Fsw
        #Salidas: L, C, R, D, Iout, Lcrit, iL_avg, TF, TFDisplay
        D=1-(Vi/Vo)
        L=Vi*D/(deltaIl*Fsw)
        R=Vo*Vo/Po
        C=(D*Vo)/(R*Fsw*deltaVo)
        Iout=Po/Vo
        Lcrit=D*(1-D)*(1-D)*R/(2*Fsw)
        iL_avg=Vi/((1-D)*(1-D)*R)
        #print(L, C, R, D, Iout, Lcrit, iL_avg)
        Gp1=tf([(L*R*iL_avg), (R*Vo*(1-D))],[C*L*R, L, (R*D*D +R -2*R*D)])
        Gp=tf([(-L*R*iL_avg), (R*Vo*(1-D))],[C*L*R, L, (R*D*D +R -2*R*D)])
        [Gmu,Pmu,G_0u,Stabilityu]=self.margins(Gp1)
        return(L, C, R, D, Iout, Lcrit, iL_avg, Gp1, Gp,Gmu,Pmu,G_0u,Stabilityu)
    def margins(self,Gp1):
        [gm,Pm,w1,Wcp]=margin(Gp1)
        iniTgain=20*np.log10(np.real(Gp1(0)))
        print(iniTgain)
        if (gm>0 and gm<6) or (Pm>0 and Pm<10):
            st='Marginally'
        elif (gm>6) and (Pm>10):
            st='Stable'
        else:
            st='Unstable'
        return(gm,Pm,iniTgain,st)

    def entryBox1(self):
        # Labels
        self.canva.create_text(160.0, 155.5, text = "Input Voltage    =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(160.0, 182.5, text = "Ouput Voltage  =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(160.0, 209.5, text = "Output Power   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(160.0, 236.5, text = "Voltage ripple   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(160.0, 263.5, text = "Current ripple   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(160.0, 289.5, text = "Frecuency        =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(160.0, 317.5, text = "Topology           =", fill = "#ffffff", font = ("Calibri", int(12.0)))

        # Entries
        self.Vin = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.Vo = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.Po = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.Vripple = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.Cripple = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.Fs = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.Topology = Combobox(background="#d9d9d9", values = ["Buck", "Boost", "Buck/Boost"],textvariable = self.typesC)
        
        # Place
        self.Vin.place(x = 222, y = 150, width = 108, height = 13)
        self.Vo.place(x = 222, y = 177, width = 108, height = 13)
        self.Po.place(x = 222, y = 204, width = 108, height = 13)
        self.Vripple.place(x = 222, y = 231, width = 108, height = 13)
        self.Cripple.place(x = 222, y = 258, width = 108, height = 13)
        self.Fs.place(x = 222, y = 285, width = 108, height = 13)
        self.Topology.place(x = 222, y = 310, width = 108, height = 18)
        
    def previousVal(self,*args):
        global DataValue
        print(DataValue)
        self.Vin.delete(0,END) 
        self.Vo.delete(0,END)
        self.Po.delete(0,END)
        self.Vripple.delete(0,END)
        self.Cripple.delete(0,END)
        self.Fs.delete(0,END)
        if len(DataValue) < 2:
            pass
        else:
            self.Vin.insert(0,str(DataValue[1]))
            self.Vo.insert(0,str(DataValue[2]))
            self.Po.insert(0,str(DataValue[3]))
            self.Vripple.insert(0,str(DataValue[4]))
            self.Cripple.insert(0,str(DataValue[5]))
            self.typesC.set(str(DataValue[6]))
            self.Fs.insert(0,str(DataValue[7]))
            
    
    def infobox(self,*args):        
        value = str(self.typesC.get())
        if value == "Buck": 
            txt = "The buck converter..."
        if value == "Boost":           
            txt = "The boost converter..."
        if value == "Buck/Boost":   
            txt = "The buck/boost converter..."
        if value == "":
            txt = "select a topology"
        pass
        message = Label(text = txt, font = ("Calibri", int(12.0)), fg = "#ffffff", bg= "#3A4C4E", justify= 'left')
        message.place(x = 97.0, y = 410, width = 242, height = 100) 
class DesignWindow:
    def __init__(self,master,canva):
        super().__init__()
        self.master = master
        self.canva = canva
        self.typeController = StringVar()
        global DataValue
        global pantalla
        pantalla = "3"
        
        self.bg2_img = ImageTk.PhotoImage(file = f"background3.png")
        background = self.canva.create_image(640.0, 366.0, image=self.bg2_img)
       
        self.DesignBtn()
        self.entryBox2()
        self.previousVal()
    def entryBox2(self):
        #labels
        self.canva.create_text(203.0, 165.5, text = "Pm                          =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 182.5, text = "Gm                          =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 203.5, text = "G(0)                        =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 222.5, text = "Stable?                   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        
        self.canva.create_text(203.0, 296.5, text = "Pm                           =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 315.5, text = "Gm                           =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 333.5, text = "Controller structure =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        
        self.canva.create_text(203.0, 453.5, text = "Pm                          =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 472.5, text = "Gm                          =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 491.5, text = "G(0)                        =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 510.5, text = "Stable?                   =", fill = "#ffffff", font = ("Calibri", int(12.0)))

        #Enable entries
        self.PmE = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.GmE = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.controller = Combobox(background="#d9d9d9", values = ["FOPID"],textvariable=self.typeController)
        
        #place enables
        self.PmE.place(x = 273, y = 292, width = 102, height = 13)
        self.GmE.place(x = 273, y = 311, width = 102, height = 13)
        self.controller.place(x = 273, y = 330, width = 102, height = 18)

        #Disable entriies
        self.PmD1 = Label( fg="#ffffff",bd = 0, bg = "#303F40", text = self.plantValue[0],highlightthickness = 0, anchor= "e")
        self.GmD1 = Label( fg="#ffffff",bd = 0, bg = "#303F40", text = self.plantValue[1],highlightthickness = 0, anchor= "e")
        self.G01 = Label( fg="#ffffff",bd = 0, bg = "#303F40", text = self.plantValue[2],highlightthickness = 0, anchor= "e")
        self.Stable1 = Label( fg="#ffffff", bd = 0, bg = "#303F40", text = self.plantValue[3],highlightthickness = 0, anchor = "e")

        self.PmD2 = Label( fg="#ffffff", bd = 0, bg = "#303F40", text = self.fraccValue[0],highlightthickness = 0, anchor= "e")
        self.GmD2 = Label( fg="#ffffff", bd = 0, bg = "#303F40", text = self.fraccValue[1],highlightthickness = 0, anchor= "e")
        self.G02 = Label( fg="#ffffff", bd = 0, bg = "#303F40", text = self.fraccValue[2],highlightthickness = 0, anchor= "e")
        self.Stable2 = Label( fg="#ffffff", bd = 0, bg = "#303F40", text = self.fraccValue[3],highlightthickness = 0, anchor= "e")

        #place disables
        self.PmD1.place(x = 273, y = 160, width = 102, height = 13)
        self.GmD1.place(x = 273, y = 179, width = 102, height = 13)
        self.G01.place(x = 273, y = 198, width = 102, height = 13)
        self.Stable1.place(x = 273, y = 217, width = 102, height = 13)

        self.PmD2.place(x = 273, y = 448, width = 102, height = 13)
        self.GmD2.place(x = 273, y = 467, width = 102, height = 13)
        self.G02.place(x = 273, y = 486, width = 102, height = 13)
        self.Stable2.place(x = 273, y = 505, width = 102, height = 13)
    
    def DesignBtn(self):       
        #image Button
        self.ApplyImg = ImageTk.PhotoImage(file = f"Apply.png")
        self.DiscardImg = ImageTk.PhotoImage(file = f"Discard.png")
        # create button
        self.Apply = Button( image = self.ApplyImg, borderwidth = 0, highlightthickness = 0, command = self.btn_Apply, relief = "flat",bg = "#303F40")
        self.Discard = Button( image = self.DiscardImg, borderwidth = 0, highlightthickness = 0, command = self.btn_Discard, relief = "flat",bg = "#303F40")
        #set button place
        self.Apply.place(x = 139, y = 365, width = 109, height = 26)
        self.Discard.place(x = 264, y = 365, width = 109, height = 26)

    def btn_Apply(self):
        global DataValue
        global TFs
        global Parameters
        DataValue[0] = pantalla
        aux = [self.PmE.get(), self.GmE.get(), self.controller.get()]
        if aux.__contains__(""):
            messagebox.showwarning(title = "Warning", message="Fill all entry values")
        else:
            DataValue[8:] = aux
            print(type(DataValue),DataValue)
            print(aux,TFs)
            if str(self.controller.get()) == "FOPID":
                val = self.fopidKhazali(TFs[8],float(aux[0]))
                self.DisplayGraphs()
        Parameters = val
        print(type(DataValue),DataValue,val)

    def btn_Discard(self):
        self.PmE.delete(0,END) 
        self.GmE.delete(0,END)
        self.controller.delete(0,END)
        aux = [self.PmE.get(), self.GmE.get(), self.controller.get()]
        DataValue[8:] = aux
        print(type(DataValue),DataValue) 
        if self.newCanva:
            self.newCanva.destroy()


    def DisplayGraphs(self):
        self.newCanva = Canvas(self.master, bg = "#3A4C4E",height = 520, width = 829, bd = 0, highlightthickness = 0, relief = "ridge")
        self.newCanva.place(x = "402", y = "135")

    def previousVal(self,*args):
        global DataValue
        global TFs
        global Parameters
        print(DataValue)
        self.PmE.delete(0,END)
        self.GmE.delete(0,END)
        if  len(DataValue) < 11:
            pass
        else:          
            self.PmE.insert(0,str(DataValue[8]))
            self.GmE.insert(0,str(DataValue[9]))
            self.controller.insert(0,str(DataValue[10]))
            
        if len(TFs) > 1:
            self.plantValue = [str(TFs[9]),str(TFs[10]),str(TFs[11]),str(TFs[12])]
        else:
            self.plantValue = ["Value","Value","Value","Value"]
        if len(Parameters) > 1:
            self.fraccValue = [str(Parameters[19]),str(Parameters[20]),str(Parameters[21]),str(Parameters[22])]
        else:
            self.fraccValue = ["Value","Value","Value","Value"]
    
    def fopidKhazali(self,Gp1,Pmd):
        #Funcion fopidKhazali
        #Entradas: TF, margen fase deseado 'Pmd'
        #Salidas: -
        plt.style.use('seaborn-whitegrid')
        sys1 = Gp1
        print(Gp1)
        [gm,Pm,w1,Wcp]=margin(Gp1)
        Pp=-180+Pm
        ##-- Caracteristicas deseadas
        Wcf=Wcp
        print(Wcf)
        alfa= (Pmd -180- Pp)/90
        Pc=(Pmd -180- Pp)*pi/180
        flag=0
        if alfa>1:
            alfa=0.99
            Pc=0.5*pi
        if alfa<0:
            flag=1
            alfa=-alfa
        if alfa<-1:
            alfa=-0.99
            flag=1
            alfa=-alfa
        mag, phase, deg,  = bode([Gp1], Hz=True)
        ## ----- Aproximaciones -----
            
        a0 = alfa**alfa + 3 * alfa + 2
        a2 = alfa**alfa - 3 * alfa + 2
        a1 = 6 * alfa * math.tan((2 - alfa) * pi / 4)

        N_alfa = [a0, (a1 * Wcf), (a2 * Wcf**2)]
        print(alfa)
        D_alfa = [a2, (a1 * Wcf), (a0 * Wcf**2)]
        
        if flag==0:
            s_alfa = tf(N_alfa, D_alfa)
        elif flag==1:
            s_alfa = tf(D_alfa, N_alfa)
        print("s_alfa",s_alfa)
        ## ----- Calculo de parametros
        a=1
        b=1
        fval=0
        for i in range (100):
            #print('a=',a)
            #print('npy')
            #print(fval)
            Ti=(math.tan(Pc/2)+math.tan((2+alfa)/(pi/4)))/(math.tan(Pc/2)-math.tan((2+alfa)/(pi/4)))
            Ti=Ti*a
            Kc=((b)*((a0-a2)**2 +(a1)**2))/((a0-a2)**2 *(1-Ti)**2 + (a1**2)*(1+Ti)**2)
            # Estructura
            Gc = Kc * (((Ti * s_alfa) + 1)**2)/(s_alfa)
            #print(Gc)
            [gm,Pm,w1,Wcp]=margin(Gp1*Gc)
            #print(Pm)
            fval=np.real(feedback(Gp1*Gc,1)(0))
            if Pm<0.98*Pmd:
                a=a+1*((Pmd-Pm)/Pmd)
            if Pm>1.02*Pmd:
                a=a-5*((Pmd-Pm)/Pmd) 
                b=b+0.5*((1-fval)/1)     
            if fval<0.98:
                b=b+0.5*((1-fval)/1)
            if fval>1.02:
                b=b-0.5*((1-fval)/1)   

        Gc=minreal(Gc,0.1)
        print(Gc)
        #Gc=tf([3.095, 5.928e04, 3.418e08, 5.549e11, 2.712e14],[1, 3.921e04, 3.802e08, 1.114e12, 8.071e14]) 
        num,den = tfdata(Gc)
        NumArray = np.array(num[0])
        DenArray = np.array(den[0])
        #print(NumArray[0])
        #num=cell2mat(num)
        #den=cell2mat(den)
        [r,p,k]= scipy.signal.residue(NumArray[0], DenArray[0])
        #print(num[0],num)
        #print(r,p,k)
        G1=r[0]/-p[0]
        G2=r[1]/-p[1]
        G3=r[2]/-p[2]
        G4=r[3]/-p[3]

        RC1=1/-p[0]
        RC2=1/-p[1]
        RC3=1/-p[2]
        RC4=1/-p[3]

        Ri1,Ri2,Ri3,Ri4,Ri5,Rf1,Rf2,Rf3,Rf4,Rf5,C1,C2,C3,C4,R1,R2,R3,R4=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

        print(G1,G2,G3,G4,k,RC1,RC2,RC3,RC4)
        try:
            if(G1<100 and G1>0.1):
                Ri3=10000
            if(G1<0.1 and G1>0.001):
                Ri3=100000
            if(G1<0.001 and G1>0.0001):
                Ri3=500000
            Rf3=G1*Ri3
            print(Ri3,Rf3)

            G2=-G2
            if(G2<100 and G2>0.1):
                Ri1=10000
            if(G2<0.1 and G2>0.010):
                Ri1=100000
            if(G2<0.001 and G2>0.0001):
                Ri1=500000
            Rf1=G2*Ri1
            print(Ri1,Rf1)

            if(G3<100 and G3>0.1):
                Ri4=10000
            if(G3<0.1 and G3>0.001):
                Ri4=100000
            if(G3<0.001 and G3>0.0001):
                Ri4=500000
            Rf4=G3*Ri4
            print(Ri4,Rf4)

            G4=-G4
            if(G4<100 and G4>0.1):
                Ri2=10000
            if(G4<0.1 and G4>0.001):
                Ri2=100000
            if(G4<0.001 and G4>0.0001):
                Ri2=500000
            Rf2=G4*Ri2
            print(Ri2,Rf2)

            if(k<100 and k>0.1):
                Ri5=10000
            if(k<0.1 and k>0.001):
                Ri5=100000
            if(k<0.001 and k>0.0001):
                Ri5=500000
            Rf5=k[0]*Ri5
            print(Ri5,Rf5)


            if(RC1<1 and RC1>0.001):
                C1=0.000001
            if(RC1<0.001 and RC1>0.00001):
                C1=0.00000001
            if(RC1<0.00001 and RC1>0.0000001):
                C1=0.000000001
            R1=RC1/C1
            print(R1,C1)

            if(RC2<1 and RC2>0.001):
                C2=0.000001
            if(RC2<0.001 and RC2>0.00001):
                C2=0.00000001
            if(RC2<0.00001 and RC2>0.0000001):
                C2=0.000000001
            R2=RC2/C2
            print(R2,C2)

            if(RC3<1 and RC3>0.001):
                C3=0.000001
            if(RC3<0.001 and RC3>0.00001):
                C3=0.00000001
            if(RC3<0.00001 and RC3>0.0000001):
                C3=0.000000001
            R3=RC3/C3
            print(R3,C3)

            if(RC4<1 and RC4>0.001):
                C4=0.000001
            if(RC4<0.001 and RC4>0.00001):
                C4=0.00000001
            if(RC4<0.00001 and RC4>0.0000001):
                C4=0.000000001
            R4=RC4/C4
            print(R4,C4)
        except:
            print("No implemenmtable")

        mag, phase, deg,  = bode([Gp1,Gp1*Gc], Hz=True)
        plt.savefig("bode.png",dpi=300)
        #files.download("bode.png") ################################Solo para Colab
        #bode([Gp1,Gp1*Gc])
        #step(feedback(Gp1,1))

        yout, T = step(feedback(Gp1,1))
        print(T[len(T)-1])
        yout2, T2 = step(feedback(Gp1*Gc,1),T=0.001)

        # plot
        fig, ax = plt.subplots()


        ax.plot(T, yout, linewidth=2.0)

        ax.plot(T2, yout2, linewidth=2.0)
        #ax.plot(T2, yout2, linewidth=2.0)

        ax.set(ylim=(0, 2), yticks=np.arange(0, 2,0.2),
                xlim=(0, T[len(T)-1]), xticks=np.arange(0, T[len(T)-1],T[len(T)-1]*0.1))
        plt.xticks(rotation=90)
        plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
        plt.tight_layout()
        plt.savefig("step.png",dpi=100)
        #files.download("step.png")  ################################Solo para Colab
        plt.show()
        [Gm,Pm,G_0,Stability]=self.margins(Gp1*Gc)
        return(Gc,Ri1,Ri2,Ri3,Ri4,Ri5,Rf1,Rf2,Rf3,Rf4,Rf5,C1,C2,C3,C4,R1,R2,R3,R4,Gm,Pm,G_0,Stability)
    
    def margins(self,Gp1):
        [gm,Pm,w1,Wcp]=margin(Gp1)
        iniTgain=20*np.log10(np.real(Gp1(0)))
        print(iniTgain)
        if (gm>0 and gm<6) or (Pm>0 and Pm<10):
            st='Marginally'
        elif (gm>6) and (Pm>10):
            st='Stable'
        else:
            st='Unstable'
        return(gm,Pm,iniTgain,st)
       
class ElementWindow:
    def __init__(self,master,canva):
        super().__init__()
        self.master = master
        self.canva = canva
        self.bg2_img = ImageTk.PhotoImage(file = f"background4.png")
        background = self.canva.create_image(640.0, 366.0, image=self.bg2_img)
        self.DesignBtn()
    
    def DesignBtn(self):
        #image Button
        self.ElemIMG = ImageTk.PhotoImage(file = f"summ.png")
        # create button
        self.ElemBtn = Button( image = self.ElemIMG, borderwidth = 0, highlightthickness = 0, command = self.btn_Action, relief = "flat",bg = "#303F40")
        #set button place
        self.ElemBtn.place(x = 130, y = 166, width = 109, height = 26)
    def btn_Action(self):
        pass
class ImplementWindow:
    def __init__(self,master=None,canva=None):
        super().__init__()
        self.master = master
        self.canva = canva
        self.bg2_img = ImageTk.PhotoImage(file = f"background1.png")
        background = self.canva.create_image(640.0, 366.0, image=self.bg2_img)
        self.DesignBtn()
        self.GralEntry()
    def GralEntry(self):
        #Label of comboBox
        self.canva.create_text(181.0, 154.5, text = "Structure               =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(181.0, 303.5, text = "Target                  =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        
        #ComboBox
        self.structure = Combobox(background="#d9d9d9", values = ["RC"])
        self.Target = Combobox(background="#d9d9d9", values = ["C"])

        self.structure.place(x = 250.0, y = 147, width = 95.0, height = 15)
        self.Target.place(x = 250.0, y = 296, width = 95.0, height = 15)
    
    def DesignBtn(self):
        #image Button
        self.ApplyImg = ImageTk.PhotoImage(file = f"Apply.png")
        self.DiscardImg = ImageTk.PhotoImage(file = f"Discard.png")
        # create button
        self.AnalogBtn1 = Button( image = self.ApplyImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_Apply("1"), relief = "flat",bg = "#303F40")
        self.AnalogBtn2 = Button( image = self.DiscardImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_Discard("1"), relief = "flat",bg = "#303F40")
        self.DigitaBtn1 = Button( image = self.ApplyImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_Apply("2"), relief = "flat",bg = "#303F40")
        self.DigitaBtn2 = Button( image = self.DiscardImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_Discard("2"), relief = "flat",bg = "#303F40")
        #set button place
        self.AnalogBtn1.place(x = 125, y = 191, width = 109, height = 26)
        self.AnalogBtn2.place(x = 241, y = 191, width = 109, height = 26)
        self.DigitaBtn1.place(x = 125, y = 379, width = 109, height = 26)
        self.DigitaBtn2.place(x = 241, y = 379, width = 109, height = 26)

        self.DigitaBtn1['state'] = DISABLED
        self.DigitaBtn2['state'] = DISABLED
        
    def btn_Apply(self,value):
        aux = self.structure.get()
        if value == "1":    
            if aux == 'RC':
                self.newCanva = Canvas(self.master, bg = "#3A4C4E",height = 520, width = 829, bd = 0, highlightthickness = 0, relief = "ridge")
                self.newCanva.place(x = "402", y = "135")
                self.BgEx = ImageTk.PhotoImage(file = f"BgEx.png")
                self.newCanva.create_image(414, 260, image=self.BgEx)
                self.AnalogRC_img = ImageTk.PhotoImage(file = f"Values_RC.png")
                self.newCanva.create_image(690.0, 275, image=self.AnalogRC_img)
                #internal labels
                self.R1 = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")
                self.R2 = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")
                self.R3 = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")
                self.R4 = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")
                
                self.Rf1 = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")
                self.Rf2 = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")
                self.Rf3 = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")
                self.Rf4 = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")
                self.Rf5 = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")

                self.Ri1 = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")
                self.R = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")
                self.C1 = Label(self.newCanva, fg="#000000",bd = 0, bg = "#ffffff", text = "Value",highlightthickness = 0, anchor= "e")
                
                self.R1.place(x = 690, y = 60, width = 105, height = 15)
                self.R2.place(x = 690, y = 95, width = 105, height = 15)
                self.R3.place(x = 690, y = 130, width = 105, height = 15)
                self.R4.place(x = 690, y = 165, width = 105, height = 15)

                self.Rf1.place(x = 690, y = 200, width = 105, height = 15)
                self.Rf2.place(x = 690, y = 235, width = 105, height = 15)
                self.Rf3.place(x = 690, y = 270, width = 105, height = 15)
                self.Rf4.place(x = 690, y = 305, width = 105, height = 15)
                self.Rf5.place(x = 690, y = 340, width = 105, height = 15)

                self.Ri1.place(x = 690, y = 375, width = 105, height = 15)
                self.R.place(x = 690, y = 410, width = 105, height = 15)
                self.C1.place(x = 690, y = 445, width = 105, height = 15)
                # creacion textos
                self.newCanva.create_text( 630.0, 66, text = "R1             =", fill = "#ffffff", font = ("Calibri", int(12.0)))
                self.newCanva.create_text( 630.0, 101, text = "R2             =", fill = "#ffffff", font = ("Calibri", int(12.0)))
                self.newCanva.create_text( 630.0, 136, text = "R3             =", fill = "#ffffff", font = ("Calibri", int(12.0)))
                self.newCanva.create_text( 630.0, 171, text = "R4             =", fill = "#ffffff", font = ("Calibri", int(12.0)))

                self.newCanva.create_text( 630.0, 206, text = "Rf1            =", fill = "#ffffff", font = ("Calibri", int(12.0)))
                self.newCanva.create_text( 630.0, 241, text = "Rf2            =", fill = "#ffffff", font = ("Calibri", int(12.0)))
                self.newCanva.create_text( 630.0, 276, text = "Rf3            =", fill = "#ffffff", font = ("Calibri", int(12.0)))
                self.newCanva.create_text( 630.0, 311, text = "Rf4            =", fill = "#ffffff", font = ("Calibri", int(12.0)))
                self.newCanva.create_text( 630.0, 346, text = "Rf5             =", fill = "#ffffff", font = ("Calibri", int(12.0)))
                
                self.newCanva.create_text( 630.0, 381, text = "Ri1-i5         =", fill = "#ffffff", font = ("Calibri", int(12.0)))
                self.newCanva.create_text( 630.0, 416, text = "R                =", fill = "#ffffff", font = ("Calibri", int(12.0)))
                self.newCanva.create_text( 630.0, 451, text = "C1-C5         =", fill = "#ffffff", font = ("Calibri", int(12.0)))

                self.btnSave = Button(self.newCanva, text = "Save", fg = "#ffffff", bg = "#303F40", font = ("Calibri", int(12.0)),   borderwidth = 0, highlightthickness = 0, command = self.btn_saveDesign, relief = "flat")
                self.btnSave.place(x = 25, y = 480, width = 109, height = 26)

    def btn_saveDesign(self):
        global Parameters
        if len(Parameters) > 12:  
            aux = "R1,"+ str(Parameters[15]) +"\nR2,"+ str(Parameters[16]) +"\nR3,"+ str(Parameters[17]) +"\nR4,"+ str(Parameters[18]),
            + "\nRf1,"+ str(Parameters[6]) +"\nRf2,"+ str(Parameters[7]) +"\nRf3,"+ str(Parameters[8]) +"\nRf4,"+ str(Parameters[9]) +"\nRf5,"+ str(Parameters[10]),
            + "\nRi1,"+ str(Parameters[1]) +"\nRi2,"+ str(Parameters[2]) +"\nRi3,"+ str(Parameters[3]) +"\nRi4,"+ str(Parameters[4]) +"\nRi5,"+ str(Parameters[5]),
            + "\nC1,"+ str(Parameters[11]) +"\nC2,"+ str(Parameters[12]) +"\nC3,"+ str(Parameters[13]) +"\nC4,"+ str(Parameters[14])    
        fname = filedialog.asksaveasfilename()
        try:
            if fname.__contains__(".txt"):
                pass
            else:
                fname = fname + ".txt"
            f = open(fname,'w',encoding = 'utf-8') 
            f.write(aux)
            #print(f.readline())
            f.close()
        except:
            pass
    
    def VerifyValues(self):
        pass



    def btn_Discard(self,value): 
        aux = self.structure.get()
        if aux == 'RC':
            self.newCanva.destroy()

class SummaryWindow:
    def __init__(self,master=None,canva=None):
        super().__init__()
        self.master = master
        self.canva = canva
        self.bg2_img = ImageTk.PhotoImage(file = f"background5.png")
        background = self.canva.create_image(640.0, 366.0, image=self.bg2_img)
        self.DesignBtn()
    def DesignBtn(self):
        #image Button
        self.SummIMG = ImageTk.PhotoImage(file = f"summ.png")
        # create button
        self.SummBtn = Button( image = self.SummIMG, borderwidth = 0, highlightthickness = 0, command = self.btn_Action, relief = "flat",bg = "#303F40")
        #set button place
        self.SummBtn.place(x = 130, y = 166, width = 109, height = 26)
    def btn_Action(self):
        pass



if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)    
    root.title("Fraxsoft Beta")
    gui = APP(root)
    root.mainloop()