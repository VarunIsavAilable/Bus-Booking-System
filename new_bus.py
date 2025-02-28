from tkinter import  *
import sqlite3
from tkinter.messagebox import *
con=sqlite3.connect("Project_Database.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS NEW_OPERATOR (operatorid INT PRIMARY KEY, name VARCHAR(20), address VARCHAR(50),phone INT, email VARCHAR(20))")
cur.execute("CREATE TABLE IF NOT EXISTS NEW_ROUTE (routeid INT PRIMARY KEY  ,  stationname  varchar (20) , stationid int)")
cur.execute("CREATE TABLE IF NOT EXISTS NEW_BUS (busid INT PRIMARY KEY, bustype varchar (10), capacity int , fare int , operatorid int , routeid int)")
cur.execute("CREATE TABLE IF NOT EXISTS NEW_RUN (busid INT PRIMARY KEY  ,  runningdate date , seatsavailable int)")
cur.execute("CREATE TABLE IF NOT EXISTS PASSENGER (phone int primary key , name varchar (20) , gender char (10) , seats int , age int , fare int , operator varchar (20) , travel_on date , boarding_point varchar (20))")
con.commit()

def new_bus():
    root4 = Tk()
    root4.geometry("2000x2000")
    root4.title("Online Bus Booking System")
    Label(root4, text="Online Bus Booking System", bg="grey", fg="red", font="Arial 20 bold").pack(side=TOP, pady=20)
    Label(root4, text="Add Bus Details", font="Arial 17 bold").pack(side=TOP, pady=10)
    fr=Frame(root4)
    fr.pack()
    
    Label(fr, text="Bus ID", font="Arial 11").grid(row=0,column=0)
    E1 = Entry(fr, font="Arial 11")
    E1.grid(row=0,column=1)
    #Buton dropdown
    Label(fr, text="Bus Type", font="Arial 11").grid(row=0,column=2)
    E2=StringVar()
    E2.set("Bus Type")
    option=["AC 2x2","AC 3X2","Non AC 2x2","Non AC 3x2","AC Sleeper 2x1","Non AC Sleeper 2x1"]
    OptionMenu(fr,E2,*option).grid(row=0,column=3)
    
    Label(fr, text="Capacity", font="Arial 11").grid(row=0,column=4)
    E3 = Entry(fr, font="Arial 11")
    E3.grid(row=0,column=5)
    
    Label(fr, text="Fair", font="Arial 11").grid(row=0,column=6)
    E4 = Entry(fr, font="Arial 11")
    E4.grid(row=0,column=7)
    
    Label(fr, text="Operator ID", font="Arial 11").grid(row=0,column=8)
    E5 = Entry(fr, font="Arial 11")
    E5.grid(row=0,column=9)

    Label(fr, text="Route ID", font="Arial 11").grid(row=0,column=10)
    E6 = Entry(fr, font="Arial 11")
    E6.grid(row=0,column=11)
    
    def display_entry_data():
        bus_id = str(E1.get())
        bus_type = str(E2.get())
        capacity = str(E3.get())
        fare = str(E4.get())
        operator_id = str(E5.get())
        route_id = str(E6.get())
        Label(root4, text="Bus ID= "+bus_id).pack()
        Label(root4, text="Bus Type= "+bus_type).pack()
        Label(root4, text="Capacity= "+capacity).pack()
        Label(root4, text="Fare= "+fare).pack()
        Label(root4, text="Operator ID= "+operator_id).pack()
        Label(root4, text="Route ID= "+route_id).pack()

    def add():
        count = 1
        cur.execute("SELECT * FROM NEW_BUS")
        data = cur.fetchall()
        for i in data:
            if int(E1.get()) == i[0]:
                showinfo("Error", "Data already exists")
                count = 0
        if count == 1:
            cur.execute("INSERT INTO NEW_BUS VALUES (?,?,?,?,?,?)", (int(E1.get()), E2.get(), int(E3.get()), int(E4.get()),int( E5.get()), int( E6.get())))
            con.commit()
            showinfo("Good", "Data inserted successfully.")
            display_entry_data()

    def edit(): 
        cur.execute("UPDATE NEW_BUS SET  bustype=?, capacity=?, fare=?, operatorid=?,routeid=? WHERE busid=?", ((E2.get()), int(E3.get()), int(E4.get()), E5.get(), int(E6.get()),int(E1.get())))
        con.commit()
        showinfo("Success", "Data has been edited successfully.")
        display_entry_data()
        
    Button(fr, text="Add", font="Arial 11 bold", bg='green', command=add).grid(row=0,column=12)
    Button(fr, text="Edit", font="Arial 11 bold", bg='green', command=edit).grid(row=0,column=13)
new_bus()
