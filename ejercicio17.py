# Ejercicio 17

# Escribir un programa que le solicite al usuario ingresar una fecha formada por 8 números,
# donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA).
# Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.

numeros = (input("ingresa un número de 8 caractéres: "))
dia = numeros[:2]
mes = numeros[2:4]
año = numeros[4:]

print(dia, '/', mes, '/', año)
