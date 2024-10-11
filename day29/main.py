import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file=r"day29\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = tkinter.Label(text="Website:")
label_website.grid(row=1, column=0)

label_email = tkinter.Label(text="Email/Username:")
label_email.grid(row=2, column=0)

label_password = tkinter.Label(text="Password:")
label_password.grid(row=3, column=0)

entry_website = tkinter.Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)

entry_email = tkinter.Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)

entry_password = tkinter.Entry(width=21)
entry_password.grid(row=3, column=1)

button_generate = tkinter.Button(text="Generate Password")
button_generate.grid(row=3, column=2)

button_add = tkinter.Button(text="Add", width=36)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
