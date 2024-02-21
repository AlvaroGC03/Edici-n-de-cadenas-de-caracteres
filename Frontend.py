#Equipo 8 GUI

import pandas as pd
import tkinter as tk
import Backend as bk
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk

root=Tk()

def principal():
    for widget in root.winfo_children():
        widget.destroy() #Esta funcion borra el contenido del widget
    ttk.Label(root, text="Menú de seleccion de archivo").place(x=490, y=15) #Imprime el titulo en la parte superior
    archivos = ttk.Label(root, text="Seleccione Archivo:") #Etiqueta de seleccionar archivo
    archivos.place(x=515, y=150) #posicion de la etiqueta archivo
    ttk.Button(root, text="Seleccionar", command=lambda: explorador(archivos)).place(x=410, y=280) #Boton que nos lleva a elegir el archivo en el del explorador
    ttk.Button(root, text="Salir", command=root.destroy).place(x=660, y=280) #Boton que cierra todo

#Explorador de archivos
def explorador(archivos):
    recorrido = tk.StringVar()
    ventana = tk.StringVar()
    f_path = askopenfilename(initialdir="/",
    title="Seleccion de Archivo", filetypes=(("*.xlsx*","csv"),("Todos los Archivos","*.*")))
    archivos.configure(text="Archivo Abierto: \n"+f_path)#realiza la apertura del explorador de archivos y lo limita a los tipos .xlsx y csv
    f_path.endswith('.csv')
    dataframe = pd.read_csv(f_path) #Lee el csv y lo mete dentro de dataframe
    ttk.Label(root, text="Ingrese el tamaño de la ventana").place(x=500, y=350) 
    ttk.Entry(root, textvariable=ventana).place(x=500, y=400) # etiqueta Solicita los chunks
    ttk.Label(root, text="Ingrese el tamaño del recorrido").place(x=500, y=450) 
    ttk.Entry(root, textvariable=recorrido).place(x=500, y=500) # etiqueta Solicita los chunks
    ttk.Button(root, text="Continuar", command=lambda: menu2(dataframe, ventana.get(), recorrido.get())).place(x=1000, y=650) #Este boton continua el programa hacia el menu2
    

#Ventana de menu principal (Donde se decidira que se quiere hacer con los datos del archivo)
def menu2(dataframe, ventana, recorrido):
    for widget in root.winfo_children():
        widget.destroy() #Esta funcion borra el contenido del widget
    
    ttk.Label(root, text="El archivo fue leido correctamente").place(x=500, y=15) #Mensaje principal de la ventana
    ttk.Label(root, text="Deseas Continuar?").place(x=540, y=80) #Etiqueta de continuar
    ttk.Button(root, text="Si", command=lambda: menu3(dataframe, ventana, recorrido)).place(x=550, y=200) #Boton que lleva al menu3 donde se imprimen los chunks
    ttk.Button(root, text="Regresar", command=principal).place(x=550, y=300) #Regresa a principal
    ttk.Button(root, text="Salir", command=root.destroy).place(x=1000, y=650) #Boton que cierra todo

#Por Rango
def menu3(dataframe, ventana, recorrido):
    for widget in root.winfo_children():
        widget.destroy()
    cadena = dataframe.iloc[0,3] #Seleccionar la columna 3 de la fila 0
    ListaChunks = bk.Alteraciones(int(ventana), int(recorrido), dataframe)
    ttk.Label(root, text="Los Chunks que se han genrado son:").place(x=500, y=50) #Mensaje de los chunks que se generaron
    ttk.Button(root, text="Combinar todo", command=lambda: menu4(ListaChunks, cadena)).place(x=750, y=650) #Boton para menu4 
    ttk.Button(root, text="Combinar por Rango", command=lambda: menu5(ListaChunks, cadena)).place(x=855, y=650) #Boton para menu5
    ttk.Button(root, text="Regresar", command=principal).place(x=990, y=650) #Regresa a principal
    # Crea un widget de texto
    output = tk.Text(root)
    output.pack(expand=True, fill="x")
    # Se inserta el texto en el widget de texto 
    for chunk in range(len(ListaChunks)):
        if ListaChunks[chunk] == []:
            output.insert(tk.END, f'\n  Chunk: {chunk} (vacio)\n')
        else:
            output.insert(tk.END, f'\n  Chunk: {chunk}\n')
            for variante in range(len(ListaChunks[chunk])):
                output.insert(tk.END,'  ' + str(ListaChunks[chunk][variante]) + '\n')
    output.see()
    


def menu4(ListaChunks, cadena): #Combinar todo
    for widget in root.winfo_children():
        widget.destroy()
    ttk.Label(root, text="Estas son todas las combinaciones posibles:").place(x=475, y=50) #Etiqueta pricipal mensaje
    ttk.Button(root, text="Regresar", command=principal).place(x=900, y=650) #Regresa a principal
    ttk.Button(root, text="Salir", command=root.destroy).place(x=1000, y=650) #Boton que cierra todo
    combinaciones = list(bk.Combinacion_total(ListaChunks, cadena))
    # Crea un widget de texto
    output = tk.Text(root)
    output.pack(expand=True, fill="x")
    # Se inserta el texto en el widget de texto 
    output.insert(tk.END, f'\n  Combinaciones posibles de la todas las variantes:\n')
    for variante in range(len(combinaciones)):
        output.insert(tk.END,'\n    ' + str(combinaciones[variante]) + '\n')
    output.insert(tk.END, f'\n\n  Total de combinaciones: {len(combinaciones)}\n')
    output.see()


def menu5(ListaChunks, cadena): #Combinar por Rango
    for widget in root.winfo_children():
        widget.destroy()
    rango_inicio = tk.StringVar()
    rango_fin = tk.StringVar()
    ttk.Label(root, text="Entre que rangos deseas combinar").place(x=495, y=15)
    ttk.Label(root, text="Del rango: ").place(x=470, y=50)
    ttk.Label(root, text="Al rango: ").place(x=470, y=80)
    ttk.Entry(root, textvariable=rango_inicio).place(x=560, y=50)
    ttk.Entry(root, textvariable=rango_fin).place(x=560, y=80)
    ttk.Button(root, text="Continuar", command=lambda: Mostrar_rangos(ListaChunks, cadena, rango_inicio, rango_fin)).place(x=540, y=110)
    
def Mostrar_rangos(ListaChunks, cadena, rango_inicio, rango_fin):
    ttk.Button(root, text="Regresar", command=principal).place(x=900, y=650) #Regresa a principal
    ttk.Button(root, text="Salir", command=root.destroy).place(x=1000, y=650) #Boton que cierra todo
    combinaciones = list(bk.Combinacion_rango(ListaChunks, cadena, int(rango_inicio.get()), int(rango_fin.get())))
    # Crea un widget de texto
    output = tk.Text(root)
    output.pack(expand=True, fill="x")
    # Se inserta el texto en el widget de texto 
    output.insert(tk.END, f'\n  Combinaciones posibles de la todas las variantes:\n')
    for variante in range(len(combinaciones)):
        output.insert(tk.END,'\n    ' + str(combinaciones[variante]) + '\n')
    output.insert(tk.END, f'\n\n  Total de combinaciones: {len(combinaciones)}\n')
    output.see()

#Ventana inicial
root.title("Actividad 4")
root.geometry("1100x700")

principal()

root.mainloop()