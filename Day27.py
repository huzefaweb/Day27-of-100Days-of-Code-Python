from tkinter import * # this module is derived from TK language

screen = Tk()  # creates screen
screen.title("My First GUI")
screen.minsize(width=500, height=300)
screen.config(padx=100, pady=200)  # use to add padding

# label
# first create a component
my_label = Label(text="First label", font=("Arial", 24, "bold"))

# to display the label use pack method
# my_label.pack()  # uses optional arguments with default values
my_label.grid(column=0, row=0)
# *args: Many Positional arguments store arguments inside a dictionary
# unlimited  positional arguments because we can get the argument at the specific position
# *args : stands for argument take unlimited arguments, and we can loop through to use each argument (*) stand for any

# **kwargs: many keyword arguments store arguments inside a dictionary

# to change already define arguments in above label
my_label["text"] = "New Text"
# or by doing this
my_label.config(text="New Text")


# button
def button_on_click():
    my_label.config(text=input.get())

# so when someone clicks the button the method is targeted and executed


# parentheses are not added at the end of the method name because command attribute only required name
button = Button(text="Click me", command=button_on_click)
# button.pack()
button.grid(column=1, row=1)
button = Button(text="Click me 2", command=button_on_click)
button.grid(column=3, row=0)
# Entry
input = Entry()
# input.place(x=0, y=0)  # is all about precious positioning.. The downside is it is very specific in positioning
input.grid(column=4, row=4)
# # text
# text = Text(height=5, width=40)
# # put cursor in text
# text.focus()
# # Add some text to begin with
# text.insert(END, "Example of multiline text entry")
# # Gets current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
#
# # spinbox
# def spinbox_used():
#     # gets the current value in spinbox
#     print(spinbox.get())
#
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
#
# # Scale
# def scale_used(value):
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# # Check Button
# def checked_button():
#     # print 1 if on button checked, otherwise off
#     print(checked_state.get())
#
#
# # variable to hold on to checked state, 0 is off 1 is on
# checked_state = IntVar()
# checked_Button = Checkbutton(text="Is On?", variable=checked_state, command=checked_button)
# checked_state.get()
# checked_Button.pack()
#
#
# # Radio Button
# def radio_used():
#     print(radio_state.get())
#
#
# # variable to hold onto which radio button value is checked
# radio_state = IntVar()
# radio_button_1 = Radiobutton(text="option1", value=1, variable=radio_state, command=radio_used)
# radio_button_2 = Radiobutton(text="option2", value=2, variable=radio_state, command=radio_used)
# radio_button_1.pack()
# radio_button_2.pack()
#
#
# # List Box
# listbox = Listbox(height=4)
#
#
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))
#
#
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
#
#
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

screen.mainloop()  # keeps the screen open
