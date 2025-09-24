def graficar_ascii(funciones, xmin=-10, xmax=10, ymin=-10, ymax=10):
    ancho = xmax - xmin + 1
    alto = ymax - ymin + 1

    # Creamos una matriz vacía (llena de espacios)
    plano = [[" " for _ in range(ancho)] for _ in range(alto)]

    # para poder dibujar los ejes
    for y in range(alto):
        for x in range(ancho):
            if x + xmin == 0 and y == alto // 2:  
                plano[y][x] = "+"  # origen
            elif x + xmin == 0:  
                plano[y][x] = "|"  # eje Y
            elif y == alto // 2:  
                plano[y][x] = "-"  # eje X

    # Dibujar funciones
    simbolos = ["*", "o", "#", "x"]  # símbolos para cada funcion
    
    for i, f in enumerate(funciones):
        simbolo = simbolos[i % len(simbolos)]
        for x in range(xmin, xmax + 1):
            try:
                y = eval(f)  # para calcular y
                if isinstance(y, (int, float)):
                    xi = x - xmin
                    yi = alto // 2 - int(round(y))
                    if 0 <= yi < alto and 0 <= xi < ancho:
                        plano[yi][xi] = simbolo
            except:
                pass

    # Imprimir el plano
    for fila in plano:
        print("".join(fila))

    # Leyenda
    print("\nLeyenda del gráfico:")
    for i, f in enumerate(funciones):
        print(f"{simbolos[i % len(simbolos)]} = f{i+1}(x) = {f}")
    print("| = Eje Y")
    print("- = Eje X")
    print("+ = Origen (0,0)")

def main():
    n = int(input("¿Cuántas funciones lineales quieres graficar? "))
    funciones = []
    for i in range(n):
        f = input(f"Ingrese la función {i+1} (ejemplo: 2*x+1): ")
        funciones.append(f)

    graficar_ascii(funciones)

main()

