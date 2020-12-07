import os
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
conn=sqlite3.connect("Food_Ordering.db")
c=conn.cursor()
'''
RESTAURANT WINDOW
'''
Restaurant=Tk()
Restaurant.geometry("1360x760")
Restaurant.title("Restaurant Home Page")

'''
SETS BACKGROUND IMAGE
'''
bckground_label = Label(height=1000, width=1900)
image1 = PhotoImage(file="Rest.gif")
bckground_label.config(image=image1)
bckground_label.image = image1
bckground_label.place(x=0, y=0)
bckground_label.pack()


'''
GOES TO PREVIOUS
'''

def back_button():
    Restaurant.destroy()
    os.system('python Home_Screen.py')



'''
NEW USER
'''
def new_user():
    Restaurant.destroy()
    os.system('python Rest_reg.py')


back_button=Button(text="Back",font=('Times',30),bg='red',command=back_button)
back_button.place(x=250,y=500)



register_button = Button(text="New User? Register Here!", font=('Times', 30),command=new_user)
register_button.place(x=600, y=500)

UN = Label(text="Username", font=('Times', 40))
UN.place(x=250, y=200)
pw = Label(text="Password", font=('Times', 40))
pw.place(x=250, y=300)


un = Entry(fg='black', bg='white', font=('Times', 40))
un.place(x=600, y=200)
password = Entry(fg='black', bg='white', font=('Times', 40), show="*")
password.place(x=600, y=300)



'''
FOR EXISTING USER
'''
def sign_in():
    try:
        query="SELECT * FROM Restaurants WHERE Username=? AND Password=?"
        c.execute(query,[un.get(),password.get()])
    except Exception as e:
        ms.showerror("Error",e)
    else:
        results=c.fetchall()
        if results:
            q="UPDATE Restaurants SET Status = 'Y' where Username = ?";
            c.execute(q,[un.get()])
            ms.showinfo(title="STATUS",message="YOU ARE SUCCESSFULLY LOGGED IN")
            conn.commit()
            conn.close()
            Restaurant.destroy()
            os.system("python RMenu.py")


        else:
            ms.showerror(title="LOGIN ERROR",message="Invalid username or password")

login_button = Button(text="Sign In", font=('Times', 30), bg='green',command=sign_in)
login_button.place(x=400, y=500)

Restaurant.mainloop()
