import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/german.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    front_canvas.clipboard_clear()
    current_card = random.choice(to_learn)
    front_canvas.itemconfig(card_title, text='German', fill='black')
    front_canvas.itemconfig(card_word, text=current_card['German'], fill='black')
    front_canvas.itemconfig(card_img, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    front_canvas.itemconfig(card_title, text='English', fill='white')
    front_canvas.itemconfig(card_word, text=current_card[' English'], fill='white')
    front_canvas.itemconfig(card_img, image=back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

window = Tk()
window.title('Anki')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

front_canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')
card_img = front_canvas.create_image(400, 263, image=front_img)
card_title = front_canvas.create_text(400, 150, text='Title', font=('Areal', 40, 'italic'))
card_word = front_canvas.create_text(400, 263, text='Word', font=('Areal', 60, 'bold'))
front_canvas.grid(column=0, row=0, columnspan=2)
front_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

next_card()

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

left_image = PhotoImage(file="./images/wrong.png")
left_button = Button(image=left_image, highlightthickness=0, command=next_card)
left_button.grid(row=1, column=0)

window.mainloop()
