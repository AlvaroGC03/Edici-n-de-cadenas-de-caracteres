#Equipo 8 GUI

import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk

root=Tk()

global lista
global chunks
global ventana

def principal():
    for widget in root.winfo_children():
        widget.destroy() #Esta funcion borra el contenido del widget
    ttk.Label(root, text="Menú de seleccion de archivo").place(x=435, y=15) #Imprime el titulo en la parte superior
    archivos = ttk.Label(root, text="Seleccione Archivo:") #Etiqueta de seleccionar archivo
    archivos.place(x=460, y=150) #posicion de la etiqueta archivo
    ttk.Button(root, text="Seleccionar", command=lambda: explorador(archivos)).place(x=360, y=280) #Boton que nos lleva a elegir el archivo en el del explorador
    #ttk.Button(root, text="Continuar", command=menu2).place(x=120, y=80)  (Se cambia de lugar para aparecer junto con la seleccion del archivo)
    ttk.Button(root, text="Salir", command=root.destroy).place(x=600, y=280) #Boton que cierra todo

#Explorador de archivos
def explorador(archivos):
    global lista
    global chunks
    global ventana

    #intvars
    chunks = IntVar()
    chunks.set(8)
    ventana = IntVar()
    ventana.set(5)


    f_path = askopenfilename(initialdir="/",
      title="Seleccion de Archivo", filetypes=(("*.xlsx*","csv"),("Todos los Archivos","*.*")))
    archivos.configure(text="Archivo Abierto: \n"+f_path)#realiza la apertura del explorador de archivos y lo limita a los tipos .xlsx y csv

    f_path.endswith('.csv')
    dataframe = pd.read_csv(f_path) #Lee el csv y lo mete dentro de dataframe

    #ttk.Label(root, text="Este es el string del csv:").place(x=20, y=480) #Imprime un mensaje para posteriormente imprimir la cadena
    lista = dataframe.iloc[0, 3] #Genera una lista de caracteres basando en los datos indicados en la posicion
    print(lista)
    #ttk.Label(root, text=lista).place(x=5, y=500) #Imprime la cadena principal

    ttk.Label(root, text="Ingrese el tamaño de los chunks").place(x=450, y=350) 
    ttk.Entry(root, textvariable=chunks).place(x=450, y=400) # etiqueta Solicita los chunks
    ttk.Button(root, text="Guardar", command=ImprimirVar).place(x=650, y=448)
    #ttk.Label(root, text=chunks).place(x=700, y=400)

    ttk.Label(root, text="Ingrese el tamaño de la ventana").place(x=450, y=450) 
    ttk.Entry(root, textvariable=ventana).place(x=450, y=500) # etiqueta Solicita los chunks

    ttk.Button(root, text="Continuar", command= menu2).place(x=900, y=600) #Este boton continua el programa hacia el menu2

def ImprimirVar():
    print(f"Chunks: {chunks.get()} ")
    ttk.Label(root, text=f"Chunks: {chunks.get()} ").place(x=700, y=400)
    print(f"Ventana: {ventana.get()} ")
    ttk.Label(root, text=f"Ventanas: {ventana.get()} ").place(x=700, y=500)

#Ventana de menu principal (Donde se decidira que se quiere hacer con los datos del archivo)
def menu2():
    for widget in root.winfo_children():
        widget.destroy() #Esta funcion borra el contenido del widget
    
    #ttk.Label(root, text=lista).place(x=5, y=500) #Imprime la cadena principal
        
    ttk.Label(root, text="El archivo fue selccionado correctamente").place(x=410, y=15) #Mensaje principal de la ventana
    ttk.Label(root, text="Deseas Continuar?").place(x=460, y=80) #Etiqueta de continuar
    ttk.Button(root, text="Si", command=menu3).place(x=470, y=200) #Boton que lleva al menu3 donde se imprimen los chunks
    ttk.Button(root, text="Regresar", command=principal).place(x=470, y=300) #Regresa a principal
    ttk.Button(root, text="Salir", command=root.destroy).place(x=900, y=600) #Boton que cierra todo
    #ttk.Button(root, text="Mostrar Todos", command=None).place(x=115, y=80)
    #ttk.Button(root, text="Por Selección", command=None).place(x=215, y=80)
    #ttk.Button(root, text="Salir", command=root.destroy).place(x=120, y=125)

#Por Rango
def menu3():
    for widget in root.winfo_children():
        widget.destroy()
    ttk.Label(root, text="Los Chunks que se han genrado son:").place(x=410, y=15) #Mensaje de los chunks que se generaron
    ttk.Button(root, text="Combinar todo", command=menu4).place(x=750, y=650) #Boton para menu4 
    ttk.Button(root, text="Combinar por Rango", command=menu5).place(x=850, y=650) #Boton para menu5

def menu4(): #Combinar todo
    for widget in root.winfo_children():
        widget.destroy()

    ttk.Label(root, text="Estas son todas las combinaciones posibles:").pack() #Etiqueta pricipal mensaje 
    barra = ttk.Scrollbar(root)
    barra.pack(side=RIGHT, fill="y")
    barra.config(command=root.yview)
    root.config(yscrollcommand=barra.set)


def menu5(): #Combinar por Rango
    for widget in root.winfo_children():
        widget.destroy()
    ttk.Label(root, text="Entre que rangos deseas combinar").pack()
    ttk.Entry(root, text="").pack()
    ttk.Entry(root, text="").pack()

    ttk.Button(root, text="Terminar", command=principal).pack()
    



#Ventana inicial
root.title("Actividad 4")

root.geometry("1000x700")

principal()

#ttk.Label(root, text="Menú de seleccion de archivo").place(x=435, y=15)
#archivos = ttk.Label(root, text="Seleccione Archivo:")
#archivos.place(x=460, y=150)
#ttk.Button(root, text="Seleccionar", command=explorador).place(x=360, y=280)
##ttk.Button(root, text="Continuar", command=menu2).place(x=120, y=80)  (Se cambia de lugar para aparecer junto con la seleccion del archivo)
#ttk.Button(root, text="Salir", command=root.destroy).place(x=600, y=280)



root.mainloop()