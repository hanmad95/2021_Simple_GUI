# -*- coding: utf-8 -*-
import tkinter as tk 
import pandas as pd 

#=========================================================================================================================
# Main Menue Class
#=========================================================================================================================

class MainMenue:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Ground GUI Main Menue")
        self.can = tk.Canvas(self.master, width=600, height=400)
        self.can.pack()
        self.bgimage = tk.PhotoImage(file="main_bg.GIF")
        self.bglabel = tk.Label(self.master, image= self.bgimage)
        self.bglabel.place(relwidth=1,relheight=1)
        self.buttonframe = tk.Frame(self.master)
        self.buttonframe.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.4)
        self.button1 = tk.Button(self.buttonframe, text ="Pre-Processing",fg="blue", bg="white", command=self.new_window)
        self.button1.place(relx=0,rely=0,relwidth=1,relheight=0.2)
        self.button2 = tk.Button(self.buttonframe, text ="Visualization",fg="blue", bg="white", command=self.new_window1)
        self.button2.place(relx=0,rely=0.2,relwidth=1,relheight=0.2)
        self.exitbutton = tk.Button(self.buttonframe,text="Exit",fg="blue", bg="white", command=self.master.destroy)
        self.exitbutton.place(relx=0,rely=0.8,relwidth=1,relheight=0.2)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        w = self.newWindow.winfo_screenwidth()
        self.newWindow.geometry("600x400+%d+%d" %(int(round(w*0.4)),0))
        #self.new = PreProcessing(self.newWindow, self.setting)

    def new_window1(self):
        self.newWindow1 = tk.Toplevel(self.master)
        w = self.newWindow1.winfo_screenwidth()
        h = self.newWindow1.winfo_screenheight()
        self.newWindow1.geometry("600x400+%d+%d" %(int(round(w*0.4)),0))
        #self.new = Calculation(self.newWindow1, self.setting)
    

  

#=========================================================================================================================
# Main File Execution
#=========================================================================================================================

def main():
    root = tk.Tk()
    root.geometry("600x400+%d+%d" %(0,0)) # WidthxHeight+X_Screen+Y_Screen
    app = MainMenue(root)
    root.mainloop()

if __name__ == "__main__":
    main()
