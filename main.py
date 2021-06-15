#Amanda Makara
import rsaidnumber
from tkinter import *
from tkinter import messagebox
import datetime

window = Tk()
window.title("lottery machine Amanda Makara")
window.geometry("593x500")
window.config(bg="yellow")



canvas = Canvas(window,width=593,height=176)
canvas.place(x=0,y=0)
img = PhotoImage(file="lottoery.png")
canvas.create_image(0, 0, anchor=NW, image=img)

#def login(_name,_email_adress, _ID_number):


def exit():
    mgbox=messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")
def login():
    id=rsaidnumber.parse(identry.get())
    current_year = datetime.date.today().year
    year_of_birth = id.date_of_birth.year
    age = current_year - year_of_birth
    if age > 18:
        messagebox.showinfo('you qualify!', 'get ready to play!')
        window.destroy()
        import numbers
        numbers.verify()
    else:
        messagebox.showinfo('sorry', ' you are under age!')
#labels

#frame = Frame(window, padx=10, pady=10)
#frame.pack(expand=True)

lbluser = Label(window, text="Enter your Username", bg= 'yellow',font=20)
lbluser.place(x=100, y=250)

userentry = Entry(window,width=25)
userentry.place(x=330, y=250)

lblpass = Label(window, text="Enter your email address", bg='yellow', font=20,)
lblpass.place(x=100, y=280)

entrypass = Entry(window,width=25)
entrypass.place(x=330, y=280)

lbluser = Label(window, text="Enter your ID number", bg='yellow',font=20)
lbluser.place(x=100, y=320)

identry = Entry(window,width=25)
identry.place(x=330, y=320)

#buttons

reset_btn = Button(window, text='clear', bg='#346ab3',pady=10, width=10)
reset_btn.place(x=430, y=370)

exit_btn = Button(window, text='Exit', bg='blue', command=exit, pady=10, width=10)
exit_btn.place(x=430, y=420)

cal_btn = Button(window, text='sign in', bg='red',pady=10, width=10, command=login)
cal_btn.place(x=120, y=370)





window.mainloop()

