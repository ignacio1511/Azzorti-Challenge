""""
Relacion lineal entre campañas y ventas (?)
"""

import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_excel('Datos_201901_202009.xlsx')

print(df.head())
print(df.describe())
print(df.info())
print(df.isnull().value_counts())


pedidos_totales = df['PEDIDOS_TOTALES']
print(pedidos_totales)
print(set(pedidos_totales))


sns.countplot(data=df,x = 'PEDIDOS_TOTALES', y = 'CAMPAÑA')



""" 
X = df.iloc[:,1:11]
y =df['PEDIDOS_TOTALES']
X_train, X_test, y_train,y_test = train_test_split(X,y)


lin = LinearRegression()
lin.fit(X_train,y_train)

y_pred = lin.predict(X_test)
print(y_pred)

coef = lin.coef_
print(coef)


ecuacion = pd.DataFrame((zip)(X.columns,coef), columns =['grupo','coeficiente'])
ecuacion = ecuacion.append({'grupo':'intercept','coeficiente':lin.intercept_},ignore_index=True)
print(ecuacion)
"""