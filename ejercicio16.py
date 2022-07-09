# Ejercicio 16

# Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”.
# Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.

def es_vocal(letra):
    if len(letra) == 1:
        letra = letra.lower()
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            return "Es una vocal."
        elif letra != 'a' or letra != 'e' or letra != 'i' or letra != 'o' or letra != 'u':
            return "No es una vocal, es una consonante."
    elif len(letra) >= 2:
        return "No es posible procesar el dato, intenta de nuevo ingresando solo una letra."
    else:
        pass

print(es_vocal(str(input("Ingresa una letra: "))))