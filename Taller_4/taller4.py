grados_empleado = {
    "desempeno_pobre": 0.1,
    "desempeno_promedio": 0.5,
    "desempeno_excelente": 0.85,
    "antiguedad_corta": 0.2,
    "antiguedad_larga": 0.6
}

def evaluar_bono_rh(grados):
    activacion_r1_bono_bajo = max(grados["desempeno_pobre"], grados["antiguedad_corta"])
    
    activacion_r2_bono_medio = grados["desempeno_promedio"]
    
    activacion_r3_bono_alto = min(grados["desempeno_excelente"], grados["antiguedad_larga"])
    
    return {
        "Bono Bajo": activacion_r1_bono_bajo,
        "Bono Medio": activacion_r2_bono_medio,
        "Bono Alto": activacion_r3_bono_alto
    }

fuerzas_bono = evaluar_bono_rh(grados_empleado)

print("--- NIVELES DE ACTIVACIÓN POR CADA TIPO DE BONO ---")
for bono, fuerza in fuerzas_bono.items():
    print(f" - {bono}: {fuerza}")

fuerza_r_alta_1 = 0.4
fuerza_r_alta_2 = 0.7

fuerza_final_bono_alto = max(fuerza_r_alta_1, fuerza_r_alta_2)

print("\n--- AGREGACIÓN DE MAMDANI (PREGUNTA TEÓRICA) ---")
print(f"Fuerza final agregada para 'Bono Alto': {fuerza_final_bono_alto}")