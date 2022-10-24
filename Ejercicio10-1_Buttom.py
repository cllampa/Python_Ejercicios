
import tkinter as tk
from tkinter import ttk

window= tk.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


def reiniciar(event):
    seleccionado.set(None)



#RADIOBUTTON

#Configuracion para el radio button
seleccionado=tk.StringVar()
rbtnOption1=ttk.Radiobutton(window, text="Opción 1",value="1", variable=seleccionado)
rbtnOption2=ttk.Radiobutton(window, text="Opción 2",value="2", variable=seleccionado)
rbtnOption3=ttk.Radiobutton(window, text="Opción 3",value="3", variable=seleccionado)

#Ubicacion radio button
rbtnOption1.grid(column=0, row=1, pady=5, padx=5)
rbtnOption2.grid(column=0, row=2, pady=5, padx=5)
rbtnOption3.grid(column=0, row=3, pady=5, padx=5)

#BUTON
btnReiniciar=ttk.Button(window,text="Reiniciar")
btnReiniciar.grid(column=0, row=4, sticky=tk.E,pady=5, padx=5)
btnReiniciar.bind('<Button-1>',reiniciar)

window.mainloop()