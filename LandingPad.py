# Landing Pad
# Main window that the
# user is going to interact with


import tkinter as tk
from tkinter import Menu
from tkinter import ttk

class LandingPad:
    
    def __init__(self):
        # Creates the initial window along with all of
        # the windows statistics
        window = tk.Tk()
        window.title("Commissioner")

        # Creates the drop-down/menu bar and configs it to
        # the main window
        menuBar = Menu(window)
        window.config(menu=menuBar)

        # Creates the file menu
        fileMenu = Menu(menuBar)

        # Adding commands to the file menu drop-down
        fileMenu.add_command(label="New")

        # Add the file menu to the Overall menubar
        menuBar.add_cascade(label="File",menu=fileMenu)

        # Calender Frame where the user can see all of the
        # active commissions and general information about them
        calenderFrame = tk.LabelFrame(window,text="Calander")
        calenderFrame.grid(column=0,row=0)

        # Displays current date for user
        calenderDate = tk.Label(calenderFrame,text="Date : ")
        calenderDate.grid(column=0,row=0)

        # Commission Statistics Frame displays statistics about
        # their commissions (Average Completion Time, Average Price
        # per commission, etc.)
        commissionsStatsFrame = tk.LabelFrame(window,text="Statistics")
        commissionsStatsFrame.grid(column=1,row=0)

        #Testing Label for frame guilding
        testingLabelStats = tk.Label(commissionsStatsFrame,text="Testing")
        testingLabelStats.grid(column=0,row=0)

        # Starts displaying the window for user
        window.mainloop()


l = LandingPad()