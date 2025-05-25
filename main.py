import json
from tkinter import *
import pandas
from tkinter import messagebox
import random
BACKGROUND_COLOR = "#B1DDC6"
pick_card={}
words={}

try:
    data=pandas.read_csv("data/words_left_to_learn.csv")
except FileNotFoundError:
    original_data =pandas.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words=data.to_dict(orient="records")


def new_card():
    global pick_card, flip_timer
    window.after_cancel(flip_timer)
    pick_card = random.choice(words)
    chosen_word_French = pick_card["French"]
    canvas.itemconfig(title_card,text="French", fill="black")
    canvas.itemconfig(word_card,text=chosen_word_French, fill="black")
    canvas.itemconfig(card_background, image=front_card)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    chosen_word_English = pick_card["English"]
    canvas.itemconfig(title_card,text="English", fill="white")
    canvas.itemconfig(word_card,text=chosen_word_English, fill="white")
    canvas.itemconfig(card_background,image=back_card)

def known():
    words.remove(pick_card)
    print(len(words))
    new_card()
    data = pandas.DataFrame(words)
    data.to_csv("data/words_left_to_learn.csv", index=False)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer=window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400, 263, image=front_card)
title_card = canvas.create_text(400,150, text="title", font= ("times new roman", 40, "italic"))
word_card = canvas.create_text(400,250, text="word", font= ("times new roman", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known)
right_button.grid(row=1, column=1)

new_card()

window.mainloop()





