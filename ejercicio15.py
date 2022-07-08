# Ejercicio 15

# Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”.
# en caso de no ser vocal, muestra el mensaje "No es vocal".

vocal = input("Ingresa una letra: ")
if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u':
    print("Es Vocal")
elif vocal != 'a' or vocal != 'e' or vocal != 'i' or vocal != 'o' or vocal != 'u':
    print("No Es Vocal")