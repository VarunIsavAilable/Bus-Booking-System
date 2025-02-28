from tkinter import *
def options(Event):
        root1= Tk()
        root1.title("Book My Bus")
        root1.geometry("1920x1090")
        img=PhotoImage(file="starbus.png")
        Label(root1,image=img).pack()
        
        Label(root1,text="Online Bus Booking System",bg="grey",fg="red",font="Arial 20 bold").pack(pady=50)

        fr=Frame(root1)
        fr.pack()
        
        Button(fr,text="Seat Booking",bg="medium orchid",fg="black",font="Arial 15 bold").grid(row=0,column=0)

        Button(fr,text="Check Booked Seat",bg="medium orchid",fg="black",font="Arial 15 bold").grid(row=0,column=3,padx=100)

        Button(fr,text="Add Bus Details",bg="medium orchid",fg="black",font="Arial 15 bold").grid(row=0,column=6)
        
        Label(fr,text="For Admin Only",fg="red",font="Arial 13 bold").grid(row=1,column=6)

        root1.mainloop()
options(Event)
