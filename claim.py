#Amanda Makara

from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("lottery machine Amanda Makara")
window.geometry("500x400")
window.config(bg="yellow")

#definitions
def exit():
    mgbox=messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")


#entries and windows
#account = Label(window, text="Enter your account name")
#account.place(x=100,y=130)

#acount = Entry(window,)
#acount.place(x= 250, y=130 )

#acountnum = Label(window, text="Enter your account number")
#acountnum.place(x=100, y= 180)

#acountnum = Entry(window,)
#acountnum.place(x=270,y= 180)

#banktype = Label(window, text="Enter your type of bank")

#banktype.place(x =100,y = 230)

#banktype= Spinbox(window, "capitec","Standard Bank")
#banktype.place(x = 250, y = 230)


#buttons
#exit_btn = Button(window, text='Exit', bg='#346ab3', command=exit, pady="10")
#exit_btn.place(x= 300, y= 200)


window.mainloop()