import tkinter
import tkinter.messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    entry_password.delete(0, "end")
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH DATA --------------------------------- #


def find_password():
    website = entry_website.get()
    try:
        with open(r"day30\password_manager\data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            tkinter.messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            tkinter.messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        try:
            with open(r"day30\password_manager\data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            # Creates new file if no file is loaded
            with open(r"day30\password_manager\data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open(r"day30\password_manager\data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, "end")  # or tkinter.END
            entry_password.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(
    width=140,
    height=200,
    highlightthickness=0,
)
logo_img = tkinter.PhotoImage(file=r"day30\password_manager\logo.png")
canvas.create_image(80, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = tkinter.Label(text="Website:")
label_website.grid(row=1, column=0, sticky="e")

label_email = tkinter.Label(text="Email/Username:")
label_email.grid(row=2, column=0, sticky="e")

label_password = tkinter.Label(text="Password:")
label_password.grid(row=3, column=0, sticky="e")


entry_website = tkinter.Entry(width=21)
entry_website.grid(row=1, column=1, sticky="w")
entry_website.focus()

entry_email = tkinter.Entry(width=21)
entry_email.grid(row=2, column=1, columnspan=2, sticky="w")
entry_email.insert(0, "ricardo@gmail.com")

entry_password = tkinter.Entry(width=21)
entry_password.grid(row=3, column=1, sticky="w")

button_search = tkinter.Button(text="Search", width=15, command=find_password)
button_search.grid(row=1, column=2, sticky="w")

button_generate = tkinter.Button(
    text="Generate Password", width=15, command=generate_password
)
button_generate.grid(row=3, column=2, sticky="w")

button_add = tkinter.Button(text="Add", width=17, command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
