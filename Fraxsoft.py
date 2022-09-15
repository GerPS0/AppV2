
from encodings import utf_8
from fileinput import close
from operator import contains
from tkinter import *
from tkinter import font
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox


DataValue = ["1"]
pantalla = "1"

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
        self.NewDesign = Button( image = self.New, borderwidth=0, highlightthickness=0, command=self.btnNew, relief = "flat")
        self.LoadDesign = Button( image = self.Load, borderwidth=0, highlightthickness=0, command=self.btnLoad, relief = "flat")
        self.Help = Button( image = self.ImgHelp, borderwidth=0, highlightthickness=0, command=self.btnHelp, relief = "flat")
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
        self.ConvDes = Button( image = self.ConvDesImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_click("1"), relief = "flat")
        self.ElemSpec = Button( image = self.ElemSpecImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_click("2"), relief = "flat")
        self.CtrlDes = Button( image = self.CtrlDesImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_click("3"), relief = "flat")
        self.CtrlImp = Button( image = self.CtrlImpImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_click("4"), relief = "flat")
        self.Summary = Button( image = self.SummaryImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_click("5"), relief = "flat")
        
        self.NweD = Button( image = self.ImgNewD, borderwidth=0, highlightthickness=0, command=lambda:self.btn_action("1"), relief = "flat")
        self.Save = Button( image = self.ImgSave, borderwidth=0, highlightthickness=0, command=lambda:self.btn_action("2"), relief = "flat")
        self.Open = Button( image = self.ImgOpen, borderwidth=0, highlightthickness=0, command=lambda:self.btn_action("3"), relief = "flat")
        self.Help2 = Button( image = self.ImgHelp2, borderwidth=0, highlightthickness=0, command=lambda:self.btn_action("4"), relief = "flat")

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
        self.previousVal1()
    
    def ConverterBtn(self):       
        #image Button
        self.ApplyImg = ImageTk.PhotoImage(file = f"Apply.png")
        self.DiscardImg = ImageTk.PhotoImage(file = f"Discard.png")
        # create button
        self.Apply = Button( image = self.ApplyImg, borderwidth = 0, highlightthickness = 0, command = self.btn_Apply, relief = "flat")
        self.Discard = Button( image = self.DiscardImg, borderwidth = 0, highlightthickness = 0, command = self.btn_Discard, relief = "flat")
        #set button place
        self.Apply.place(x = 96, y = 360, width = 109, height = 26)
        self.Discard.place(x = 229, y = 360, width = 109, height = 26)

    def btn_Apply(self):
        DataValue[0] = pantalla
        aux = [self.Vin.get(), self.Vo.get(), self.Po.get(), self.Vripple.get(), self.Cripple.get(), self.Topology.get()]
        if aux.__contains__(""):
            messagebox.showwarning(title = "Warning", message="Fill all entry values")
        DataValue[1:] = aux
        print(type(DataValue),DataValue)
        self.DisplayConverter()

    def btn_Discard(self):
        self.Vin.delete(0,END) 
        self.Vo.delete(0,END)
        self.Po.delete(0,END)
        self.Vripple.delete(0,END)
        self.Cripple.delete(0,END)
        DataValue[1:] = [self.Vin.get(), self.Vo.get(), self.Po.get(), self.Vripple.get(), self.Cripple.get(), self.Topology.get()]
        print(type(DataValue),DataValue)   
        self.newCanva.destroy()
    def DisplayConverter(self):
        self.newCanva = Canvas(self.master, bg = "#3A4C4E",height = 520, width = 829, bd = 0, highlightthickness = 0, relief = "ridge")
        self.newCanva.place(x = "402", y = "135")

    def entryBox1(self):
        
        # Labels
        self.canva.create_text(165.0, 155.5, text = "Input Voltage    =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(165.0, 182.5, text = "Ouput Voltage  =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(165.0, 209.5, text = "Output Power   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(165.0, 236.5, text = "Voltage ripple   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(165.0, 263.5, text = "Current ripple   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(165.0, 293.5, text = "Topology           =", fill = "#ffffff", font = ("Calibri", int(12.0)))

        # Entries
        self.Vin = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.Vo = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.Po = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.Vripple = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.Cripple = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, justify=RIGHT)
        self.Topology = Combobox(background="#d9d9d9", values = ["Buck", "Boost", "Buck/Boost"],textvariable = self.typesC)
        
        # Place
        self.Vin.place(x = 222, y = 150, width = 108, height = 13)
        self.Vo.place(x = 222, y = 177, width = 108, height = 13)
        self.Po.place(x = 222, y = 204, width = 108, height = 13)
        self.Vripple.place(x = 222, y = 231, width = 108, height = 13)
        self.Cripple.place(x = 222, y = 258, width = 108, height = 13)
        self.Topology.place(x = 222, y = 288, width = 108, height = 18)
        
    def previousVal1(self,*args):
        global DataValue
        print(DataValue)
        self.Vin.delete(0,END) 
        self.Vo.delete(0,END)
        self.Po.delete(0,END)
        self.Vripple.delete(0,END)
        self.Cripple.delete(0,END)
        if DataValue.__contains__("") or len(DataValue) < 7:
            pass
        else:
            self.Vin.insert(0,str(DataValue[1]))
            self.Vo.insert(0,str(DataValue[2]))
            self.Po.insert(0,str(DataValue[3]))
            self.Vripple.insert(0,str(DataValue[4]))
            self.Cripple.insert(0,str(DataValue[5]))
            self.typesC.set(str(DataValue[6]))
            
    
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
        
        global DataValue
        global pantalla
        pantalla = "2"
        
        self.bg2_img = ImageTk.PhotoImage(file = f"background3.png")
        background = self.canva.create_image(640.0, 366.0, image=self.bg2_img)
        
        self.DesignBtn()
        self.entryBox2()
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
        self.controller = Combobox(background="#d9d9d9", values = ["FOPID", "FOPI", "FOPD", "PID"])
        

        #place enables
        self.PmE.place(x = 273, y = 292, width = 102, height = 13)
        self.GmE.place(x = 273, y = 311, width = 102, height = 13)
        self.controller.place(x = 273, y = 330, width = 102, height = 18)

        #Disable entriies
        self.PmD1 = Label( fg="#ffffff",bd = 0, bg = "#303F40", text = "Value",highlightthickness = 0, anchor= "e")
        self.GmD1 = Label( fg="#ffffff",bd = 0, bg = "#303F40", text = "Value",highlightthickness = 0, anchor= "e")
        self.G01 = Label( fg="#ffffff",bd = 0, bg = "#303F40", text = "Value",highlightthickness = 0, anchor= "e")
        self.Stable1 = Label( fg="#ffffff", bd = 0, bg = "#303F40", text = "Value",highlightthickness = 0, anchor = "e")

        self.PmD2 = Label( fg="#ffffff", bd = 0, bg = "#303F40", text = "Value",highlightthickness = 0, anchor= "e")
        self.GmD2 = Label( fg="#ffffff", bd = 0, bg = "#303F40", text = "Value",highlightthickness = 0, anchor= "e")
        self.G02 = Label( fg="#ffffff", bd = 0, bg = "#303F40", text = "Value",highlightthickness = 0, anchor= "e")
        self.Stable2 = Label( fg="#ffffff", bd = 0, bg = "#303F40", text = "Value",highlightthickness = 0, anchor= "e")

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
        self.Apply = Button( image = self.ApplyImg, borderwidth = 0, highlightthickness = 0, command = self.btn_Apply, relief = "flat")
        self.Discard = Button( image = self.DiscardImg, borderwidth = 0, highlightthickness = 0, command = self.btn_Discard, relief = "flat")
        #set button place
        self.Apply.place(x = 139, y = 365, width = 109, height = 26)
        self.Discard.place(x = 264, y = 365, width = 109, height = 26)

    def btn_Apply(self):
        DataValue[0] = pantalla
        aux = [self.PmE.get(), self.GmE.get(), self.controller.get()]
        if aux.__contains__(""):
            messagebox.showwarning(title = "Warning", message="Fill all entry values")
        DataValue[7:] = aux
        print(type(DataValue),DataValue)
        self.DisplayGraphs()
    def btn_Discard(self):
        self.PmE.delete(0,END) 
        self.GmE.delete(0,END)
        aux = [self.PmE.get(), self.GmE.get(), self.controller.get()]
        DataValue[7:] = aux
        print(type(DataValue),DataValue) 
        self.newCanva.destroy()

    def DisplayGraphs(self):
        self.newCanva = Canvas(self.master, bg = "#3A4C4E",height = 520, width = 829, bd = 0, highlightthickness = 0, relief = "ridge")
        self.newCanva.place(x = "402", y = "135")
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
        self.ElemBtn = Button( image = self.ElemIMG, borderwidth = 0, highlightthickness = 0, command = self.btn_Action, relief = "flat")
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
        self.AnalogBtn1 = Button( image = self.ApplyImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_Apply("1"), relief = "flat")
        self.AnalogBtn2 = Button( image = self.DiscardImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_Discard("1"), relief = "flat")
        self.DigitaBtn1 = Button( image = self.ApplyImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_Apply("2"), relief = "flat")
        self.DigitaBtn2 = Button( image = self.DiscardImg, borderwidth = 0, highlightthickness = 0, command = lambda:self.btn_Discard("2"), relief = "flat")
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
        self.SummBtn = Button( image = self.SummIMG, borderwidth = 0, highlightthickness = 0, command = self.btn_Action, relief = "flat")
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