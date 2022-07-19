# Ejercicio 18

# Escribí un programa que,dada una cadena de texto por el usuario,
# imprima True si la cantidad de caracteres en la cadena es un número impar, o False si no lo es.

texto = input("Ingresa un enunciado: ")
caracteres = len(texto)
if caracteres % 2 == 0:
    print("El número es par", True)
else:
    print("El número es impar", False)

print(caracteres)