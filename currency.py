# Amanda Makara

from tkinter.ttk import Combobox
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



window = Tk()
window.title("lottery machine Amanda Makara")
window.geometry("500x450")
window.config(bg="yellow")

canvas = Canvas(window, width=593, height=176)
canvas.place(x=0, y=0)
img = PhotoImage(file="istockphoto-168637625-612x612.png")
canvas.create_image(0, 0, anchor=NW, image=img)


# API
url = "https://v6.exchangerate-api.com/v6/52f23c7db09d54899cbe4221/latest/USD"

req = requests.get(url)

result = req.json()
print(result)
rates = result['conversion_rates'].keys()



# function
def convertor():

    amount = float(amount_entry.get())

    new_amnt = amount * result['conversion_rates'][lst.get()]  # converting currency

    answer['text'] = new_amnt

def exit():
    mgbox = messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")


def claim():
        window.destroy()
        import claim


# Labels


amount = Label(text="your Amount", bg="yellow", fg="black", font=("bold", 15))
amount.place(x=100, y=200)

# Entry
amount_entry = Entry(window)
amount_entry.place(x=290, y=200)

# Label
crrncy1 = Label(text="convert here", bg="yellow", fg="black", font=("bold", 15))
crrncy1.place(x=100, y=250)

# function
lst = Combobox(window, width=20, text="")
rates = list(rates)
lst["values"] = rates



for i in rates:

    lst.insert(END, str(i))
    lst.place(x=290, y=250)

# button
btn = Button(window, text="convert", bg='green', command=convertor, width=10, pady=10)
btn.place(x=220, y=330)

reset_btn = Button(window, text='claim', bg='green', command=claim, width=10, pady=10)
reset_btn.place(x=350, y=380)

exit_btn = Button(window, text='Exit', bg='green', command=exit, width=10, pady=10)
exit_btn.place(x=350, y=330)


# Label
answer = Label(window, font=('bold', 12))
answer.place(x=220, y=380)


window.mainloop()