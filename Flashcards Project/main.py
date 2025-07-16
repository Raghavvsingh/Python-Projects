from tkinter import *

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ----------------- Accessing DATA ----------------- #
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pd.read_csv("./data/french_words.csv")
    data_records=original_data.to_dict(orient="records")
else:
    data_records = data.to_dict(orient="records")


# ----------------- NEW WORD ----------------- #
def new_word():
    global current_card
    current_card = random.choice(data_records)
    canvas.itemconfig(front_img, image=card_front_img)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card['French'], fill="black")
    window.after(3000, flip_card)

#------------------REMOVE KNOWN WORDS--------------------#
def is_known():
    data_records.remove(current_card)

    data=pandas.DataFrame(data_records)
    data.to_csv("data/words_to_learn.csv",index=False)

    new_word()


# ----------------- FLIP CARD ----------------- #
def flip_card():
    canvas.itemconfig(front_img, image=card_back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card['English'], fill="white")

# ----------------- UI SETUP ----------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
front_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

tick_img = PhotoImage(file="./images/right.png")
tick_button = Button(image=tick_img, highlightthickness=0, command=is_known)
tick_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_word)
wrong_button.grid(row=1, column=0)

new_word()

window.mainloop()
