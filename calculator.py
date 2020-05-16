#yes this has a number of bugs :(

from tkinter import *

root = Tk()
root.title("S1mple Calculator")
num1 = 0
choice = ""
e = Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

def button_click(num):                              #To add the digit on the screen
    current = e.get()
    e.delete(0,END)
    if num != -1:
        e.insert(0,str(current) + str(num))
    else:
        e.insert(0,str(current) + ".")

def button_equ():                                   #Things to be done when "=" is pressed
    global choice, num1    
    if num1 == 1 and choice == "+":
        e.insert(0,"NEVER SETTLE")
    else:
        def printit(ans):
            if not ans.is_integer():
                e.insert(0,f"{ans:.2f}")
            else:
                e.insert(0, int(ans))

        
        num2 = float(e.get())
        e.delete(0,END)
        if choice == "+":
            num1 += num2
            printit(num1)
        elif choice == "-":
            num1 -= num2
            printit(num1)
        elif choice == "*":
            num1 *= num2
            printit(num1)    
        elif choice == "/":
            num1 /= num2
            printit(num1)
        elif choice == "%":
            num1 = (num2 / num1) * 100
            if num1.is_integer():
                e.insert(0, int(num1))
            else:
                e.insert(0,f"{num1:.2f}")


def clrscr():                                               # C nostalgia XD
    e.delete(0,END)

def correct():                                              # for the backspace
    temp = float(e.get())
    e.delete(0,END)


    if temp == 0:
        e.insert(0,"")
    else:
        if temp.is_integer():
            e.insert(0,str(temp))
        

def dosomething(x):
    global choice, num1
    num1 = float(e.get())
    e.delete(0,END)
    choice = x
    

b_ac = Button(root, text="AC", padx=36, pady=20,command=clrscr)
b_corr = Button(root, text="<-", padx=37, pady=20, command=correct)
b_per = Button(root, text="%", padx=38, pady=20, command=lambda: dosomething("%"))
b_div = Button(root, text="/", padx=40, pady=20, command=lambda: dosomething("/"))
b_ac.grid(row=1, column=0)
b_corr.grid(row=1, column=1)
b_per.grid(row=1,column=2)
b_div.grid(row=1, column=3)

b_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
b_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
b_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
b_mul = Button(root, text="*", padx="39", pady=20, command=lambda: dosomething("*"))
b_7.grid(row=2, column=0)
b_8.grid(row=2, column=1)
b_9.grid(row=2, column=2)
b_mul.grid(row=2, column=3)

b_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
b_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
b_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
b_sub = Button(root, text="-", padx=40, pady=20, command=lambda: dosomething("-"))
b_4.grid(row=3, column=0)
b_5.grid(row=3, column=1)
b_6.grid(row=3, column=2)
b_sub.grid(row=3, column=3)

b_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
b_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
b_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
b_add = Button(root, text="+", padx=37, pady=20, command=lambda: dosomething("+"))
b_1.grid(row=4, column=0)
b_2.grid(row=4, column=1)
b_3.grid(row=4, column=2)
b_add.grid(row=4, column=3)

b_dot = Button(root, text=".", padx=42, pady=20, command=lambda: button_click(-1))
b_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
b_equ = Button(root, text="=", padx=85, pady=20, command=button_equ)
b_dot.grid(row=5, column=0)
b_0.grid(row=5, column=1)
b_equ.grid(row=5, column=2, columnspan=2)

root.mainloop()