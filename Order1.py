from tkinter import *
import sqlite3
import uuid
import os
import time
from tkinter import messagebox as ms
from datetime import datetime

#DATABASE CONNECTIVITY

conn=sqlite3.connect("Food_Ordering.db")
c=conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS Orders(Phone_No TEXT NOT NULL,CName TEXT NOT NULL,RName TEXT NOT NULL,Ordered_Items,Ordered_Quantities,Order_Date TEXT,Order_Time TEXT,Bill FLOAT NOT NULL,Pincode TEXT NOT NULL,PRIMARY KEY(Phone_No,Order_Date,Order_Time))")

Order=Tk()
Order.geometry("1400x760")
Order.config(bg='powderblue')
Order.title("Order Your Meal")

def back():
    Order.destroy()
    os.system('python CMenu.py')
#Select a Hotel
global select1
rests=[]
pc=Label(text="Enter Pincode",font=("Times",20),bg="powderblue")
pc.place(x=200,y=50)
pin=Entry(font=("Times",20))
pin.place(x=400,y=50)

def log_out():
    id = c.execute("SELECT Phone_No FROM Customer WHERE STATUS = 'Y'")
    for row in id:
        pass
    j = row[0]
    q = "UPDATE Customer SET Status = 'N' where Phone_No= ?";
    c.execute(q, [j])
    conn.commit()
    conn.close()
    Order.destroy()
    os.system('python home_screen.py')

logout=Button(text="Log Out",font=('Times',25),command=log_out)
logout.place(x=1100,y=0)
#Drop-down with hotels
def show_hotels():
    try:
        q="SELECT RName FROM Restaurants WHERE Pincode=?"
        re=c.execute(q,[pin.get()])
        for i in re:
            rests.extend(i)
        global hotel
        hotel=StringVar(Order)
        hotel.set("Select")
        select_hotel=Label(text="Select Restaurant",font=("Times",20),bg="powderblue")
        select_hotel.place(x=200,y=120)
        hotels=OptionMenu(Order,hotel,*rests)
        hotels.config(font=('Times',15))
        hotels.place(x=500,y=120)
    except Exception as e:
        ms.showerror("Error","We dont serve in your area")
    else:
        select1=Button(text="SELECT",font=("Times",15),state=ACTIVE,command=Select_Food)
        select1.place(x=750,y=120)

#Enter Pincode
enter_code=Button(text="View Hotels",command=show_hotels,font=("Times",15))
enter_code.place(x=750,y=50)

#selecting food (1st item)
def Select_Food():
    global food
    global price
    global comb
    q="SELECT Username FROM Restaurants WHERE RName=? and Pincode=?"
    a=c.execute(q,[hotel.get(),pin.get()])
    for i in a:
        pass
    un=i[0]
    food=[]
    price=[]
    q1="SELECT Item FROM Menu WHERE Username=?"
    a=c.execute(q1,[un])
    for i in a:
        food.extend(i)
    q2="SELECT Cost FROM Menu WHERE Username=?"
    b=c.execute(q2,[un])
    for j in b:
        price.extend(j)
    no=len(food)
    comb=[]
    for i in range(no):
        comb.append([food[i],price[i]])
    select_food=Label(text="Select Food",font=("Times",30),bg="powderblue")
    select_food.place(x=200,y=200)
    global dish
    dish=StringVar(Order)
    dish.set("Select Food")

    food_option=OptionMenu(Order,dish,*comb)
    food_option.config(font=('Times',20))
    food_option.place(x=500,y=200)
    qty=Label(text="Select Quantity",font=("Times",25),bg="powderblue")
    qty.place(x=200,y=300)
    global qt
    qt=Spinbox(Order,values=(1,2,3,4,5),font=("Times",20),width=15)
    qt.pack()
    qt.place(x=500,y=300)
    add_to_cart=Button(text="Add To Cart",font=("Times",25),command=cart)
    add_to_cart.place(x=750,y=200)

ordered_food=[]
ordered_price=[]
ordered_qty=[]
bill=[]

# Labels for cart table in window
Items=Label(text="Items",font=("Times",20),bg="powderblue")
Items.place(x=400,y=350)
co=Label(text="Cost",font=("Times",20),bg="powderblue")
co.place(x=575,y=350)
quant=Label(text="Quantity",font=("Times",20),bg="powderblue")
quant.place(x=700,y=350)
st=Label(text="Subtotal",font=("Times",20),bg="powderblue")
st.place(x=850,y=350)
ca=Label(text="CART",font=("Times",40),bg="powderblue")
ca.place(x=100,y=450)

#Cart-Shows details of Ordered Items
m=Listbox(Order,width=50,font=('Arial',20),justify="center",selectmode=SINGLE)
m.place(x=300,y=400)

#Adds selected food Item to Cart
def cart():
    d=dish.get()
    a=d.split("'")
    fpos=food.index(a[1])
    ordered_food.append(food[fpos])
    x=price[fpos]
    ordered_price.append(x)
    ordered_qty.append(qt.get())
    m1=ordered_food[-1]
    m2=str(ordered_price[-1])
    m3=str(ordered_qty[-1])
    l1=len(ordered_food[-1])
    l2=len(str(ordered_price[-1]))
    # Amount of selected item
    x=int(m2)*int(m3)
    #Total Bill
    total=0
    bill.append(x)
    for i in bill:
        total=total+i
    b=Label(text="Total Bill:Rs."+str(total),font=("Times",35),bg="powderblue")
    b.place(x=1070,y=600)
    m.insert(END,m1+((20-l1)*" ")+m2+((10-l2)*" ")+m3+(20*" ")+str(x))
    #Removing ordered food item from drop down
    del(food[fpos])
    del(price[fpos])
    del(comb[fpos])
    placed=0
    def place_order():
        details=[]
        query="SELECT Phone_No,CName from Customer WHERE Status='Y'"
        pn=c.execute(query)
        for i in pn:
            details.extend(i)
        rn=hotel.get()
        now=datetime.now()
        d=now.date()
        t=now.time()
        th=str(t.hour)
        tm=str(t.minute)
        time=th+":"+tm

        of=""
        oq=""
        for i in ordered_food:
            of=of+i+","
        for j in ordered_qty:
            oq=oq+j+","
        try:
            query="INSERT INTO Orders(Order_Date,Order_Time,CName,RName,Ordered_Items,Ordered_Quantities,Bill,Phone_No,Pincode) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(query,[str(d),time,details[1],rn,of,oq,total,details[0],pin.get()])
        except Exception as e:
            ms.showerror("Error",e)
        else:
            conn.commit()
            ms.showinfo("Success","Your Order has been succesfully placed")

    Checkout=Button(text="Place Order",font=("Times",35),command=place_order)
    Checkout.place(x=1070,y=400)
    if len(comb)>0:
        d=StringVar(Order)
        d.set("Select Food")
        food_option1=OptionMenu(Order,dish,*comb)
        food_option1.config(font=('Times',20))
        food_option1.place(x=500,y=200)

    else:
        ms.showinfo("Out of Limit","You ordered every item")
back_button=Button(text="Back",font=('Times',20),bg="red",command=back)
back_button.place(x=50,y=0)


Order.mainloop()
