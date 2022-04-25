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
    campañas_grupo = pd.Series(data.groupby(["CAMP","GRUPO"])["PRECIO"].mean()) #precio promedio por campaña y grupo
    return campañas_grupo

def precio_promedio_subgrupo(data):
    campañas_subgrupo = pd.DataFrame(data.groupby(["CAMP","SUBGRUPO"])["PRECIO"].mean()) #precio promedio por campaña y subgrupo
    return campañas_subgrupo
    

df_grupo = precio_promedio_grupo(df)
df_subgrupo = precio_promedio_subgrupo(df)

df_grupo
df_subgrupo

df_grupo.to_excel("p2-grupos.xlsx",sheet_name="grupos")
df_subgrupo.to_excel("p2-subgrupos.xlsx",sheet_name="subgrupos")
