import os
from tkinter import *
import sqlite3
import sqlite3
from tkinter import messagebox as ms

conn=sqlite3.connect("Food_Ordering.db")
c=conn.cursor()
'''
DECLARATION OF
CUSTOMER WINDOW
'''


Customer=Tk()
Customer.geometry("1360x760")
Customer.title("Login")

'''
BACKGROUND IMAGE SET
'''


bckground_label = Label(height=1000, width=1900)
image1 = PhotoImage(file="C.gif")
bckground_label.config(image=image1)
bckground_label.image = image1
bckground_label.place(x=0, y=0)
bckground_label.pack()
'''
WHEN BACK BUTTON CLICKED,
GOES TO PREVIOUS WINDOW
'''

def back_button():
    Customer.destroy()
    os.system('python Home_Screen.py')


'''
WHEN CLICKED NEW USER
CAN BE REGISTERED
'''

def new_user():
    Customer.destroy()
    os.system('python Cust_reg.py')

'''
RESPECTIVE BUTTON WIDGETS
ALONG WITH ENTRY FIELDS
'''

back_button=Button(text="Back",font=('Times',20),bg='red',command=back_button)
back_button.place(x=350,y=500)


register_button = Button(text="New User? Register Here!", font=('Times', 20),command=new_user)
register_button.place(x=700, y=500)


mob = Label(text="MOBILE NO", font=('Times', 40))
mob.place(x=250, y=200)
pw = Label(text="PASSWORD", font=('Times', 40))
pw.place(x=250, y=300)


mobile_no = Entry(fg='black', bg='white', font=('Times', 40))
mobile_no.place(x=600, y=200)
password = Entry(fg='black', bg='white', font=('Times', 40), show="*")
password.place(x=600, y=300)

'''
EXISTING USER CAN SIGN IN WITH DETAILS
DATA VALIDATION IS PERFORMED FROM DATABASE
AND ACCESS IS GRANTED
'''


def sign_in():
    query="SELECT * FROM Customer WHERE Phone_No=? AND Password=?"
    c.execute(query,[mobile_no.get(),password.get()])
    results=c.fetchall()

    if results:
        ms.showinfo(title="STATUS", message="YOU ARE SUCCESSFULLY LOGGED IN")
        q = "UPDATE Customer SET Status = 'Y' where Phone_No = ?";
        c.execute(q, [mobile_no.get()])
        conn.commit()
        Customer.destroy()
        os.system("python CMenu.py")

    else:
        ms.showerror(title="LOGIN ERROR",message="Invalid username or password")

login_button =Button(text="Sign In", font=('Times', 20), bg='green',command=sign_in)
login_button.place(x=500, y=500)

Customer.mainloop()
