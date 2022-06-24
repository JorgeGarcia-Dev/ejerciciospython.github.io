# Ejercicio 3

#Escribí un programa que solicite al usuario dos números y los almacene en dos variables.
# En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
# A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable.
# Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.

numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa un segundo número: "))
suma = numero1 + numero2
print(suma)
numero3 = int(input("Ingresa un tercer número: "))
multiplicacion = suma * numero3
print(multiplicacion)