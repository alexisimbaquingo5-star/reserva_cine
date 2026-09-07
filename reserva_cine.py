asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

fila = int(input("Ingrese la fila (0 a 2): "))
columna = int(input("Ingrese la columna (0 a 3): "))

if 0 <= fila <= 2 and 0 <= columna <= 3:
    if asientos[fila][columna] == 0:
        asientos[fila][columna] = 1
        print("Asiento reservado correctamente.")
    else:
        print("El asiento ya está reservado.")
else:
    print("Fila o columna fuera de rango.")

print("\nEstado de la sala:")

for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()