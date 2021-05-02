import tkinter
import random


screen = tkinter.Tk()
screen.geometry("600x500")
screen.title('App')

user_var = tkinter.StringVar()
machine_var = tkinter.StringVar()
Result = tkinter.StringVar()
Result.set('')


def rock():
    user_var.set('ROCK')
    machine_var.set(random.choice(['ROCK','PAPPER','SCISSOR']) )
    check()
def papper():
    user_var.set('PAPPER')
    machine_var.set(random.choice(['ROCK','PAPPER','SCISSOR']) )
    check()
def scissor():
    user_var.set('SCISSOR')
    machine_var.set(random.choice(['ROCK','PAPPER','SCISSOR']) )
    check()

def check():
    if user_var.get() == "ROCK" and machine_var.get() == "PAPPER" :
        Result.set('MACHINE WINS')
    elif user_var.get() == 'PAPPER'  and machine_var.get() == "ROCK" :
        Result.set('USER WINS')

    elif user_var.get() == 'PAPPER' and machine_var.get() == "SCISSOR" :
        Result.set('MACHINE WINS')
    elif user_var.get() == 'SCISSOR'  and machine_var.get() == "PAPPER" :
        Result.set('USER WINS')

    elif user_var.get() == 'SCISSOR' and machine_var.get() == "ROCK" :
        Result.set('MACHINE WINS')
    elif user_var.get() == 'ROCK'  and machine_var.get() == "SCISSOR" :
        Result.set('USER WINS')
    else:
        Result.set('TIE')

label = tkinter.Label(screen,text = "RPS",font=('arial',50,'bold'))
label.place(x = 230 , y = 0)


buton_rock = tkinter.Button(screen,text = "ROCK" , bg = "black" , fg = "white",height = 2,width = 17,font=('arial',10,'bold'),activebackground='black',activeforeground='white',command=rock)
buton_rock.place(x = 30 , y = 100)

buton_papper = tkinter.Button(screen,text = "PAPPER" , bg = "black" , fg = "white",height = 2,width = 17,font=('arial',10,'bold'),activebackground='black',activeforeground='white',command=papper)
buton_papper.place(x = 220 , y = 100)

buton_scissor = tkinter.Button(screen,text = "SCISSOR" , bg = "black" , fg = "white",height = 2,width = 17,font=('arial',10,'bold'),activebackground='black',activeforeground='white',command=scissor)
buton_scissor.place(x = 420 , y = 100)



user_choice = tkinter.Label(screen,text = "User : ",font=('arial',20,'bold'))
user_choice.place(x = 30 , y = 200)
User_button = tkinter.Button(screen,textvariable=user_var, bg = "white" , fg = "black",height = 2,width = 17,font=('arial',10,'bold'),activebackground='black',activeforeground='white')
User_button.place(x = 220 , y = 195)



Machine_choice = tkinter.Label(screen,text = "Machine : ",font=('arial',20,'bold'))
Machine_choice.place(x = 30 , y = 250)
Machine_button = tkinter.Button(screen,textvariable=machine_var, bg = "white" , fg = "black",height = 2,width = 17,font=('arial',10,'bold'),activebackground='black',activeforeground='white')
Machine_button.place(x = 220 , y = 250)

Result_area = tkinter.Label(screen,text = "Result_ : ",font=('arial',20,'bold'))
Result_area.place(x = 30 , y = 350)
Result_button = tkinter.Button(screen,textvariable=Result, bg = "white" , fg = "black",height = 2,width = 17,font=('arial',10,'bold'),activebackground='black',activeforeground='white')
Result_button.place(x = 220 , y = 350)

screen.mainloop()
