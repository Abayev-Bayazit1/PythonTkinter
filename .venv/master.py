import tkinter
from tkinter import *
from tkinter import Toplevel,messagebox
from database import Database


class System():
    def __init__(self,db):
        self.db = db



    def login(self):
        #новое окно
        new_window = Toplevel()
        new_window.title("Login Form")

        new_window.geometry("400x300")

        #создаем label и поле ввода
        username_label = Label(new_window, text="Username")
        username_label.pack(pady=10)

        #делаем поле ввода для юзернейма
        entry_username = Entry(new_window)
        entry_username.pack(pady=10)


        password_label = Label(new_window, text="Password")
        password_label.pack(pady=10)

        #поле ввода для пароля
        password_entry = Entry(new_window)
        password_entry.pack(pady=10)


        log_in = Button(new_window, text="Log in")
        log_in.place(x=200,y=250,anchor=CENTER)




    def register(self):
        new_window = Toplevel()
        new_window.title("Registration Form")
        new_window.geometry("400x300")

        username_label = Label(new_window, text="Username")
        username_label.pack(pady=10)

        entry_username = Entry(new_window)
        entry_username.pack(pady=10)

        password_label = Label(new_window, text="password")
        password_label.pack(pady=10)

        entry_password = Entry(new_window)
        entry_password.pack(pady=10)

        def register_user():
            username = entry_username.get()
            password = entry_password.get()

            if not username or not password:
                messagebox.showerror("Error", "Please enter both username and password")
                return

            success = self.db.add_user(username, password)

            if success:
                messagebox.showinfo("Success", "User registered successfully")
                new_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to register")


        register = Button(new_window, text="Register",command=register_user)
        register.place(x=200,y=250,anchor=CENTER)




    def exit(self,window):
        window.quit()



def main():
    db = Database()
    sys = System(db)

    #cоздание окна
    window = Tk()
    window.geometry("400x400")
    window.title("Main menu")

    #создание двух кнопок
    login = Button(window, text="Login",command=sys.login)
    login.place(x=200, y=100,anchor=CENTER)

    register = Button(window, text="Register",command=sys.register)
    register.place(x=200, y=150,anchor=CENTER)

    exit = Button(window, text="Exit", command=lambda: sys.exit(window))
    exit.place(x=200, y=300,anchor=CENTER)








    window.mainloop()

if __name__ == '__main__':
    main()