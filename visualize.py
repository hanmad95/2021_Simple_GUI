from tkinter.filedialog import askopenfilename
from tkinter import ttk
import tkinter as tk
import pandas as pd
import numpy as np
import re
import os
import distance

#=========================================================================================================================
# Visualization
#=========================================================================================================================


class PreProcessing:
    def __init__(self, master, settings):
        self.setting = settings
        self.master = master
        self.master.title("Visualization")
        self.can = tk.Canvas(self.master, width=600, height=400)
        self.can.pack()
        self.label1=tk.Label(self.master, text="Please load an SLR:")
        self.label1.place(relx=0.2,rely=0.1)
        self.loadbutton = tk.Button(self.master, text="Load SLR", bg="gray",command=self.loadslr)
        self.loadbutton.place(relx=0.5, rely=0.1)
        self.label2=tk.Label(self.master, text="Please load Zoning:")
        self.label2.place(relx=0.2,rely=0.2)
        self.loadbuttonzones = tk.Button(self.master, text="Load Zoning", bg="gray",command=self.loadzones)
        self.loadbuttonzones.place(relx=0.5, rely=0.2)
        self.cleanbutton = tk.Button(self.master, text="Clean Report",bg="gray", command=self.cleanbutton)
        self.cleanbutton.place(relx=0.2, rely=0.4)
        self.cleanprogress = ttk.Progressbar(self.master, orient="horizontal", length=200, mode="determinate")
        self.cleanprogress.place(relx=0.42, rely=0.4)
        self.lanebutton = tk.Button(self.master, text="Add Lanes", bg="gray", command = self.add_lanes)
        self.lanebutton.place(relx=0.2,rely=0.5)
        self.laneprogress = ttk.Progressbar(self.master, orient="horizontal", length=200, mode="determinate")
        self.laneprogress.place(relx=0.42, rely=0.5)
        self.bundlingbutton = tk.Button(self.master, text="Bundling", bg="gray", command = self.bundling)
        self.bundlingbutton.place(relx=0.2,rely=0.6)
        self.bundlingprogress = ttk.Progressbar(self.master, orient="horizontal", length=200, mode="determinate")
        self.bundlingprogress.place(relx=0.42, rely=0.6)
        self.exitbutton = tk.Button(self.master,text="Save & Close",bg="gray", command=self.close_and_save)
        self.exitbutton.place(relx=0.375, rely=0.85)




    #=====================================================================================================================   
    # Load the Dataframe
    #=====================================================================================================================
    
    def loadslr(self):
        # Create the Basis SLR Path:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        SLR_path = str(current_dir + "\\" + "SLR").replace(r"\Funktionen","")
        
        # Load only the necessary fields into DataFrame:
        use_fields = [self.setting.origlkz, self.setting.origzip, self.setting.origcity, self.setting.origstreet,
                      self.setting.destlkz, self.setting.destzip, self.setting.destcity, self.setting.deststreet,
                      self.setting.date, self.setting.grossweight, self.setting.volume]

        # We try to open the SLR:
        try:
            self.SLR_filepath = askopenfilename(initialdir = SLR_path,title="Select SLR") # Ask for File
            self.SLR_frame = pd.read_csv(self.SLR_filepath, delimiter=";",encoding=self.setting.encode1,low_memory=False,skipinitialspace=True,usecols=use_fields)# Load CSV File into Dataframe
            print("Load SLR File: ", self.SLR_filepath)
            print(self.SLR_frame.info())
            headers = list(self.SLR_frame)
            print(headers)
            self.loadbutton.config(text="DONE",bg="green")
        except:
            try:
                self.SLR_filepath = askopenfilename(initialdir = SLR_path,title="Select SLR") # Ask for File
                self.SLR_frame = pd.read_csv(self.SLR_filepath, delimiter=";",encoding=self.setting.encode2,low_memory=False,skipinitialspace=True,usecols=use_fields)# Load CSV File into Dataframe
                print("Load SLR File: ", self.SLR_filepath)
                print(self.SLR_frame.info())
                headers = list(self.SLR_frame)
                print(headers)
                self.loadbutton.config(text="DONE",bg="green")

            except:
                print("Some Error Accured... Please Try Again")
                self.loadbutton.config(text="Try Again",bg="red")

    def loadzones(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        zoning_path = str(current_dir + "\\" + "Zoning").replace(r"\Funktionen","")

        try:
            zoning_filepath = askopenfilename(initialdir = zoning_path,title="Select Zoning") # Ask for File
            self.zone_frame = pd.read_csv(zoning_filepath, delimiter=";",encoding=self.setting.encode1)
            print("Load Zoning File: ", zoning_filepath) 
            headers = list(self.zone_frame)
            print(headers)
            self.loadbuttonzones.config(text="DONE",bg="green")
        except:
            print("Some Error Accured... Please Try Again")
            self.loadbuttonzones.config(text="Try Again",bg="red")
            
