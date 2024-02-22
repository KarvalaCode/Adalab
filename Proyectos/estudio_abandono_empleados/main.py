#%%
# Importaciones #
#################

# Importar librerías para manipulación y análisis de datos
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np

# Importar librería para la conexión con MySQL
# -----------------------------------------------------------------------
import mysql.connector

# Importar archivos para usa sus funciones
# -----------------------------------------------------------------------
from src import etl1_exploracion as e
from src import etl2_transformacion as t
from src import etl3_bbdd as b
from src import queries_bbdd as q


# Importar librerias para gestión de contraseñas y .env
# -----------------------------------------------------------------------
from dotenv import load_dotenv
import os
load_dotenv()


pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

#%%
# Exploración #
###############

#cargamos el csv y exploramos el dataframe
df = e.exploracion_csv('data/HR_RAW_DATA.csv')

#%%
# Transformación #
##################

# Cambio nombres columnas dataframe
df = t.columnas_minusculas(df)

dic_columnas = {"businesstravel": "business_travel",
                "dailyrate": "daily_rate", 
                "distancefromhome": "distance_from_home", 
                    "educationfield": "education_field", 
                    "employeecount": "employee_count",
                    "employeenumber": "employee_number",
                    "environmentsatisfaction": "environment_satisfaction",
                    "hourlyrate": "hourly_rate", 
                    "jobinvolvement": "job_involvement",
                    "joblevel": "job_level",
                    "jobrole": "job_role",
                    "jobsatisfaction": "job_satisfaction",
                    "maritalstatus": "marital_status",
                    "monthlyincome": "monthly_income",
                    "monthlyrate": " monthly_rate",
                    "numcompaniesworked": "num_companies_worked",
                    "over18": "over_18",
                    "percentsalaryhike": "percent_salary_hike",
                    "performancerating": "performance_rating",
                    "relationshipsatisfaction": "relationship_satisfaction",
                    "standardhours": "standard_hours",
                    "stockoptionlevel": "stock_option_level",
                    "totalworkingyears": "total_working_years",
                    "trainingtimeslastyear": "training_times_last_year",
                    "worklifebalance": "work_life_balance",
                    "yearsatcompany": "years_at_company",
                    "yearsincurrentrole": "years_in_current_role",
                    "yearssincelastpromotion": "years_since_last_promotion",
                    "yearswithcurrmanager": "years_with_curr_manager",
                    "sameasmonthlyincome": "same_as_monthly_income",
                    "datebirth": "date_birth",
                    "roledepartament": "role_departament",
                    "numberchildren": "number_children",
                    "remotework": "remote_work"}

df = t.cambiar_nombre_columnas(df, dic_columnas)
print(df.columns)

#%%
#columnas individuales

## columna 'age'
cambio_age =  {'fifty-five': '55', 'thirty-six': '36', 'forty-seven': '47', 'twenty-four': '24', 'thirty-seven': '37', 'fifty-two': '52', 'fifty-eight': '58', 'twenty-six': '26', 'thirty-one': '31', 'thirty': '30', 'thirty-two': '32'} 
df['age'] = t.cambio_valores_dic(df['age'], cambio_age)

## columna 'buisness_travel'
df['business_travel'] = t.a_barra_baja(df['business_travel'], "-")

## columna 'distance_from_home'
df["distance_from_home"] = df["distance_from_home"].apply(t.tonull)

## columna 'education'
mapa_education = {1: "eso", 2:"fp", 3:"bachillerato", 4:"universidad", 5:"doctorado"}
df['education'] = t.cambio_valores_map(df['education'], mapa_education)

## columna 'education_field'
mapa_education_field = {"Life Sciences":"life_sciences",
                 "Medical"  :"medical",
                 "Marketing": "marketing",
                 "Technical Degree" : "technical_degree",
                 "Other": "other",
                 "Human Resources": "human_resources",
                 "desconocido": "desconocido"}

df["education_field"] = t.cambio_valores_map(df["education_field"], mapa_education_field)

## columna 'environment_satisfaction'
df["environment_satisfaction"] = df["environment_satisfaction"].apply(t.primer_digito)

## columna 'gender'
mapa_gender ={0:"male", 1:"female"}
df["gender"] = t.cambio_valores_map(df["gender"], mapa_gender)

## columna 'daily_rate'
df['daily_rate'] = t.sin_dolar(df['daily_rate'])
df['daily_rate'] = t.str_to_nan(df['daily_rate'], 'nan')

## columna 'hourly_rate' 
df['hourly_rate'] = t.str_to_nan(df['hourly_rate'], 'Not Available')

## columna 'buisness_travel'
df['job_role'] = t.a_barra_baja(df['job_role'], " ")

## columna 'performance_rating'
df["performance_rating"] = t.nan_to_str(df["performance_rating"], "3.0")

## columna 'remote_work'
mapa_remoto = {"1": "yes", "0":"no", "True":"yes", "False":"no", "Yes":"yes"}
df["remote_work"] = t.cambio_valores_map(df["remote_work"], mapa_remoto)

#columna 'employee_number'
df.loc[df["employee_number"].isnull(), "employee_number"] =  t.rellena_nulos_suma(df["employee_number"])

df = t.elimina_duplicados_columna(df, 'employee_number', 'last')

# eliminamos columnas que no nos aportan información
columnas_a_eliminar = ['employee_count', 'employee_number', "over_18", "number_children", 'standard_hours', 'years_in_current_role', 'salary', 'role_departament']
for col in columnas_a_eliminar:
    df = t.eliminar_col(df, col)

df = t.col_autoincremental(df, 'employee_number')

#%%
## Pasamos columnas a float (cambiando comas por puntos)
col_to_float = ['daily_rate', 'monthly_income', 'performance_rating', 'total_working_years', 'work_life_balance']

for f in col_to_float:
    df[f] = df[f].apply(t.to_float).astype(float)

#%%
## imputación de nulos
lista_nulos = ["hourly_rate","daily_rate", "distance_from_home", "monthly_income", "total_working_years", 'work_life_balance']

df[lista_nulos] = t.imputar_nulos_knn(df, lista_nulos)

# Rellenamos nulos con 'desconocido' en algunas columnas categóricas
col_a_desconocido = ['business_travel', 'department', 'education_field', 'marital_status', 'overtime']

for columna in col_a_desconocido:
    df[columna] = t.nan_to_str(df[columna], 'desconocido')

#%%
# Columnas con valores a poner en minúscula
valores_minuscula = ['department', 'job_role', 'marital_status']

for elemento in valores_minuscula:
    df[elemento] = t.valores_col_lower(df[elemento])

## columna 'marital_status'
df['marital_status'] = t.cambio_valores_individual(df['marital_status'], "marreid", "married")

## columna 'department'
dic_department = {"research & development" : "research_development", "human resources" :  "human_resources"}

df['department'] = t.cambio_valores_dic(df['department'], dic_department)
display(df)

#%%
# cambiamos columnas a integer    
col_a_int = ['age', 'daily_rate', 'hourly_rate', "employee_number","hourly_rate","total_working_years","work_life_balance", 'monthly_income', 'performance_rating']

for i in col_a_int:
    df[i] = df[i].apply(t.to_int).astype(int)

#%%
# guardamos el csv
df.to_csv("data/datos_empleados.csv")

# %%
# Preparar datos para cargar #
##############################

# leemos el csv en un dataframe
df_empleados = pd.read_csv(f'data/datos_empleados.csv', index_col=0)

# creamos las distintas listas de tuplas para las tablas de la bbdd

##Datos personales
orden_datos_personales = ['employee_number', 'age', 'date_birth', 'gender', 'marital_status', 'distance_from_home', 'num_companies_worked', 'total_working_years', 'education', 'education_field']
lista_tuplas_datos_personales = b.orden_df_tuplas(df_empleados, orden_datos_personales)
lista_tuplas_datos_personales = b.convertir_float(lista_tuplas_datos_personales)

##Valoraciones
orden_valoraciones = ['employee_number', 'environment_satisfaction', 'job_involvement', 'job_satisfaction', 'performance_rating', 'relationship_satisfaction', 'work_life_balance', 'employee_number']
lista_tuplas_valoraciones =  b.orden_df_tuplas(df_empleados, orden_valoraciones)
lista_tuplas_valoraciones = b.convertir_float(lista_tuplas_valoraciones)

##Salarios
orden_salarios = ['employee_number', 'monthly_rate', 'percent_salary_hike', 'hourly_rate', 'daily_rate', 'monthly_income', 'employee_number']
lista_tuplas_salarios = b.orden_df_tuplas(df_empleados, orden_salarios)
lista_tuplas_salarios = b.convertir_float(lista_tuplas_salarios)

##Gestión interna de la empresa
orden_empresa = ['employee_number', 'attrition', 'business_travel', 'department', 'job_level', 'job_role', 'overtime', 'stock_option_level', 'training_times_last_year', 'years_at_company', 'years_since_last_promotion', 'years_with_curr_manager', 'remote_work', 'employee_number']
lista_tuplas_empresa = b.orden_df_tuplas(df_empleados, orden_empresa)
lista_tuplas_empresa = b.convertir_float(lista_tuplas_empresa)

# Carga de datos a la BBDD #
############################

# Recuperamos la contraseña del .env
contrasena = os.getenv('contrasena')

## Crear la BBDD
b.creacion_bbdd_tablas(q.query_creacion_bbdd, contrasena)

## Crear la tabla datos personales
b.creacion_bbdd_tablas(q.query_tabla_datos_personales, contrasena)

## Crear la tabla gestión interna empresa
b.creacion_bbdd_tablas(q.query_tabla_empresa, contrasena)

## Crear la tabla salarios
b.creacion_bbdd_tablas(q.query_tabla_salarios, contrasena)

## Crear la tabla valoraciones
b.creacion_bbdd_tablas(q.query_tabla_valoraciones, contrasena)

# Insertar los datos

## Insertar los datos personales
b.insertar_datos(q.query_insertar_datos_personales, contrasena, "empleados", lista_tuplas_datos_personales)

## Insertar los datos de gestión interna empresa
b.insertar_datos(q.query_insertar_empresa, contrasena, "empleados", lista_tuplas_empresa)

## Insertar los datos salarios
b.insertar_datos(q.query_insertar_salarios, contrasena, "empleados", lista_tuplas_salarios)

## Insertar los datos valoraciones
b.insertar_datos(q.query_insertar_valoraciones, contrasena, "empleados", lista_tuplas_valoraciones)