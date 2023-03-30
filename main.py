from tkinter import *

window = Tk()
window.title("Km to Miles Converter")
window.minsize(width=250, height=200)
window.config(padx=30, pady=30)

text_input = Entry()
text_input.config(width=10)
text_input.grid(row=0, column=1)

label1 = Label(text="KM")
label1.grid(row=0, column=2)
label1.config(padx=10, pady=10)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)
label2.config(padx=10, pady=10)

label3 = Label(text="0 miles")
label3.grid(row=1, column=1)
label3.config(padx=10, pady=10)


def calculate():
    km = text_input.get()
    miles = float(km) / 1.60934
    label3["text"] = f"{round(miles, 2)} miles"


submit_button = Button()
submit_button.config(text="Calculate", command=calculate)
submit_button.grid(row=2, column=1)

window.mainloop()
