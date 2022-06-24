# Ejercicio 9

# Escribir un programa para solicitar al usuario el ingreso de un número entero
# y que luego imprima un valor de verdad dependiendo de si el número es par o no.
# Recordar que un número es par si el resto, al dividirlo por 2, es 0.

numeroEntero = int(input("Ingresa un número: "))
if numeroEntero % 2 == 0:
    print("El número es par", True)
else:
    print("El número es impar", False)
    
print(numeroEntero)

