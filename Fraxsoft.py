from msilib.schema import ComboBox
from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

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
        window = ("1")
        MainBackgraound(self.master,window)

    def btnLoad(self):
        archivo = filedialog.askopenfilename()
        if archivo == "":
            messagebox.showwarning(title = "Warning", message="Escoger un archivo correcto")
        else:
            messagebox.askyesno(title = "", message= "Do you wish to proceed?")
    def btnHelp(self):
        pass     

class MainBackgraound:
    def __init__(self,master,window):
        super().__init__()
        self.master = master
        self.Ventanas(window)
        #ConverterWindow(self.master,self.MainBG)
    
    def Ventanas(self,value):
        self.bg2()
        self.BgButtons()
        if value == "1":
            ConverterWindow(self.master,self.MainBG)
            self.ConvDes['state'] = DISABLED
        if value == "3":
            DesignWindow(self.master,self.MainBG)
            self.CtrlDes['state'] = DISABLED
            self.ConvDes['state'] = NORMAL
    
    def bg2(self):
        self.master.geometry("1280x720")
        self.master.configure(bg = "#253132")
        self.MainBG = Canvas(self.master,bg = "#253132", height = 720, width = 1280, bd = 0, highlightthickness = 0, relief = "ridge")
        self.MainBG.place(x = 0, y = 0)
      
    def btn_click(self,value):
        self.value = value
        print(self.value)
        self.Ventanas(self.value)
    def btn_action(self):
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
        
        self.NweD = Button( image = self.ImgNewD, borderwidth=0, highlightthickness=0, command=self.btn_action, relief = "flat")
        self.Save = Button( image = self.ImgSave, borderwidth=0, highlightthickness=0, command=self.btn_action, relief = "flat")
        self.Open = Button( image = self.ImgOpen, borderwidth=0, highlightthickness=0, command=self.btn_action, relief = "flat")
        self.Help2 = Button( image = self.ImgHelp2, borderwidth=0, highlightthickness=0, command=self.btn_action, relief = "flat")

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
    def __init__(self,master=None,canva=None):
        super().__init__()
        self.master = master
        self.canva = canva
        self.bg2_img = ImageTk.PhotoImage(file = f"background2.png")
        background = self.canva.create_image(640.0, 366.0, image=self.bg2_img)
        self.ConverterBtn()
        self.entryBox1()
    
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
        global Values
        Values = [self.Vin.get(), self.Vo.get(), self.Po.get(), self.Vripple.get(), self.Cripple.get(), self.Topology.get()]
        if Values.__contains__(""):
            messagebox.showwarning(title = "Warning", message="Fill all entry values")
    
    def btn_Discard(self):
        self.Vin.delete(0,END) 
        self.Vo.delete(0,END)
        self.Po.delete(0,END)
        self.Vripple.delete(0,END)
        self.Cripple.delete(0,END)
        Values = [self.Vin.get(), self.Vo.get(), self.Po.get(), self.Vripple.get(), self.Cripple.get(), self.Topology.get()]
           
    def entryBox1(self):
        # Labels
        self.canva.create_text(165.0, 139.5, text = "Input Voltage    =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(165.0, 166.5, text = "Ouput Voltage  =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(165.0, 193.5, text = "Output Power   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(165.0, 220.5, text = "Voltage ripple   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(165.0, 247.5, text = "Current ripple   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(165.0, 274.5, text = "Topology           =", fill = "#ffffff", font = ("Calibri", int(12.0)))

        # Entries
        self.Vin = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0)
        self.Vo = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0)
        self.Po = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0)
        self.Vripple = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0)
        self.Cripple = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0)
        self.Topology = Combobox(values = ["Buck", "Boost", "Buck/Boost"])
        
        # Place
        self.Vin.place(x = 222, y = 134, width = 108, height = 13)
        self.Vo.place(x = 222, y = 161, width = 108, height = 13)
        self.Po.place(x = 222, y = 188, width = 108, height = 13)
        self.Vripple.place(x = 222, y = 215, width = 108, height = 13)
        self.Cripple.place(x = 222, y = 242, width = 108, height = 13)
        self.Topology.place(x = 222, y = 269, width = 108, height = 18)

class DesignWindow:
    def __init__(self,master=None,canva=None):
        super().__init__()
        self.master = master
        self.canva = canva
        self.bg3_img = ImageTk.PhotoImage(file = f"background3.png")
        background = self.canva.create_image(640.0, 366.5, image=self.bg3_img)
        self.entryBox2()
    
    def entryBox2(self):
        #labels
        self.canva.create_text(203.0, 167.5, text = "Pm                           =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 184.5, text = "Gm                           =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 205.5, text = "G(0)                          =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 224.5, text = "Stable?                    =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        
        self.canva.create_text(203.0, 298.5, text = "Pm                           =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 317.5, text = "Gm                           =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 336.5, text = "Controller structure =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        
        self.canva.create_text(203.0, 455.5, text = "Pm                           =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 474.5, text = "Gm                           =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 493.5, text = "G(0)                          =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.canva.create_text(203.0, 512.5, text = "Stable?                    =", fill = "#ffffff", font = ("Calibri", int(12.0)))

        #Enable entries
        self.PmE = Entry( bd = 0, bg = "#3a4c4e", highlightthickness = 0)
        self.GmE = Entry( bd = 0, bg = "#3a4c4e", highlightthickness = 0)
        self.controller = Combobox(values = ["FOPID", "FOPI", "FOPD", "PID"])

        #place enables
        self.PmE.place(x = 273, y = 292, width = 102, height = 13)
        self.GmE.place(x = 273, y = 311, width = 102, height = 13)
        self.controller.place(x = 273, y = 330, width = 102, height = 18)

        #Disable entriies
        self.PmD1 = Entry( bd = 0, bg = "#3a4c4e", highlightthickness = 0,state= "disabled")
        self.GmD1 = Entry( bd = 0, bg = "#3a4c4e", highlightthickness = 0,state= "disabled")
        self.G01 = Entry(bd = 0, bg = "#3a4c4e", highlightthickness = 0,state= "disabled")
        self.Stable1 = Entry(bd = 0, bg = "#3a4c4e", highlightthickness = 0,state= "disabled")

        self.PmD2 = Entry( bd = 0, bg = "#3a4c4e", highlightthickness = 0,state= "disabled")
        self.GmD2 = Entry( bd = 0, bg = "#3a4c4e", highlightthickness = 0,state= "disabled")
        self.G02 = Entry(bd = 0, bg = "#3a4c4e", highlightthickness = 0, state= "disabled")
        self.Stable2 = Entry(bd = 0, bg = "#3a4c4e", highlightthickness = 0,state= "disabled")

        #place disables
        self.PmD1.place(x = 273, y = 160, width = 102, height = 13)
        self.GmD1.place(x = 273, y = 179, width = 102, height = 13)
        self.G01.place(x = 273, y = 198, width = 102, height = 13)
        self.Stable1.place(x = 273, y = 217, width = 102, height = 13)

        self.PmD2.place(x = 273, y = 448, width = 102, height = 13)
        self.GmD2.place(x = 273, y = 467, width = 102, height = 13)
        self.G02.place(x = 273, y = 486, width = 102, height = 13)
        self.Stable2.place(x = 273, y = 505, width = 102, height = 13)

        #default Values of Disabled entries
        self.PmD1.insert(0,"Value°")
        self.GmD1.insert(0,"Value")
        self.G01.insert(0,"Value")
        self.Stable1.insert(0,"Yes/No")

        self.PmD2.insert(0,"Value°")
        self.GmD2.insert(0,"ValuedB")
        self.G02.insert(0,"ValuedB")
        self.Stable2.insert(0,"Yes/No")

if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)    
    gui = APP(root)
    root.mainloop()