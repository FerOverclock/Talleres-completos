servidor_estado = {
    "cpu_uso": 88.5,
    "memoria_libre": 512,
    "ping_respuesta": 150,
    "temperatura": 85.0,
    "ventilador_activo": False
}

def diagnosticar_servidor(hechos):
    if hechos["temperatura"] > 80 and not hechos["ventilador_activo"]:
        return "CRÍTICO: Sobrecalentamiento inminente. Ventilador apagado y T > 80°C."
    elif hechos["cpu_uso"] > 80 or hechos["memoria_libre"] < 1024:
        if hechos["ping_respuesta"] > 200:
            return "ADVERTENCIA: Alto consumo de recursos y latencia elevada en red."
        return "ADVERTENCIA: Recursos de hardware limitados (CPU alta o Memoria baja)."
    else:
        return "NORMAL: El servidor opera dentro de los parámetros estables."

if __name__ == "__main__":
    print("--- PRUEBA 1 ---")
    print("Estado:", servidor_estado)
    print("Diagnóstico:", diagnosticar_servidor(servidor_estado))
    print()

    print("--- PRUEBA 2 ---")
    servidor_estado_2 = {
        "cpu_uso": 85.0,
        "memoria_libre": 2048,
        "ping_respuesta": 250,
        "temperatura": 65.0,
        "ventilador_activo": True
    }
    print("Estado:", servidor_estado_2)
    print("Diagnóstico:", diagnosticar_servidor(servidor_estado_2))
    print()

    print("--- PRUEBA 3 ---")
    servidor_estado_3 = {
        "cpu_uso": 35.0,
        "memoria_libre": 4096,
        "ping_respuesta": 20,
        "temperatura": 50.0,
        "ventilador_activo": True
    }
    print("Estado:", servidor_estado_3)
    print("Diagnóstico:", diagnosticar_servidor(servidor_estado_3))