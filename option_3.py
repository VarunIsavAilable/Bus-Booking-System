from tkinter import *
def option3():
    root3 = Tk()
    root3.geometry("2000x2000")
    root3.title("Online Bus Booking System")
    Label(root3, text="Online Bus Booking System", bg="grey", fg="red", font="Arial 20 bold").pack(side=TOP, pady=20)
    Label(root3, text="Add New Details To Database", font="Arial 17 bold").pack(side=TOP, pady=30)
    Button(root3,text="New Operator",font="Arial 15 bold").pack(side=LEFT,pady=100,padx=100)
    Button(root3,text="New Bus",font="Arial 15 bold").pack(side=LEFT,pady=100,padx=200)
    Button(root3,text="New Route",font="Arial 15 bold").pack(side=LEFT,pady=100,padx=80)
    Button(root3,text="New Run",font="Arial 15 bold").pack(side=LEFT,pady=100,padx=120)
    root3.mainloop()
option3()
