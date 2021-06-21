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
        messagebox.showinfo("return", "you'll return to your application")

def claim():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    sender = 'amandamakara7@gmail.com'
    receiver = emailentry.get()
    password = "@manda20W"
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(sender, password)
    # message to be sent
    message = "Congradulations!\n"
    message = message + "You can continue to play and good luck"
    # sending the mail
    s.sendmail(sender, receiver, message)
    # terminating the session
    s.quit()


# entries and windows
account = Label(window, text="Enter your account name", bg="yellow")
account.place(x=100, y=180)

acount = Entry(window,)
acount.place(x=275, y=180)

acountnum = Label(window, text="Enter your account number", bg="yellow")
acountnum.place(x=100, y=230)

acountnum = Entry(window,)
acountnum.place(x=280, y=230)

banktype = Label(window, text="Enter your type of bank", bg="yellow")
banktype.place(x=100, y=280)

banktype = Combobox(window, value=['Savings', 'cheque', 'credit', 'debit'])
banktype.place(x=280, y=280)
banktype = Label (window, text="enter your branch", bg="yellow")
banktype.place(x=100, y=330)
banktype = Combobox(window, value=['Capitec ', "Standard bank", "FNB", "Nedbank", "ABSA"])
banktype.place(x=280, y=330)
emailadd = Label(window, text="Enter your Email address", bg="yellow")
emailadd.place(x=100, y=380)
emailentry = Entry(window)
emailentry.place(x=280, y=380)


# buttons

exit_btn = Button(window, text='Exit', bg='blue', command=close, pady="10", width=10)
exit_btn.place(x=340, y=440)

cal_btn = Button(window, text='CLAIM!', bg='red', pady="10", width=10, command=claim)
cal_btn.place(x=220, y=440)


window.mainloop()