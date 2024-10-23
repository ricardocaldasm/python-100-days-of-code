import tkinter
import pandas
from random import choice

BG_COLOR = "#B1DDC6"

# ---------------------------- NEXT CARD ------------------------------- #
current_card = dict()
to_learn = dict()

try:
    data = pandas.read_csv(r"day31\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"day31\data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(2000, func=flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


# ---------------------------- REMOVE WORD ------------------------------- #
def remove_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(r"day31\data\words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=25, pady=25, bg=BG_COLOR)

flip_timer = window.after(2000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=550, highlightthickness=0, bg=BG_COLOR)

card_front = tkinter.PhotoImage(file=r"day31\images\card_front.png")
card_back = tkinter.PhotoImage(file=r"day31\images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 100, text="Language", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="French Word", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

image_right = tkinter.PhotoImage(file=r"day31\images\right.png")
button_right = tkinter.Button(
    image=image_right, highlightthickness=0, command=remove_card
)
button_right.grid(row=1, column=1)

image_wrong = tkinter.PhotoImage(file=r"day31\images\wrong.png")
button_wrong = tkinter.Button(
    image=image_wrong, highlightthickness=0, command=next_card
)
button_wrong.grid(row=1, column=0)

next_card()

window.mainloop()
