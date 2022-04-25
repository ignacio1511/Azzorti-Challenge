def regresion_lineal(df):
    from sklearn.model_selection import train_test_split
    import numpy as np
    import seaborn as sns
    from sklearn.linear_model import LinearRegression
    df = pd.DataFrame(df)
    X = df.iloc[:,1:4]
    X
    y =df['PEDIDOS_TOTALES']
    X_train, X_test, y_train,y_test = train_test_split(X,y)

    lin = LinearRegression()
    lin.fit(X_train,y_train)
    y_pred = lin.predict(X_test)
    coef = lin.coef_

    for i in coef:
        print(i)
    
    ecuacion = pd.DataFrame((zip)(X.columns,coef), columns =['grupo','coeficiente m'])
    ecuacion = ecuacion.append({'grupo':'intercepto b','coeficiente m':lin.intercept_},ignore_index=True)
    df['Coeficiente G1'] = str(coef[0])
    df['Coeficiente G2'] = str(coef[1])
    df['Coeficiente G3'] = str(coef[2])
    return df








