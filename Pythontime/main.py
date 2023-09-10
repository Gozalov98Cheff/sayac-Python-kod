from tkinter import *
from datetime import datetime

temp = 0
after_id = ''

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    lable1.configure(text=str(f_temp))
    temp += 1


def strat_tick():
    btnStart.pack_forget()
    btnStop.pack()
    tick()

def stop_tick():
    btnStop.pack_forget()
    btnContinue.pack()
    btnReset.pack()
    root.after_cancel(after_id)

def continue_tick():
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStop.pack()
    tick()

def reset_tick():
    global temp
    temp = 0
    lable1.configure(text='00:00')
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStart.pack()


root = Tk()
root.title('sayac')
root.resizable(width=False, height=False)
root.geometry('300x200')


lable1 = Label(root, width=10, font=('Comic Sans MS', 30), text='00:00')
lable1.pack()

btnStart = Button(root, text='Baslat', font=('Comic Sans MS', 20), width=15, command=strat_tick)
btnStop = Button(root, text='Dur', font=('Comic Sans MS', 20), width=15, command=stop_tick)
btnContinue = Button(root, text='Devam', font=('Comic Sans MS', 20), width=15, command=continue_tick)
btnReset = Button(root, text='Sifirla', font=('Comic Sans MS', 20), width=15, command=reset_tick)
btnStart.pack()


root.mainloop()



