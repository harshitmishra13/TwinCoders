from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests
from PIL import ImageTk, Image
from tkinter import ttk
from time import strftime
import tkinter.messagebox as Msgbox

#------------------Window Property----------------------#            

def foodmenu():
    res=Toplevel()
    res.geometry('650x750')
    res.title("Yum Bites MenuCard")
    res.resizable(False,False)
    res.iconbitmap('yumbites.ico')
    res.config()

    Menu=ImageTk.PhotoImage(file='foodmenufinal.png')
    hmenu=Label(res,image=Menu)
    hmenu.place(relx=0.5,rely=0.5, anchor="center")

    res.mainloop()

    
        
