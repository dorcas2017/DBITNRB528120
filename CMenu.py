from tkinter import *
import sqlite3
import os
conn=sqlite3.connect("Food_Ordering.db")
c=conn.cursor()


'''

GOES TO WINDOW WHERE FOOD ORDER OPTIONS ARE PROVIDED
'''
def order_food():
    CMenu.destroy()
    os.system('python Order1.py')
'''

'''

def view_menu():
    CMenu.destroy()
    Root=Tk()
    Root.geometry("1360x760")
    def back():
        Root.destroy()
        os.system('python CMenu.py')
    hotel_names=[]
    address=[]
    q="SELECT RName,Address FROM Restaurants"
    hotels=c.execute(q)
    for i in hotels:
        hotel_names.append(i[0])
        address.append(i[1])
    print(hotel_names)
    print(address)
    l=len(hotel_names)
    comb=[]
    for i in range(l):
        comb.append([hotel_names[i],address[i]])
    print(comb)
    f1 = StringVar(Root)
    f1.set("Restaurant/Address")
    hotels = OptionMenu(Root, f1, *comb)
    hotels.config(font=('Times', 15))
    hotels.place(x=400, y=150)

    def show_menu():
        h=f1.get()
        print(h)
        Item=Label(text="Item Name",font=('Times',15))
        Item.place(x=300,y=230)
        Qty=Label(text="Price",font=('Times',15))
        Qty.place(x=400,y=230)
        food = []
        cost = []
        comb=[]
        foods=[]
        costs=[]
        q = "SELECT ITEM FROM Menu WHERE RName=?"
        print("Before splitting:",f1.get())
        ab=(f1.get().split("'"))
        print("After splitting",ab)
        print(ab[1])

        items = c.execute(q, [(str)(ab[1])])


        for i in items:
             food.extend(i)
        q = "SELECT COST FROM Menu WHERE RName=?"
        items = c.execute(q, [(str)(ab[1])])
        for i in items:
            cost.extend(i)
        l=len(food)
        for i in range(l):
            comb.append([food[i],cost[i]])
        print(food)
        print(comb)
        menus=[]
        for i in range(l):
            menus.append([food[i],cost[i]])
        print(menus)
        m=Listbox(Root,width=50,font=('Arial',20))
        m.place(x=300,y=300)
        for i in menus:
            m.insert(END,i)





    Select=Button(text="View Menu",font=('Times',30),command=show_menu)
    Select.place(x=700,y=150)
    Select=Button(text="Back",font=('Times',30),command=back)
    Select.place(x=100,y=150)
    Root.mainloop()

'''
WHEN USER IS LOGGED IN, HIS STATUS IS MARKED AS 'Y'
WHEN LOGGING OUT,HIS STATUS IS 'N'
'''

def log_out():
    id = c.execute("SELECT Phone_No FROM Customer WHERE STATUS = 'Y'")
    for row in id:
        pass
    j = row[0]
    q = "UPDATE Customer SET Status = 'N' where Phone_No= ?";
    c.execute(q, [j])
    conn.commit()
    CMenu.destroy()
    os.system('python home_screen.py')

CMenu=Tk()
CMenu.geometry("1360x760")
CMenu.config(bg='DeepSkyBlue4')

def view_order():
    CMenu.destroy()
    q1="SELECT Phone_No FROM Customer WHERE Status='Y'"
    p=c.execute(q1)
    for i in p:
        pass
    pn=i[0]
    q2="SELECT RName,Order_Date,Order_Time,Ordered_Items,Ordered_Quantities,Bill FROM Orders WHERE Phone_No=?"
    details=c.execute(q2,[pn])
    Root=Tk()
    Root.geometry("1300x760")
    lab=Label(text="Restaurant Name\t Date\tTime\t\tOrdered Items\t\t\tQuantity\t\tBill",font=("Arial",15))
    lab.place(x=100,y=0)
    m=Listbox(Root,width=70,font=("Arial",20))
    m.place(x=100,y=100)

    order=[]
    for i in details:
        order.append(i)
    for i in order:
        m.insert(END,i)
    def back_button():
        Root.destroy()
        os.system('CMenu.py')
    back_button=Button(text="Back",font=('Times',20),bg='red',command=back_button)
    back_button.place(x=350,y=500)
    Root.mainloop()


order=Button(text="Order Food",font=('Times',30),command=order_food)
order.place(x=200,y=100)

logout=Button(text="Log Out",font=('Times',30),command=log_out)
logout.place(x=500,y=300)

View_menu=Button(text="View Restaurant Menu",font=('Times',30),command=view_menu)
View_menu.place(x=500,y=100)

View_orders=Button(text="View Orders",font=('Times',30),command=view_order)
View_orders.place(x=200,y=300)



CMenu.mainloop()
