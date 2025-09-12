import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    aaaa = entry_int.get()*2
    output_string.set(aaaa)




#create window
window = ttk.Window(themename= "darkly")
window.title("Teste")
window.geometry('300x150')

#widgets
test_label = ttk.Label(master=window, text="Miles to kilometers", font="calibre 24 bold")
test_label.pack()
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="convert", command= convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady = 10)


output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                        font="calibre 24",
                        textvariable= output_string)
output_label.pack()



window.mainloop()

