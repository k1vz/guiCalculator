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


def butao(txt, bg, row, column, cmd = "command = lambda: press()"):
    global janela
    butao = Button(janela, text = txt, fg = "white", bg = bg, command = cmd, height = 2,
                   width = 6)
    butao.grid(row = row, column = column)

# Making Buttons #
# Buttons - Numbers #

butao(" 1 ", "black", 1, 0)

#b_um = Button(janela, text = " 1 ", fg = "white", bg = "black", command = lambda: press(1),
#              height = 2, width = 6)
#b_um.grid(row = 1, column = 0)

b_dois = Button(janela, text = " 2 ", fg = "white", bg = "black", command = lambda: press(2),
              height = 2, width = 6)
b_dois.grid(row = 1, column = 1)

b_tres = Button(janela, text = " 3 ", fg = "white", bg = "black", command = lambda: press(3),
              height = 2, width = 6)
b_tres.grid(row = 1, column = 2)

b_quatro = Button(janela, text = " 4 ", fg = "white", bg = "black", command = lambda: press(4),
              height = 2, width = 6)
b_quatro.grid(row = 2, column = 0)

b_cinco = Button(janela, text = " 5 ", fg = "white", bg = "black", command = lambda: press(5),
              height = 2, width = 6)
b_cinco.grid(row = 2, column = 1)

b_seis = Button(janela, text = " 6 ", fg = "white", bg = "black", command = lambda: press(6),
              height = 2, width = 6)
b_seis.grid(row = 2, column = 2)

b_sete = Button(janela, text = " 7 ", fg = "white", bg = "black", command = lambda: press(7),
              height = 2, width = 6)
b_sete.grid(row = 3, column = 0)

b_oito = Button(janela, text = " 8 ", fg = "white", bg = "black", command = lambda: press(8),
              height = 2, width = 6)
b_oito.grid(row = 3, column = 1)

b_nove = Button(janela, text = " 9 ", fg = "white", bg = "black", command = lambda: press(9),
              height = 2, width = 6)
b_nove.grid(row = 3, column = 2)

b_zero = Button(janela, text = " 0 ", fg = "white", bg = "black", command = lambda: press(0),
              height = 2, width = 6)
b_zero.grid(row = 4, column = 1)

b_dot = Button(janela, text = " . ", fg = "white", bg = "#181818", command = lambda: press("."),
              height = 2, width = 6)
b_dot.grid(row = 4, column = 2)

# Buttons - Operations #

b_equal = Button(janela, text = " = ", fg = "white", bg = "#181818", command = equal,
                 height = 2, width = 6)
b_equal.grid(row = 4, column = 0)

b_plus = Button(janela, text = " + ", fg = "white", bg = "#181818", command = lambda: press("+"),
                height = 2, width = 6)
b_plus.grid(row = 1, column = 3)

b_minus = Button(janela, text = " - ", fg = "white", bg = "#181818", command = lambda:
                press("-"), height = 2, width = 6)
b_minus.grid(row = 2, column = 3)

b_multiply = Button(janela, text = " x ", fg = "white", bg = "#181818", command = lambda:
                    press("*"), height = 2, width = 6)
b_multiply.grid(row = 3, column = 3)

b_divide = Button(janela, text = " / ", fg = "white", bg = "#181818", command = lambda:
                    press("/"), height = 2, width = 6)
b_divide.grid(row = 4, column = 3)

# Starting GUI #
janela.mainloop()