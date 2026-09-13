hechos = {
    "monto_alto": True,
    "pais_extranjero": True,
    "hora_madrugada": True,
    "dispositivo_desconocido": True
}

reglas = [
    {
        "id": "R1",
        "condiciones": {"monto_alto": True, "hora_madrugada": True},
        "conclusion": {"transaccion_inusual": True}
    },
    {
        "id": "R2",
        "condiciones": {"transaccion_inusual": True, "pais_extranjero": True},
        "conclusion": {"sospecha_fraude": True}
    },
    {
        "id": "R3",
        "condiciones": {"sospecha_fraude": True, "dispositivo_desconocido": True},
        "conclusion": {"alerta_critica": True}
    },
    {
        "id": "R4",
        "condiciones": {"alerta_critica": True},
        "conclusion": {"bloquear_tarjeta": True}
    }
]

nuevos_hechos = True

while nuevos_hechos:
    nuevos_hechos = False
    for regla in reglas:
        condiciones_cumplidas = all(hechos.get(k) == v for k, v in regla["condiciones"].items())
        if condiciones_cumplidas:
            for clave, valor in regla["conclusion"].items():
                if clave not in hechos:
                    hechos[clave] = valor
                    nuevos_hechos = True
                    print(f"Disparando {regla['id']} -> Nuevo hecho: {clave}={valor}")

print("\nMemoria final de hechos:", hechos)