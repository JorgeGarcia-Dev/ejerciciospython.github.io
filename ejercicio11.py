# Ejercicio 11

# Escribir un programa que solicite al usuario el ingreso de dos números diferentes
# y muestre en pantalla al mayor de los dos.

num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa un segundo número entero: "))

if num1 > num2:
    print("El Mayor es: ", num1)
elif num1 < num2:
    print("El Mayor es: ", num2)
else:
    print("Ingresa números enteros")
