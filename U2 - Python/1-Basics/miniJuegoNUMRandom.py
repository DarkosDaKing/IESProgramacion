import random

numerito = random.randint(1, 10)
print(numerito)
cantIntentos = 0

print("Adivina el número del 1 al 10")

while cantIntentos < 3:
        intento = int(input("Ingresa tu número: "))
        if intento == numerito:
            print("¡Felicidades! Adivinaste el número.")
            break
        else:
            print("Inténtalo de nuevo.")
            cantIntentos += 1