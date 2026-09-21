import numpy as np

# 1. Función de Activación (Escalón)
def funcion_escalon(z):
    if z >= 0:
        return 1
    else:
        return 0

# 2. Estructura de la Neurona
def perceptron(X, W, b):
    Z = np.dot(X, W) + b
    return funcion_escalon(Z)

# 3. Pesos y Sesgo configurados manualmente para la Compuerta OR
pesos_or = np.array([0.5, 0.5])
sesgo_or = -0.2

# 4. Tabla de verdad para la Compuerta OR
casos_prueba = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

print("--- EVALUACIÓN COMPUERTA OR ---")
print(f"Configuración de parámetros: Pesos = {pesos_or}, Sesgo = {sesgo_or}\n")

for X in casos_prueba:
    resultado = perceptron(X, pesos_or, sesgo_or)
    print(f"Entrada: {X} => Salida del Perceptrón: {resultado}")