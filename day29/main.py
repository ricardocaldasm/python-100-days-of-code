import tkinter
import tkinter.messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        is_ok = tkinter.messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it OK to save?",
        )

        if is_ok == True:
            with open(r"day29\data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0, "end")  # or tkinter.END
                entry_password.delete(0, "end")


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


entry_website = tkinter.Entry(width=40)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_email = tkinter.Entry(width=40)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "ricardo@gmail.com")

entry_password = tkinter.Entry(width=21)
entry_password.grid(row=3, column=1)


button_generate = tkinter.Button(text="Generate Password", width=15)
button_generate.grid(row=3, column=2)

button_add = tkinter.Button(text="Add", width=34, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
