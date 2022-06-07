# Calculator app

from tkinter import *
import math

# ------------------------------------------------------------------------
# GUI
root = Tk()
root.title('Calculadora')
root.resizable(False, False)


# ------------------------------------------------------------------------
# Entry
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# ------------------------------------------------------------------------
# Functions
# Insert number
def button_click(number):
    e.insert(END, number)


# Clear screen
def button_clear():
    e.delete(0, END)


# Add two numbers
def button_add():
    first_number = e.get()
    global operation
    operation = '+'
    global f_num
    f_num = float(first_number)
    e.delete(0, END)


# Subtract two numbers
def button_sub():
    first_number = e.get()
    global operation
    operation = '-'
    global f_num
    f_num = float(first_number)
    e.delete(0, END)


# Multiply two numbers
def button_mulp():
    first_number = e.get()
    global operation
    operation = '*'
    global f_num
    f_num = float(first_number)
    e.delete(0, END)


# Divide two numbers
def button_div():
    first_number = e.get()
    global operation
    operation = '/'
    global f_num
    f_num = float(first_number)
    e.delete(0, END)


# Exponentiation a number
def button_exp():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    e.insert(0, pow(f_num, 2))


# Square a number
def button_square():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    e.insert(0, math.sqrt(f_num))


# Equal
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if operation == '+':
        e.insert(0, f_num + float(second_number))
    elif operation == '-':
        e.insert(0, f_num - float(second_number))
    elif operation == '*':
        e.insert(0, f_num * float(second_number))
    elif operation == '/':
        try:
            e.insert(0, f_num / float(second_number))
        except:
            e.insert(0, 'DIVISÃO POR ZERO')



# ------------------------------------------------------------------------
# Define Buttons
# Numbers
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
# Buttons Operations
button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_sub = Button(root, text='-', padx=39, pady=20, command=button_sub)
button_mulp = Button(root, text='*', padx=39, pady=20, command=button_mulp)
button_div = Button(root, text='/', padx=39, pady=20, command=button_div)
button_exp = Button(root, text='Exp', padx=33, pady=20, command=button_exp)
button_square = Button(root, text=u'\u221A', padx=37, pady=20, command=button_square)
# Button Equal
button_equal = Button(root, text='=', padx=85, pady=20, command=button_equal)
# Button Clear
button_clear = Button(root, text='C', padx=40, pady=20, command=button_clear)
# Button Decimal
button_decimal = Button(root, text=u'\u002E', padx=40, pady=20, command=lambda: button_click("."))


# ------------------------------------------------------------------------
# Buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_mulp.grid(row=4, column=3)
button_div.grid(row=5, column=3)
button_exp.grid(row=4, column=2)
button_square.grid(row=4, column=1)

button_clear.grid(row=1, column=3)
button_equal.grid(row=5, column=0, columnspan=2)
button_decimal.grid(row=5, column=2)


mainloop()


