# README: Proyecto de Exploración, Limpieza y Análisis de Datos de Sara Gómez para la evaluación final del módulo 3

## Objetivo del Proyecto
El objetivo de este proyecto es realizar una exploración, limpieza de datos y análisis estadístico. Se abordarán tres fases principales: Exploración y Limpieza de Datos, Visualización de Datos y Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo.

## Flujo de trabajo
1. **Exploración y Limpieza de Datos:**
   - **Exploración Inicial:**
     - Utilizamos funciones de Pandas para obtener información estructural y estadísticas básicas.
     - Unimos dos conjuntos de datos de la forma más eficiente.
   - **Limpieza de Datos:**
     - Tratamos los valores nulos en columnas clave utilizando sklearn.impute.
     - Verificamos la consistencia y corrección de los datos.
     - Realizamos ajustes necesarios en las columnas.

2. **Visualización:**
   - Utilizamos herramientas de visualización para responder a diversas preguntas sobre los datos.
   - Gráficas abordadas:
     1. Distribución de la cantidad de vuelos reservados por mes durante el año.
     2. Relación entre la distancia de los vuelos y los puntos acumulados por los clientes.
     3. Distribución de los clientes por provincia o estado.
     4. Comparación del salario promedio entre los diferentes niveles educativos de los clientes.
     5. Proporción de clientes con diferentes tipos de tarjetas de fidelidad.
     6. Distribución de los clientes según su estado civil y género.

3. **Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo:**
   - **Preparación de Datos:**
     - Filtramos el conjunto de datos para incluir las columnas relevantes: 'Flights Booked' y 'Education'.
   - **Análisis Descriptivo:**
     - Agrupamos los datos por nivel educativo y calculamos estadísticas descriptivas básicas.
   - **Prueba Estadística:**
     - Realizamos una prueba de A/B testing para determinar si existen diferencias significativas en el número de vuelos reservados entre los diferentes niveles educativos.

## Estructura de Carpetas del Repositorio
- **/data:** Contiene los conjuntos de datos utilizados en el proyecto.
- **/notebooks:** Archivos Jupyter con el código utilizado en cada fase del proyecto.
- **/images:** Gráficas generadas durante la fase de visualización.

## Librerías Utilizadas
- Pandas: [Documentación](https://pandas.pydata.org/pandas-docs/stable/index.html)
- Matplotlib: [Documentación](https://matplotlib.org/stable/contents.html)
- Seaborn: [Documentación](https://seaborn.pydata.org/)
- SciPy: [Documentación](https://docs.scipy.org/doc/)
- scikit-learn (sklearn.impute): [Documentación](https://scikit-learn.org/stable/modules/impute.html)
- NumPy: [Documentación](https://numpy.org/doc/stable/)