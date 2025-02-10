from tkinter import Toplevel, Label, Entry, Button, messagebox
from tkinter import CENTER


class System:
    def __init__(self,db,mn):
        self.db = db
        self.mn = mn



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
        password_entry = Entry(new_window,show="*")
        password_entry.pack(pady=10)

        def attempt_login():
            username = entry_username.get()
            password = password_entry.get()

            if not username or not password:
                messagebox.showerror("Error", "Please enter both username and password")
                return

            if self.db.login(username,password):
                # messagebox.showinfo("Login", "Login Successful")
                new_window.destroy()
                self.mn.login_menu(username,password)
            else:
                messagebox.showerror("Error", "Login Failed")


        log_in = Button(new_window, text="Log in",command= attempt_login)
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