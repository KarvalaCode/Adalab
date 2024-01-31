# Importaciones #
#################
# Importar librerias para conexión con bbdd
# -----------------------------------------------------------------------
import mysql.connector
from mysql.connector import errorcode

# Importar librerías para manipulación y análisis de datos
# -----------------------------------------------------------------------
import pandas as pd# Importar librería para la conexión con MySQL
import numpy as np


def orden_df_tuplas(dataframe, lista_columnas):
    """
    Función para reordenar un dataframe y convertirlo en una lista de tuplas

    Args:
        dataframe (DataFrame): un dataframe del que reordenar sus columnas 
        lista_columnas (list): lista de los nombres de las columnas en el orden que queremos ordenarlas en el dataframe

    Returns:
        lista_tuplas (list): Lista de tuplas con el orden indicado
    """

    df = dataframe.reindex(columns = lista_columnas)
    lista_tuplas = [tuple (fila) for fila in df.values]

    return list(set(lista_tuplas))

def convertir_float(lista_tuplas):
    """
    Convierte los elementos de una lista de tuplas a float cuando sea posible.

    Args:
    - lista_tuplas (list): Una lista que contiene tuplas con elementos que pueden ser convertidos a float.

    Returns:
    - list: Una nueva lista con las mismas tuplas de entrada, pero con los elementos convertidos a float si es posible.
    """
    datos_tabla_caracteristicas = []
    
    for tupla in lista_tuplas:
        lista_intermedia = []
        for elemento in tupla:
            try:
                lista_intermedia.append(float(elemento))
            except:
                lista_intermedia.append(elemento)
            
        datos_tabla_caracteristicas.append(tuple(lista_intermedia))
    
    return datos_tabla_caracteristicas

def creacion_bbdd_tablas(query, contraseña, nombre_bbdd=None):
    """
    Crea una conexión a la base de datos MySQL y ejecuta una consulta para crear una tabla.

    Args:
    - query (str): Consulta SQL para crear la tabla en la base de datos.
    - contraseña (str): Contraseña para acceder a la base de datos.
    - nombre_bbdd (str): Nombre de la base de datos a la que se conectará.

    Returns:
        - None

    """
    if nombre_bbdd is not None:
        cnx = mysql.connector.connect(
            user="root", 
            password=contraseña, 
            host="127.0.0.1"
        )

        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
    else:
        cnx = mysql.connector.connect(
            user="root", 
            password=contraseña,
            host="127.0.0.1", 
            database=nombre_bbdd
        )

        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)
            cnx.close()

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            cnx.close()

def insertar_datos(query, contraseña, nombre_bbdd, lista_tuplas):
    """
    Inserta datos en una base de datos utilizando una consulta y una lista de tuplas como valores.

    Args:
    - query (str): Consulta SQL con placeholders para la inserción de datos.
    - contraseña (str): Contraseña para la conexión a la base de datos.
    - nombre_bbdd (str): Nombre de la base de datos a la que se conectará.
    - lista_tuplas (list): Lista que contiene las tuplas con los datos a insertar.

    Returns:
    - None: No devuelve ningún valor, pero inserta los datos en la base de datos.

    This function connects to a MySQL database using the given credentials, executes the query with the provided list of tuples, and commits the changes to the database. In case of an error, it prints the error details.
    """
    cnx = mysql.connector.connect(
        user="root", 
        password=contraseña, 
        host="127.0.0.1", database=nombre_bbdd
    )

    mycursor = cnx.cursor()

    try:
        mycursor.executemany(query, lista_tuplas)
        cnx.commit()
        print(mycursor.rowcount, "registro/s insertado/s.")
        cnx.close()

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cnx.close()