from tkinter import *
import pandas
import random
from card_save import CardSave
import time

BACKGROUND_COLOR = "#B1DDC6"
timer = None


# ---------------------------- Functions ------------------------------- #
def next_card():
    global flip_timer
    # if we only had the window.after at the bottom of this function then it would wait 3 seconds then flip
    # regardless of when the button was pressed. with the window.after_cancel below it resets it when the buttons
    # are pressed. and it needs to be global because we cant see it inside this function
    window.after_cancel(flip_timer)
    c.random_word()
    card.itemconfigure(card_title, text="French", fill="black")
    card.itemconfigure(card_word, text=c.french_word, fill="black")
    card.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip)

def correct():
    c.words_left.remove(c.current_card)
    # Converting our words left dict to a pandas dataframe so we can then create a csv out of it
    data = pandas.DataFrame(c.words_left)
    # setting index to false below doesn't place add anew index number everytime this program runs
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
def flip():
    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_word, text=c.english_word, fill="white")
    card.itemconfig(card_background, image=card_back)

# ---------------------------- Data ------------------------------- #

c = CardSave()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# after 3 seconds it flips the card
flip_timer = window.after(3000, func=flip)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")



card = Canvas(width=1000, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = card.create_image(500, 280, image=card_front)
card.grid(column=0, row=0, columnspan=2)
card_title = card.create_text(500, 200, text="French", fill="black", font=("Arial", 28, "normal"))
card_word = card.create_text(500, 300, text=c.french_word, fill="black", font=("Arial", 28, "bold"))

right_button = Button(image=right_img, command=correct, highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_img, command=next_card, highlightthickness=0)
wrong_button.grid(column=0, row=1)

window.mainloop()
