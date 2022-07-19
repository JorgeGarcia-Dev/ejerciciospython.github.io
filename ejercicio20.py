# Escribir un programa que solicite ingresar un nombre de usuario y una contraseña.
# Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla
# “Usuario y contraseña correctos. Puede ingresar a Camelot”.
# Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.

nombre = input("Ingresa tu nombre: ")
contraseña = input("Ingresa tu contraseña: ")

if nombre == 'Gwenevere' and contraseña == 'excalibur':
    print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
else:
    print("Acceso denegado.")
