from tkinter import Toplevel, messagebox,Entry,Label,Button,Radiobutton
import tkinter as tk


class Menu():
    def __init__(self,db):
        self.db = db



    def login_menu(self,username,password):
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        succes = self.db.login(username,password)

        if not succes:
            messagebox.showerror("Error", "Login Failed")

        else:
            self.main_menu()



    def main_menu(self):
        new_window = Toplevel()
        new_window.title("Main menu")
        new_window.geometry("500x500")


        def setting():
            new_window.destroy()
            setting_window = Toplevel()

            setting_window.title("Settings")
            setting_window.geometry("400x400")

            update_password = Button(setting_window,text="Update Password",command= lambda: self.passwordMenu(setting_window))
            update_password.pack(padx=5, pady=10)


        setting = Button(new_window,text="Settings",command=setting)
        setting.pack(pady = 200)



    def passwordMenu(self,setting_window):
        #это меню для ввода логина и пароля
        setting_window.destroy()
        updater_menu = tk.Tk()
        updater_menu.geometry("400x400")

        updater_menu.title("Updater Menu")

        # создаем label и поле ввода
        username_label = Label(updater_menu, text="Username")
        username_label.pack(pady=10)

        # делаем поле ввода для юзернейма
        entry_username = Entry(updater_menu)
        entry_username.pack(pady=10)

        password_label = Label(updater_menu, text="Password")
        password_label.pack(pady=10)

        # поле ввода для пароля
        password_entry = Entry(updater_menu, show="*")
        password_entry.pack(pady=10)

 #дочерняя функция которая общается с БД
        def update_password():
            username = entry_username.get()
            password = password_entry.get()

            if not username or not password:
                messagebox.showerror("Error", "Please enter both username and password")

            succes = self.db.update_password(username,password)

            if not succes:
                messagebox.showerror("Error", "Update Failed")
            else:
                messagebox.showinfo("Success", "Password Updated")
                updater_menu.destroy()

        #кнопка чтобы дернуть нашу дочернуюю функцию
        update_button = Button(updater_menu, text="Update", command=update_password)
        update_button.pack(pady=10)
