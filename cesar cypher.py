import tkinter as tk
from tkinter import ttk


def test_func (var = "", index = "", mode = ""):
    original = entry_var.get()
    cyphered = ""
    for x in original:
        a = ord(x) + int(spinbox.get())
        if a > 122:
            a = 97 + (a-123)
        cyphered = cyphered + (chr(a))
    label_var.set(cyphered)
    

#create window
window = tk.Tk()
window.title("cesar cypher")
window.geometry('500x300')

#tkinter variable
entry_var = tk.StringVar()
label_var = tk.StringVar()
sb_var = tk.IntVar()

#create widgets
label = ttk.Label(master=window, text= "label", textvariable=label_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=entry_var)
entry.pack()

spinbox = ttk.Spinbox(master=window, from_=0, to=25, command=test_func, textvariable=sb_var)
sb_var.set(0)
spinbox.pack()

#create trace stringVar
entry_var.trace_add('write', test_func)


#create mainloop
window.mainloop()