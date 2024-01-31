# Transformando el Talento: Análisis de Datos para Retener y Potenciar Empleados en ABC Corporation

Somos la empresa DFE ANALYSIS y con el objetivo de reducir la rotación de empleados, retener el talento y mejorar la satisfacción en el trabajo la empresa ABC Corporation, nos han contratado para desarrollar un proyecto de análisis de datos y experimentación A/B de gran alcance. Nuestra misión es identificar factores clave que influyen en la satisfacción en el trabajo y, en última instancia, en la retención de empleados.
En este proyecto, presentaremos los resultados de nuestro análisis exploratorio de datos, diseñaremos un experimento A/B para probar hipótesis críticas y analizaremos los resultados para proporcionar a ABC Corporation información valiosa que informe sus decisiones estratégicas.


Para realizar este analisis hemos utilizado diferentes herramientas como Pandas para poder tener una visualizacion y un buen manejo para tras realizar el EDA identificar la limpieza, la homogeneización y la transformacion que hay que hacer a los datos. 
[pagina panda](https://pandas.pydata.org/docs/index.html)

Además hemos utilizado MYSQL Workbench para almacenar toda la información en una base de datos , hemos diseñado la estructura y hemos insertado los datos con Python.
[pagina_mysql](https://dev.mysql.com/doc/)

Para hacer las graficas hemos utilizado Seaborn y Matplotlib para poder tener informacion de un vistazo y poder tener una idea generalizada del estudio que estamos haciendo.
[pagina_seaborn] (https://seaborn.pydata.org/)
[pagina_matplotlib] (https://matplotlib.org/stable/index.html)

Para evaluar la linealidad de las variables analizadas y poder hacer un A/B testing hemos utilizado herramientas de estadistica descriptiva e inferencial, hemos realizado estos analisis con Python con herramientas como shapiro, levene, etc
[shapiro_pagina](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html)


Dentro del repositorio encontramos varias carpetas con diferentes archivos que hemos utilizado para el estudio

BBDD empleados: son los archivos que hemos utlizado para obtener la base de datos en MySql.
Data: Aqui encontramos la información, almacenada en formato Csv con la que estamos trabajando.
Notebooks: En esta carpeta hay varios jupiters en los que vamos diferenciando las distintas etapas del trabajo, como exploración, transformación, nulos, bbdd, visualización, y estadistica.
SRC: en esta carpeta estan almacenados los archivos en formato .PY y en el archivo "main" encontramos todas las funciones en este formato ejecutadas


Algunas de las librerias que hemos utilizado son: 

# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np

# Visualización
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# Evaluar linealidad de las relaciones entre las variables
# y la distribución de las variables
# ------------------------------------------------------------------------------
from scipy.stats import shapiro, kstest

import scipy.stats as stats

# Gestión de los warnings
# -----------------------------------------------------------------------
import warnings
warnings.filterwarnings("ignore")


# -----------------------------------------------------------------------
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu
from scipy.stats import levene

# Configuración
# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames
