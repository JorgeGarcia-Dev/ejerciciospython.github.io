# Ejercicio 5

# Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales)
# y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_

Fahrenheit = float(input("Ingresa la Temperatura expresada en Grados Fahrenheit: "))
print("El equivalente en Grados Celcius es: ",(5/9) * (Fahrenheit-32))