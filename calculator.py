import tkinter as tk
from tkinter import messagebox
import math

e = None
sign = None
f_num = None
frame = None
num = None


def sin():
    global sign
    global num
    sign = "sin"
    num = float(e.get())
    e.delete(0,len(e.get()))
    e.insert(0, "sin(" + str(num) + ")")


def cos():
    global sign
    global num
    sign = "cos"
    num = float(e.get())
    e.delete(0,len(e.get()))
    e.insert(0, "cos(" + str(num) + ")")

def tan():
    global sign
    global num
    sign = "tan"
    num = float(e.get())
    e.delete(0,len(e.get()))
    e.insert(0, "tan(" + str(num) + ")")

"""
def cot():
    global sign
    global cot_no
    sign = "cot"
    cot_no = float(e.get())
    e.delete(0,len(e.get()))
    e.insert(0, "cot(" + str(cot_no) + ")")

def sec():
    global sign
    global sec_no
    sign = "sec"
    sec_no = float(e.get())
    e.delete(0,len(e.get()))
    e.insert(0, "sec(" + str(sec_no) + ")")
    
def cosec():
    global sign
    global cosec_no
    sign = "cosec"
    cosec_no = float(e.get())
    e.delete(0,len(e.get()))
    e.insert(0, "cosec(" + str(cosec_no) + ")")
"""
    
def tan_inv():
    global sign
    global num
    sign = "tan_inv"
    num = float(e.get())
    e.delete(0,len(e.get()))
    e.insert(0, "tan^-1(" + str(num) + ")")
    
def cos_inv():
    global sign
    global num
    sign = "cos_inv"
    num = float(e.get())
    e.delete(0,len(e.get()))
    e.insert(0, "cos^-1(" + str(num) + ")")
    
def sin_inv():
    global sign
    global num
    sign = "sin_inv"
    num = float(e.get())
    e.delete(0,len(e.get()))
    e.insert(0, "sin^-1(" + str(num) + ")")
    
def exp():
    global num
    num = e.get()
    global sign
    sign = "exp"
    e.delete(0,len(e.get()))
    e.insert(0, "E" + num)
    
def fact():
    global num
    global sign
    num = int(e.get())
    sign = "fact"
    # e.delete(0,len(e.get()))
    e.insert(len(e.get()), "!")
    
def sqrt():
    global num
    num = float(e.get())
    global sign
    sign = "sqrt"
    e.delete(0, len(e.get()))
    e.insert(0, "sqrt(" + str(num) + ")")
    
def cube():
    global num
    num = float(e.get())
    global sign
    sign = "cube"
    e.delete(0,len(e.get()))
    e.insert(len(e.get()), "^3")
    
def n_pow():
    global f_num
    f_num = e.get()
    global sign
    sign = "n_pow"
    e.delete(0,len(e.get()))
    # e.insert(len(e.get()), "^")
    
def inv():
    global num 
    global sign
    sign = "inv"
    num = float(e.get())
    # e.delete(0,len(e.get()))
    e.insert(len(e.get()), "^(-1)")

def rem():
    global f_num
    f_num = float(e.get())
    global sign
    sign = "rem"
    # rem_no = e.get()
    e.delete(0,len(e.get()))
    # e.insert(len(e.get()), "%")


def show(number):
    current = e.get()
    e.delete(0,len(current))
    e.insert(0,str(current) + str(number))


def addition():
    first_num = e.get()
    global sign
    sign = "addition"
    global f_num
    f_num = float(first_num)
    e.delete(0,len(e.get()))

def subtraction():
    first_num = e.get()
    global sign
    sign= "subtraction"
    global f_num
    f_num = float(first_num)
    e.delete(0,len(e.get()))

def multiplication():
    first_num = e.get()
    global sign
    sign = "multiplication"
    global f_num
    f_num = float(first_num)
    e.delete(0,len(e.get()))

def division():
    first_num = e.get()
    global sign
    sign = "division"
    global f_num
    f_num = float(first_num)
    e.delete(0, len(e.get()))

def equal():
    try:
        second_num = e.get()
        e.delete(0, len(second_num))

        if sign == "addition":
            e.insert(0, f_num + float(second_num))

        if sign == "subtraction":
            e.insert(0, f_num - float(second_num))

        if sign == "multiplication":
            e.insert(0, f_num * float(second_num))

        if sign == "division":
            if int(second_num) == 0:
                e.insert(0, "NaN")
            else:
                e.insert(0, f_num / int(second_num))

        if sign == "sin":
            print(math.sin(num))
            e.insert(0, math.sin(math.radians(num)))
            
        if sign == "cos":
            e.insert(0, math.cos(math.radians(num)))
            
        if sign == "tan":
            e.insert(0, math.tan(math.radians(num)))
            
        if sign == "n_pow":
            e.insert(0, float(f_num) ** int(second_num))

        if sign == "exp":
            e.insert(0, math.exp(num))

        if sign == "fact":
            e.insert(0, math.factorial(num))

        if sign == "sqrt":
            e.insert(0, math.sqrt(num))

        if sign == "inv":
            e.insert(0, (1/num))

        if sign == "rem":
            e.insert(0, f_num % int(second_num))
            
        if sign == "sin_inv":
            e.insert(0, str(math.degrees(math.asin(num))) + " (degree)")

        if sign == "cos_inv":
            e.insert(0, str(math.degrees(math.acos(num))) + " (degree)")
        
        if sign == "tan_inv":
            e.insert(0, str(math.degrees(math.atan(num))) + " (degree)")
        
        if sign == "cube":
            e.insert(0, str(num**3))
    except Exception as ValueError:
        messagebox.showerror("Value Error", "Math Error")


def delete():
    current = e.get()
    # e.insert(0, current)
    e.delete(len(current)-1, len(current))

def clear():
    e.delete(0,len(e.get()))

            
def create_frame(mode):
    
    global frame

    try:
        frame.destroy()
    except:
        pass

    frame = tk.Label(root, background = "sky blue")
    frame.grid(row=1, column=0, columnspan=3, padx = 10, pady = 10)
        
    global e
    e = tk.Entry(frame, font = ("Helvetica", 9, "bold"), width = 40, borderwidth = 5)
    e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10, ipady = 8)

    if mode == 'n':
        
        button_1 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "1", padx = 35, pady = 5, command = lambda:show(1))
        button_2 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "2", padx = 35, pady = 5, command = lambda:show(2))
        button_3 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "3", padx = 35, pady = 5, command = lambda:show(3))
        button_4 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "4", padx = 35, pady = 5, command = lambda:show(4))
        button_5 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "5", padx = 35, pady = 5, command = lambda:show(5))
        button_6 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "6", padx = 35, pady = 5, command = lambda:show(6))
        button_7 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "7", padx = 35, pady = 5, command = lambda:show(7))
        button_8 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "8", padx = 35, pady = 5, command = lambda:show(8))
        button_9 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "9", padx = 35, pady = 5, command = lambda:show(9))
        button_0 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "0", padx = 35, pady = 5, command = lambda:show(0))
        button_del = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "<--", padx = 31, pady = 5, command = delete)
        
        button_add = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "+", padx = 35, pady = 5, command = addition)
        button_clear = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "Clear", padx = 77, pady = 5, command = clear)
        button_equal = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "=", padx = 89, pady = 5, command = equal)
        button_dot = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = ".", padx = 37, pady = 5, command = lambda:show("."))
        
        button_sqrt = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "sqrt", padx = 27, pady = 5, command = sqrt)
        button_sub = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "-", padx = 37, pady = 5, command = subtraction)
        button_mul = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "*", padx = 37, pady = 5, command = multiplication)
        button_div = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "/", padx = 37, pady = 5, command = division)

        button_1.grid(row = 1, column = 0, pady = 5)
        button_2.grid(row = 1, column = 1, pady = 5)
        button_3.grid(row = 1, column = 2, pady = 5)
        button_4.grid(row = 2, column = 0, pady = 5)
        button_5.grid(row = 2, column = 1, pady = 5)
        button_6.grid(row = 2, column = 2, pady = 5)
        button_7.grid(row = 3, column = 0, pady = 5)
        button_8.grid(row = 3, column = 1, pady = 5)
        button_9.grid(row = 3, column = 2, pady = 5)
        button_0.grid(row = 4, column = 0, pady = 5)

        button_sqrt.grid(row = 5, column = 0, pady = 5)
        button_clear.grid(row =5, column = 1, columnspan=2, pady = 5)
        button_equal.grid(row =7, column = 1, columnspan=2, pady = 5)
        button_del.grid(row = 4, column = 2)
        button_dot.grid(row = 4, column = 1)

        button_add.grid(row = 7, column = 0)
        button_sub.grid(row = 6, column = 0, pady = 5)
        button_mul.grid(row = 6, column = 1, pady = 5)
        button_div.grid(row = 6, column = 2, pady = 5)

    else:

        button_1 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "1", padx = 35, pady = 5, command = lambda:show(1))
        button_2 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "2", padx = 36, pady = 5, command = lambda:show(2))
        button_3 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "3", padx = 35, pady = 5, command = lambda:show(3))
        button_4 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "4", padx = 35, pady = 5, command = lambda:show(4))
        button_5 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "5", padx = 36, pady = 5, command = lambda:show(5))
        button_6 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "6", padx = 35, pady = 5, command = lambda:show(6))
        button_7 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "7", padx = 35, pady = 5, command = lambda:show(7))
        button_8 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "8", padx = 36, pady = 5, command = lambda:show(8))
        button_9 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"),text = "9", padx = 35, pady = 5, command = lambda:show(9))
        button_0 = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"),text = "0", padx = 35, pady = 5, command = lambda:show(0))

        button_add = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "+", padx = 35, pady = 5, command = addition)
        button_clear = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "<--", padx = 31, pady = 5, command = delete)
        button_dot = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = ".", padx = 37, pady = 5, command = lambda:show("."))
        button_equal = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "=", padx = 89, pady = 5, command = equal)
        
        button_sin = tk.Button(frame, background = "light gray", padx = 29, pady = 5, font = ("Helvetica", 9, "bold"), text = "sin", command = sin)
        button_cos = tk.Button(frame, background = "light gray", padx = 30, pady = 5, font = ("Helvetica", 9, "bold"), text = "cos", command = cos)
        button_tan = tk.Button(frame, background = "light gray", padx = 31, pady = 5, font = ("Helvetica", 9, "bold"), text = "tan", command = tan)
        button_cot = tk.Button(frame, background = "light gray", padx = 20, pady = 5, font = ("Helvetica", 9, "bold"), text = "sin^-1", command = sin_inv)
        button_cosec = tk.Button(frame, background = "light gray", padx = 21, pady = 5, font = ("Helvetica", 9, "bold"), text = "cos^-1", command = cos_inv)
        button_sec = tk.Button(frame, background = "light gray", padx = 22, pady = 5, font = ("Helvetica", 9, "bold"), text = "tan^-1", command = tan_inv)
        button_fact = tk.Button(frame, background = "light gray", padx = 35, pady = 5, font = ("Helvetica", 9, "bold"), text = "X!", command = fact)
        button_sqrt = tk.Button(frame, background = "light gray", padx = 26, pady = 5, font = ("Helvetica", 9, "bold"), text = "sqrt", command = sqrt)
        button_exp = tk.Button(frame, background = "light gray", padx = 30, pady = 5, font = ("Helvetica", 9, "bold"), text = "exp", command = exp)
        button_cube = tk.Button(frame, background = "light gray", padx = 27, pady = 5, font = ("Helvetica", 9, "bold"), text = "X^3", command = cube)
        button_n_pow = tk.Button(frame, background = "light gray", padx = 30, pady = 5, font = ("Helvetica", 9, "bold"), text = "X^n", command = n_pow)
        button_inv = tk.Button(frame, background = "light gray", padx = 27, pady = 5, font = ("Helvetica", 9, "bold"), text = "X^-1", command = inv)
        button_rem = tk.Button(frame, background = "light gray", padx = 26, pady = 5, font = ("Helvetica", 9, "bold"), text = "X%n", command = rem)
        button_e = tk.Button(frame, background = "light gray", padx = 78, pady = 5, font = ("Helvetica", 9, "bold"), text = "Clear", command = clear)
        
        button_sub = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "-", padx = 37, pady = 5, command = subtraction)
        button_mul = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"), text = "*", padx = 37, pady = 5, command = multiplication)
        button_div = tk.Button(frame, background = "light gray", font = ("Helvetica", 9, "bold"),text = "/", padx = 37, pady = 5, command = division)

        button_1.grid(row = 6, column = 0, pady = 5)
        button_2.grid(row = 6, column = 1, pady = 5)
        button_3.grid(row = 6, column = 2, pady = 5)
        button_4.grid(row = 7, column = 0, pady = 5)
        button_5.grid(row = 7, column = 1, pady = 5)
        button_6.grid(row = 7, column = 2, pady = 5)
        button_7.grid(row = 8, column = 0, pady = 5)
        button_8.grid(row = 8, column = 1, pady = 5)
        button_9.grid(row = 8, column = 2, pady = 5)
        button_0.grid(row = 9, column = 0, pady = 5)

        button_add.grid(row = 10, column = 0, pady = 5)
        button_clear.grid(row = 9, column = 1, pady = 5)
        button_dot.grid(row = 9, column = 2, pady = 5)
        button_equal.grid(row =10, column = 1, columnspan=2, pady = 5)

        button_sub.grid(row = 11, column = 0, pady = 5)
        button_mul.grid(row = 11, column = 1, pady = 5)
        button_div.grid(row = 11, column = 2, pady = 5)

        button_sin.grid(row = 1, column = 0, pady = 5)
        button_cos.grid(row = 1, column = 1, pady = 5)
        button_tan.grid(row = 1, column = 2, pady = 5)
        button_cot.grid(row = 2, column = 0, pady = 5)
        button_cosec.grid(row = 2, column = 1, pady = 5)
        button_sec.grid(row = 2, column = 2, pady = 5)
        button_sqrt.grid(row = 3, column = 0, pady = 5)
        button_fact.grid(row = 3, column = 1, pady = 5)
        button_inv.grid(row = 3, column = 2, pady = 5)
        button_rem.grid(row = 4, column = 0, pady = 5)
        button_n_pow.grid(row = 4, column = 1, pady = 5)
        button_exp.grid(row = 4, column = 2, pady = 5)
        button_cube.grid(row=5, column=0, pady = 5)
        button_e.grid(row = 5, column = 1, columnspan = 2, pady = 5)


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Calculator")
    root.configure(background = "sky blue")

    """
    global frame
    frame = tk.Label(root)
    frame.grid(row=1, column=0, columnspan=2)
    """

    mode = tk.StringVar()
    tk.Radiobutton(root, background = "light gray", variable = mode, font = ("Helvetica", 9, "bold"), text = "Scientific", value = "s").grid(row=0, column=0, padx = 5, pady = 5, ipadx = 10)
    tk.Radiobutton(root, background = "light gray", variable = mode, font = ("Helvetica", 9, "bold"), text = "Simple", value = "n").grid(row = 0, column = 1, padx = 5, pady = 5, ipadx = 10)

    choose_btn = tk.Button(root, background = "light gray", width = 10, font = ("Helvetica", 9, "bold"), text = "Select", command = lambda: create_frame(mode.get()))
    choose_btn.grid(row=0, column=2, padx = 5, pady = 5)

    root.mainloop()
