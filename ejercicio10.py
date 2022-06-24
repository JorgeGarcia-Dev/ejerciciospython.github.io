# Ejercicio 10

# Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año y almacene ese número en una variable.
# A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3 shows.

showsMusicales = int(input("A cuantos shows has asistido durante el último año?: "))
if (showsMusicales >= 3):
    print("Has asistido a muchos shows este año (True)")
else:
    print("Debes asistir a más shows (False)")