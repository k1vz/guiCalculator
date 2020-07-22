from tkinter import *

expression = ''


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("Simple Calculator")
    display = StringVar()
    expression_field = Entry(gui, textvariable=display)
    expression_field.grid(columnspan=4, ipadx=70)

    me = Frame(gui)


def press(n):
    global expression
    expression = expression + str(n)
    display.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        display.set(total)
        expression = ""

    except:
        display.set(" error ")
        expression = ""


button1 = Button(gui, text=' 1 ', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

equal = Button(gui, text=' = ', fg='black', bg='red', command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

minus = Button(gui, text=' - ', fg='black', bg='red',
                  command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                     command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

gui.mainloop()
