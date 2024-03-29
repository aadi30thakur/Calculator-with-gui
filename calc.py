from tkinter import *

root = Tk()
root.title("simle calculator")

e = Entry(root, width=60, borderwidth=5)
e.grid(row=0, column=0, rowspan=2, columnspan=5, padx=10, pady=10)


def button_click(number):
    current = e.get()
    global expr

    expr = str(current)+str(number)
    e.delete(0, END)
    e.insert(0, expr)


def clr():
    e.delete(0, END)


def button_equal():
    total = eval(expr)
    e.delete(0, END)
    e.insert(0, total)


button1 = Button(root, text="1", padx=40, pady=20,
                 command=lambda: button_click("1"))
button2 = Button(root, text="2", padx=40, pady=20,
                 command=lambda: button_click("2"))
button3 = Button(root, text="3", padx=40, pady=20,
                 command=lambda: button_click("3"))
button4 = Button(root, text="4", padx=40, pady=20,
                 command=lambda: button_click("4"))
button5 = Button(root, text="5", padx=40, pady=20,
                 command=lambda: button_click("5"))
button6 = Button(root, text="6", padx=40, pady=20,
                 command=lambda: button_click("6"))
button7 = Button(root, text="7", padx=40, pady=20,
                 command=lambda: button_click("7"))
button8 = Button(root, text="8", padx=40, pady=20,
                 command=lambda: button_click("8"))
button9 = Button(root, text="9", padx=40, pady=20,
                 command=lambda: button_click("9"))
button0 = Button(root, text="0", padx=40, pady=20,
                 command=lambda: button_click("0"))
button_add = Button(root, text="+", padx=40, pady=20,
                    command=lambda: button_click("+"))
button_diff = Button(root, text="-", padx=40, pady=20,
                     command=lambda: button_click("-"))
button_multiply = Button(root, text="*", padx=40, pady=20,
                         command=lambda: button_click("*"))
button_div = Button(root, text="/", padx=40, pady=20,
                    command=lambda: button_click("/"))
button_equals = Button(root, text="=", padx=200, pady=20,
                       command=button_equal)


button_clear = Button(root, text="clear", padx=90, pady=20, command=clr)


button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)

button0.grid(row=5, column=0)


button_diff.grid(row=4, column=4)
button_clear.grid(row=5, column=1, columnspan=2)
button_equals.grid(row=6, column=0, columnspan=5)
button_add.grid(row=5, column=4)
button_div.grid(row=2, column=4)
button_multiply.grid(row=3, column=4)


root.mainloop()
