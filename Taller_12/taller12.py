import numpy as np

def sigmoide(x):
    return 1 / (1 + np.exp(-x))

# 1. ENTRADA (X): Matriz de 2 clientes x 3 características (Procesamiento en Lote / Batch)
X = np.array([
    [0.5, 0.8, 0.2],
    [0.1, 0.9, 0.9]
])

# 2. CAPA OCULTA (4 Neuronas)
# Matriz W1 de 3 entradas x 4 neuronas
W1 = np.array([
    [0.1, 0.2, 0.3, 0.4],
    [-0.5, 0.6, 0.7, -0.8],
    [0.9, -0.1, 0.2, 0.3]
])
b1 = np.array([0.1, 0.2, 0.3, 0.4])

# PROCESO CAPA OCULTA
Z1 = np.dot(X, W1) + b1
A1 = sigmoide(Z1)

# 3. CAPA DE SALIDA (1 Neurona)
# Matriz W2 de 4 entradas ocultas x 1 neurona final
W2 = np.array([0.5, 0.6, 0.7, 0.8])
b2 = np.array([-0.1])

# PROCESO CAPA FINAL
Z2 = np.dot(A1, W2) + b2
Salida_Final = sigmoide(Z2)

# IMPRESIÓN DE RESULTADOS
print("--- VALORES INTERMEDIOS CAPA OCULTA ---")
print("Z1 (Valores puros sin activar):\n", Z1)
print("\nA1 (Valores transformados por Sigmoide entre 0 y 1):\n", A1)

print("\n--- PREDICCIÓN FINAL POR LOTE ---")
for i, proba in enumerate(Salida_Final):
    print(f"Cliente {i + 1} - Probabilidad de Aprobación: {np.round(proba, 4)}")