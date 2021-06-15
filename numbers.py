#Amanda Makara
import random
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("lottery machine Amanda Makara")
window.geometry("593x500")
window.config(bg="yellow")

canvas = Canvas(window,width=593,height=176)
canvas.place(x=0, y=0)
img = PhotoImage(file="lottoery.png")
canvas.create_image(0, 0, anchor=NW, image=img)

#initialising numbers
number1=(IntVar)
number2=(IntVar)
number3=(IntVar)
number4=(IntVar)
number5=(IntVar)
number6=(IntVar)


#defining


def draws():
    x=number1.get()
    y=number2.get()
    z=number3.get()
    b=number4.get()
    a=number5.get()
    c=number6.get()

    draw_list=[x,y,z,b,a,c]
    draw_list.sort()

    actual_lotto=sorted(random.sample(range(1,49),6))

  #  if any (draw_list)<0 or any(draw_list) >50:






def exit():
    mgbox=messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")
#labels and entries
lbl=Label(window, text="Tata ama chance tata ama Million!", font=("bolder",15), bg='yellow')
lbl.place(x=20, y=200)
box1 = Spinbox(window, from_=0, to=49, width=2,textvariable=number1, font=("bold", 20))
box1.place(x=20, y=250)
box2 = Spinbox(window, from_=0, to=49, width=2,textvariable=number2, font=("bold", 20))
box2.place(x=100, y=250)
box3 = Spinbox(window, from_=0, to=49, width=2, textvariable=number3,font= ("bold", 20))
box3.place(x=180,y=250)
box4 = Spinbox(window, from_=0, to=49, width=2,textvariable=number4, font=("bold", 20))
box4.place(x=250, y=250)
box5 = Spinbox(window, from_=0, to=49, width=2, textvariable=number5, font=("bold", 20))
box5.place(x=330, y=250)
box6 = Spinbox(window, from_=0, to=49, width=2, textvariable=number6, font= ("bold", 20))
box6.place(x=400,y=250)


#buttons
reset_btn = Button(window, text='clear', bg='#346ab3',pady=10, width=10)
reset_btn.place(x=360, y=370)

exit_btn = Button(window, text='Exit', bg='blue', command=exit, pady=10, width=10)
exit_btn.place(x=360, y=420)

cal_btn = Button(window, text='Play!', bg='red',pady=10, width=10)
cal_btn.place(x=96, y=370)

window.mainloop()