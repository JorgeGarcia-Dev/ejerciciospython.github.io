# Ejercicio 15

# Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es una vocal”.
# en caso de no ser vocal, muestra el mensaje "No es una vocal, es una consonante".

vocal = input("Ingresa una letra: ").lower()
if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u':
    letra = vocal.lower()
    print("Es una vocal")
elif vocal != 'a' or vocal != 'e' or vocal != 'i' or vocal != 'o' or vocal != 'u':
    print("No es una vocal, es una consonante")