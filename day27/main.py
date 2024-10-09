import tkinter


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
# configure and change or update the properties of a particular component
my_label.config(text="New Text")  # same as above
my_label.grid(row=0, column=0)  # pack(), place(x=0,y=0) or grid(column=0,row=0)

# button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

button2 = tkinter.Button(text="Click Me 2", command=button_clicked)
button2.grid(row=0, column=2)

# entry
input = tkinter.Entry(width=10)
print(input.get())
input.grid(row=2, column=3)

window.mainloop()
