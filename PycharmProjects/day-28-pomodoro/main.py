import pygame
from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
BLUE = '#46244C'
PURPLE = '#712B75'
PINK = "#C74B50"
PEACH = '#D49B54'
GREEN = '#3CAB4C'
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 60
count = 5
reps = 0
my_timer = None

pygame.mixer.init()


def study_play():
    pygame.mixer.music.load('audio_2022.mp3')
    pygame.mixer.music.play(loops=0)


def rest_play():
    pygame.mixer.music.load('Stop_it.mp3')
    pygame.mixer.music.play(loops=0)
# ---------------------------- TIMER RESET ------------------------------- #


def study_button():
    title_label.config(fg=PEACH, text='Study')
    study_play()


def rest_button():
    title_label.config(fg=GREEN, text='Rest')
    rest_play()


def new_check_mark():
    global check_mark
    mark = ''
    work_sessions = math.floor(reps / 2)
    for _ in range(work_sessions):
        mark += '✔'
    check_mark.config(text=mark)


def reset_timer():
    global reps
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', bg=BLUE, fg=PINK)
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        reps = 0
        rest_button()
    if reps % 2 == 0:
        count_down(short_break_sec)
        rest_button()
    else:
        count_down(work_sec)
        study_button()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time_count):
    count_min = math.floor(time_count / 60)
    count_sec = time_count % 60
    if count_min < 10:
        count_min = f'0{count_min}'

    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if time_count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, time_count - 1)
    else:
        start_timer()
        new_check_mark()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=BLUE)

title_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=BLUE, fg=PINK)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', font=FONT_NAME, bg=PEACH, fg=PURPLE, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', font=FONT_NAME, bg=PEACH, fg=PURPLE, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text='', font=1, bg=BLUE, fg=GREEN)
check_mark.grid(column=1, row=3)

window.mainloop()
