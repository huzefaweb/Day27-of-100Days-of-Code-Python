from tkinter import *


def button_on_click():
    mile = int(input.get())
    km = str(mile * 1.609344)
    answer.config(text=km)


screen = Tk()
screen.title("Mile to KM")
screen.config(padx=20, pady=20)

input = Entry(width=7)
input.grid(column=1, row=0)

Miles = Label(text="Miles", font=("Arial", 14))
Miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Arial", 14))
is_equal_to.grid(column=0, row=1)

answer = Label(text="0", font=("Arial", 14))
answer.grid(column=1, row=1)


KM = Label(text="Km", font=("Arial", 14))
KM.grid(column=2, row=1)

button = Button(text="Calculate", command=button_on_click)
button.grid(column=1, row=2)

screen.mainloop()
