import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer


#columnas a minúsculas
def columnas_minusculas(dataframe):
    """
    Función para cambiar los nombres de las columnas de un datframe a minúsculas y eliminar posibles espacios antes y después de los nombres
    
    Args:
        dataframe (DataFrame): dataframe 

    Returns:
        dataframe (DataFrame): Devuelve el mismo dataframe pero con el nombre de las columnas en minúsculas 
    """
    nuevas_columnas = {columna: columna.lower().strip() for columna in dataframe.columns}
    dataframe.rename(columns=nuevas_columnas, inplace= True)

    return dataframe

def cambiar_nombre_columnas(dataframe, diccionario):
    """
    Función para cambiar los nombres de las columnas de un datframe
    
    Args:
        dataframe (DataFrame): dataframe 
        diccionario (dict): diccionario dónde las llaves son los nombres de las columnas y los valores los nuevos nombres

    Returns:
        dataframe (DataFrame): Devuelve el mismo dataframe pero con el nombre de las columnas cambiado
    """
    dataframe.rename(columns=diccionario, inplace= True)

    return dataframe

# columna a integer:
def to_int(num):
    """
    Convierte una cadena que representa un número a tipo de dato integer

    Args:
        num (str): Una cadena que representa un número entero.

    Returns:
        int: El número equivalente en formato de tipo integer.
    """
    return int(num)

# columna a float:
def to_float(numero):
    """
    Convierte una cadena que representa un número decimal a un número con punto flotante,.cambiando además, las comas por los puntos.

    Args:
        numero (str): Una cadena que representa un número decimal.

    Returns:
        float: El número equivalente en formato de tipo float.
    """
    try:
        if "," in numero:
            return float(numero.replace(",","."))
        else:
            return float(numero)
    except:
        return numero
    
def tonull(numero):
    """
    Convierte los números negativos en np.nan

    Args:
        numero (str): un número

    Returns:
        float: El número si es positivo o np.nan en caso de que fuera negativo.
    """
    if numero <0:
        return np.nan
    else:
        return numero    

def col_to_int(columna):
    """
    Convierte los datos de una columna númerica a tipo integer y luego toda la columna a tipo integer

    Args:
        columna (Series): columna de un dataframe que pasar a tipo int

    Returns:
        columna (Series): devuelve la columna del dataframe en tipo int
    """ 
    return columna.apply(to_int).astype(int)

def nan_to_str(columna, cadena):
    """
    Convierte los datos nulos de una columna categórica al string introducido

    Args:
        columna (Series): columna de un dataframe donde cambiar los nulos por 'desconocido'
        cadena (str): un string por el que se quiere cambiar los valores nulos

    Returns:
        columna (Series): devuelve la columna del dataframe con los nulos cambiados
    """  
    return columna.replace(np.nan, cadena)

def str_to_nan(columna, cadena):
    """
    Convierte un string a un nulo de numpy

    Args:
        columna (Series): columna de un dataframe donde cambiar un string por np.nan

    Returns:
        columna (Series): devuelve la columna del dataframe con los strings especificados cambiados por nulos 
    """  
    return columna.replace(cadena, np.nan)

def a_barra_baja(columna, cadena):
    """
    Reemplazar un string a barras bajas en una columna de strings y elimina los espacios del principio y final de los valores

    Args:
        columna (Serie): Una serie de pandas que resprensenta a una columna del dataframe de tipo 'object'
        cadena (str): cadena a sustituir por una barra baja (" ", "-", ...)

    Returns:
        columna (Serie): la serie que representa una columna del datafrme con la string cambiada por una barra baja
    """
    return columna.str.strip().str.replace(cadena,"_")

def valores_col_lower(columna):
    """
    Convierte los valores de una columna de un dataframe a minúscula

    Args:
        columna (Serie): Una serie de pandas que resprensenta a una columna del dataframe de tipo 'object'

    Returns:
        columna (Serie): la serie que representa una columna del datafrme con los valores en minúsculas
    """
    return columna.str.strip().str.lower()

def cambio_valores_dic(columna, diccionario):
    """
    Reemplazar los valores de una columna

    Args:
        columna (Serie): Una serie de pandas que resprensenta a una columna del dataframe
        diccionario(dict): un diccionario donde las llaves son valores en la columna y los valores son los valores a cambiar

    Returns:
        columna (Serie): La columna del data frame con los valores cambiados
    """
    return columna.replace(diccionario)

def cambio_valores_map(columna, mapa):
    """
    Reemplazar los valores de una columna

    Args:
        columna (Serie): Una serie de pandas que resprensenta a una columna del dataframe
        mapa (map): un mapa donde las llaves son valores en la columna y los valores son los valores a cambiar

    Returns:
        columna (Serie): La columna del data frame con los valores cambiados
    """
    return columna.map(mapa)

def cambio_valores_individual(columna, cadena1, cadena2):
    """
    Reemplazar los valores de una columna

    Args:
        columna (Serie): Una serie de pandas que resprensenta a una columna del dataframe
        cadena1 (str): valor en la columna que se quiere cambiar
        cadena2 (str): valor por el que se quiere cambiar

    Returns:
        columna (Serie): La columna del data frame con los valores cambiados
    """
    return columna.str.replace(cadena1, cadena2)

def eliminar_col(dataframe, nombre_columna):
    """
    Elimina columnas de un dataframe

    Args:
        dataframe (DataFrame): un dataframe donde eliminar la columna
        nombre_columna (str): el nombre de la columna a eliminar
    
    Returns:
        dataframe (DataFrame): el dataframe sin la columna a eliminar
    """
    dataframe.drop(nombre_columna, axis=1, inplace= True)

    return  dataframe

def primer_digito(numero):
    """
    Devuelve el primr digito de un número   

    Args:
        numero (int): un número
    
    Returns:
        número (int): el primer digito del número introducido
    """
    digitos = [int(d) for d in str(numero)]
    return digitos[0]     

def sin_dolar(columna):
    """
    Elimina los símbolos de dolar en los valores de una columana

    Args:
        columna (Serie): Una serie de pandas que resprensenta a una columna del dataframe 

    Returns:
        columna (Serie): la serie que representa una columna del datafrme con los símbolos de doalr eliminados
    """
    return columna.str.replace("$", "")

def rellena_nulos_suma(columna):
    """
    Rellena los nulos con una suma acumulativa

    Args:
        columna (Serie): Una serie de pandas que resprensenta a una columna del dataframe 

    Returns:
        columna (Serie): la serie que representa una columna del datafrme con los nulos rellenados
    """
    return columna.isnull().cumsum()

def elimina_duplicados_columna(dataframe, nombre_columna, mantener = 'first'):
    """
    Elimina los duplicados en una columana de un dataframe

    Args:
        nombre_columna (str): el nokmbre de la columna donde eliminar duplicados
        keep (str): cadena de texto 
            - 'first' (por defecto): mantiene el primer elemento de los duplocados 
            - 'last' (por defecto): mantiene el último elemento de los duplocados 

    Returns:
        dataframe (DataFrame): un dataframe donde se han eliminado los duplicados en una columna concreta
    """
    dataframe.drop_duplicates(subset=nombre_columna,keep=mantener, inplace=True)

    return dataframe

def col_autoincremental(dataframe, nombre_columna, posicion=0, num=1):
    """
    crea una columna nueva con valores autoincrementales desde el indicado

    Args:
        dataframe (DataFrame): un dataframe donde añadir la columna autoincremental
        nombre_columna (str): el nombre de la columna que se añadirá
        posicion (int): posición del dataframe dónde añadir la columna (por defecto, 0)
        num (int): número apartir edl que se empezara a autoincrementar

    Returns:
        dataframe (DataFrame): un dataframe donde añadir la columna autoincremental
    """
    dataframe.insert(posicion, nombre_columna, range(num, num + len(dataframe)))

    return dataframe


def imputar_nulos_knn(dataframe, lista_columnas, vecinos = 5):
    """
    Imputa los nulos en las columnas seleccionadas segun el método de los veciona (knn)

    Args:
        dataframe (DataFrame): un dataframe donde imputar los hulos
        lista_columnas (list): lista de las columnas del dataframe donde imputar los nulos
        vecinos = número de vecinos a tener en cuenta a la hora de imputar los nulos (por defecto, 5)

    Returns:
        imputer_knn_imputado (array): devuelve un array de las columnas con los nulos ya imputados
    """
    imputer_knn = KNNImputer(n_neighbors = vecinos)

    # ajustamos y transformamos los datos
    imputer_knn_imputado = imputer_knn.fit_transform(dataframe[lista_columnas])

    # comprobamos que es lo que nos devuelve, que sigue siendo un array
    return imputer_knn_imputado

