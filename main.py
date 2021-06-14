#Amanda Makara

from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("lottery machine Amanda Makara")
window.geometry("500x500")
window.config(bg="yellow")

#def login(_name,_email_adress, _ID_number):


def exit():
    mgbox=messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")
#labels

#frame = Frame(window, padx=10, pady=10)
#frame.pack(expand=True)

lbluser = Label(window, text="Enter your Username")
lbluser.place(x=100,y=130)

userentry = Entry(window,)
userentry.place(x= 250, y=130 )

lblpass = Label(window, text="Enter your email adress")
lblpass.place(x=100, y= 180)

entrypass = Entry(window,)
entrypass.place(x=270,y= 180)

lbluser = Label(window, text="Enter your ID number")
lbluser.place(x =100,y = 230)

userentry = Entry(window,)
userentry.place(x = 250, y = 230)

#buttons

reset_btn = Button(window, text='clear', bg='#346ab3')
reset_btn.place(x = 96 ,y =300)

exit_btn = Button(window, text='Exit', bg='#346ab3', command=exit)
exit_btn.place(x= 300, y= 300)

cal_btn = Button(window, text='sign in', bg='#346ab3')
cal_btn.place(x =200,y= 300)





window.mainloop()

