# Ejercicio 6

# Escribir un programa que solicite al usuario ingresar tres calificaciones (números) para luego mostrarle el promedio general de los tres.

matematicas = int(input("Ingresa la calificación de matemáticas: "))
español = int(input("Ingresa la calificación de español: "))
ingles = int(input("Ingresa la calificación de inglés: "))
suma = matematicas + español + ingles
print("La suma total es de: ", suma)
resultado = suma / 3
print("El promedio general es de: ", resultado)