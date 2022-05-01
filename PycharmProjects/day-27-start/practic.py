from tkinter import *

window = Tk()
window.title('Nikola')
window.minsize(width=500, height=300)

# Label

my_label = Label(text="Hello", font=('Arial', 24, 'bold'))
my_label.pack()
my_label['text'] = 'New Text'


# Button


def button_clicked():
    my_label.config(text=input.get())


button = Button(text='click me :3', command=button_clicked)
button.pack()
# import turtle
#
# tim = turtle.Turtle()
# tim.write('Sam huj', font=('Areal', 60, 'bold'))

input = Entry(width=10)
input.pack()

text = Text(height=5, width=30)
text.focus()
text.insert(END, 'email.ru')
print(text.get('1.0', END))
text.pack()


# Spinbox


def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale


def scale_used(value):
    print(value)
scale = Scale(from_=100, to=0, command=scale_used)
scale.pack()

# Checkbutton


def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text='Is on?', variable=checked_state, command=checkbutton_used)
checkbutton.pack()


# Radiobutton


def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox


def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ['Apple', 'Pear', 'Orange', 'Banana']
for item in fruits:
    listbox.insert(fruits.index(item), item)
# listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()


window.mainloop()
