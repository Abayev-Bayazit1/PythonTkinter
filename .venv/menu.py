from tkinter import Toplevel, messagebox

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
            new_window = Toplevel()
            new_window.title("Main menu")
            new_window.geometry("600x600")




