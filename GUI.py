
''' Aplicacion de usuario para las busquedas (GUI) '''

from tkinter import *
from tkinter import ttk 
from eutils import Eutils

def ejecutarBusqueda ():


	term = busqueda.get()
	search = Eutils(term,ret_max=3)
	txtrespuesta = '\n'.join(search.titles)
	result.set(txtrespuesta)



root = Tk()
root.title("EUTILITIES")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# etiqueta "busqueda:"
lblBusqueda = ttk.Label(mainframe, text="Busqueda: ",).grid(column=1, row =1, sticky=W)

# cuadro de texto para incluir el texto de busqueda
busqueda = StringVar()
txtBusqueda = ttk.Entry(mainframe, width=50, textvariable=busqueda)
txtBusqueda.grid(column=2, row=1, sticky=W)

# etiqueta donde se muestra el texto encontrado

result = StringVar()
lblResult = ttk.Label(mainframe, textvariable=result)
lblResult.grid(column=(1), row=2, sticky=W)


# boton para ejecutar la busqueada (despues lo quitaremos)

btnGo = ttk.Button(mainframe,text="Buscar", command=ejecutarBusqueda)
btnGo.grid(column=1,row=3)

#txtBusqueda.focus()
txtBusqueda.bind("<Return>", ejecutarBusqueda)

root.mainloop()






