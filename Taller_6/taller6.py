import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text

# 1. Dataset de Entrenamiento (Marketing - 10 Clientes)
# Columnas X: [Edad, Horas_Online, Compras_Previas][cite: 6, 7]
X = np.array([
    [18, 5, 0],
    [22, 8, 1],
    [45, 1, 4],
    [50, 2, 5],
    [19, 6, 0],
    [35, 7, 3],
    [60, 1, 1],
    [28, 9, 2],
    [40, 2, 0],
    [25, 6, 2]
])

# Etiqueta Y: [1: Hizo clic, 0: Lo ignoró][cite: 6, 7]
Y = np.array([0, 1, 0, 0, 0, 1, 0, 1, 0, 1])

# 2. Entrenamiento del Modelo
arbol = DecisionTreeClassifier(max_depth=3)[cite: 6, 7]
arbol.fit(X, Y)[cite: 6, 7]

# 3. Extracción e Impresión de Reglas
nombres_variables = ["Edad", "Horas_Online", "Compras_Previas"]
reglas_texto = export_text(arbol, feature_names=nombres_variables)[cite: 6, 7]

print("--- BASE DE REGLAS GENERADA AUTOMÁTICAMENTE ---")
print(reglas_texto)