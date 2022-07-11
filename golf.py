#golf app
import imp
from tkinter import *

from cProfile import label
import tkinter as tk
from tkinter import font
from turtle import width
#create window for input

#### MAIN ####
root = tk.Tk()
root.title('My Golf App')
root.geometry('600x600+50+50')
root.configure(background="#426851")



#create numberbox for input

current_value = tk.StringVar()
spin_box = tk.Spinbox(root, from_=0, to=500, textvariable=current_value, wrap=True)
spin_box.pack()



def spin():
    my_label = Label(root, text=spin_box.get()).pack()

my_btn = Button(root, text="which club", command=spin).pack()

#get the range of club distance
dist = 30
if (dist > 211):
    print("Driver")
elif (dist > 196) and (dist < 210):
    print("3 Wood")
elif (dist > 181) and (dist < 195):
    print("5 Wood")
elif (dist > 171) and (dist < 180):
    print("Hybrid")
elif (dist > 161) and (dist < 170):
    print("3 Iron")
elif (dist > 156) and (dist < 160):
    print("4 Iron")
elif (dist > 146) and (dist < 155):
    print("5 Iron")
elif (dist > 141) and (dist < 145):
    print("6 Iron")
elif (dist > 131) and (dist < 140):
    print("7 Iron")
elif (dist > 116) and (dist < 130):
    print("8 Iron")
elif (dist > 101) and (dist < 115):
    print("9 Iron")
elif (dist > 91) and (dist < 100):
    print("Pitching Wedge")
elif (dist > 81) and (dist < 90):
    print("Gap Wedge")
elif (dist > 61) and (dist < 80):
    print("Sand Wedge")
elif (dist >= 40) and (dist < 60):
    print("Lob Wedge")
else:
    print("looks like you'll be putting...")

#### RUN MAIN ####
root.mainloop()

