import tkinter


def action():
    result = float(entry.get())
    convert_result = result * 1.609
    label3.config(text=f"{convert_result}")


window = tkinter.Tk()
window.title("Distance Converter")
window.config(padx=20, pady=20)

# entry
entry = tkinter.Entry(width=10)
entry.grid(row=0, column=1)

# label
label = tkinter.Label(text="Miles")
label.grid(row=0, column=2)

label2 = tkinter.Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = tkinter.Label(text="0")
label3.grid(row=1, column=1)

label4 = tkinter.Label(text="Km")
label4.grid(row=1, column=2)

# button

button = tkinter.Button(text="Calculate", command=action)
button.grid(row=2, column=1)

window.mainloop()
