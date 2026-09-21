import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 1. Dataset ampliado: 10 clientes con 3 características [Edad, Salario_Miles, Num_Hijos]
X_entrenamiento = np.array([
    [20, 30, 0],
    [40, 50, 2],
    [35, 45, 1],
    [18, 22, 0],
    [50, 80, 3],
    [25, 35, 1],
    [42, 60, 2],
    [60, 90, 4],
    [22, 28, 0],
    [30, 40, 1]
])

# Etiquetas: 0 = NO COMPRA, 1 = COMPRA
Y_entrenamiento = np.array([0, 1, 1, 0, 1, 0, 1, 1, 0, 1])

# 2. Inferencia con K = 1
modelo_k1 = KNeighborsClassifier(n_neighbors=1)
modelo_k1.fit(X_entrenamiento, Y_entrenamiento)

# 3. Inferencia con K = 5
modelo_k5 = KNeighborsClassifier(n_neighbors=5)
modelo_k5.fit(X_entrenamiento, Y_entrenamiento)

# 4. Evaluación de un nuevo cliente [30 años, 40 mil salario, 1 hijo]
nuevo_cliente = np.array([[30, 40, 1]])

pred_k1 = modelo_k1.predict(nuevo_cliente)
pred_k5 = modelo_k5.predict(nuevo_cliente)

print("--- PREDICCIÓN CON K-NEAREST NEIGHBORS ---")
print(f"Clase predicha con K=1: {pred_k1[0]} ({'COMPRA' if pred_k1[0] == 1 else 'NO COMPRA'})")
print(f"Clase predicha con K=5: {pred_k5[0]} ({'COMPRA' if pred_k5[0] == 1 else 'NO COMPRA'})")

# 5. Pregunta de Análisis (La Maldición de la Dimensionalidad):
# Al aumentar las dimensiones a 1,000 columnas, el espacio multidimensional se vuelve
# extremadamente disperso y la Distancia Euclidiana entre cualquier par de puntos tiende
# a volverse equivalente (equidistante). Esto degrada la noción de "cercanía" o "vecindad",
# haciendo que KNN pierda su capacidad discriminativa a menos que se apliquen técnicas
# de reducción de dimensionalidad (como PCA) o normalización previa.