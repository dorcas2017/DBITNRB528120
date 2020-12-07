from tkinter import *
import os

# with sqlite3.connect("Food_Ordering.db") as db:

'''
WINDOW DECLARATION
'''
root=Tk()
root.geometry("1360x760")
root.title("QuickDel")

'''
BUTTONCLICK
FOR CHOOSING OPTION
RESTAURANT
'''
def r_buttonclick():
    root.destroy()
    os.system('python Restaurant.py')




'''
BUTTON CLICK METHOD
FOR CHOOSING
OPTION CUSTOMER
'''

def c_buttonclick():
    root.destroy()
    os.system('python Customer.py')

'''
BUTTONS WITH
LEFT HAND SIDE RESTAURANT IMAGE
RIGHT HAND SIDE CUSTOMER IMAGE
'''
rest_button = Button()
r_img = PhotoImage(file="Restaurants.gif")
rest_button.config(image=r_img,command=r_buttonclick)
rest_button.image = r_img
rest_button.place(x=0, y=0)

cust_button = Button()

c_img = PhotoImage(file="Customer.gif")
cust_button.config(image=c_img,command=c_buttonclick)
cust_button.image = c_img

cust_button.place(x=680, y=0)


header = Label( text="LOGIN AS:", font=('Verdana', 45), fg="BLUE")
header.place(x=550, y=100)

cust = Label( text="CUSTOMER", font=('Verdana', 30), fg="RED")
cust.place(x=900, y=300)




root.mainloop()
