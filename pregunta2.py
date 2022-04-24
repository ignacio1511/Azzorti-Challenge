""" 
Calcular una funcion que bote el promedio de ventas de una campaña  con respecto a la campaña pasada

1. Encontrar el año y numero de la camopaña -> CAMP
2. Buscar todas las campañas anteriores a esa
3. Sumar el precio de cada una 
4. Dividirlo entre el total de datos analizados

"""

import pandas as pd 

df = pd.read_excel("DATOS_SKU.xlsx", sheet_name="DATOS_SKU")

df.info()
df.describe()
print(df.head()) 
print(df.dtypes) #ok

precio = df["PRECIO"]
camp = df["CAMP"]

print(set(precio)) # rango de precio de 49 a 120 
print(set(camp)) # campañas #17 y #18 del 2020 y #1-#5 del 2021 

def precio_promedio_grupo(data):
    campañas = pd.DataFrame(data.groupby(["CAMP","GRUPO"])["PRECIO"].mean()) #precio promedio por campaña y grupo
    print(campañas)

def precio_promedio_subgrupo(data):
    campañas = pd.DataFrame(data.groupby(["CAMP","SUBGRUPO"])["PRECIO"].mean()) #precio promedio por campaña y subgrupo
    print(campañas)

#campañas.to_excel("campañas.xlsx")

df_grupo = precio_promedio_grupo(df)
df_subgrupo = precio_promedio_subgrupo(df)

df_grupo
df_subgrupo