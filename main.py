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

class project_bus:
    def fun1(self):
        root=Tk()
        root.title("Front Page")
        root.geometry("%dx%d+0+0"%(root.winfo_screenwidth(),root.winfo_screenheight()))
        img=PhotoImage(file="D:\VS_Code\Python\Python_project_bus_booking_system\starbus.png")
        Label(root,image=img).pack(side=TOP)
        Label(root,text="Online Bus Booking System",bg="grey",fg="red",font="Arial 20 bold").pack()
        Label(root,text='\n\n').pack()
        Label(root,text="NAME: VARUN PAREEK",font="Arial 14",fg="blue").pack(pady=20)
        Label(root,text="Er: 221B434",font="Arial 14",fg="blue").pack(pady=20)
        Label(root,text="Mobile: 9303959118",font="Arial 14",fg="blue").pack(pady=20)
        Label(root,text='\n\n').pack()
        Label(root,text="Sumitted to : Dr. Mahesh Kumar",bg="grey",fg="red",font="Arial 20 bold").pack()
        Label(root,text="Project Based Learning",fg="red",font="Arial 12").pack()
        Label(root,text="PRESS ANY KEY TO EXIT",font="Arial 30 bold").pack()
        def fun2(event):
            root.destroy()
            self.options()
        root.bind('<Key>',fun2)
        root.mainloop()

    def options(self):
        root1= Tk()
        root1.title("Book My Bus")
        root1.geometry("1920x1090")
        img=PhotoImage(file="D:\VS_Code\Python\Python_project_bus_booking_system\starbus.png")
        Label(root1,image=img).pack()
        Label(root1,text="Online Bus Booking System",bg="grey",fg="red",font="Arial 20 bold").pack(pady=50)
        fr=Frame(root1)
        fr.pack()

        def fun3():
            root1.destroy()
            self.option1()
        Button(fr,text="Seat Booking",bg="medium orchid",fg="black",font="Arial 15 bold",command=fun3).grid(row=0,column=0)

        def fun4():
            root1.destroy()
            self.option2()
        Button(fr,text="Check Booked Seat",bg="medium orchid",fg="black",font="Arial 15 bold",command=fun4).grid(row=0,column=3,padx=100)

        def fun5():
            root1.destroy()
            self.option3()
        Button(fr,text="Add Bus Details",bg="medium orchid",fg="black",font="Arial 15 bold",command=fun5).grid(row=0,column=6)
        
        Label(fr,text="For Admin Only",fg="red",font="Arial 13 bold").grid(row=1,column=6)
        root1.mainloop()
        
#option 1 starting\\
    def option1(self):
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
        
        def show_ticket():
            pass
        def passenger(name,gender,no_of_seats,phone,age,fare,operator_name,travel_on,boarding_point):
            
            def add_passenger(name,gender,no_of_seats,phone,age,fare,operator_name,travel_on,boarding_point):
                total_amount = int(fare)*int(no_of_seats)
                confirmation = askquestion("Fare Confermation", "Total amount to be paid "+str(total_amount) )
                if confirmation == 'yes':
                    cur.execute("INSERT INTO PASSENGER VALUES (?,?,?,?,?,?,?,?,?)",
                                (phone, name, gender, no_of_seats, age, total_amount, operator_name, travel_on, boarding_point))
                    con.commit()
                    showinfo("Success", "Seat(s) have been booked.")
                    #############################################
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
        def fun6():
            root2.destroy()
            self.options()
        Button(fr, text="Home", command=fun6, font="Arial 10 bold").grid(row=1, column=7,  pady=10)
        root2.mainloop()
#option 1 ending\\

#option 2 starting\\
    def option2(self):
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
        def check():
            pass
                
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
        def fun7():
            root5.destroy()
            self.options()
        Button(fr, text="Home", command=fun7, font="Arial 10 bold").grid(row=0, column=3)
        root5.mainloop()
#option 2 ending\\

#option 3 starting\\
    def option3(self):
        root3 = Tk()
        root3.geometry("2000x2000")
        root3.title("Online Bus Booking System")
        Label(root3, text="Online Bus Booking System", bg="grey", fg="red", font="Arial 20 bold").pack(side=TOP, pady=20)
        Label(root3, text="Add New Details To Database", font="Arial 17 bold").pack(side=TOP, pady=30)

        def fun9():
            root3.destroy()
            self.new_operator()
        Button(root3,text="New Operator",font="Arial 15 bold",command=fun9).pack(side=LEFT,pady=100,padx=100)

        def fun10():
            root3.destroy()
            self.new_bus()
        Button(root3,text="New Bus",font="Arial 15 bold",command=fun10).pack(side=LEFT,pady=100,padx=200)

        def fun11():
            root3.destroy()
            self.new_route()
        Button(root3,text="New Route",font="Arial 15 bold",command=fun11).pack(side=LEFT,pady=100,padx=80)

        def fun12():
            root3.destroy()
            self.new_run()
        Button(root3,text="New Run",font="Arial 15 bold",command=fun12).pack(side=LEFT,pady=100,padx=120)
        def fun8():
            root3.destroy()
            self.options()
        Button(root3, text="Home", command=fun8, font="Arial 10 bold").pack(side=LEFT)
        root3.mainloop()

#new operator\\
    def new_operator(self):
        root4 = Tk()
        root4.geometry("2000x2000")
        root4.title("Online Bus Booking System")
        Label(root4, text="Online Bus Booking System", bg="grey", fg="red", font="Arial 20 bold").pack(side=TOP, pady=20)
        Label(root4, text="Add Bus Operator Details", font="Arial 17 bold").pack(side=TOP, pady=10)
        fr=Frame(root4)
        fr.pack()
        Label(fr, text="Operator ID", font="Arial 11").grid(row=0,column=0)
        E1 = Entry(fr, font="Arial 11")
        E1.grid(row=0,column=1)
        Label(fr, text="Name", font="Arial 11").grid(row=0,column=2)
        E2 = Entry(fr, font="Arial 11")
        E2.grid(row=0,column=3)
        Label(fr, text="Address", font="Arial 11").grid(row=0,column=4)
        E3 = Entry(fr, font="Arial 11")
        E3.grid(row=0,column=5)
        Label(fr, text="Phone", font="Arial 11").grid(row=0,column=6)
        E4 = Entry(fr, font="Arial 11")
        E4.grid(row=0,column=7)
        Label(fr, text="Email", font="Arial 11").grid(row=0,column=8)
        E5 = Entry(fr, font="Arial 11")
        E5.grid(row=0,column=9)
        
        def display_entry_data():
            operator_id = str(E1.get())
            name = str(E2.get())
            address = str(E3.get())
            phone = str(E4.get())
            email = str(E5.get())
            Label(root4, text="Operator ID= "+operator_id).pack()
            Label(root4, text="Operator Name= "+name).pack()
            Label(root4, text="Operator Address= "+address).pack()
            Label(root4, text="Operator Phone= "+phone).pack()
            Label(root4, text="Operator Email= "+email).pack()

        def add():
            count = 1
            cur.execute("SELECT * FROM NEW_OPERATOR")
            data = cur.fetchall()
            for i in data:
                if int(E1.get()) == i[0]:
                    showinfo("Error", "Data already exists")
                    count = 0
            if count == 1:
                cur.execute("INSERT INTO NEW_OPERATOR VALUES (?,?,?,?,?)", (int(E1.get()), E2.get(), E3.get(), int(E4.get()), E5.get()))
                con.commit()
                showinfo("Good", "Data inserted.")
                display_entry_data()

        def edit(): 
            cur.execute("UPDATE NEW_OPERATOR SET name=?, address=?, phone=?, email=? WHERE operatorid=?", (E2.get(), E3.get(), int(E4.get()), E5.get(), int(E1.get())))
            con.commit()
            showinfo("Success", "Data has been edited successfully.")
            display_entry_data()
        
        Button(fr, text="Add", font="Arial 11 bold", bg='green', command=add).grid(row=0,column=10)    
        Button(fr, text="Edit", font="Arial 11 bold", bg='green', command=edit).grid(row=0,column=11)
        def fun13():
            root4.destroy()
            self.options()
        Button(root4, text="Home", command=fun13, font="Arial 15 bold").pack(pady=100)


#new bus\\
    def new_bus(self):
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
        def fun14():
            root4.destroy()
            self.options()
        Button(root4, text="Home", command=fun14, font="Arial 15 bold").pack(pady=100)

#new route\\
    def new_route(self):
        root4 = Tk()
        root4.geometry("2000x2000")
        root4.title("Online Bus Booking System")
        Label(root4, text="Online Bus Booking System", bg="grey", fg="red", font="Arial 20 bold").pack(side=TOP, pady=20)
        Label(root4, text="Add Route Details", font="Arial 17 bold").pack(side=TOP, pady=10)
        fr=Frame(root4)
        fr.pack()
        Label(fr, text="Route ID", font="Arial 11").grid(row=0,column=0)
        E1 = Entry(fr, font="Arial 11")
        E1.grid(row=0,column=1)
        Label(fr, text="Station Name", font="Arial 11").grid(row=0,column=2)
        E2 = Entry(fr, font="Arial 11")
        E2.grid(row=0,column=3)
        Label(fr, text="Station ID", font="Arial 11").grid(row=0,column=4)
        E3 = Entry(fr, font="Arial 11")
        E3.grid(row=0,column=5)
        
        def display_entry_data():
            route_id = str(E1.get())
            station_name = str(E2.get())
            station_id = str(E3.get())
            Label(root4, text="Route ID= "+route_id).pack()
            Label(root4, text="Station Name= "+station_name).pack()
            Label(root4, text="Station ID= "+station_id).pack()

        def add():
            count = 1
            cur.execute("SELECT * FROM NEW_ROUTE")
            data = cur.fetchall()
            for i in data:
                if int(E1.get()) == i[0]:
                    showinfo("Error", "Data already exists")
                    count = 0
            if count == 1:
                cur.execute("INSERT INTO NEW_ROUTE VALUES (?,?,?)", (int(E1.get()), E2.get(), int(E3.get())))
                con.commit()
                showinfo("Good", "Data inserted successfuly.")
                display_entry_data()

        def delete():
            value=int(E1.get())
            cur.execute("delete from NEW_ROUTE where routeid=?",(value,))
            con.commit()
            showinfo("Good", "Data has been deleted successfuly.")
            display_entry_data()
            

        Button(fr, text="Add Route", font="Arial 11 bold", bg='green', command=add).grid(row=0,column=10)
        
        Button(fr, text="Delete Route", font="Arial 11 bold", bg='green', command=delete).grid(row=0,column=11)

        def fun15():
            root4.destroy()
            self.options()
        Button(root4, text="Home", command=fun15, font="Arial 15 bold").pack(pady=100)

#new run\\
    def new_run(self):
        root4 = Tk()
        root4.geometry("2000x2000")
        root4.title("Online Bus Booking System")
        Label(root4, text="Online Bus Booking System", bg="grey", fg="red", font="Arial 20 bold").pack(side=TOP, pady=20)
        Label(root4, text="Add Bus Running Details", font="Arial 17 bold").pack(side=TOP, pady=10)
        fr=Frame(root4)
        fr.pack()
        Label(fr, text="Bus ID", font="Arial 11").grid(row=0,column=0)
        E1 = Entry(fr, font="Arial 11")
        E1.grid(row=0,column=1)
        Label(fr, text="Running Date", font="Arial 11").grid(row=0,column=2)
        E2 = Entry(fr, font="Arial 11")
        E2.grid(row=0,column=3)
        Label(fr, text="Seats Available", font="Arial 11").grid(row=0,column=4)
        E3 = Entry(fr, font="Arial 11")
        E3.grid(row=0,column=5)
        
        def display_entry_data():
            bus_id = str(E1.get())
            running_date = str(E2.get())
            seats = str(E3.get())
            Label(root4, text="Bus ID= "+bus_id).pack()
            Label(root4, text="Running Date= "+running_date).pack()
            Label(root4, text="Seats Availability= "+seats).pack()

        def add():
            count = 1
            cur.execute("SELECT * FROM NEW_RUN")
            data = cur.fetchall()
            for i in data:
                if int(E1.get()) == i[0]:
                    showinfo("Error", "Data already exists")
                    count = 0
            if count == 1:
                cur.execute("INSERT INTO NEW_RUN VALUES (?,?,?)", (int(E1.get()), E2.get(), int(E3.get())))
                con.commit()
                showinfo("Good", "Data inserted successfuly.")
                display_entry_data()

        def delete():
            value=int(E1.get())
            cur.execute("delete from NEW_RUN where busid=?",(value,))
            con.commit()
            showinfo("Good", "Data has been deleted successfuly.")
            display_entry_data()
            
        Button(fr, text="Add Run", font="Arial 11 bold", bg='green', command=add).grid(row=0,column=10)
        Button(fr, text="Delete Run", font="Arial 11 bold", bg='green', command=delete).grid(row=0,column=11)

        def fun16():
            root4.destroy()
            self.options()
        Button(root4, text="Home", command=fun16, font="Arial 15 bold").pack(pady=100)
    

bus=project_bus()
bus.fun1()
