#%%
import pandas as pd
import numpy as np

def exploracion_csv(archivo):
    """
    Función para explorar un archivo csv
    
    Args:
        archivo (str): Archivo csv separado por comas

    Returns:
        df (DataFrame): Devuelve un dataframe directamente del archivo csv, además de realizar varios prints con información de los datos incluidos en dicho csv
    """
    
    # Convertimos el csv a DataFrame
    df = pd.read_csv(archivo,index_col=0)

    #Echamos un vistazo
    print("Primeras filas:")
    display(df.head(10))
    print("-----------------------------")

    print("Últimas filas:")
    display(df.tail(10))
    print("-----------------------------")

    print("Filas aleatorias:")
    display(df.sample(10))
    print("-----------------------------")

    print("El df tiene {df.shape[0]} filas y {df.shape[1]} columnas")
    print("-----------------------------")

    print("Tipos de datos y nulos:")
    display(df.info())
    print("-----------------------------")
    
    print("Características columnas númericas:")
    display(df.describe().T)
    print("-----------------------------")

    print("Características columnas de texto")
    display(df.describe (include='object').T)
    print("-----------------------------")

    print("Duplicados:")
    display(df.duplicated().sum())
    print("-----------------------------")

    # generamos un DataFrame para los valores nulos
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(df.isnull().sum() / df.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])

    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    df_categoricas = df.select_dtypes(include = "O")
    
    for col in df_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valore únicos:")
        display(pd.DataFrame(df[col].value_counts()/df[col].shape[0])*100) 

    return pd.read_csv(archivo,index_col=0)     




# %%
