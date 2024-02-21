import pandas as pd

def Leercsv():
    dataframe = pd.read_csv('dataset.csv') #leer el archivo csv
    tam_chunk = int(input('Cual sera el tamaño de las ventanas/chuk?: ')) #tamaño de los chunks
    recorrido = int(input('Cual sera el recorrimiento de las ventanas/chunks?: ')) #tamaño del recorrido
    #print(dataframe)
    Alteraciones(tam_chunk, recorrido, dataframe)
    

def Combinacion_cadenas(ListaCadenas):
    if len(set(map(len, ListaCadenas))) > 1: #Se verifica que todas las cadenas tengan la misma longitud
        raise ValueError("Las cadenas deben tener la misma longitud") #Si no tienen la misma longitud, se levanta un error
    
    combinaciones = set(ListaCadenas) #Se crea un conjunto ya inicializado con las cadenas "originales"

    for i in range(len(ListaCadenas[0])): #Bucle para recorrer cada uno de los elementos de las cadenas
        for j in range(len(ListaCadenas)): #Bucle para recorrer cada una de las cadenas
            if all(cadena[i] == ListaCadenas[j][i] for cadena in ListaCadenas): #Si el elemento de la cadena en la posicion i es igual al de la cadena j en la posicion i
                continue #Se continua con el siguiente elemento
            for combinacion in list(combinaciones): #Bucle para recorrer cada una de las cadenas del conjunto combinaciones
                nueva_combinacion = list(combinacion) #Se convierte la cadena en una lista
                nueva_combinacion[i] = ListaCadenas[j][i] #Se reemplaza el elemento de la cadena por el de la cadena j
                combinaciones.add(''.join(nueva_combinacion)) #Se agrega la nueva combinacion al conjunto ya convertido nuevamente en cadena
    
    return combinaciones

def Alteraciones(tam_chunk,recorrido,dataframe):
    cadena = dataframe.iloc[0,3] #Seleccionar la columna 3 de la fila 0
    inicio = 0
    index = 0 #Indice de elemento en cadena
    rango = int(len(cadena)/recorrido + 1) #Calculo de iteraciones para realizar los recorridos de chunks 
    ListaChunks = [[] for lst in range(rango)] #Lista de listas que representan cada chunk
    filas = dataframe.shape[0] #numero de filas/Instrucciones

    for chunk in range (rango): #Bucle para recorrer los chunks/ventanas
        if index > len(cadena): #Si el indice es mayor al tamaño de la cadena
            break
        else: 
            for elemento in cadena[inicio:tam_chunk:1]: #Bucle para recorrer los elementos de cada chunk/ventana
                for instruccion in range(filas): #Bucle cada una de las instrucciones
                    if int(dataframe.iloc[instruccion,0]) == index: #Si la posicion del elemento coincide con el de la instruccion
                        if dataframe.iloc[instruccion,1] == cadena[index]: #Si el elemento coincide con la referencia de la instruccion
                            reemplazado = cadena[index] #Se guarda el elemento a reemplazar
                            cadena_list = list(cadena) #Se convierte la cadena en una lista
                            cadena_list[index] = dataframe.iloc[instruccion,2] #Se reemplaza el elemento por el de la instruccion
                            cadena = ''.join(cadena_list) #Se convierte la lista en cadena
                            ListaChunks[chunk].append(cadena)  #Se agrega la cadena modificada a la lista de variantes
                            cadena_list = list(cadena) #Se convierte la cadena en una lista
                            cadena_list[index] = reemplazado #Se regresa la cadena a su estado original
                            cadena = ''.join(cadena_list) #Se convierte la lista en cadena
                index = index + 1 #Se aumenta el indice
        inicio = inicio + recorrido #Se aumenta el inicio del chunk
        tam_chunk = tam_chunk + recorrido #Se aumenta el tamaño del chunk (Hasta donde se leeran los elementos)
        index = index - recorrido #Se disminuye el indice para tener en cuenta el recorrido del chunk
    
    for lst_ch in range(len(ListaChunks)): #Bucle para recorrer cada una de las listas de chunks
        if len(ListaChunks[lst_ch]) > 1: #Si la lista tiene mas de una variante
            Lst_Com = Combinacion_cadenas(ListaChunks[lst_ch]) #Se obtiene la combinacion de las cadenas
            for variante in Lst_Com: #Bucle para recorrer cada una de las variantes en el conjunto de combinaciones ralizadas
                if variante not in ListaChunks[lst_ch] and variante != cadena: #Si la variante no esta en el chunk y es diferente a la cadena original
                    ListaChunks[lst_ch].append(variante) #Se agrega la variante al chunk del que es perteneciente
        else:
            continue #Si no tiene mas de una variante, se continua con el siguiente chunk
    return ListaChunks #Se retorna la lista de chunks con sus variantes


def Combinacion_total(ListaChunks, cadena):
    Variantes = [] #Lista de variantes de la cadena
    Variantes.append(cadena) #Se agrega la cadena original a la lista de variantes
    for chunk in range(len(ListaChunks)): #Bucle para recorrer cada una de las listas de chunks
        for variante in ListaChunks[chunk]: #Bucle para recorrer cada una de las variantes en el chunk actual
            if variante not in Variantes and variante != cadena: #Si la variante no esta en la lista de variantes y es diferente a la cadena original
                Variantes.append(variante) #Se agrega la variante a la lista de variantes
    Combinaciones = Combinacion_cadenas(Variantes) #Se obtiene la combinacion de las variantes
    return Combinaciones #Se retorna el conjunto de combinaciones
        

def Combinacion_rango(ListaChunks, cadena, rango_inicio, rango_fin):
    Variantes = [] #Lista de variantes de la cadena
    Variantes.append(cadena) #Se agrega la cadena original a la lista de variantes
    Sublista=ListaChunks[rango_inicio:rango_fin] #Se obtiene la sublista de chunks
    if rango_inicio == rango_fin:
        Sublista = [ListaChunks[rango_inicio]]
    for chunk in Sublista: #Bucle para recorrer cada una de las listas de chunks
        for variante in chunk: #Bucle para recorrer cada una de las variantes en el chunk actual
            if variante not in Variantes and variante != cadena: #Si la variante no esta en la lista de variantes y es diferente a la cadena original
                Variantes.append(variante) #Se agrega la variante a la lista de variantes
    Combinaciones = Combinacion_cadenas(Variantes) #Se obtiene la combinacion de las variantes
    return Combinaciones #Se retorna el conjunto de combinaciones

#Leercsv()