import os
from tkinter import *
from tkinter import messagebox as ms
import sqlite3

'''
CONNECTION TO DATABASE
'''
conn=sqlite3.connect("Food_Ordering.db")
c=conn.cursor()

'''
WILL CREATE TABLE WITH RESTAURANT REGISTRATION ID ITS NAME
ALONGWITH COST AND NAME OF PRODUCT
'''

c.execute("CREATE TABLE IF NOT EXISTS Menu(Username TEXT NOT NULL, RName TEXT NOT NULL,ITEM TEXT NOT NULL, COST INTEGER NOT NULL,PRIMARY KEY(RName,ITEM) );")
c.execute("SELECT * FROM Menu")


'''
THIS WINDOW WILL HELP RESTAURANT TO ADD UPDATE AND DELETE MENU ITEMS
'''
menu=Tk()
menu.geometry("1360x760")
menu.config(bg='DeepSkyBlue4')


'''
THROUGH ADD ITEM THE LOGGED IN RESTAURANT CAN ADD NEW ITEMS
THESE ITEMS ARE ADDED INTO THE MENU TABLE AS NEW DISHES

'''

def add_item() :
    #insert item and cost into db
    def insert():
        try:
            query=("INSERT INTO Menu (Username,RName,ITEM,COST)VALUES (?,?,?,?)")
            conn.execute(query,[j,k,item.get(),int(price.get())])
        except Exception as e:
            ms.showerror("Error",e)
        else:
            conn.commit()
            ms.showinfo(title="STATUS",message="ITEM ADDED")
    #sets labels and textboxes
    id = conn.execute("SELECT Username,RName FROM Restaurants WHERE STATUS = 'Y'")
    for row in id:
        pass
    j=row[0]
    k=row[1]
    print(k)
    i = Label(text = 'Item Name', font =('Times',20))
    i.place(x=500,y=100)
    item = Entry(font =('Times',20))
    item.place(x=650,y=100)
    p = Label(text = 'Price', font =('Times',20))
    p.place(x=500,y=150)
    price = Entry(font = ('Times',20))
    price.place(x=650,y=150)
    ai = Button(text = "Add", font = ('Times',20),command = insert)
    ai.place(x=700,y=220)







'''
THE ITEMS AVAILABLE IN THE RESTAURANT ARE RETRIEVED VIA DROPDOWN MENU
AFTER THE ITEM SELECTION,NEW PRICE IS SET TO UPDATE EXISTING PRICE
'''
def update_cost() :
    #Updates cost of item
    def ucost():
        b=[]
        b.extend(option.get().split("'"))
        print(b)
        conn.execute("UPDATE Menu set COST=? WHERE ITEM=?",[int(price.get()),b[1]])
        conn.commit()
        ms.showinfo(title="STATUS",message="ITEM PRICE UPDATED")
    #sets gui
    id = conn.execute("SELECT Username FROM Restaurants WHERE STATUS = 'Y'")
    for row in id:
        pass
    j=row[0]
    i = Label(text = 'Item Name', font =('Times',20))
    i.place(x=500,y=100)
    itlist = []
    query = "SELECT ITEM FROM Menu WHERE Username=?"
    q = c.execute(query,[j])
    for item in q:
        itlist.append(item)
    option = StringVar(menu)
    option.set(itlist[0])
    w= OptionMenu(menu,option,*itlist)
    w.config(font=("Times",25))
    w.place(x=650,y=100)
    p = Label(text = 'New Price', font =('Times',20))
    p.place(x=500,y=150)
    price = Entry(font = ('Times',20))
    price.place(x=650,y=150)
    ai = Button(text = "Update", font = ('Times',20),command = ucost)
    ai.place(x=700,y=220)





'''
DELETES AN ITEM

'''
def del_item() :
    def delete():
        b=[]
        b.extend(option.get().split("'"))
        conn.execute("DELETE FROM Menu WHERE Username=? AND ITEM=?",[j,b[1]])
        conn.commit()
        ms.showinfo(title="STATUS",message="ITEM DELETED")
    id = conn.execute("SELECT Username FROM Restaurants WHERE STATUS = 'Y'")
    for row in id:
        pass
    j=row[0]
    i = Label(text = 'Item Name', font =('Times',20))
    i.place(x=500,y=100)
    itlist = []
    query = "SELECT ITEM FROM Menu WHERE Username=?"
    q = c.execute(query,[j])
    for item in q:
        itlist.append(item)
    option = StringVar(menu)
    option.set(itlist[0])
    w= OptionMenu(menu,option,*itlist)
    w.config(font=("Times",30))
    w.place(x=650,y=100)
    ai = Button(text = "Delete", font = ('Times',20),command = delete)
    ai.place(x=700,y=220)






'''
LOGS OUT USER

'''
def log_out():
    id = conn.execute("SELECT Username FROM Restaurants WHERE STATUS = 'Y'")
    for row in id:
        pass
    j=row[0]
    q="UPDATE Restaurants SET Status = 'N' where Username = ?"
    c.execute(q,[j])
    conn.commit()
    ms.showinfo(title="STATUS",message="Logged Out Successfully!!")
    menu.destroy()
    os.system('python home_screen.py')


'''
BUTTONS AND WIDGETS
'''

add = Button(text = "Add Item",font = ('Times',20),command = add_item)
add.place(x = 100, y =100)

update = Button(text = "Update Item Cost",font = ('Times',20),command = update_cost)
update.place(x = 100, y =200)

delete = Button(text = "Delete Item",font = ('Times',20),command = del_item)
delete.place(x = 100, y =300)

logout = Button(text = "Log Out",font = ('Times',20),command = log_out)
logout.place(x = 100, y =500)






menu.mainloop()
