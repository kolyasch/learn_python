from tkinter import *


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=220, height=80)
window.config(padx=20, pady=20)


my_label = Label(text="is equal to", font=('Arial', 12))
my_label.grid(column=0, row=1)

answer = Label(text="0", font=('Arial', 12))
answer.grid(column=1, row=1)

miles = Label(text="Miles", font=('Arial', 12))
miles.grid(column=2, row=0)

km = Label(text="Km", font=('Arial', 12))
km.grid(column=2, row=1)

input = Entry(width=7)
input.grid(column=1, row=0)


def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.609)
    answer.config(text=f'{km}')
button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)




window.mainloop()