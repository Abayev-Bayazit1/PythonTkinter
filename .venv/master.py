import tkinter
from tkinter import *
from database import Database
from system  import System
from menu import Menu
from mainMenu import MainMenu



def main():
    db = Database()
    mn = Menu(db)
    system = System(db,mn)
    app = MainMenu(system)


if __name__ == '__main__':
    main()