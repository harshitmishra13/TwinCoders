from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import random
import time
import requests

#Functions
def billing():
    root=Toplevel()
    w=root.winfo_screenwidth()
    h=root.winfo_screenheight()
    root.geometry(f'{w}x{h}')
    root.title("Yum Bites Cafe")
    root.iconbitmap("yumbites.ico")
    bgi=ImageTk.PhotoImage(file='YumBites Blur.png')
    bg = Label(root, image=bgi)
    bg.place(x=0, y=0)
    root.resizable(0,0)
    root.config()

    topFrame=Frame(root,relief=SOLID)
    topFrame.pack(side=TOP)
    labelTitle=Label(topFrame,text='YUM BITES BILLING',font=('franchise-bold',40,'bold'))
    labelTitle.grid(row=0,column=0)

    def reset():
        textReceipt.delete(1.0,END)
        e_americano.set('0')
        e_espresso.set('0')
        e_cafelatte.set('0')
        e_cappuccino.set('0')
        e_caramellatte.set('0')

        e_hazelnutfrappe.set('0')
        e_tiramisufrappe.set('0')
        e_cinnamonfrappe.set('0')

        e_kitkat.set('0')
        e_oreo.set('0')
        e_cookie.set('0')
        e_blackforest.set('0')
        
        e_alootikki.set('0')
        e_paneergrilled.set('0')

        e_cheesyburst.set('0')
        e_onionpizza.set('0')
        e_yumspecial.set('0')
     

        

        textespresso.config(state=DISABLED)
        textamericano.config(state=DISABLED)
        textcafelatte.config(state=DISABLED)
        textcappuccino.config(state=DISABLED)
        textcaramellatte.config(state=DISABLED)

        texthazelnutfrappe.config(state=DISABLED)
        texttiramisufrappe.config(state=DISABLED)
        textcinnamonfrappe.config(state=DISABLED)
        
        textkitkat.config(state=DISABLED)
        textoreo.config(state=DISABLED)
        textcookie.config(state=DISABLED)
        textblackforest.config(state=DISABLED)
        
        textalootikki.config(state=DISABLED)
        textpaneergrilled.config(state=DISABLED)

        textcheesyburst.config(state=DISABLED)
        textonionpizza.config(state=DISABLED)
        textyumspecial.config(state=DISABLED)

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)


        costofdrinksvar.set('')
        costoffoodvar.set('')
        subtotalvar.set('')
        servicetaxvar.set('')
        totalcostvar.set('')

    def save():
        if textReceipt.get(1.0,END)=='\n':
            pass
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
            if url==None:
                pass
            else:

                bill_data=textReceipt.get(1.0,END)
                url.write(bill_data)
                url.close()
                messagebox.showinfo('Information','Your Bill Is Succesfully Saved')

    def receipt():
        global billnumber,date
        if costoffoodvar.get() != '' or costofdrinksvar.get() != '':
            textReceipt.delete(1.0,END)
            x=random.randint(100,10000)
            billnumber='BILL'+str(x)
            date=time.strftime('%d/%m/%Y')
            textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
            textReceipt.insert(END,'***************************************************************\n')
            textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
            textReceipt.insert(END,'***************************************************************\n')

            #hc
            if e_espresso.get()!='0':
                textReceipt.insert(END,f'Espresso\t\t\t{int(e_espresso.get())*70}\n\n')

            if e_americano.get()!='0':
                textReceipt.insert(END,f'Americano\t\t\t{int(e_americano.get())*100}\n\n')

            if e_cappuccino.get()!='0':
                textReceipt.insert(END,f'Cappuccino\t\t\t{int(e_cappuccino.get())*65}\n\n')

            if e_cafelatte.get() != '0':
                textReceipt.insert(END, f'Cafe Latte:\t\t\t{int(e_cafelatte.get()) * 105}\n\n')

            if e_caramellatte.get() != '0':
                textReceipt.insert(END, f'Caramel Latte:\t\t\t{int(e_caramellatte.get()) * 120}\n\n')
            
            #cc
            if e_hazelnutfrappe.get() != '0':
                textReceipt.insert(END, f'Hazelnut Frappe:\t\t\t{int(e_hazelnutfrappe.get()) * 140}\n\n')

            if e_tiramisufrappe.get() != '0':
                textReceipt.insert(END, f'Tiramisu Frappe:\t\t\t{int(e_tiramisufrappe.get()) * 140}\n\n')

            if e_cinnamonfrappe.get() != '0':
                textReceipt.insert(END, f'Cinnamon Frappe:\t\t\t{int(e_cinnamonfrappe.get()) * 150}\n\n')

            
            #ms
            if e_kitkat.get() != '0':
                textReceipt.insert(END, f'Kitkat Shake\t\t\t{int(e_kitkat.get()) * 150}\n\n')

            if e_oreo.get() != '0':
                textReceipt.insert(END, f'Oreo Shake\t\t\t{int(e_oreo.get()) * 150}\n\n')

            if e_cookie.get() != '0':
                textReceipt.insert(END, f'Cream & Cookiee Shake\t\t\t{int(e_cookie.get()) * 170}\n\n')

            if e_blackforest.get() != '0':
                textReceipt.insert(END, f'Black Forest Shake\t\t\t{int(e_blackforest.get()) * 180}\n\n')

            
            #bgr
            if e_alootikki.get() != '0':
                textReceipt.insert(END, f'Aloo Tikki Burger\t\t\t{int(e_alootikki.get()) * 100}\n\n')

            if e_paneergrilled.get() != '0':
                textReceipt.insert(END, f'Paneer Grilled Burger\t\t\t{int(e_paneergrilled.get()) * 140}\n\n')


            #pizza
            if e_cheesyburst.get() != '0':
                textReceipt.insert(END, f'Cheesy Burst Pizza\t\t\t{int(e_cheesyburst.get()) * 150}\n\n')

            if e_onionpizza.get() != '0':
                textReceipt.insert(END, f'Onion Pizza\t\t\t{int(e_onionpizza.get()) * 140}\n\n')

            if e_yumspecial.get() != '0':
                textReceipt.insert(END, f'Yum Special Pizza\t\t\t{int(e_yumspecial.get()) * 190}\n\n')



            textReceipt.insert(END,'***************************************************************\n')
            if costoffoodvar.get()!='0 Rs':
                textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
            if costofdrinksvar.get() != '0 Rs':
                textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')

            textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
            textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
            textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
            textReceipt.insert(END,'***************************************************************\n')

        else:
            messagebox.showerror('Error','No Item Is selected')



    def totalcost():
        global priceofFood,priceofDrinks,priceofCakes,subtotalofItems
        if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0:

            item1=int(e_espresso.get())
            item2=int(e_americano.get())
            item3=int(e_cappuccino.get())
            item4 = int(e_cafelatte.get())
            item5 = int(e_caramellatte.get())

            item6 = int(e_hazelnutfrappe.get())
            item7 = int(e_tiramisufrappe.get())
            item8 = int(e_cinnamonfrappe.get())

            item9 = int(e_kitkat.get())
            item10 = int(e_oreo.get())
            item11 = int(e_cookie.get())
            item12 = int(e_blackforest.get())

            item13 = int(e_alootikki.get())
            item14 = int(e_paneergrilled.get())

            item15 = int(e_cheesyburst.get())
            item16 = int(e_onionpizza.get())
            item17 = int(e_yumspecial.get())



            priceofDrinks=(item1*70)+(item2*100)+(item3*65)+(item4*105)+ (item5*120) + (item6 * 140) + (item7 * 140) \
                        + (item8 * 150) + (item9 * 150) +  (item10*150) + (item11*170)+ (item12 * 180)

            priceofFood= (item13 * 100) + (item14 * 140) + (item15 * 150) + (item16 * 140) + (item17 * 190)


            costoffoodvar.set(str(priceofFood)+ ' Rs')
            costofdrinksvar.set(str(priceofDrinks)+ ' Rs')


            subtotalofItems=priceofFood+priceofDrinks
            subtotalvar.set(str(subtotalofItems)+' Rs')

            servicetaxvar.set('₹50')

            tottalcost=subtotalofItems+50
            totalcostvar.set(str(tottalcost)+' Rs')

        else:
            messagebox.showerror('Select Items','No Item is selected!!')



    def espresso():
        if var1.get()==1:
            textespresso.config(state=NORMAL)
            textespresso.delete(0,END)
            textespresso.focus()
        else:
            textespresso.config(state=DISABLED)
            e_espresso.set('0')

    def americano():
        if var2.get()==1:
            textamericano.config(state=NORMAL)
            textamericano.delete(0,END)
            textamericano.focus()

        else:
            textamericano.config(state=DISABLED)
            e_americano.set('0')

    def cappuccino():
        if var3.get()==1:
            textcappuccino.config(state=NORMAL)
            textcappuccino.delete(0,END)
            textcappuccino.focus()

        else:
            textcappuccino.config(state=DISABLED)
            e_cappuccino.set('0')

    def cafelatte():
        if var4.get() == 1:
            textcafelatte.config(state=NORMAL)
            textcafelatte.focus()
            textcafelatte.delete(0, END)
        elif var4.get() == 0:
            textcafelatte.config(state=DISABLED)
            e_cafelatte.set('0')


    def caramellatte():
        if var5.get() == 1:
            textcaramellatte.config(state=NORMAL)
            textcaramellatte.focus()
            textcaramellatte.delete(0, END)
        elif var5.get() == 0:
            textcaramellatte.config(state=DISABLED)
            e_caramellatte.set('0')


    def hazelnutfrappe():
        if var6.get() == 1:
            texthazelnutfrappe.config(state=NORMAL)
            texthazelnutfrappe.focus()
            texthazelnutfrappe.delete(0, END)
        elif var6.get() == 0:
            texthazelnutfrappe.config(state=DISABLED)
            e_hazelnutfrappe.set('0')


    def tiramisufrappe():
        if var7.get() == 1:
            texttiramisufrappe.config(state=NORMAL)
            texttiramisufrappe.focus()
            texttiramisufrappe.delete(0, END)
        elif var7.get() == 0:
            texttiramisufrappe.config(state=DISABLED)
            e_tiramisufrappe.set('0')


    def cinnamonfrappe():
        if var8.get() == 1:
            textcinnamonfrappe.config(state=NORMAL)
            textcinnamonfrappe.focus()
            textcinnamonfrappe.delete(0, END)
        elif var8.get() == 0:
            textcinnamonfrappe.config(state=DISABLED)
            e_cinnamonfrappe.set('0')


    def kitkat():
        if var9.get() == 1:
            textkitkat.config(state=NORMAL)
            textkitkat.focus()
            textkitkat.delete(0, END)
        elif var9.get() == 0:
            textkitkat.config(state=DISABLED)
            e_kitkat.set('0')


    def oreo():
        if var10.get() == 1:
            textoreo.config(state=NORMAL)
            textoreo.focus()
            textoreo.delete(0, END)
        elif var10.get() == 0:
            textoreo.config(state=DISABLED)
            e_oreo.set('0')


    def cookie():
        if var11.get() == 1:
            textcookie.config(state=NORMAL)
            textcookie.focus()
            textcookie.delete(0, END)
        elif var11.get() == 0:
            textcookie.config(state=DISABLED)
            e_cookie.set('0')


    def blackforest():
        if var12.get() == 1:
            textblackforest.config(state=NORMAL)
            textblackforest.focus()
            textblackforest.delete(0, END)
        elif var12.get() == 0:
            textblackforest.config(state=DISABLED)
            e_blackforest.set('0')


    def alootikki():
        if var13.get() == 1:
            textalootikki.config(state=NORMAL)
            textalootikki.focus()
            textalootikki.delete(0, END)
        elif var13.get() == 0:
            textalootikki.config(state=DISABLED)
            e_alootikki.set('0')


    def paneergrilled():
        if var14.get() == 1:
            textpaneergrilled.config(state=NORMAL)
            textpaneergrilled.focus()
            textpaneergrilled.delete(0, END)
        elif var14.get() == 0:
            textpaneergrilled.config(state=DISABLED)
            e_paneergrilled.set('0')


    def cheesyburst():
        if var15.get() == 1:
            textcheesyburst.config(state=NORMAL)
            textcheesyburst.focus()
            textcheesyburst.delete(0, END)
        elif var15.get() == 0:
            textcheesyburst.config(state=DISABLED)
            e_cheesyburst.set('0')


    def onionpizza():
        if var16.get() == 1:
            textonionpizza.config(state=NORMAL)
            textonionpizza.focus()
            textonionpizza.delete(0, END)
        elif var16.get() == 0:
            textonionpizza.config(state=DISABLED)
            e_onionpizza.set('0')


    def yumspecial():
        if var17.get() == 1:
            textyumspecial.config(state=NORMAL)
            textyumspecial.focus()
            textyumspecial.delete(0, END)
        elif var17.get() == 0:
            textyumspecial.config(state=DISABLED)
            e_yumspecial.set('0')


    #frames

    menuFrame=Frame(root,bd=10,relief=RIDGE,bg='#876445')
    menuFrame.pack(side=LEFT)

    costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='#876445',pady=10)
    costFrame.pack(side=BOTTOM)

    drinksFrame=LabelFrame(menuFrame,text='Coffee and Shakes',font=('arial',19,'bold'),bd=10)
    drinksFrame.pack(side=LEFT)

    foodFrame=LabelFrame(menuFrame,text='Burger and Pizza',font=('arial',19,'bold'),bd=10)
    foodFrame.pack(side=LEFT)


    rightFrame=Frame(root)
    rightFrame.pack(side=RIGHT)

    calculatorFrame=Frame(rightFrame,bd=1)
    calculatorFrame.pack()

    recieptFrame=Frame(rightFrame,bd=2)
    recieptFrame.pack()

    buttonFrame=Frame(rightFrame,bd=2)
    buttonFrame.pack()

    #Variables

    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    var17 = IntVar()


    e_espresso=StringVar()
    e_americano=StringVar()
    e_cappuccino = StringVar()
    e_cafelatte = StringVar()
    e_caramellatte = StringVar()

    e_hazelnutfrappe = StringVar()
    e_tiramisufrappe = StringVar()
    e_cinnamonfrappe = StringVar()

    e_kitkat=StringVar()
    e_oreo=StringVar()
    e_cookie = StringVar()
    e_blackforest = StringVar()

    e_alootikki = StringVar()
    e_paneergrilled = StringVar()

    e_cheesyburst = StringVar()
    e_onionpizza = StringVar()
    e_yumspecial = StringVar()


    costoffoodvar=StringVar()
    costofdrinksvar=StringVar()

    subtotalvar=StringVar()
    servicetaxvar=StringVar()
    totalcostvar=StringVar()

    e_espresso.set('0')
    e_americano.set('0')
    e_cappuccino.set('0')
    e_cafelatte.set('0')
    e_caramellatte.set('0')

    e_hazelnutfrappe.set('0')
    e_tiramisufrappe.set('0')
    e_cinnamonfrappe.set('0')

    e_kitkat.set('0')
    e_oreo.set('0')
    e_cookie.set('0')
    e_blackforest.set('0')

    e_alootikki.set('0')
    e_paneergrilled.set('0')

    e_cheesyburst.set('0')
    e_onionpizza.set('0')
    e_yumspecial.set('0')

    #hc
    espresso=Checkbutton(drinksFrame,text='Espresso',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1
                     ,command=espresso)
    espresso.grid(row=0,column=0,sticky=W)

    americano=Checkbutton(drinksFrame,text='Americano',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2
                     ,command=americano)
    americano.grid(row=1,column=0,sticky=W)

    cappuccino=Checkbutton(drinksFrame,text='Cappuccino',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3
                     ,command=cappuccino)
    cappuccino.grid(row=2,column=0,sticky=W)

    cafelatte=Checkbutton(drinksFrame,text='Cafe Latte',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4
                      ,command=cafelatte)
    cafelatte.grid(row=3,column=0,sticky=W)

    caramellatte=Checkbutton(drinksFrame,text='Caramel Latte',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5
                      ,command=caramellatte)
    caramellatte.grid(row=4,column=0,sticky=W)

    #cc
    hazelnutfrappe=Checkbutton(drinksFrame,text='Hazelnut Frappe',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6
                       ,command=hazelnutfrappe)
    hazelnutfrappe.grid(row=5,column=0,sticky=W)

    tiramisufrappe=Checkbutton(drinksFrame,text='Tiramisu Frappe',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,
                       command=tiramisufrappe)
    tiramisufrappe.grid(row=6,column=0,sticky=W)

    cinnamonfrappe=Checkbutton(drinksFrame,text='Cinnamon Frappe',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8
                       ,command=cinnamonfrappe)
    cinnamonfrappe.grid(row=7,column=0,sticky=W)

    #ms
    kitkat=Checkbutton(drinksFrame,text='KitKat Shake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9
                         ,command=kitkat)
    kitkat.grid(row=8,column=0,sticky=W)

    oreo=Checkbutton(drinksFrame,text='Oreo Shake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10
                      ,command=oreo)
    oreo.grid(row=9,column=0,sticky=W)

    cookie=Checkbutton(drinksFrame,text='Cookie & Cream Skake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11
                       ,command=cookie)
    cookie.grid(row=10,column=0,sticky=W)

    blackforest=Checkbutton(drinksFrame,text='Blackforest Shake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12
                       ,command=blackforest)
    blackforest.grid(row=11,column=0,sticky=W)

    #Entry Fields for Food Items

    textespresso=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_espresso)
    textespresso.grid(row=0,column=1)

    textamericano=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_americano)
    textamericano.grid(row=1,column=1)

    textcappuccino=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cappuccino)
    textcappuccino.grid(row=2,column=1)

    textcafelatte = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cafelatte)
    textcafelatte.grid(row=3, column=1)

    textcaramellatte = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_caramellatte)
    textcaramellatte.grid(row=4, column=1)

    texthazelnutfrappe = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_hazelnutfrappe)
    texthazelnutfrappe.grid(row=5, column=1)

    texttiramisufrappe = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tiramisufrappe)
    texttiramisufrappe.grid(row=6, column=1)

    textcinnamonfrappe = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cinnamonfrappe)
    textcinnamonfrappe.grid(row=7, column=1)

    textkitkat = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkat)
    textkitkat.grid(row=8, column=1)

    textoreo = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
    textoreo.grid(row=9, column=1)

    textcookie = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cookie)
    textcookie.grid(row=10, column=1)

    textblackforest = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_blackforest)
    textblackforest.grid(row=11, column=1)

    #fooditemsburger

    alootikki=Checkbutton(foodFrame,text='Aloo Tikki Burger',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13
                         ,command=alootikki)
    alootikki.grid(row=0,column=0,sticky=W)

    paneergrilled=Checkbutton(foodFrame,text='Paneer Grilled Burger',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14
                         ,command=paneergrilled)
    paneergrilled.grid(row=1,column=0,sticky=W)

    #pizza

    cheesyburst=Checkbutton(foodFrame,text='Cheesy Burst Pizza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15
                          ,command=cheesyburst)
    cheesyburst.grid(row=2,column=0,sticky=W)

    onionpizza=Checkbutton(foodFrame,text='Onion Pizza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16
                          ,command=onionpizza)
    onionpizza.grid(row=3,column=0,sticky=W)

    yumspecial=Checkbutton(foodFrame,text='Yum Special Pizza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17
                           ,command=yumspecial)
    yumspecial.grid(row=4,column=0,sticky=W)

    #entry fields for drink items


    textalootikki = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_alootikki)
    textalootikki.grid(row=0, column=1)

    textpaneergrilled = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_paneergrilled)
    textpaneergrilled.grid(row=1, column=1)

    textcheesyburst = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_cheesyburst)
    textcheesyburst.grid(row=2, column=1)

    textonionpizza = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_onionpizza)
    textonionpizza.grid(row=3, column=1)

    textyumspecial = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_yumspecial)
    textyumspecial.grid(row=4, column=1)



    #costlabels & entry fields

    labelCostofFood=Label(costFrame,text='Cost of Burger and/or Pizza',font=('arial',16,'bold'),bg='#876445',fg='white')
    labelCostofFood.grid(row=0,column=0)

    textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
    textCostofFood.grid(row=0,column=1,padx=41)

    labelCostofDrinks=Label(costFrame,text='Cost of Coffee and/or Milkshakes',font=('arial',16,'bold'),bg='#876445',fg='white')
    labelCostofDrinks.grid(row=1,column=0)

    textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
    textCostofDrinks.grid(row=1,column=1,padx=41)

    labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='#876445',fg='white')
    labelSubTotal.grid(row=0,column=2)

    textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
    textSubTotal.grid(row=0,column=3,padx=41)

    labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='#876445',fg='white')
    labelServiceTax.grid(row=1,column=2)

    textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
    textServiceTax.grid(row=1,column=3,padx=41)

    labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='#876445',fg='white')
    labelTotalCost.grid(row=2,column=2)

    textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
    textTotalCost.grid(row=2,column=3,padx=41)

    #Buttons

    buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='green4',bd=3,padx=5,
                       command=totalcost)
    buttonTotal.grid(row=0,column=0)

    buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='green4',bd=3,padx=5
                         ,command=receipt)
    buttonReceipt.grid(row=0,column=1)

    buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='green4',bd=3,padx=5
                      ,command=save)
    buttonSave.grid(row=0,column=2)

    buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='green4',bd=3,padx=5,
                       command=reset)
    buttonReset.grid(row=0,column=4)

    #textarea for receipt

    textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
    textReceipt.grid(row=0,column=0)

    #Calculator
    operator='' #7+9
    def buttonClick(numbers): #9
        global operator
        operator=operator+numbers
        calculatorField.delete(0,END)
        calculatorField.insert(END,operator)

    def clear():
        global operator
        operator=''
        calculatorField.delete(0,END)

    def answer():
        global operator
        result=str(eval(operator))
        calculatorField.delete(0,END)
        calculatorField.insert(0,result)
        operator=''



    calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
    calculatorField.grid(row=0,column=0,columnspan=4)

    button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),bd=6,width=6,
                   command=lambda:buttonClick('7'))
    button7.grid(row=1,column=0)

    button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),bd=6,width=6,
                   command=lambda:buttonClick('8'))
    button8.grid(row=1,column=1)

    button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),bd=6,width=6
                   ,command=lambda:buttonClick('9'))
    button9.grid(row=1,column=2)

    buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),bd=6,width=6
                      ,command=lambda:buttonClick('+'))
    buttonPlus.grid(row=1,column=3)

    button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),bd=6,width=6
                   ,command=lambda:buttonClick('4'))
    button4.grid(row=2,column=0)

    button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),bd=6,width=6
                   ,command=lambda:buttonClick('5'))
    button5.grid(row=2,column=1)

    button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),bd=6,width=6
                   ,command=lambda:buttonClick('6'))
    button6.grid(row=2,column=2)

    buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),bd=6,width=6
                       ,command=lambda:buttonClick('-'))
    buttonMinus.grid(row=2,column=3)

    button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),bd=6,width=6
                   ,command=lambda:buttonClick('1'))
    button1.grid(row=3,column=0)

    button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),bd=6,width=6
                   ,command=lambda:buttonClick('2'))
    button2.grid(row=3,column=1)

    button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),bd=6,width=6
                   ,command=lambda:buttonClick('3'))
    button3.grid(row=3,column=2)

    buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),bd=6,width=6
                      ,command=lambda:buttonClick('*'))
    buttonMult.grid(row=3,column=3)

    buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),bd=6,width=6,
                     command=answer)
    buttonAns.grid(row=4,column=0)

    buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),bd=6,width=6
                       ,command=clear)
    buttonClear.grid(row=4,column=1)

    button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),bd=6,width=6
                   ,command=lambda:buttonClick('0'))
    button0.grid(row=4,column=2)

    buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),bd=6,width=6,
                     command=lambda:buttonClick('/'))
    buttonDiv.grid(row=4,column=3)

    root.mainloop()
