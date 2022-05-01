import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)
    password_field.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_field.get()
    email = email_field.get()
    password = password_field.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if website == '' or password == '':
        messagebox.showerror(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open("passwords.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('passwords.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('passwords.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_field.delete(0, END)
            password_field.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_field.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message='No Data File Found', title='Error')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Your email: {email}\nYour password: {password}\nI coped '
                                                       f'your password. Relax ^_^')
            pyperclip.copy(password)
        else:
            messagebox.showerror(title='Error', message=f'No details for {website} exists')
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

website_field: Entry = Entry(width=35)
website_field.grid(column=1, row=1)
website_field.focus()
email_field = Entry(width=53)
email_field.grid(column=1, row=2, columnspan=2)
email_field.insert(END, 'kolyasch@internet.com')
password_field = Entry(width=35)
password_field.grid(column=1, row=3)

search_button = Button(text='Search', width=14, command=find_password)
search_button.grid(column=2, row=1, columnspan=2)
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text='Add', width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
