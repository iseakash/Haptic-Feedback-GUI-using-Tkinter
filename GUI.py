# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:37:43 2020

@author: puni3lv
"""

from numpy import *
import numpy as np
import pandas as pd
from apyori import apriori
from scipy.interpolate import *
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox
from ttkthemes import themed_tk as tk
import cx_Freeze
import csv
import time
import tkinter as tki
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import tkinter.font as font

def callback(url):
    webbrowser.open_new(url)


#Creating Functions
def upload_file():
    global filepath
    filepath = filedialog.askopenfilename()
    global file
    file = pd.read_csv(filepath)
    filelabel['text'] = "Step 2 :- Click on  Open MPP Process Data"
    #fileload['text'] = os.path.basename(filepath) + " Uploaded"
    status_bar['text'] = "Uploaded" + ' ' + os.path.basename(filepath)

def run_algorithm():
    global file_new
    groupset = file['General Category'].groupby(file['PRODUCT_SERNO'])
 
    rules = apriori(c, min_support = supp, min_confidence = conf, min_lift = liftt, min_length = 2)
    results = list(rules)
    #print(results)
    
    file_new = [list(results[i][0]) for i in range(0,len(results))]
    status_bar['text'] = "Predicted Result of" + ' ' + os.path.basename(filepath)
    filelabel['text'] = "Step 3 :- Prediction Completed, Click on Download to get the Output"
    #predict['text'] = "Prediction Completed"

def download_file():
    path = 'C:/Users/puni3lv/Desktop/'
    savefile = time.strftime("%Y-%m-%d-%H-%M")
    with open(path+ savefile+'.csv', 'w', newline='') as f1:
    #with open('C:/Users/puni3lv/Desktop/now_test1.csv', 'w', newline='') as f1:
        writer = csv.writer(f1)
        writer.writerows(file_new)
    status_bar['text'] = "Downloaded" + ' ' + os.path.basename(filepath)
    filelabel['text'] = "Step 4 :- File Downloaded on your Desktop"
    #out1['text'] = "File Downloaded"

######################################## Graph ################################
data1 = {'Country': ['US','CA','GER','UK','FR'],
         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
        }
df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])

######################################## Graph ################################
root = tk.ThemedTk()
root.get_themes()
root.set_theme("plastik")
root.title("System for Operator Vibration Exposure Prediction")
root.iconbitmap(r'C:/Users/puni3lv/Downloads/Akash/Python/deere.ico')
#root.configure()

border_effects = {
    "flat": tki.FLAT,
    "sunken": tki.SUNKEN,
    "raised": tki.RAISED,
    "groove": tki.GROOVE,
    "ridge": tki.RIDGE,
}

topframe = Frame(root) #,relief = RAISED, borderwidth = 1
topframe.pack(pady =10)
middleframe = Frame(root) #,relief = RAISED, borderwidth = 1
middleframe.pack()
bottomframe = Frame(root, pady = 40) #,relief = RAISED, borderwidth = 1
bottomframe.pack()

############################# GRAPH #######################################
figure1 = plt.Figure(figsize=(4,3), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, bottomframe)
bar1.get_tk_widget().pack(side=tki.RIGHT, fill=tki.BOTH)
df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')
###################################################################
# Creating Text and Link Font
linkFont = font.Font(size=20)

#Creating Link
link = Label(bottomframe, text="Google Hyperlink", fg="blue", cursor="hand2")
link['font'] = linkFont
link.pack(pady = 50)
link.bind("<Button-1>", lambda e: callback("http://www.google.com"))

# Creating Text
text = Label(middleframe, text = "Let's run the program", fg = "green", font = 'Times 14 underline')
text['font'] = linkFont
text.pack()
filelabel = Label(middleframe, text = "Step 1 :- Open MPP Process Data ", relief = GROOVE, bg = "white", fg = "green", font = 'bold')
filelabel.pack(pady = 10)


photo = PhotoImage(file = 'C:/Users/puni3lv/Downloads/Akash/Python GUI/Haptic_GUI/Snap.png')
labelphoto = Label(topframe, image = photo, figsize = (6,3))
labelphoto.pack()

#Creating Menubar
menubar = Menu(root)
root.config(menu = menubar)
    
#Creating Submenubar
submenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = submenu)
submenu.add_command(label = "Open", command = upload_file)
submenu.add_command(label = "Exit")
submenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = submenu)
submenu.add_command(label = "About Algorithm")
submenu.add_command(label = "Exit", command = root.destroy)

# define font
myFont = font.Font(size=13)
#Creating Buttons
theButton0 = tki.Button(bottomframe, text="Upload File", width= 20, height= 3, bg="green", fg="yellow", command = upload_file)
theButton1 = tki.Button(bottomframe, text="Predict Category", width= 20, height= 3, bg="green", fg="yellow", command = run_algorithm)
theButton2 = tki.Button(bottomframe, text="Download", width= 20, height= 3, bg="green", fg="yellow", command = download_file)
# apply font to the button label
theButton0['font'] = myFont
theButton1['font'] = myFont
theButton2['font'] = myFont

theButton0.pack(side = LEFT, padx = 60)
theButton1.pack(side = LEFT, padx = 10)
theButton2.pack(side = RIGHT, padx = 70)
root.minsize(400, 750)

#Creaing Status Bar
status_bar = Label(root, text = "Welcome", relief = SUNKEN, anchor = W, font = 'Times 12 italic')
status_bar.pack(side = BOTTOM, fill = X)
  

root.mainloop()


# Converting .py to .exe
#Run in conda command window
#pip install auto-py-to-exe
#auto-py-to-exe