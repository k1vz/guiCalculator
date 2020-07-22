from tkinter import *

expression = ''

# Creating GUI (Janela) #
janela = Tk()
janela.title("André Mama")
janela.geometry("208x212")
janela.configure(background = "black")

# Creating display #
display = StringVar()
expression_field = Entry(janela, textvariable = display, bg = "#181818", fg = "white")
expression_field.grid(columnspan = 4, ipadx = 40, ipady = 15)

# Setting Functions #
def press(n):
    global expression
    expression = expression + str(n)
    display.set(expression)

def equal():
    try:
        global expression
        total = str(eval(expression))
        display.set(total)
        expression = ""

    except:
        display.set("ERROR ...")
        expression = ""


def butao(txt, bg, row, column, cmd):
    global janela
    butao = Button(janela, text = txt, fg = "white", bg = bg, command = cmd, height = 2,
                   width = 6)
    butao.grid(row = row, column = column)

#  \-_=_- Making Buttons -_=_-/ #

# Buttons - Numbers #

butao(" 1 ", "black", 1, 0, lambda: press(1))
butao(" 2 ", "black", 1, 1, lambda: press(2))
butao(" 3 ", "black", 1, 2, lambda: press(3))
butao(" 4 ", "black", 2, 0, lambda: press(4))
butao(" 5 ", "black", 2, 1, lambda: press(5))
butao(" 6 ", "black", 2, 2, lambda: press(6))
butao(" 7 ", "black", 3, 0, lambda: press(7))
butao(" 8 ", "black", 3, 1, lambda: press(8))
butao(" 9 ", "black", 3, 2, lambda: press(9))
butao(" 0 ", "black", 4, 1, lambda: press(0))

# Buttons - Operations #

butao(" = ", "#181818", 4, 0, equal)
butao(" . ", "#181818", 4, 2, lambda: press("."))
butao(" + ", "#181818", 1, 3, lambda: press("+"))
butao(" - ", "#181818", 2, 3, lambda: press("-"))
butao(" x ", "#181818", 3, 3, lambda: press("*"))
butao(" / ", "#181818", 4, 3, lambda: press("/"))

# Starting GUI #
janela.mainloop()