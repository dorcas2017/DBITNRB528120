from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import os



conn=sqlite3.connect("Food_Ordering.db")
c=conn.cursor()

#CREATES TABLE FOR RESTAURANTS

c.execute("CREATE TABLE IF NOT EXISTS Restaurants(RName TEXT NOT NULL ,Pincode INTEGER NOT NULL,Username TEXT NOT NULL UNIQUE,Password TEXT NOT NULL,Contact TEXT NOT NULL,Address TEXT NOT NULL,Status TEXT DEFAULT 'N',Landmark TEXT,PRIMARY KEY (Pincode,RName,Landmark) )")
c.execute("SELECT * FROM Restaurants")


Rest_reg=Tk()
Rest_reg.geometry("1360x760")
Rest_reg.config(bg='LightCyan2')
Rest_reg.title("Register With Us")


#Rest_name
n=Label(text="Restaurant Name",font=('Times', 20),bg='LightCyan2')
n.place(x=200,y=50)
name=Entry(width=50,font=('Times', 20))
name.place(x=600,y=50)

#Pincode
pc=Label(text="Pincode",font=('Times', 20),bg='LightCyan2')
pc.place(x=200,y=100)
pincode=Entry(width=50,font=('Times', 20))
pincode.place(x=600,y=100)

#user_name
un=Label(text="Username",font=('Times', 20),bg='LightCyan2')
un.place(x=200,y=150)
username=Entry(width=50,font=('Times', 20))
username.place(x=600,y=150)

#PASSWORD LABELS AND ENTRY WITH CONFIRMATION
pw1=Label(text="Password",font=('Times', 20),bg='LightCyan2')
pw1.place(x=200,y=200)
pass1=Entry(width=50,font=('Times', 20),show='*')
pass1.place(x=600,y=200)


pw2=Label(text="Confirm Password",font=('Times', 20),bg='LightCyan2')
pw2.place(x=200,y=250)
pass2=Entry(width=50,font=('Times', 20),show='*')
pass2.place(x=600,y=250)


mob=Label(text="Mobile No",font=('Times', 20),bg='LightCyan2')
mob.place(x=200,y=300)
no=Entry(width=50,font=('Times', 20))
no.place(x=600,y=300)



add=Label(text="Address",font=('Times', 20),bg='LightCyan2')
add.place(x=200,y=350)
address=Entry(width=80,font=('Times', 20))
address.place(x=600,y=350)

lm=Label(text="Landmark",font=('Times', 20),bg='LightCyan2')
lm.place(x=200,y=400)
landmark=Entry(width=80,font=('Times', 20))
landmark.place(x=600,y=400)





#PREVIOUS SCREEN
def back_button():
    Rest_reg.destroy()
    os.system('python Home_Screen.py')

'''
FOR PASSWORD VERIFICATION

'''
def reg_button():
    if len(no.get())!=10:
        ms.showerror("Invalid Mobile No","Please enter a valid no")
    if pass2.get()!=pass1.get():
        ms.showerror(title="Error",message="Passwords do not match")
    else:
        try:
            query=("INSERT INTO Restaurants (RName,Pincode,Landmark,Username,Password,Contact,Address)VALUES (?,?,?,?,?,?,?)")
            c.execute(query,[name.get(),pincode.get(),landmark.get(),username.get(),pass1.get(),no.get(),address.get()])
        except Exception as e:
            ms.showerror("Error",e)
        else:
            ms.showinfo(title="Welcome",message="You are successfully Registered")
            conn.commit()
            conn.close()
            Rest_reg.destroy()
            os.system('python Restaurant.py')



back_button=Button(text="Back",font=('Times',30),bg='IndianRed3',command=back_button)
back_button.place(x=500,y=550)

login_button = Button(text="REGISTER", font=('Times', 30), bg='DarkOliveGreen3',command=reg_button)
login_button.place(x=700, y=550)

Rest_reg.mainloop()
