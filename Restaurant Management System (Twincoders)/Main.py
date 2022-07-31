from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests
from PIL import ImageTk, Image
from tkinter import ttk
from time import strftime
import tkinter.messagebox as Msgbox
import foodmenupy as fmp
import billingpy as bsp
#------------------Window Property----------------------#            

root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry(f'{w}x{h}')
root.title("Yum Bites Cafe")
root.iconbitmap("yumbites.ico")
bgi=ImageTk.PhotoImage(file='YumBites Blur.png')
bg = Label(root, image=bgi)
bg.place(x=0, y=0)
root.overrideredirect(False)
root.config()

foodmenu=ImageTk.PhotoImage(file="foodmenubutton.png")
billing=ImageTk.PhotoImage(file="billingbutton.png")

def time(): 
    string = strftime("%d-%m-%Y / %H:%M:%S") 
    lbl.config(text = string) 
    lbl.after(1000, time) 
lbl=Label(root,font=('arial', 13, "bold"), background = 'White')
lbl.place(relx=1.0,rely=0, anchor ='ne')

time()

lf=LabelFrame(root,bg="white",width=650,height=400,borderwidth=0,relief="solid")
lf.place(relx=0.5,rely=0.5, anchor="center")

head=Label(lf,text="YUM BITES CAFE",font=('franchise bold', 90, 'bold'),anchor="center", bg="white")
head.place(relx=0.5,rely=0.2, anchor="center")

#------Buttons--------#

resmenu=Button(lf,image=foodmenu, command = fmp.foodmenu, text="GR", bg="white", borderwidth="0")
resmenu.place(relx=0.27,rely=0.68, anchor="center")

resbill=Button(lf,image=billing, command=bsp.billing, borderwidth="0", bg="white")
resbill.place(relx=0.73,rely=0.68, anchor="center")

root.mainloop()
