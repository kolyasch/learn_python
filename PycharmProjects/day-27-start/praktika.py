from tkinter import *

window = Tk()
window.title('Nikola')
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label

my_label = Label(text="Hello", font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
my_label['text'] = 'New Text'


# Button


def button_clicked():
    my_label.config(text=input.get())


button = Button(text='click me :3', command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=20, pady=20)

button2 = Button(text='new button')
button2.grid(column=2, row=0)
button2.config(padx=20, pady=20)
# Entry

input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
