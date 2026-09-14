import numpy as np

def defuzz_centroide(x, mu):
    return np.sum(x * mu) / np.sum(mu)

x_taller = np.array([10, 20, 30, 40])
mu_taller = np.array([0.2, 0.8, 0.8, 0.0])

descuento_crisp = defuzz_centroide(x_taller, mu_taller)
print(f"Descuento exacto: {descuento_crisp:.2f}%")

x_frenado = np.linspace(0, 100, 100)
centro = 70
sigma = 10
curva_gaussiana = np.exp(-0.5 * ((x_frenado - centro) / sigma) ** 2)

fuerza_frenado_exacta = defuzz_centroide(x_frenado, curva_gaussiana)
print(f"Fuerza de frenado exacta: {fuerza_frenado_exacta:.2f} N")