from tkinter import *


root = Tk()
root.title("Simple Calculator")

text_box = Entry(root, width=40, borderwidth=5)
text_box.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
f_num = ""
math = ""


def button_num(num):
    current = text_box.get()
    text_box.delete(0, END)
    text_box.insert(0, str(current) + str(num))


def click_clear():
    text_box.delete(0, END)


def click_add():
    global math
    # global f_num
    math = "addition"
    # f_num = text_box.get()
    current = str(text_box.get())
    # text_box.delete(0, END)
    pos = len(current) + 1
    text_box.insert(pos, "+")
    # text_box.delete(0, END)


def click_sub():
    global math
    # global f_num
    math = "subtraction"
    # f_num = text_box.get()
    # text_box.delete(0, END)
    current = str(text_box.get())
    pos = len(current) + 1
    text_box.insert(pos, "-")


def click_div():
    global math
    math = "division"
    current = str(text_box.get())
    pos = len(current) + 1
    text_box.insert(pos, "/")


def click_mul():
    global math
    math = "multiplication"
    current = str(text_box.get())
    pos = len(current) + 1
    text_box.insert(pos, "*")


def click_equal_to():
    global math
    # global f_num
    # if math == "addition":
    #     # ans = int(text_box.get()) + int(f_num)
    #     # text_box.delete(0, END)
    #     # text_box.insert(0, ans)
    # elif math == "subtraction":
    #     ans = int(f_num) - int(text_box.get())
    #     text_box.delete(0, END)
    #     text_box.insert(0, ans)
    expression = str(text_box.get())
    fi_num = 0
    se_num = 0
    i = 0
    ch = ""
    if math == "addition":
        while expression[i] != "+":
            fi_num = (fi_num*10) + int(expression[i])
            i = i + 1
        i = i + 1
        while i != len(expression):
            se_num = (se_num*10) + int(expression[i])
            i = i + 1
        text_box.delete(0, END)
        ans = int(fi_num + se_num)
        text_box.insert(0, str(ans))
    elif math == "subtraction":
        while expression[i] != "-":
            fi_num = (fi_num*10) + int(expression[i])
            i = i + 1
        i = i + 1
        while i != len(expression):
            se_num = (se_num*10) + int(expression[i])
            i = i + 1
        text_box.delete(0, END)
        ans = int(fi_num - se_num)
        text_box.insert(0, str(ans))
    elif math == "division":
        while expression[i] != "/":
            fi_num = (fi_num*10) + int(expression[i])
            i = i + 1
        i = i + 1
        while i != len(expression):
            se_num = (se_num*10) + int(expression[i])
            i = i + 1
        text_box.delete(0, END)
        ans = int(fi_num / se_num)
        text_box.insert(0, str(ans))
    elif math == "multiplication":
        while expression[i] != "*":
            fi_num = (fi_num*10) + int(expression[i])
            i = i + 1
        i = i + 1
        while i != len(expression):
            se_num = (se_num*10) + int(expression[i])
            i = i + 1
        text_box.delete(0, END)
        ans = int(fi_num * se_num)
        text_box.insert(0, str(ans))


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_num(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_num(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_num(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_num(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_num(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_num(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_num(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_num(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_num(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_num(0))
button_add = Button(root, text="+", padx=40, pady=20, command=click_add)
button_sub = Button(root, text="-", padx=40, pady=20, command=click_sub)
button_mul = Button(root, text="*", padx=41, pady=20, command=click_mul)
button_div = Button(root, text="/", padx=40, pady=20, command=click_div)
button_equal_to = Button(root, text="=", padx=40, pady=52, command=click_equal_to)
button_clear = Button(root, text="Clear", padx=78, pady=20, command=click_clear)

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
button_clear.grid(row=4, column=1, columnspan=2)
button_equal_to.grid(row=5, column=2, rowspan=3)

button_add.grid(row=5, column=0)
button_sub.grid(row=5, column=1)
button_mul.grid(row=6, column=0)
button_div.grid(row=6, column=1)

root.mainloop()
