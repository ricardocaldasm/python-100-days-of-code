import tkinter

BG_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=25, pady=25, bg=BG_COLOR)

canvas = tkinter.Canvas(width=800, height=550, highlightthickness=0, bg=BG_COLOR)

card_front = tkinter.PhotoImage(file=r"day31\images\card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 100, text="French", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="French Word", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

image_right = tkinter.PhotoImage(file=r"day31\images\right.png")
button_right = tkinter.Button(image=image_right, highlightthickness=0)
button_right.grid(row=1, column=0)

image_wrong = tkinter.PhotoImage(file=r"day31\images\wrong.png")
button_wrong = tkinter.Button(image=image_wrong, highlightthickness=0)
button_wrong.grid(row=1, column=1)

window.mainloop()
