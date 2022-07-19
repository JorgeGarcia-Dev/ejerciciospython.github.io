# Ejercicio 19

# Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables,
# y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es.

palabra_1 = input("Ingresa una palabra: ")
caracteres_palabra_1 = len(palabra_1)
palabra_2 = input("ingresa otra palabra: ")
caracteres_palabra_2 = len(palabra_2)

if caracteres_palabra_1 < caracteres_palabra_2:
    print("Es menor", True)
else:
    print("No es menor", False)
