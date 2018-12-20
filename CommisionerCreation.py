import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

from Commisioner import Commisioner

#Creating a Commisioner for easy use later
class CommisionerWindow:

    def __init__(self):
        self.comOut = Commisioner("",0,"")
        self.createWindow()
    
    def __del__(self):
        return self.comOut

    def destroyWindow(self,window,isReturning):
        window.quit()
        window.destroy()


        
    def createWindow(self):
        win = tk.Tk()
        win.title("Creating Commisioner...")
        
        #win.geometry("300x300")

        subFrame = ttk.LabelFrame(win,text="General Info")
        subFrame.grid(row=0,column=0)

        #Name Infomation
        ttk.Label(subFrame,text="Name:").grid(row=0,column=0)
        ttk.Entry(subFrame, width=12).grid(row=0,column=1)

        #Price Infomation
        ttk.Label(subFrame,text="Price:").grid(row=0,column=2)
        ttk.Entry(subFrame,width=12).grid(row=0,column=3)

        #Email Information
        ttk.Label(subFrame,text="Email:").grid(row=1,column=0)
        ttk.Entry(subFrame,width=12).grid(row=1,column=1)
        
        #Priority Information
        ttk.Label(subFrame,text="Priority Level:").grid(row=1,column=2)
        ttk.Combobox(subFrame,width=9,values=["Low","Medium","High"]).grid(row=1,column=3)

        #Notes Information
        ttk.Label(subFrame,text="Notes:").grid(row=3,column=0)
        scrolledtext.ScrolledText(win,width=25,height=10,wrap=tk.WORD).grid(row=1,column=0)

        #Aligns buttons nicely
        buttonFrame = ttk.Frame(win)
        buttonFrame.grid(row=2,column=0)

        ttk.Button(buttonFrame,text="Submit",command=lambda: self.destroyWindow(win,True)).grid(row=0,column=0)
        ttk.Button(buttonFrame,text="Cancel",command=lambda: self.destroyWindow(win,False)).grid(row=0,column=1)

        win.mainloop()

test = CommisionerWindow()
print(test.comOut.getName())