from tkinter import *
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
def option1():
    root2 = Tk()
    root2.geometry("2000x2000")
    root2.title("Book the bus")

    Label(root2, text="Online Bus Booking System", bg="grey", fg="red", font="Arial 20 bold").pack(side=TOP, pady=10)
    Label(root2, text="Enter Journey Details", font="Arial 12 bold").pack(side=TOP,pady=10)

    fr = Frame(root2)
    fr.pack()

    Label(fr, text="To", font="Arial 10 bold").grid(row=1, column=0, pady=10)
    to_entry = Entry(fr, font="Arial 10 bold")
    to_entry.grid(row=1, column=1, pady=10)

    Label(fr, text="From", font="Arial 10 bold").grid(row=1, column=2, pady=10)
    from_entry = Entry(fr, font="Arial 10 bold")
    from_entry.grid(row=1, column=3, pady=10)

    Label(fr, text="Journey Date", font="Arial 10 bold").grid(row=1, column=4, pady=10)
    date_entry = Entry(fr, font="Arial 10 bold")
    date_entry.grid(row=1, column=5, pady=10)

    def passenger(name,gender,no_of_seats,phone,age,fare,operator_name,travel_on,boarding_point):
        
        def add_passenger(name,gender,no_of_seats,phone,age,fare,operator_name,travel_on,boarding_point):
            total_amount = int(fare)*int(no_of_seats)
            confirmation = askquestion("Fare Confermation", "Total amount to be paid "+str(total_amount) )
            if confirmation == 'yes':
                cur.execute("INSERT INTO PASSENGER VALUES (?,?,?,?,?,?,?,?,?)",
                            (phone, name, gender, no_of_seats, age, total_amount, operator_name, travel_on, boarding_point))
                con.commit()
                showinfo("Success", "Seat(s) have been booked.")
            else:
                showinfo("Cancelled", "Booking has been cancelled.")
        add_passenger(name,gender,no_of_seats,phone,age,fare,operator_name,travel_on,boarding_point)
            
    def proceed_to_book(fare , operator_name , travel_on , boarding_point):
        Label(root2,text="Fill passenger details to book the bus", bg="grey", fg="red", font="Arial 20 bold").pack(pady=50)
        fr = Frame(root2)
        fr.pack()
        Label(fr,text="Name").grid(row=0,column=0)
        E1=Entry(fr)
        E1.grid(row=0,column=1)

        #Buton dropdown
        Label(fr, text="Gender").grid(row=0,column=2)
        E2=StringVar()
        E2.set("Gender")
        option=["Male","Female","Other"]
        OptionMenu(fr,E2,*option).grid(row=0,column=3)

        Label(fr,text="No of seats").grid(row=0,column=4)
        E3=Entry(fr)
        E3.grid(row=0,column=5)

        Label(fr,text="Mobile").grid(row=0,column=6)
        E4=Entry(fr)
        E4.grid(row=0,column=7)

        Label(fr,text="Age").grid(row=0,column=8)
        E5=Entry(fr)
        E5.grid(row=0,column=9)

        Button(fr,text="Book",command = lambda : passenger(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),fare,operator_name,travel_on,boarding_point)).grid(row=0,column=10)
        
    def show_bus(s1,s2,d):
        check=0
        def date_of_running(operator_ID , operator_NAME , boarding_POINT , bus_ID , bus_TYPE , capacitY , farE , route_ID,r,cnt,num):
            def show_available_bus(operator_NAME , bus_TYPE , seatsavailable , capacitY , farE ,r,cnt ,num,date):
                if seatsavailable == capacitY:
                    Label(fr,text="Bus is full check another bus.").grid(row=2, column=4, pady=20)
                else:
                    c=2
                    if cnt == 0:
                        Label(fr,text="Operator").grid(row=2, column=2, pady=5)
                        Label(fr,text="Bus type").grid(row=2, column=3, pady=5)
                        Label(fr,text="A/C").grid(row=2, column=4, pady=5)
                        Label(fr,text="Fare").grid(row=2, column=5, pady=5)
                        
                    Label(fr,text=operator_NAME).grid(row=r, column=c, pady=5)
                    c=c+1
                    Label(fr,text=bus_TYPE).grid(row=r, column=c, pady=5)
                    c=c+1
                    Label(fr,text=str(seatsavailable)+"/"+str(capacitY)).grid(row=r, column=c, pady=5)
                    c=c+1
                    Label(fr,text=farE).grid(row=r, column=c, pady=5)
                    c=c+1
                    Button(fr,text="Book Bus"+str(num), command=lambda:proceed_to_book(farE ,operator_NAME , date , boarding_POINT)).grid(row=r,column=c)
                    
                   
            if bus_ID == None:
                showinfo("Error","3Bus is not available right now")
            else:
                date=None
                seatsavailable=None
                cur.execute("SELECT * FROM NEW_RUN")
                data = cur.fetchall()
                for i in data:
                    if bus_ID == i[0]:
                        if d==i[1]:
                            date=i[1]
                            seatsavailable=i[2]
                            check=1
                            show_available_bus(operator_NAME , bus_TYPE , seatsavailable , capacitY , farE,r,cnt,num , date)
                if check==0:
                    showinfo("Error","2Bus is not available right now")
                
        def stop_bus(operator_ID , operator_NAME , boarding_POINT,r,cnt,num):
            bus_ID=None
            bus_TYPE=None
            capacitY=None
            farE=None
            route_ID=None
            cur.execute("SELECT * FROM NEW_BUS")
            data = cur.fetchall()
            for i in data:
                if operator_ID == i[4]:
                    bus_ID=i[0]
                    bus_TYPE=i[1]
                    capacitY=i[2]
                    farE=i[3]
                    route_ID=i[5]
                    date_of_running(operator_ID , operator_NAME , boarding_POINT , bus_ID , bus_TYPE , capacitY , farE , route_ID,r,cnt,num)

        def start_station():
            operator_ID = None  
            operator_NAME = None
            boarding_POINT = None
            count = 1
            r=2
            cnt=-1
            num=0
            cur.execute("SELECT * FROM NEW_OPERATOR")
            data = cur.fetchall()
            for i in data:
                if s2 == i[2]:
                    operator_ID=i[0]
                    operator_NAME=i[1]
                    boarding_POINT=i[2]
                    count=0
                    r=r+1
                    cnt=cnt+1
                    num=num+1
                    stop_bus(operator_ID , operator_NAME , boarding_POINT,r,cnt,num)
            if count == 1:
                showinfo("Error","1Bus is not available right now")
        start_station()
    
    Button(fr, text="Show Bus", command=lambda: show_bus(to_entry.get(),from_entry.get(),date_entry.get()), font="Arial 10 bold").grid(row=1, column=6,  pady=10)
    root2.mainloop()
option1()
