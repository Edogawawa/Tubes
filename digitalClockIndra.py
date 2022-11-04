import time
from sys import *
from tkinter import *

def view():
    clockview = Tk()
    clockview.title("Digital Clock")
    clockview.geometry("1000x750")
    clockview.configure(bg='black')
    
    def Timer():
        timer = Tk()
        timer.title("Digital timer")
        timer.geometry("750x400")
        timer.configure(bg="black")
        timer.mainloop()

    def Stopwatch():
        clockview.destroy()
        stopwatch = Tk()
        stopwatch.title("Stopwatch")
        stopwatch.geometry("750x400")
        stopwatch.configure(bg="black")
        
        stopwatch.mainloop()

    def Alarm():
        clockview.destroy()
        alarm = Tk()
        alarm.title("Alarm")
        alarm.geometry("750x400")
        alarm.configure(bg="black")
        
        alarm.mainloop()

    def get_time():
        timeVar = time.strftime("%H:%M:%S", time.localtime())
        clock.config(text = timeVar)
        clock.after(1000, get_time)
        
    clock = Label(clockview, font=("Helvetica", 80), bg="black", fg="white")
    clock.place(x = 265, y = 300)
    get_time()

    f=Frame(clockview,bg="black",highlightbackground="black",highlightthickness=1,width=985,height=100)
    Button(f, font=("Arial", 16, 'bold'), text="Timer", fg="black", bg="grey", command=Timer).place(x=4, y=4)
    Button(f, font=("Arial", 16, 'bold'), text="Alarm", fg="black", bg="grey", command=Alarm).place(x=84, y=4)
    Button(f, font=("Arial", 16, 'bold'), text="Stopwatch", fg="black", bg="grey", command=Stopwatch).place(x=166, y=4)
    
    f.place(x = 5, y = 5)

    clockview.mainloop()

view()
    
