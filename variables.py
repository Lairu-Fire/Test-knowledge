import tkinter as tk
from tkinter import ttk


def test_func (var, index, mode):
    print(string_var.get().upper())

#create window
window = tk.Tk()
window.title("tkinter variables")
window.geometry('500x300')

#tkinter variable
string_var = tk.StringVar()

#create widgets
label = ttk.Label(master=window, text= "label", textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

#create trace stringVar
string_var.trace_add('write', test_func)


#create mainloop
window.mainloop()