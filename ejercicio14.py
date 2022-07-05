# Dada una cadena de texto, comprobar si es un palíndromo o no.
# Los palíndromos son palabras que se leen igual aún estando invertidas.
# Por ejemplo: ana, otto, kayak, ojo, etc...

palabra = str(input("Ingresa una palabra: "))

if str(palabra) == str(palabra) [::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")