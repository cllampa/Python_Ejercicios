import tkinter as tk
from tkinter import ttk

window= tk.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

#LABEL

lblSaludo=tk.Label(window,text="Elija un lenguaje de programación")
lblSaludo.grid(column=0, row=0, sticky=tk.W,pady=5, padx=5)

#LISTBOX
list=["Python", "C++", "Java"]
list_items=tk.StringVar(value=list)
lstboxLenguajes=tk.Listbox(window, height=4, listvariable=list_items)
lstboxLenguajes.grid(column=0, row=1, sticky=tk.W)

window.mainloop()
