import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print(" ")
longitud = int(input("Cuantos caracteres quieres que tenga tu contraseña? "))

password = ""

for i in range(longitud):
    nuevoCaracter = random.choice(caracteres)
    password += nuevoCaracter
print(" ")
print("Una contraseña segura es: " + "'" + password + "'")
print("Recuerda no utilizar la misma contraseña para todas tus cuentas (;")
print(" ")