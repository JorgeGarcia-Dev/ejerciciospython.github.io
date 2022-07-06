# Ejercicio 13

# Dado un numero, devolver su tabla de multiplicar completa.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, " * ", i, " = ", numero * i)

tabla_multiplicar(int(input("Ingresa el número del cual deseas ver su tabla de multiplicar: ")))