# Landing Pad
# Main window that the
# user is going to interact with


import tkinter as tk

class LandingPad:

    def __init__(self):
        window = tk.Tk()
        window.title("Commissioner")

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


        # Starts displaying the window for user
        window.mainloop()


l = LandingPad()