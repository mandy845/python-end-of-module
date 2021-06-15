#Amanda Makara

from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("lottery machine Amanda Makara")
window.geometry("597x500")
window.config(bg="yellow")
#canvas = Canvas(window,width=593,height=176)
#canvas.place(x=0, y=0)
#img = PhotoImage(file="lottoery.png")
#canvas.create_image(0, 0, anchor=NW, image=img)

#definitions
def exit():
    mgbox=messagebox.askquestion("exit application", "are you sure you want to exit?", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")


#entries and windows
account = Label(window, text="Enter your account name")
account.place(x=100,y=180)

acount = Entry(window,)
acount.place(x= 275, y=180 )

acountnum = Label(window, text="Enter your account number")
acountnum.place(x=100, y= 230)

acountnum = Entry(window,)
acountnum.place(x=280,y= 230)

banktype = Label(window, text="Enter your type of bank")
banktype.place(x =100,y = 270)

banktype=Entry(window)
banktype.place(x=280,y=270)

banktype=Label (window, text="enter your branch")
banktype.place(x = 100, y = 330)
banktype=Entry(window)
banktype.place(x=280,y=330)


#buttons

exit_btn = Button(window, text='Exit', bg='blue', command=exit, pady="10", width=10)
exit_btn.place(x=340, y=400)

cal_btn = Button(window, text='CLAIM!', bg='red', pady="10", width=10)
cal_btn.place(x=220, y=400)

#exit_btn = Button(window, text='Exit', bg='#346ab3', command=exit, pady="10")
#exit_btn.place(x= 300, y= 200)


window.mainloop()