# Dado un numero, devolver su tabla de multiplicar completa.

def tabla_multiplicar(numero):
    for i in range(11):
        print(numero, " * ", i, " = ", numero * i)

tabla_multiplicar(int(input("Ingresa el número que deseas multiplicar: ")))