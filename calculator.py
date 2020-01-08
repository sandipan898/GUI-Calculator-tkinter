import tkinter as tk

root = tk.Tk()

root.title("Simple Calculator")

frame = tk.Frame(root, bg = "gray", padx = 10, pady = 10)
frame.pack(padx = 5, pady = 5)

e = tk.Entry(frame, width = 35, borderwidth = 7)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 20)

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



button_1 = tk.Button(frame, text = "1", padx = 40, pady = 20, bd = 2, command = lambda:button_show(1))
button_2 = tk.Button(frame, text = "2", padx = 40, pady = 20, bd = 2, command = lambda:button_show(2))
button_3 = tk.Button(frame, text = "3", padx = 40, pady = 20, bd = 2, command = lambda:button_show(3))
button_4 = tk.Button(frame, text = "4", padx = 40, pady = 20, bd = 2, command = lambda:button_show(4))
button_5 = tk.Button(frame, text = "5", padx = 40, pady = 20, bd = 2, command = lambda:button_show(5))
button_6 = tk.Button(frame, text = "6", padx = 40, pady = 20, bd = 2, command = lambda:button_show(6))
button_7 = tk.Button(frame, text = "7", padx = 40, pady = 20, bd = 2, command = lambda:button_show(7))
button_8 = tk.Button(frame, text = "8", padx = 40, pady = 20, bd = 2, command = lambda:button_show(8))
button_9 = tk.Button(frame, text = "9", padx = 40, pady = 20, bd = 2, command = lambda:button_show(9))
button_0 = tk.Button(frame, text = "0", padx = 40, pady = 20, bd = 2, command = lambda:button_show(0))

button_add = tk.Button(frame, text = "+", padx = 40, pady = 20, command = button_add, bd = 2)
button_clear = tk.Button(frame, text = "Clear", padx = 76, pady = 20, command = button_clear, bd = 2)
button_equal = tk.Button(frame, text = "=", padx = 87, pady = 20, command = button_equal, bd = 2)

button_sub = tk.Button(frame, text = "-", padx = 41, pady = 20, bd = 2, command = button_subtraction)
button_mul = tk.Button(frame, text = "*", padx = 41, pady = 20, bd = 2, command = button_multiplication)
button_div = tk.Button(frame, text = "/", padx = 41, pady = 20, bd = 2, command = button_division)
button_quit = tk.Button(frame, text = "Exit", padx = 128, pady = 12, bd = 2, command = frame.quit)

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
frame.mainloop()
