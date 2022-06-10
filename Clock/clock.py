# Digital Clock

# -------------------------------------------
# Packages
from tkinter import *
import time


# -------------------------------------------
# Functions
def clock():
    # Time
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    # Day
    day = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    # Configure
    myTime.config(text=hour + ':' + minute + ':' + second)
    myDay.config(text=day + '/' + month + '/' + year)
    myTime.after(1000, clock)
    myDay.after(1000, clock)


# -------------------------------------------
# GUI
root = Tk()
root.title('Digital Clock')
root.geometry('250x150')
root.resizable(False, False)
root.config(background='black')


# -------------------------------------------
# Widgets
myTime = Label(root, text="", font=('Helvetica', 40), fg='red', bg='black')
myDay = Label(root, text="", font=('Helvetica', 20), fg='red', bg='black')


# -------------------------------------------
# Layouts
myTime.pack(pady=20)
myDay.pack()

# Call Function
clock()


# -------------------------------------------
# MainLoop
root.mainloop()