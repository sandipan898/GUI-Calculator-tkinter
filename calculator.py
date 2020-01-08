#Simple Calculator
import tkinter as tk

root = tk.Tk()

root.title("Simple Calculator")

e = tk.Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 15)

def button_show(number):
    current = e.get()
    e.delete(0,len(current))
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,len(e.get()))

def button_add():
    first_num = e.get()
    global sign
    sign = "addition"
    global f_num
    f_num = int(first_num)
    e.delete(0,len(e.get()))

def button_subtraction():
    first_num = e.get()
    global sign
    sign= "subtraction"
    global f_num
    f_num = int(first_num)
    e.delete(0,len(e.get()))

def button_multiplication():
    first_num = e.get()
    global sign
    sign = "multiplication"
    global f_num
    f_num = int(first_num)
    e.delete(0,len(e.get()))

def button_division():
    first_num = e.get()
    global sign
    sign = "division"
    global f_num
    f_num = int(first_num)
    e.delete(0,len(e.get()))

def button_equal():
    second_num = e.get()
    e.delete(0, len(second_num))
    if sign == "addition":
        e.insert(0, f_num + int(second_num))
    if sign == "subtraction":
        e.insert(0, f_num - int(second_num))
    if sign == "multiplication":
        e.insert(0, f_num * int(second_num))
    if sign == "division":
        if int(second_num) == 0:
            e.insert(0, "NaN")
        else:
            e.insert(0, f_num / int(second_num))



button_1 = tk.Button(root, text = "1", padx = 40, pady = 20, command = lambda:button_show(1))
button_2 = tk.Button(root, text = "2", padx = 40, pady = 20, command = lambda:button_show(2))
button_3 = tk.Button(root, text = "3", padx = 40, pady = 20, command = lambda:button_show(3))
button_4 = tk.Button(root, text = "4", padx = 40, pady = 20, command = lambda:button_show(4))
button_5 = tk.Button(root, text = "5", padx = 40, pady = 20, command = lambda:button_show(5))
button_6 = tk.Button(root, text = "6", padx = 40, pady = 20, command = lambda:button_show(6))
button_7 = tk.Button(root, text = "7", padx = 40, pady = 20, command = lambda:button_show(7))
button_8 = tk.Button(root, text = "8", padx = 40, pady = 20, command = lambda:button_show(8))
button_9 = tk.Button(root, text = "9", padx = 40, pady = 20, command = lambda:button_show(9))
button_0 = tk.Button(root, text = "0", padx = 40, pady = 20, command = lambda:button_show(0))

button_add = tk.Button(root, text = "+", padx = 39, pady = 20, command = button_add)
button_clear = tk.Button(root, text = "Clear", padx = 77, pady = 20, command = button_clear)
button_equal = tk.Button(root, text = "=", padx = 86, pady = 20, command = button_equal)

button_sub = tk.Button(root, text = "-", padx = 40, pady = 20, command = button_subtraction)
button_mul = tk.Button(root, text = "*", padx = 40, pady = 20, command = button_multiplication)
button_div = tk.Button(root, text = "/", padx = 40, pady = 20, command = button_division)
button_quit = tk.Button(root, text = "Exit", padx = 126, pady = 15, command = root.quit)

button_1.grid(row = 1, column = 0)
button_2.grid(row = 1, column = 1)
button_3.grid(row = 1, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 3, column = 0)
button_8.grid(row = 3, column = 1)
button_9.grid(row = 3, column = 2)
button_0.grid(row = 4, column = 0)

button_add.grid(row = 5, column = 0)
button_clear.grid(row =4, column = 1, columnspan=2)
button_equal.grid(row =5, column = 1, columnspan=2)

button_sub.grid(row = 6, column = 0)
button_mul.grid(row = 6, column = 1)
button_div.grid(row = 6, column = 2)
button_quit.grid(row = 7, column = 0, columnspan = 3)
root.mainloop()

