# README: Proyecto Análisis de Aplicaciones Android 

(English Below)

Este proyecto tiene como objetivo el análisis de datos sobre aplicaciones Android (datos hasta 2018). Los datos se han cargado en un DataFrame de Pandas para limpiar y transformar y posteriormente subidos a Power BI para su análisis y presentación.

## Librerías y Herramientas Utilizadas

- **Pandas**: Librería poderosa para manipulación y análisis de datos. [Documentación](https://pandas.pydata.org/pandas-docs/stable/)

- **Power BI**: Herramienta de software que permite conectarse con facilidad a los orígenes de datos, visualizar y descubrir qué es importante y compartirlo con cualquiera o con todos los usuarios que desee. [Documentación](https://docs.python.org/3/library/time.htmlhttps://learn.microsoft.com/es-es/power-bi/)

## Descripción del Proyecto

El proyecto comienza importando el conjunto de [datos](https://www.kaggle.com/datasets/lava18/google-play-store-apps) de Google Play Store en un DataFrame de Pandas. A continuación, se realizan diversas operaciones de limpieza y análisis, como la eliminación de duplicados, la conversión de tipos de datos y la manipulación de columnas.

## Análisis Exploratorio

Se realiza un análisis exploratorio de los datos, las distribuciones y se proporcionó un resumen estadístico de las columnas.

## Limpieza de Datos

- Se identificaron y eliminaron registros duplicados en el conjunto de datos.
- Se eliminaron registros específicos con valores incoherentes en varias columnas.
- Se realizaron ajustes en las columnas 'Price', 'Installs', 'Size' y 'Android Ver' para asegurar la coherencia y facilitar el análisis.

## Conversión de Datos

- Se aplicó una función para convertir la columna 'Rating' a formato de cadena y ajustar su representación.
- Se realizaron ajustes en la representación de moneda en la columna 'Price'.

## Carga de Datos en Power BI

Además del análisis en Python, el conjunto de datos se cargó en Power BI para un análisis más profundo y la creación de paneles interactivos.

## Licencia

Este proyecto está bajo la licencia Creative Commons Attribution 4.0 International License.

![cc-by-image](https://i.creativecommons.org/l/by/4.0/88x31.png)

---

# README: Android Applications Analysis Project

This project aims to analyze data on Android applications (data up to 2018). The data has been loaded into a Pandas DataFrame for cleaning and transformation and subsequently uploaded to Power BI for analysis and presentation.

## Libraries and Tools Used

- **Pandas**: A powerful library for data manipulation and analysis. [Documentation](https://pandas.pydata.org/pandas-docs/stable/)

- **Power BI**: Software tool that allows easy connection to data sources, visualization, and discovery of what is important, and sharing it with anyone or everyone you want. [Documentation](https://docs.python.org/3/library/time.htmlhttps://learn.microsoft.com/es-es/power-bi/)

## Project Description

The project begins by importing the [data](https://www.kaggle.com/datasets/lava18/google-play-store-apps) set from Google Play Store into a Pandas DataFrame. Various cleaning and analysis operations are then performed, such as removing duplicates, converting data types, and manipulating columns.

## Exploratory Analysis

An exploratory analysis of the data is conducted, including distributions, and a statistical summary of the columns is provided.

## Data Cleaning

- Duplicate records in the data set were identified and removed.
- Specific records with inconsistent values in various columns were removed.
- Adjustments were made to the 'Price', 'Installs', 'Size', and 'Android Ver' columns to ensure consistency and facilitate analysis.

## Data Conversion

- A function was applied to convert the 'Rating' column to string format and adjust its representation.
- Adjustments were made to the currency representation in the 'Price' column.

## Data Loading in Power BI

In addition to the Python analysis, the data set was loaded into Power BI for deeper analysis and the creation of interactive dashboards.

## License

This project is under the Creative Commons Attribution 4.0 International License.

![cc-by-image](https://i.creativecommons.org/l/by/4.0/88x31.png)

