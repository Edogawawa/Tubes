import time
from sys import *
from tkinter import *

clockview = Tk()
clockview.title("Digital Clock")
clockview.geometry("1000x750")
clockview.configure(bg='black')

def get_time():
    timeVar = time.strftime("%H:%M:%S", time.localtime())
    clock.config(text = timeVar)
    clock.after(1000, get_time)

clock = Label(clockview, font=("Helvetica", 80), bg="black", fg="white")
clock.place(x = 265, y = 300)
get_time()


f=Frame(clockview,bg="black",highlightbackground="black",highlightthickness=1,width=985,height=100)
Button(f, font=("Arial", 20, 'bold'), text="Timer", fg="black", bg="grey").place(x=5, y=10)
Button(f, font=("Arial", 20, 'bold'), text="Alarm", fg="black", bg="grey").place(x=110, y=10)
Button(f, font=("Arial", 20, 'bold'), text="Stopwatch", fg="black", bg="grey").place(x=216, y=10)
f.place(x = 5, y = 5)

clockview.mainloop()

