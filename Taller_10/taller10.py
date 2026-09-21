import numpy as np
from sklearn.svm import SVC

# 1. Dataset ampliado con el punto complejo [5, 5] etiquetado como Clase 0
X = np.array([
    [2, 2],
    [3, 3],
    [4, 2],
    [6, 6],
    [7, 8],
    [8, 7],
    [5, 5]  # Punto para forzar frontera no lineal
])

Y = np.array([0, 0, 0, 1, 1, 1, 0])

# 2. Inicializar y entrenar SVM con Kernel RBF (Radial Basis Function)
modelo_svm_rbf = SVC(kernel='rbf')
modelo_svm_rbf.fit(X, Y)

# 3. Extraer Vectores de Soporte identificados por el modelo RBF
vectores_soporte = modelo_svm_rbf.support_vectors_

# 4. Predicción sobre un nuevo punto de prueba
nuevo_punto = np.array([[5, 4]])
prediccion = modelo_svm_rbf.predict(nuevo_punto)

print("--- MODELO SVM CON KERNEL RBF ---")
print("Vectores de Soporte identificados por la IA:\n", vectores_soporte)
print(f"\nPredicción para el punto [5, 4]: Clase {prediccion[0]}")

# 5. Reflexión teórica sobre aplicaciones del Kernel RBF:
# El Kernel RBF es imprescindible en escenarios como la Detección de Tumores en
# imágenes médicas o la Biometría Facial, donde los patrones de salud/identidad
# no se pueden separar con una simple línea recta sino que están rodeados
# o entremezclados con tejidos sanos o patrones de variabilidad normal.