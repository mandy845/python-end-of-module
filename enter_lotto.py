# Amanda Makara
import datetime
import random
from tkinter import *
from tkinter import messagebox
from playsound import playsound

window = Tk()
window.title("lottery machine Amanda Makara")
window.geometry("593x550")
window.config(bg="yellow")

canvas = Canvas(window, width=593, height=176)
canvas.place(x=0, y=0)
img = PhotoImage(file="lottoery.png")
canvas.create_image(0, 0, anchor=NW, image=img)


# initialising numbers


number1 = (IntVar)
number2 = (IntVar)
number3 = (IntVar)
number4 = (IntVar)
number5 = (IntVar)
number6 = (IntVar)

# labels and entries
lbl = Label(window, text="Tata ama chance tata ama Million!", font=("bolder", 15), bg='yellow')
lbl.place(x=20, y=200)
box1 = Spinbox(window, from_=0, to=49, width=2, textvariable=number1, font=("bold", 20))
box1.place(x=20, y=250)
box2 = Spinbox(window, from_=0, to=49, width=2, textvariable=number2, font=("bold", 20))
box2.place(x=100, y=250)
box3 = Spinbox(window, from_=0, to=49, width=2, textvariable=number3,font=("bold", 20))
box3.place(x=180, y=250)
box4 = Spinbox(window, from_=0, to=49, width=2, textvariable=number4, font=("bold", 20))
box4.place(x=250, y=250)
box5 = Spinbox(window, from_=0, to=49, width=2, textvariable=number5, font=("bold", 20))
box5.place(x=330, y=250)
box6 = Spinbox(window, from_=0, to=49, width=2, textvariable=number6, font=("bold", 20))
box6.place(x=400, y=250)
# answer = Entry(window, state="readonly")

answer = Text(window, height=2, width=30)

answer.place(x=135, y=300, width=330, height=120)

# defining


def draws():
    x = int(box1.get())
    y = int(box2.get())
    z = int(box3.get())
    b = int(box4.get())
    a = int(box5.get())
    c = int(box6.get())

    draw_list = [x, y, z, b, a, c]
    draw_list.sort()
    print(draw_list)

    actual_lotto = sorted(random.sample(range(1, 49), 6))
    print(actual_lotto)

    if any(draw_list) < 0 or any(draw_list) > 50:
        messagebox.showinfo("sorry", "invalid input", icon='warning')

    else:
        messagebox.showinfo("great!", "let's play!")

        if len(actual_lotto) == len(draw_list):
            identical = set(actual_lotto).intersection(set(draw_list))
            print(len(identical))
            if len(identical) == 6:
                print("6")

                message = "you got all correct numbers!\n " + \
                          "You got yourself 10,000 000.00 \n today lotto numbers are " + str(actual_lotto) + \
                          "\n and your numbers are " + str(draw_list)
                answer.config(state="normal")
                answer.insert(END, message)
                answer.config(state="readonly")
                prize = 10000000
                playsound("lotto_winner_nz.mp3")
            elif len(identical) == 5:
                print("5")



                message="you got 5 correct numbers. \n" + \
                        "You got yourself 8,584.00 \n today lotto numbers are " +\
                        str(actual_lotto) + "\n and your numbers are " + str(draw_list)
                answer.config(state="normal")
                answer.insert(END, message)
                answer.config(state="readonly")
                prize = 8584.00
                playsound("lotto_winner_nz.mp3")

            elif len(identical) == 4:
                print("4")

                message = f'you got 4 correct numbers. \n You got yourself 2,384.00 \n today lotto numbers are \n{str(actual_lotto)} \n and your numbers are {str(draw_list)}'
                answer.config(state="normal")
                answer.insert(END, message)
                answer.config(state="readonly")
                prize = 2384.00
                playsound("lotto_winner_nz.mp3")

            elif len(identical) == 3:
                print("3")

                message = "you got 3 correct numbers. " + "\n You got yourself 100.50 \n today lotto numbers are " +\
                          str(actual_lotto) + "\n and your numbers are " + str(draw_list)
                answer.config(state="normal")
                answer.insert(END, message)
                answer.config(state="readonly")
                prize = 100.50
                playsound("lotto_winner_nz.mp3")

            elif len(identical) == 2:
                print("2")
                message = f'you got 2 correct numbers.\n You got yourself 20.00 \n Today lotto numbers are \n {str(actual_lotto)}\n and your numbers are {str(draw_list)}'
                answer.config(state="normal")
                #  answer.insert(0, message)
                answer.insert(END, message)
                answer.config(state="readonly")
                prize = 20.00
                playsound("looser.mp3")

            elif len(identical) == 1:
                messagebox.showinfo("Sorry", "you got 1 correct number. " +
                                    " you did not get a prize keep trying \n today lotto numbers are " +
                                    str(actual_lotto) + "\n and your numbers are " + str(draw_list))
                prize = 0
                playsound("looser.mp3")
            else:
                messagebox.showinfo("sorry", "you didn't get  numbers correct. " +
                                    "You did not have a prize \n " "today lotto numbers are " +
                                    str(actual_lotto) + "\n and your numbers are " + str(draw_list))
                prize = 0
                playsound("looser.mp3")

            lotto = actual_lotto
            played= draw_list
            price = prize
            currentdate=datetime.date.today()
            textFile = open("competer.txt", "a+")
            textFile.write("winning numbers:" + lotto)
            textFile.write("\n")
            textFile.write("played:" + played)
            textFile.write("\n")
            textFile.write("prices:" + price)
            textFile.write("\n")
            textFile.write("date played:" + currentdate)


def close():
    mgbox = messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        window.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")


def claimbtn():
    msg = messagebox.askquestion("", "Do you want to convert your prize")
    if msg == "yes":
        window.destroy()
        import currency
    else:
        messagebox.showinfo("", "you can claim")
        window.destroy()
        import claim


number1 = IntVar(window)
number2 = IntVar(window)
number1 = IntVar(window)
number1 = IntVar(window)
number1 = IntVar(window)
number1 = IntVar(window)


def clearbtn():
    number1.set(0)
    number1.set(0)
# buttons


reset_btn = Button(window, text='clear', bg='#346ab3', pady=10, width=10, command=clearbtn)
reset_btn.place(x=360, y=440)

exit_btn = Button(window, text='Exit', bg='blue', command=close, pady=10, width=10)
exit_btn.place(x=360, y=490)

cal_btn = Button(window, text='Play!', bg='red', pady=10, width=10, command=draws)
cal_btn.place(x=96, y=440)

claimon = Button(window, text="Claim", bg="green", pady=10, width=10, command=claimbtn)
claimon.place(x=96, y=490)


window.mainloop()