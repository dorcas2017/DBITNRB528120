from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import os



'''
DATABASE CONNECTION
'''

conn=sqlite3.connect("Food_Ordering.db")
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Customer(Phone_No TEXT NOT NULL PRIMARY KEY,CName TEXT NOT NULL ,Password TEXT NOT NULL,Address TEXT NOT NULL,Status TEXT DEFAULT 'N' );")
c.execute("SELECT * FROM Restaurants")

Rest_reg=Tk()
Rest_reg.geometry("1360x760")
Rest_reg.config(bg="LightCyan2")
Rest_reg.title("Register With Us")

'''
Regid text box and label
'''
mob=Label(text="Mobile No",font=('Times', 20),bg='LightCyan2')
mob.place(x=200,y=100)
mobno=Entry(width=50,font=('Times', 20))
mobno.place(x=600,y=100)

'''
CUST_name LABELS
WITH TEXT ENTRIES

'''
cn=Label(text="Name",font=('Times', 20),bg='LightCyan2')
cn.place(x=200,y=200)
name=Entry(width=50,font=('Times', 20))
name.place(x=600,y=200)

pw1=Label(text="Password",font=('Times', 20),bg='LightCyan2')
pw1.place(x=200,y=300)
pass1=Entry(width=50,font=('Times', 20),show="*")
pass1.place(x=600,y=300)


pw2=Label(text="Confirm Password",font=('Times', 20),bg='LightCyan2')
pw2.place(x=200,y=400)
pass2=Entry(width=50,font=('Times', 20),show="*")
pass2.place(x=600,y=400)


add=Label(text="Address",font=('Times', 20),bg='LightCyan2')
add.place(x=200,y=500)
address=Entry(width=50,font=('Times', 20))
address.place(x=600,y=500)

'''
Mobile Number Validation
'''

def valid(no):
    l = str(no)
    le = len(l)+3
    if le != 10 :
        print(le)
        ms.showerror(title="Error", message="Invalid Mobile Number")
    else :
        return

'''
PREVIOUS SCREEN
'''

def back_button():
    Rest_reg.destroy()
    os.system('python Home_Screen.py')


'''
PASSWORD AND CONFIRM PASSWORD

'''

def reg_button():
    valid(mobno)
    if pass2.get()!=pass1.get():
        ms.showerror(title="Error", message="Passwords do not match")
    else:
        query=("INSERT INTO Customer (Phone_No,CName,Password,Address)VALUES (?,?,?,?)")
        ms.showinfo(title="Registered",message="You are registered")
        c.execute(query,[mobno.get(),name.get(),pass1.get(),address.get()])
        conn.commit()
        Rest_reg.destroy()
        os.system('python Customer.py')



back_button=Button(text="Back",font=('Times',20),bg='IndianRed3',command=back_button)
back_button.place(x=500,y=600)

login_button = Button(text="REGISTER", font=('Times', 20), bg='DarkOliveGreen3',command=reg_button)
login_button.place(x=700, y=600)

Rest_reg.mainloop()
