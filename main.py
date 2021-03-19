from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
# import csv as data frame
# data = pandas.read_csv("../flash_cards/data/words_to_learn.csv")
# else FileNotFoundError:
try:
    data = pandas.read_csv("../flash_cards/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("../flash_cards/data/french_words.csv")
    data = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# print(language_dict)
current_card = {}

# if green check remove from list

# If user 1st time no try words_to_learn file there then finally use french_words

# to_learn dict at close should be 'red x words only(or words that hadn't been learned)

# So convert to_learn to a csv called words_to_learn.csv

# Create a loop? No a boolean? That says when gameover = True save file to csv



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    """If user knows word they click green check. This
    funciton is triggered and removes the entry from
    the to_learn dict so it is gone"""
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("../flash_cards/data/words_to_learn.csv", index=False)
    print(len(to_learn))
    next_card()

#to_learn.to_csv("words_to_learn.csv", index=False)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)

# -------------------------

# Window
window = Tk()
window.title("Memory Synapse Engraver")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="../flash_cards/images/card_front.png")
card_back_img = PhotoImage(file="../flash_cards/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
#front = Label(image=f_img, width=800, height=526, highlightthickness=0)
#front.grid(row=0, column=0, columnspan=2)

# Buttons
green_check_img = PhotoImage(file="../flash_cards/images/right.png")
yes_button = Button(image=green_check_img, borderwidth=0, highlightthickness=0, command=is_known)
yes_button.grid(column=0, row=1)

red_cross_img = PhotoImage(file="../flash_cards/images/wrong.png")
unknown_button = Button(image=red_cross_img, borderwidth=0, highlightthickness=0, command=next_card)
unknown_button.grid(column=1, row=1)

next_card()


window.mainloop()
