"""print("Ejercicio 1")
shift = [
    ("1", "2", "3", "4"),
    ("1", "2", "3", "4"),
    ("1", "2", "3", "4"),
    ("1", "2", "3", "4")
]

print("La matriz original es:")
for fila in shift:
    print(fila)

for i in range(4):
    shift[i] = shift[i][i:] + shift[i][:i]  

print("\nLa matriz nueva es:")
for fila in shift:
    print(fila)"""

def inicializar(nf, nc):
    A = []
    for i in range(nf):
        A.append(("1", "2", "3", "4"))
    return A


shift = inicializar(4, 4)

print("La matriz original es:")
for fila in shift:
    print(fila)

for i in range(4):
    shift[i] = shift[i][i:] + shift[i][:i]

print("\nLa matriz nueva es:")
for fila in shift:
    print(fila)

