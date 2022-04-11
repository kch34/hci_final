#on ubuntu sudo apt-get install python3-pil python3-pil.imagetk
# import required modules
""""
import tkinter
import tkinter.messagebox as msgbox
top = tkinter.Tk()
def helloCallBack():
   msgbox.showinfo( "Hello Python", "Hello World")
B = tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()
"""
#slideshow
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
  
# adjust window
root=tk.Tk()
root.geometry("800x800")
  
# loading the images
img=ImageTk.PhotoImage(Image.open("photo1.jpeg"))
img2=ImageTk.PhotoImage(Image.open("photo2.jpeg"))
img3=ImageTk.PhotoImage(Image.open("photo3.jpeg"))
  
l=Label()
l.pack()
  
  
# using recursion to slide to next image
x = 1
  
# function to change to next image
def move():
    global x
    if x == 4:
        x = 1
    if x == 1:
        l.config(image=img)
    elif x == 2:
        l.config(image=img2)
    elif x == 3:
        l.config(image=img3)
    x = x+1
    root.after(2000, move)
  
# calling the function
move()
  
  
  
root.mainloop()