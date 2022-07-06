# Ejercicio 12

# Escribir un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.

num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa un segundo número entero: "))
num3 = int(input("Ingresa un tercer número entero: "))

if num1 < num2 and num1 < num3:
    print("El número menor es: " + str(num1))
elif num2 < num1 and num2 < num3:
    print("El número menor es: " + str(num2))
else:
    print("El número menor es: " + str(num3))