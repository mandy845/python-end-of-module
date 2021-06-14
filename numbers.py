#Amanda Makara

from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("lottery machine Amanda Makara")
window.geometry("500x400")
window.config(bg="yellow")

#defining
def exit():
    mgbox=messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")
#labels and entries
box1 = Spinbox(window, from_=0, to=49, width=2, font=("bold", 20))
box1.place(x=20, y=110)
box2 = Spinbox(window, from_=0, to=49, width=2, font=("bold", 20))
box2.place(x=100, y=110)
box3 = Spinbox(window, from_=0, to=49, width=2, font= ("bold", 20))
box3.place(x=180,y=110)
box4 = Spinbox(window, from_=0, to=49, width=2, font=("bold", 20))
box4.place(x=250, y=110)
box5 = Spinbox(window, from_=0, to=49, width=2, font=("bold", 20))
box5.place(x=330, y=110)
box6 = Spinbox(window, from_=0, to=49, width=2, font= ("bold", 20))
box6.place(x=400,y=110)


#buttons
reset_btn = Button(window, text='play again?', bg='#346ab3',pady="10")
reset_btn.place(x = 96 ,y =200)

exit_btn = Button(window, text='Exit', bg='#346ab3', command=exit, pady="10")
exit_btn.place(x= 300, y= 200)

cal_btn = Button(window, text='CLAIM!', bg='#346ab3', pady="10")
cal_btn.place(x =220,y= 200)

window.mainloop()