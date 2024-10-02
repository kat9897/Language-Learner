from tkinter import *
from tkinter import messagebox
from random import *

import pandas

# ---------------------- Constants ---------------------- #
BACKGROUND_COLOR = "#B1DDC6"
COUNTDOWN_SEC = 5
LANGUAGE_1 = "English"
LANGUAGE_2 = "French"


# ---------------------- Generate New Random Word ---------------------- #
def generate_random_word():
    global random_word
    try:
        random_word = choice(french_words_dict)
        canvas.itemconfig(language_word_text, text=random_word[LANGUAGE_2])
        canvas.itemconfig(language_text, text=LANGUAGE_2)
    except KeyError:
        messagebox.showwarning(title="KeyError", message="Had a key error. Try again")
    finally:
        count_down(COUNTDOWN_SEC)


# ---------------------- Countdown ---------------------- #
def count_down(count):
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        flip_card(back_card_img, LANGUAGE_1)


def reset_card():
    flip_card(front_card_img, LANGUAGE_2)
    generate_random_word()


def flip_card(image, language):
    global random_word
    canvas.itemconfig(card, image=image)
    canvas.itemconfig(language_text, text=language)
    canvas.itemconfig(language_word_text, text=random_word[language])


# ---------------------- UI Setup ---------------------- #
window = Tk()
window.title("Language Learner")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526)
# Card Images
back_card_img = PhotoImage(file="images/card_back.png")
front_card_img = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=front_card_img)
# Text
language_text = canvas.create_text(400, 150, text="",  font=("Arial", 40, "italic"))
language_word_text = canvas.create_text(400, 263, text="",  font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=reset_card)
wrong_button.grid(column=0, row=1)
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=reset_card)
right_button.grid(column=1, row=1)

# Learning Language Words
french_words_csv = "data/french_words.csv"
french_words = pandas.read_csv(french_words_csv)
french_words_dict = french_words.to_dict(orient="records")
random_word = ""
generate_random_word()

# Countdown
count_down(COUNTDOWN_SEC)





window.mainloop()
