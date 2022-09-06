import tkinter
import random


def clicked():
    current_num = int(txt.get())

    def try_again_message(num, current_num):
        window.destroy()
        try_again_message = tkinter.Tk()
        try_again_message.title('Wrong number!')
        try_again_message.geometry("450x350")
        if num < current_num:
            message = 'Number you are searching for is smaller than this! Try again!'
        else:
            message = 'Number you are searching for is bigger than this! Try again!'
        try_again_label = tkinter.Label(master=try_again_message, text=message, font=('Arial Bold', 10))
        try_again_label.place(x=10, y=30)
        try_label = tkinter.Label(try_again_message, text='Enter your number: ', font=('Arial Bold', 15))
        try_label.place(x=110, y=50)
        txt_new = tkinter.Entry(master=try_again_message, width=30)
        txt_new.place(x=110, y=90)
        okay_button = tkinter.Button(master=try_again_message, text='OK', font='Arial', command=clicked)
        okay_button.place(x=110, y=110)

    if num == current_num:
        window.destroy()
        win_message = tkinter.Tk()
        win_message.title('You won!')
        win_message.geometry("450x350")
        win_label = tkinter.Label(master=win_message, text=f'END of the game!\nYou found the missing number {num}',
                                  font=('Arial Bold', 10))
        win_label.place(x=110, y=30)
    else:
        try_again_message(num, current_num)


num = random.randint(0, 9)

window = tkinter.Tk()

window.title("Python Number Guessing Game")
window.geometry("450x350")
try_label = tkinter.Label(window, text='Enter your number: ', font=('Arial Bold', 15))
try_label.place(x=110, y=30)

txt = tkinter.Entry(master=window, width=30)
txt.place(x=110, y=70)

okay_button = tkinter.Button(master=window, text='OK', font='Arial', command=clicked)
okay_button.place(x=110, y=90)

window.mainloop()
