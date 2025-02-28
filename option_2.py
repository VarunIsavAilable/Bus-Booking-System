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

def option2():
    root5=Tk()
    root5.geometry("2000x2000")
    root5.title("Check bookings")
    Label(root5, text="Online Bus Booking System", bg="grey", fg="red", font="Arial 20 bold").pack(side=TOP, pady=20)
    Label(root5, text="Check Your Booking", bg="grey", fg="red", font="Arial 16 bold").pack(side=TOP, pady=20)
    fr=Frame(root5)
    fr.pack()
    Label(fr,text="Enter your mobile no : ",font="Arial 16 bold").grid(row=0,column=0)
    E=Entry(fr)
    E.grid(row=0,column=1)
    def check_booked_bus(ph):
        fr2=Frame(root5,bd=5,relief=SUNKEN)
        fr2.pack()
        cur.execute("SELECT * FROM PASSENGER WHERE phone=?", (ph,))
        data = cur.fetchall()
        for i in data:
            Label(fr2,text="Name :").grid(row=0,column=0)
            Label(fr2,text=i[1]).grid(row=0,column=1)
               
            Label(fr2,text="Gender :").grid(row=0,column=3)
            Label(fr2,text=i[2]).grid(row=0,column=4)
               
            Label(fr2,text="Phone :").grid(row=1,column=0)
            Label(fr2,text=i[0]).grid(row=1,column=1)
               
            Label(fr2,text="Seats :").grid(row=1,column=3)
            Label(fr2,text=i[3]).grid(row=1,column=4)
               
            Label(fr2,text="Age  :").grid(row=2,column=0)
            Label(fr2,text=i[4]).grid(row=2,column=1)
               
            Label(fr2,text="Fare Rs :").grid(row=2,column=3)
            Label(fr2,text=i[5]).grid(row=2,column=4)
               
            Label(fr2,text="Operator :").grid(row=3,column=0)
            Label(fr2,text=i[6]).grid(row=3,column=1)
               
            Label(fr2,text="Travel On :").grid(row=3,column=3)
            Label(fr2,text=i[7]).grid(row=3,column=4)
               
            Label(fr2,text="Boarding Point :").grid(row=4,column=0)
            Label(fr2,text=i[8]).grid(row=4,column=1)
               
            Label(fr2,text="Total amount is :").grid(row=5,column=0)
            Label(fr2,text=i[5]).grid(row=5,column=1)
               
            
    Button(fr,text="Check Booked Bus",command=lambda :check_booked_bus(E.get())).grid(row=0,column=2)
    root5.mainloop()
option2()
