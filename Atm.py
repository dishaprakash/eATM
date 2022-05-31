import tkinter as tk
from tkinter import font
import sqlite3
import time
import datetime

i='id'
pw=''
d=0
def lim():
    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)

    label1=tk.Label(root,text='TRANSACTION LIMIT IS Rs 20,000',font=('Courier New TUR',30),fg='red')
    label1.place(relx=0.25,rely=0.25)

    button1= tk.Button(root,text='BACK',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                      font=('Courier New TUR',20),command = functionality)
    button1.place(relx=0.4,rely=0.65,relheight=0.1, relwidth=0.2)
    
    root.mainloop()
    
def dcheck():
    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)

    label1=tk.Label(root,text='INCORRECT AMOUNT',font=('Courier New TUR',30),fg='red')
    label1.place(relx=0.25,rely=0.25,relwidth=0.5)

    button1= tk.Button(root,text='BACK',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                      font=('Courier New TUR',20),command = functionality)
    button1.place(relx=0.4,rely=0.65,relheight=0.1, relwidth=0.2)
    
    root.mainloop()

def main():
    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)


    labelm = tk.Label(root, text='  Welcome to \n PESU online ATM',font=('Courier New TUR',39))
    labelm.place(relx=0.27,rely=0.2,relheight = 0.2,relwidth=0.47)

    buttonm= tk.Button(root,text='New user',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                       command = lambda : new_user(0,0),font=('Courier New TUR',20))
    buttonm.place(relx=0.2,rely=0.6,relheight=0.1, relwidth=0.2)

    buttonm1= tk.Button(root,text='Existing user',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                        command = lambda: existing_user(1,1),font=('Courier New TUR',20))
    buttonm1.place(relx=0.6,rely=0.6,relheight=0.1, relwidth=0.2)


    root.mainloop()

def ac_t_ac(l):
    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)

    label = tk.Label(root,text='Acc. TRANSFER',font=('Courier New TUR',25))
    label.place(relx=0.38,rely=0.2)

    label1 = tk.Label(root,text='Amount in Rs.',font=('Courier New TUR',20))
    label1.place(relx=0.63,rely=0.4)

    label2 = tk.Label(root,text='Acc. Number of the beneficiary',font=('Courier New TUR',20))
    label2.place(relx=0.1,rely=0.4)    

    entrylmn = tk.Entry(root,font=('Courier New TUR',20))
    entrylmn.place(relx = 0.12,rely=0.5)

    entrypqr = tk.Entry(root,font=('Courier New TUR',20))
    entrypqr.place(relx = 0.57,rely=0.5)

    if l == -1 :
        label1=tk.Label(root,text='That account does not exist',font=('Courier New TUR',15),fg='red')
        label1.place(relx=0.25,rely=0.6,relheight=0.07,relwidth=0.5)
    
    button = tk.Button(root,text='BACK',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                       font=('Courier New TUR',20), command=functionality)
    button.place(relx=0.57,rely=0.69,relheight=0.1, relwidth=0.3)

    button1 = tk.Button(root,text='CONFIRM',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                       font=('Courier New TUR',20), command=lambda:check(entrylmn.get(),entrypqr.get(),l))
    button1.place(relx=0.12,rely=0.69,relheight=0.1, relwidth=0.3)

    root.mainloop()

def check(u,d,l):
    u = 'id'+u
    c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?",[u])
    temp = (c.fetchone())
    if temp[0] == 0:
        return ac_t_ac(-1)
    else :
        return screen(u,d,2)
    
def bal_en():
    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)

    label = tk.Label(root,text='BALANCE ENQUIRY',font=('Courier New TUR',25))
    label.place(relx=0.35,rely=0.2)

    label1 = tk.Label(root,text='Current Balance',font=('Courier New TUR',20))
    label1.place(relx=0.25,rely=0.46)

    c.execute("SELECT balance FROM "+i)
    b=c.fetchall()[-1][0]
    
    label2 = tk.Label(root,text="Rs "+str(b),font=('Courier New TUR',25))
    label2.place(relx=0.65,rely=0.46)

    button1 = tk.Button(root,text='BACK',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                        font=('Courier New TUR',20), command = functionality)
    button1.place(relx=0.35,rely=0.69,relheight=0.1, relwidth=0.3)

    root.mainloop()
    
def state():
    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)

    label = tk.Label(root,text='You last 10 transactions are',font=('Courier New TUR',20))
    label.place(relx=0.15,rely=0.07,relheight=0.1,relwidth=0.7)

    c.execute("SELECT date,value,balance from "+i)
    n=c.fetchall()[::-1]
    f=len(n)
    if f <= 11:
        j=n[:f-1]
    else:
        j=n[0:10]
    j.insert(0,("DATE","TRANSACTION","BALANCE"))
    for o in range(0,len(j)):
        for k in range(0,3):
            l=tk.Label(root,text=j[o][k],font=('Courier New TUR',17))
            l.place(relx=0.23+0.2*k,rely=0.2+0.05*o)

    button = tk.Button(root,text='BACK',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                       font=('Courier New TUR',20), command=functionality)
    button.place(relx=0.3,rely=0.8,relheight=0.1, relwidth=0.4)

    root.mainloop()
    
def screen(u,n,r):
    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)

    if r == 1:
        
        label = tk.Label(root,text='Confirm deposition of Rs. '+n,font=('Courier New TUR',20))
        label.place(relx=0.15,rely=0.1,relheight=0.2,relwidth=0.7)

        button = tk.Button(root,text='CONFIRM',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                       font=('Courier New TUR',20), command=lambda: ins(int(n)) if n.isdigit() else dcheck())
        button.place(relx=0.3,rely=0.49,relheight=0.1, relwidth=0.4)

    elif r == -1:
        label = tk.Label(root,text='Confirm withdrawal of Rs. '+n,font=('Courier New TUR',20))
        label.place(relx=0.15,rely=0.1,relheight=0.2,relwidth=0.7)

        button = tk.Button(root,text='CONFIRM',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                       font=('Courier New TUR',20), command=lambda: ins(int(n)*r) if n.isdigit() else dcheck())
        button.place(relx=0.3,rely=0.49,relheight=0.1, relwidth=0.4)

    elif r == 2:
        label = tk.Label(root,text='Confirm transfer of Rs. '+n,font=('Courier New TUR',20))
        label.place(relx=0.15,rely=0.1,relheight=0.2,relwidth=0.7)

        button = tk.Button(root,text='CONFIRM',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                       font=('Courier New TUR',20), command=lambda: transfer(u,n) if n.isdigit() else dcheck())
        button.place(relx=0.3,rely=0.49,relheight=0.1, relwidth=0.4)

    label1=tk.Label(root,text='After this you will be redircted to the main menu',font=('Courier New TUR',15),fg='red')
    label1.place(relx=0.25,rely=0.65,relheight=0.07,relwidth=0.5)

    root.mainloop()
def transfer(u,n):
    tim = time.time()
    date = str(datetime.datetime.fromtimestamp(tim).strftime('%d/%m/%Y'))
    c.execute("SELECT balance FROM "+i)
    ba=c.fetchall()[-1][0]
    if float(n)<ba:
        if float(n)<=20000:
            c.execute("INSERT INTO "+i+"(date,balance,value,password)VALUES(?,?,?,?)",(date,ba-float(n),(-float(n)),pw))
            c.execute("SELECT password FROM "+u)
            p = c.fetchall()[-1][0]
            c.execute("SELECT balance FROM "+u)
            b=c.fetchall()[-1][0] + float(n)
            c.execute("INSERT INTO "+u+"(date,balance,value,password) VALUES(?,?,?,?)",
                      (date,b,n,p))
            conn.commit()
            return(functionality())
        else:
            return(lim())
    else:
        return(low_bal())
def low_bal():
    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)

    label1=tk.Label(root,text='LOW BALANCE',font=('Courier New TUR',30),fg='red')
    label1.place(relx=0.25,rely=0.25,relwidth=0.5)

    button1= tk.Button(root,text='BACK',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                      font=('Courier New TUR',20),command = functionality)
    button1.place(relx=0.4,rely=0.65,relheight=0.1, relwidth=0.2)
    
    root.mainloop()
    
def tran(q):
    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)

    if q == 1:
        label=tk.Label(root,text="Enter amount to be deposited from eWallet",font=('Courier New TUR',20))
        label.place(relx=0.15,rely=0.1,relheight=0.2,relwidth=0.7)
        button = tk.Button(root,text='CONFIRM',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                       font=('Courier New TUR',20),command = lambda : screen(0,entry.get(),1))
        button.place(relx=0.1,rely=0.69,relheight=0.1, relwidth=0.4)
                     


    elif q == -1:
        label=tk.Label(root,text="Enter amount to be withdrawn into eWallet",font=('Courier New TUR',20))
        label.place(relx=0.15,rely=0.1,relheight=0.2,relwidth=0.7)

    
        button = tk.Button(root,text='CONFIRM',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                       font=('Courier New TUR',20),command = lambda : screen(0,entry.get(),-1))
        button.place(relx=0.1,rely=0.69,relheight=0.1, relwidth=0.4)
    
    entry=tk.Entry(root,font=('Courier New TUR',20)) 
    entry.place(relx=0.35,rely=0.4)

    button1 = tk.Button(root,text='BACK',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                        font=('Courier New TUR',20), command = functionality)
    button1.place(relx=0.6,rely=0.69,relheight=0.1, relwidth=0.3)

    root.mainloop()

    

def functionality():
    
    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)

    label=tk.Label(root,text="Select your desired transaction",font=('Courier New TUR',20))
    label.place(relx=0.15,rely=0.1,relheight=0.2,relwidth=0.7)
    

    button1 = tk.Button(root,text='BALANCE\nENQUIRY',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                        font=('Courier New TUR',20), command = bal_en)
    button1.place(relx=0.05,rely=0.4,relheight=0.1, relwidth=0.4)
    

    button2 = tk.Button(root,text='MINI\nSTATEMENT',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                        font=('Courier New TUR',20),command=state)
    button2.place(relx=0.05,rely=0.55,relheight=0.1, relwidth=0.4)

    

    button3 = tk.Button(root,text='Acc. TO eWALLET\nMONEY WITHDRAWAL',bg = '#444657',activebackground='black',fg='white',activeforeground='white',font=('Courier New TUR',20),
                        command = lambda: tran(-1))
    button3.place(relx=0.55,rely=0.4,relheight=0.1, relwidth=0.4)
    
                                            

    button4 = tk.Button(root,text=' Acc. TO Acc.\nMONEY TRANSFER',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                        font=('Courier New TUR',20),command= lambda : ac_t_ac(0))
    button4.place(relx=0.55,rely=0.55,relheight=0.1, relwidth=0.4)


    button5 = tk.Button(root,text='eWALLET TO Acc\nMONEY TRANSFER',bg = '#444657',activebackground='black',fg='white',activeforeground='white',font=('Courier New TUR',20),
                        command = lambda: tran(1))
    button5.place(relx=0.05,rely=0.7,relheight=0.1, relwidth=0.4)

    button6 = tk.Button(root,text='EXIT',bg = '#444657',activebackground='black',fg='white',activeforeground='white',font=('Courier New TUR',20),
                        command=qui)
    button6.place(relx=0.55,rely=0.7,relheight=0.1, relwidth=0.4)
    
    root.mainloop()
    
def qui():
    c.close()
    conn.close()
    root.destroy()

def new_user(w,z):

    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)

    label=tk.Label(root,text="To start using PES Online ATM\nplease enter your 13 digit account number\nand an appropriate password ",
                   font=('Courier New TUR',20))
    label.place(relx=0.15,rely=0.1,relheight=0.2,relwidth=0.7)

    label1=tk.Label(root,text="Account Number",font=('Courier New TUR',20))
    label1.place(relx=0.17,rely=0.4)

    label2=tk.Label(root,text="Password",font=('Courier New TUR',20))
    label2.place(relx=0.65,rely=0.4)

    
    entry1m = tk.Entry(root,font=('Courier New TUR',20))
    entry1m.place(relx=0.09,rely=0.5,relheight=0.1,relwidth=0.35)

    entry2m = tk.Entry(root,font=('Courier New TUR',20),show='*')
    entry2m.place(relx=0.55,rely=0.5,relheight=0.1,relwidth=0.35)


    if w == 1:
        label1=tk.Label(root,text='That Acc. already exists\nPlease use the existing user option',font=('Courier New TUR',15),fg='red')
        label1.place(relx=0.25,rely=0.65,relheight=0.07,relwidth=0.5)
    elif w == 2:
        label1=tk.Label(root,text='Password cannot be blank',font=('Courier New TUR',15),fg='red')
        label1.place(relx=0.25,rely=0.65,relheight=0.07,relwidth=0.5)
    elif w == 3:
        label1=tk.Label(root,text='The account number needs to be 13 digits',font=('Courier New TUR',15),fg='red')
        label1.place(relx=0.25,rely=0.65,relheight=0.07,relwidth=0.5)


    button= tk.Button(root,text='SUBMIT',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                      font=('Courier New TUR',20),command =lambda: define(entry1m.get(),entry2m.get(),0))
    button.place(relx=0.2,rely=0.75,relheight=0.1, relwidth=0.2)

    button1= tk.Button(root,text='BACK',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                      font=('Courier New TUR',20),command = main)
    button1.place(relx=0.6,rely=0.75,relheight=0.1, relwidth=0.2)

        
    root.mainloop()

def existing_user(w,z):
    background_image = tk.PhotoImage(file = 'yo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(y=-0.3,x=-0.3,relheight=1,relwidth=1)

    label=tk.Label(root,text="Please enter your 13 digit account number\nand password ",
                   font=('Courier New TUR',20))
    label.place(relx=0.15,rely=0.1,relheight=0.2,relwidth=0.7)


    label1=tk.Label(root,text="Account Number",font=('Courier New TUR',20))
    label1.place(relx=0.17,rely=0.4)

    label2=tk.Label(root,text="Password",font=('Courier New TUR',20))
    label2.place(relx=0.65,rely=0.4)

    
    entry1 = tk.Entry(root,font=('Courier New TUR',20))
    entry1.place(relx=0.09,rely=0.5,relheight=0.1,relwidth=0.35)

    entry2 = tk.Entry(root,font=('Courier New TUR',20),show='*')
    entry2.place(relx=0.55,rely=0.5,relheight=0.1,relwidth=0.35)


    button= tk.Button(root,text='SUBMIT',bg = '#444657',activebackground='black',fg='white',activeforeground='white',font=('Courier New TUR',20),
                      command=lambda: define(entry1.get(),entry2.get(),1))
    button.place(relx=0.2,rely=0.75,relheight=0.1, relwidth=0.2)

    button1= tk.Button(root,text='BACK',bg = '#444657',activebackground='black',fg='white',activeforeground='white',
                      font=('Courier New TUR',20),command = main)
    button1.place(relx=0.6,rely=0.75,relheight=0.1, relwidth=0.2)
    
    if w == 2:
        label1=tk.Label(root,text='There is no pre existing account with this number\nPlease use the new user option',font=('Courier New TUR',15),fg='red')
        label1.place(relx=0.25,rely=0.65,relheight=0.07,relwidth=0.5)
    elif w == -1:
        label1=tk.Label(root,text='Please enter the correct password',font=('Courier New TUR',15),fg='red')
        label1.place(relx=0.25,rely=0.65,relheight=0.07,relwidth=0.5)

    root.mainloop()
def ins(a):
    global d
    d=a
    tim = time.time()
    date = str(datetime.datetime.fromtimestamp(tim).strftime('%d/%m/%Y'))
    c.execute("SELECT balance FROM "+i)
    b=c.fetchall()[-1][0]
    if (d<=0 and -d<=b) or d>=0:
        if d<=20000 and -d<=20000:
            b = b + float(d)
            c.execute("INSERT INTO "+i+"(date,balance,value,password) VALUES(?,?,?,?)",
                      (date,b,d,pw))
            conn.commit()
            return(functionality())
        else:
            return(lim())
    else :
        return(low_bal())
def define(u,p,z):
    global i
    global pw
    i='id';pw='';d=0
    i=i+u
    pw=p
    if z == 0 :
        c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?",[i])
        temp = (c.fetchone())
        if temp[0] == 0 and pw != '' and len(i)==15:
            c.execute("CREATE TABLE IF NOT EXISTS "+i+"(date TEXT, balance REAL,value REAL,password TEXT)")
            c.execute("INSERT INTO "+i+"(date,balance,value,password) VALUES(?,?,?,?)",('0',0,0,pw))
            conn.commit()
            return(functionality())
        else:
            if pw == '':
                return(new_user(2,z))
            elif len(i)!=15:
                return(new_user(3,z))
            else: 
                return(new_user(1,z))
    elif z == 1:
        c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?",[i])
        temp = (c.fetchone())
        if temp[0]==0:
            return(existing_user(2,z))
        else:
            c.execute("SELECT password FROM "+i)
            temp = c.fetchall()
            if pw == temp[0][0] :
                return(functionality())
            else :
                return(existing_user(-1,z))
    
root = tk.Tk()
root.title("PESU eATM")
root.iconbitmap("atmicon.ico")

conn = sqlite3.connect('eAtm.db')
c = conn.cursor()

canvas = tk.Canvas(root,height=1800,width=1000)
canvas.pack()

main()

root.mainloop()

