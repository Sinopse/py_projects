from tkinter import * # calling tkinter without prefix
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# setting up the main application window
root = Tk()
root.title("Feet to meters")

# creating a content frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# creating the entry widget
feet = StringVar() # declaring variable of a class StringVar
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) # mainframe passed in as the first param
feet_entry.grid(column=2, row=1, sticky=(W, E))

# remaining widgets
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(columns=3,row=2, sticky=W)

ttk.Label(mainframe, text="feet").grid(columns=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(columns=3, row=2, sticky=W)

# finishing touches
for child in mainframe.winfo_children():      # adds padding to the widgets
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()                           # cursor starts in the entry widget
root.bind("<Return>", calculate)             # pressing Enter does the calculation

# start the main event loop
root.mainloop()
