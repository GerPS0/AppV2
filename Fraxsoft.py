from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

class MainWindow:
    def __init__(self,master = None):
        super().__init__()
        self.master = master
        self.bg1()
        Buttons.mainBtn(self)
        
    def bg1(self):
        self.master.geometry("920x720")
        self.master.configure(bg = "#253132")
        self.MainW = Canvas(self.master,bg = "#253132", height = 720, width = 920, bd = 0, highlightthickness = 0, relief = "ridge")
        self.MainW.place(x = 0, y = 0)
        # Define Background
        self.background_img = ImageTk.PhotoImage(file = f"background.png")
        background = self.MainW.create_image(475.0, 204.0, image=self.background_img)
    
    def btnNew(self):
        self.MainW.destroy()
        self.newWindow()

    def btnLoad(self):
        archivo = filedialog.askopenfilename()
        if archivo is "":
            messagebox.showwarning(title = "Warning", message="Escoger un archivo correcto")
        else:
            messagebox.askyesno(title = "", message= "Do you wish to proceed?")
    def btnHelp(self):
        pass 
    def Generalbg(self):
        self.master.geometry("1280x720")
        self.master.configure(bg = "#253132")
        self.ConverterW = Canvas(self.master,bg = "#253132", height = 720, width = 920, bd = 0, highlightthickness = 0, relief = "ridge")
        self.ConverterW.place(x = 0, y = 0)
        self.bg2_img = ImageTk.PhotoImage(file = f"background2.png")
        bg2 = self.ConverterW.create_image(640.0, 366.0, image=self.bg2_img)

    def newWindow(self):
        self.Generalbg()
        ConverterWindow.__init__(self)
        self.entryBox1()
    def btn_clicked(self):
        pass
    def entryBox1(self):
        # Labels
        self.ConverterW.create_text(165.0, 139.5, text = "Input Voltage    =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.ConverterW.create_text(165.0, 166.5, text = "Ouput Voltage  =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.ConverterW.create_text(165.0, 193.5, text = "Output Power   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.ConverterW.create_text(165.0, 220.5, text = "Voltage ripple   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.ConverterW.create_text(165.0, 247.5, text = "Current ripple   =", fill = "#ffffff", font = ("Calibri", int(12.0)))
        self.ConverterW.create_text(165.0, 274.5, text = "Topology               ", fill = "#ffffff", font = ("Calibri", int(12.0)))

        # Image
        #entry0_bg = ConverterW.create_image(278.0, 247.5, image = entry0_img)
        # Entries
        self.Vin = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0)
        self.Vo = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0)
        self.Po = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0)
        self.Vripple = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0)
        self.Cripple = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0)
        # Place
        self.Vin.place(x = 222, y = 134, width = 108, height = 13)
        self.Vo.place(x = 222, y = 161, width = 108, height = 13)
        self.Po.place(x = 222, y = 188, width = 108, height = 13)
        self.Vripple.place(x = 222, y = 215, width = 108, height = 13)
        self.Cripple.place(x = 222, y = 242, width = 108, height = 13)

class Buttons:
    def __init__(self) -> None:
        pass   
    def mainBtn(self):
        # image for buttons
        self.New = ImageTk.PhotoImage(file = f"New.png")
        self.Load = ImageTk.PhotoImage(file = f"Load.png")
        self.ImgHelp = ImageTk.PhotoImage(file = f"Help.png")
        # create button
        self.NewDesign = Button(image = self.New, borderwidth=0, highlightthickness=0, command=self.btnNew, relief = "flat")
        self.LoadDesign = Button(image = self.Load, borderwidth=0, highlightthickness=0, command=self.btnLoad, relief = "flat")
        self.Help = Button(image = self.ImgHelp, borderwidth=0, highlightthickness=0, command=self.btnHelp, relief = "flat")
        self.NewDesign.place(x = 335, y = 405, width= 280, height=70)
        self.LoadDesign.place(x = 335, y = 505, width= 280, height=70)
        self.Help.place(x = 335, y = 605, width= 280, height=70)
    
    def ConverterBtn(self):
       # image for buttons
        self.BuckImg = ImageTk.PhotoImage(file = f"Buck.png")
        self.BoostImg = ImageTk.PhotoImage(file = f"Boost.png")
        self.BBImg = ImageTk.PhotoImage(file = f"BB.png")
        self.ApplyImg = ImageTk.PhotoImage(file = f"Apply.png")
        self.DiscardImg = ImageTk.PhotoImage(file = f"Discard.png")
        
        self.ConvDesImg = ImageTk.PhotoImage(file = f"ConvDes.png")
        self.ElemSpecImg = ImageTk.PhotoImage(file = f"ElemSpec.png")
        self.CtrlDesImg = ImageTk.PhotoImage(file = f"CtrlDes.png")
        self.CtrlImpImg = ImageTk.PhotoImage(file = f"CtrlImp.png")
        self.SummaryImg = ImageTk.PhotoImage(file = f"Summary.png")
        # create button
        self.Buck = Button(image = self.BuckImg, borderwidth = 0, highlightthickness = 0, command = ConverterWindow.btn_clicked(self), relief = "flat")
        self.Boost = Button(image = self.BoostImg, borderwidth = 0, highlightthickness = 0, command = ConverterWindow.btn_clicked(self), relief = "flat") 
        self.BB = Button(image = self.BBImg, borderwidth = 0, highlightthickness = 0, command = ConverterWindow.btn_clicked(self), relief = "flat")
        self.Apply = Button(image = self.ApplyImg, borderwidth = 0, highlightthickness = 0, command = ConverterWindow.btn_clicked(self), relief = "flat")
        self.Discard = Button(image = self.DiscardImg, borderwidth = 0, highlightthickness = 0, command = ConverterWindow.btn_clicked(self), relief = "flat")
        
        self.ConvDes = Button(image = self.ConvDesImg, borderwidth = 0, highlightthickness = 0, command = ConverterWindow.btn_clicked(self), relief = "flat")
        self.ElemSpec = Button(image = self.ElemSpecImg, borderwidth = 0, highlightthickness = 0, command = ConverterWindow.btn_clicked(self), relief = "flat")
        self.CtrlDes = Button(image = self.CtrlDesImg, borderwidth = 0, highlightthickness = 0, command = ConverterWindow.btn_clicked(self), relief = "flat")
        self.CtrlImp = Button(image = self.CtrlImpImg, borderwidth = 0, highlightthickness = 0, command = ConverterWindow.btn_clicked(self), relief = "flat")
        self.Summary = Button(image = self.SummaryImg, borderwidth = 0, highlightthickness = 0, command = ConverterWindow.btn_clicked(self), relief = "flat")
        #set button place
        self.Buck.place(x = 109, y = 299, width = 45, height = 20)
        self.Boost.place(x = 166, y = 299, width = 45, height = 20)
        self.BB.place(x = 222, y = 299, width = 45, height = 20) 
        self.Apply.place(x = 96, y = 360, width = 109, height = 26)
        self.Discard.place(x = 229, y = 360, width = 109, height = 26)

        self.ConvDes.place(x = 6, y = 90, width = 70, height = 61)
        self.ElemSpec.place(x = 6, y = 171, width = 70, height = 61)
        self.CtrlDes.place(x = 6, y = 252, width = 70, height = 61)
        self.CtrlImp.place(x = 6, y = 333, width = 70, height = 61)
        self.Summary.place(x = 6, y = 414, width = 70, height = 61)
class ConverterWindow(MainWindow):
    def __init__(self):
        Buttons.ConverterBtn(self)
        

if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)    
    gui = MainWindow(root)
    root.mainloop()