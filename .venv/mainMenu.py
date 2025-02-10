import tkinter as tk
import system

class MainMenu:
    def __init__(self, system):
        self.system = system

        # cоздание окна
        self.window = tk.Tk()
        self.window.geometry("400x400")
        self.window.title("Main menu")

        # создание двух кнопок
        login = tk.Button(self.window, text="Login", command=self.system.login)
        login.place(x=200, y=100, anchor=tk.CENTER)

        register = tk.Button(self.window, text="Register", command=self.system.register)
        register.place(x=200, y=150, anchor=tk.CENTER)

        exit = tk.Button(self.window, text="Exit", command=lambda: self.system.exit(self.window))
        exit.place(x=200, y=300, anchor=tk.CENTER)

        self.window.mainloop()

