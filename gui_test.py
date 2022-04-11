#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:33:32 2022

@author: kch34
"""

import tkinter
import tkinter.messagebox as msbox
from tkinter import *
from tkinter.ttk import *
from PIL import Image
from PIL import ImageTk


# adjust window
root=tkinter.Tk()
root.geometry("2000x1600")
img=Image.open("photo1.jpeg")
h = 300
w = 300
img = img.resize((w, h))
img = ImageTk.PhotoImage(img)



b_nuc = tkinter.Button(root,text="Nuclear",width=w,height=h,image=img)
b_en  = tkinter.Button(root,text="energy",width=10,height=10)


b_nuc.place(x=10, y=600)



"""
def helloCallBack():
   msbox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(root, text ="Hello")

B.pack(side="top", anchor="nw")
"""
root.mainloop()