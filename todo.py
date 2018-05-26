from tkinter import Tk
from tkinter import *


class ChecklistGUI:
    def __init__(self, master):
        self.master = master
        master.title("ToDo Checklist")
        self.n = 2
        self.item_list = [()]
        self.label = Label(master, text="Enter your items below")
        self.label.grid(row=1,column=1,columnspan=2)
        
        tmpbutt = Checkbutton(master, command=lambda row=self.n,: self.check(row))
        tmpbutt.grid(row=self.n,column=1)
        tmpent = Entry(master)
        tmpent.grid(row=self.n,column=2)
        tmpent.focus()
        self.item_list.append((tmpbutt, tmpent))
        tmpbutt = None
        tmpent = None
        
        self.plus = Button(master, text="   +   ", command=self.add_one)
        self.plus.grid(row=self.n+1,column=2)

    def check(self, row):
        textobj = self.item_list[row-1][1]
        txt = str(textobj.get())

        if '\u0336' not in txt:            
            txt = '\u0336'.join(txt) + '\u0336'
            print("Checked: " + str(row) + " - " + txt )
        else:
            txt = txt.replace('\u0336','')

        textobj.delete(0, END)
        textobj.insert(0, txt)
        

    ## End check


    def add_one(self):
        self.n += 1
        tmpbutt = Checkbutton(self.master, command=lambda row=self.n,: self.check(row))
        tmpbutt.grid(row=self.n,column=1)
        tmpent = Entry(self.master)
        tmpent.grid(row=self.n,column=2)
        self.item_list.append((tmpbutt, tmpent))
        tmpbutt = None
        tmpent = None

        self.plus.grid(row=self.n+1,column=2)
    ## End add_one



## End class ChecklistGUI

## Code Entry ##
root = Tk()
my_gui = ChecklistGUI(root)
root.mainloop()