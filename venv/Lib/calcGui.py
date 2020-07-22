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

#  \=_- Making Buttons -_=/ #

# Buttons - Numbers #

txt = 0 # Starting var 'txt' #
butao(str(txt), "black", 4, 1, lambda: press(txt))

# Loop responsible for create the buttons #

for (r) in range(1, 4):
    for (c) in range(0, 3):
        txt += 1
        butao(str(txt), "black", r, c, lambda: press(txt))


# Buttons - Operators #

butao(" = ", "#181818", 4, 0, equal)
butao(" . ", "#181818", 4, 2, lambda: press("."))
butao(" + ", "#181818", 1, 3, lambda: press("+"))
butao(" - ", "#181818", 2, 3, lambda: press("-"))
butao(" x ", "#181818", 3, 3, lambda: press("*"))
butao(" / ", "#181818", 4, 3, lambda: press("/"))

# Starting GUI #
janela.mainloop()