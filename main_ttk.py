# -*- coding: utf-8 -*-
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter as tk 
import os
import sys
 
#==========================================================================================================================
# Import Windows:
#==========================================================================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
Funktion_path = current_dir + "\\" + "windows"
sys.path.insert(0,Funktion_path)

from visualization import vis_window
#=========================================================================================================================
# Main Menue Class
#=========================================================================================================================

class MainMenue:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Ground GUI Main Menue")
        self.bgimage = tk.PhotoImage(file="main_bg.GIF")
        self.bglabel = tk.Label(self.master, image= self.bgimage)
        self.bglabel.place(relwidth=1,relheight=1)
        self.buttonframe = ttk.Frame(self.master)
        self.buttonframe.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.4)
        self.button1 = ttk.Button(self.buttonframe, text ="Pre-Processing", command=self.new_window)
        self.button1.place(relx=0,rely=0,relwidth=1,relheight=0.2)
        self.button2 = ttk.Button(self.buttonframe, text ="Visualization", command=self.new_window1)
        self.button2.place(relx=0,rely=0.2,relwidth=1,relheight=0.2)
        self.exitbutton = ttk.Button(self.buttonframe,text="Exit", command=self.master.destroy)
        self.exitbutton.place(relx=0,rely=0.8,relwidth=1,relheight=0.2)
    

    def new_window(self): 
        self.newWindow = tk.Toplevel(self.master)
        w = self.newWindow.winfo_screenwidth()
        self.newWindow.geometry("600x400+%d+%d" %(int(round(w*0.4)),0))
        #self.new = vis_window(self.newWindow)
        
    # Visualization Window  
    def new_window1(self):
        self.newWindow1 = tk.Toplevel(self.master)
        w = self.newWindow1.winfo_screenwidth()
        self.newWindow1.geometry("600x400+%d+%d" %(int(round(w*0.4)),0))
        self.new = vis_window(self.newWindow)
    
#========================================================================================================================
# Main File Execution
#=========================================================================================================================

def main():
    root = ThemedTk(theme='aqua')
    root.geometry("600x400+%d+%d" %(0,0)) # WidthxHeight+X_Screen+Y_Screen
    app = MainMenue(root)
    root.mainloop()

if __name__ == "__main__":
    main()
