#!python3
from tkinter import *
from tkinter import filedialog

class ChecklistGUI:
    ''' GUI class for checklist/todo program '''
    def __init__(self, master):
        '''Initialize default values'''
        self.master = master
        self.master.title("To Do Checklist")
        self.n = 2
        self.item_list = [()]
        self.label = Label(self.master, text="Enter your items below")
        self.label.grid(row=1,column=1,columnspan=2)
        
        # setup std checkbox and textbox
        tmpbutt = Checkbutton(self.master, command=lambda row=self.n,: self.check_button(row))
        tmpbutt.grid(row=self.n,column=1)

        tmpent = Entry(self.master)
        tmpent.grid(row=self.n,column=2)
        tmpent.focus()
        tmpent.bind('<Return>', self.enter_event)
        # add them to the 'global' list of all the items
        self.item_list.append((tmpbutt, tmpent))
        tmpbutt = None
        tmpent = None
       
        # add a "plus 1 item" button
        self.plus = Button(self.master, text="   +   ", command=self.add_one)
        self.plus.grid(row=self.n+1,column=2)
    
    ## End __init__

    def check_button(self, row):
        '''Check & Cross out items on the checklist'''
        textobj = self.item_list[row-1][1]
        txt = str(textobj.get())

        if '\u0336' not in txt:            
            txt = '\u0336'.join(txt) + '\u0336'
            #print("Checked: " + str(row) + "  - " + txt )
        else:
            txt = txt.replace('\u0336','')

        textobj.delete(0, END)
        textobj.insert(0, txt)
    ## End check_button

    def enter_event(self, event):
        '''Add one item to the checklist, need this method to call another...'''
        self.add_one()

    def new(self):
        '''Wipe out whatever's on the checklist'''
        self.n = 2
        for i in self.item_list:
            for j in i:
                j.destroy()

        self.item_list = [()]
        tmpbutt = Checkbutton(self.master, command=lambda row=self.n,: self.check_button(row))
        tmpbutt.grid(row=self.n,column=1)

        tmpent = Entry(self.master)
        tmpent.grid(row=self.n,column=2)
        tmpent.focus()
        tmpent.bind('<Return>', self.enter_event)
        
        self.item_list.append((tmpbutt, tmpent))
        tmpbutt = None
        tmpent = None
    ## End new

    def save(self):
        '''Save current checklist to file'''
        pass

    def load(self):
        '''Load checklist from file to program'''
        filename = filedialog.askopenfilename(initialdir=".", title="Select file",
                                                filetypes=(("Checklist Files", "*.chk"), ("all files", "*.*")))
        items = [()]
        with open(filename, "r") as lines:
            for line in lines:
                #print(line)
                spl = line.split("`") # note that this is a tick `
                x = spl[0].strip()
                itm = spl[1].strip()
                items.append((x,itm))
        if len(items) < 1:
            return
        else:
            self.item_list = [()]
            self.n = 1
        for i in items:
            if len(i) < 2:
                continue
            #print(i)
            self.load_one(i)
            
    ## End load

    def load_one(self, itm):
        '''Load one item into the checklist'''
        if len(itm) < 1:
            return
        self.n += 1
        tmpbutt = Checkbutton(self.master, command=lambda row=self.n,: self.check_button(row))
        tmpbutt.grid(row=self.n,column=1)

        tmpent = Entry(self.master)
        tmpent.bind('<Return>', self.enter_event)
        tmpent.insert(0,str(itm[1]))
        tmpent.grid(row=self.n,column=2)

        self.item_list.append((tmpbutt, tmpent))

        # If the box is checked, check it and strikethru
        if 'x' in itm[0]:
            tmpbutt.invoke()

        tmpbutt = None
        tmpent = None

        self.plus.grid(row=self.n+1,column=2)
    ## End load_one


    def add_one(self):
        '''Add a new item to the checklist'''
        self.n += 1
        tmpbutt = Checkbutton(self.master, command=lambda row=self.n,: self.check_button(row))
        tmpbutt.grid(row=self.n,column=1)

        tmpent = Entry(self.master)
        tmpent.grid(row=self.n,column=2)
        tmpent.bind('<Return>', self.enter_event)

        self.item_list.append((tmpbutt, tmpent))
        tmpbutt = None
        tmpent = None

        self.plus.grid(row=self.n+1,column=2)
    ## End add_one

## End class ChecklistGUI

### Code Entry ###
root = Tk()
my_gui = ChecklistGUI(root)

mb = Menu(root)
filemenu = Menu(mb, tearoff=0)
filemenu.add_command(label="New", command=my_gui.new)     
filemenu.add_command(label="Open", command=my_gui.load)
filemenu.add_command(label="Save as", command=my_gui.save)
filemenu.add_command(label="Exit", command=root.quit)
mb.add_cascade(label="File", menu=filemenu)
mb.add_cascade(label="Exit", command=root.quit)

root.config(menu=mb)
root.mainloop()
