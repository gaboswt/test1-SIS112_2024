import ensayo
ensayo.matriz
def ingresar_matriz(matriz):
    for i in range(9):
        x=int(input("Ingresa los valores de la matriz"))
        x.append(matriz)

def suma_total(matriz):
    suma = sum(matriz)
    return suma

def suma_filas_columnas(matriz):
    print("1) Calcular Filas")
    print("2) Calcular Columnas")
    while True:
        y=int(input("->"))
        if y > 2 or y < 1:
            print("Dato incorrecto.")
        else:
            break
    if y == 1:
        sf= 

