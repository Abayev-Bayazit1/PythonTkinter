import tkinter
from tkinter import *
from database import Database
from system  import System
from menu import Menu



def main():
    db = Database()
    mn = Menu(db)
    system = System(db,mn)

    #cоздание окна
    window = Tk()
    window.geometry("400x400")
    window.title("Main menu")

    #создание двух кнопок
    login = Button(window, text="Login",command=system.login)
    login.place(x=200, y=100,anchor=CENTER)

    register = Button(window, text="Register",command=system.register)
    register.place(x=200, y=150,anchor=CENTER)

    exit = Button(window, text="Exit", command=lambda: system.exit(window))
    exit.place(x=200, y=300,anchor=CENTER)


    window.mainloop()



if __name__ == '__main__':
    main()