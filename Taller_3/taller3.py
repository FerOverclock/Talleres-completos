def membresia_triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)

conductores_anios = [3, 6, 12]

for anios in conductores_anios:
    g_novato = membresia_triangular(anios, 0, 0, 5)
    g_intermedio = membresia_triangular(anios, 2, 5, 8)
    g_experto = membresia_triangular(anios, 5, 10, 20)
    
    categorias = {
        "Novato": g_novato,
        "Intermedio": g_intermedio,
        "Experto": g_experto
    }
    
    mejor_categoria = max(categorias, key=categorias.get)
    
    print(f"Conductor con {anios} años de experiencia:")
    print(f" - Novato: {g_novato * 100:.1f}%")
    print(f" - Intermedio: {g_intermedio * 100:.1f}%")
    print(f" - Experto: {g_experto * 100:.1f}%")
    print(f" => Categoria principal: {mejor_categoria}\n")