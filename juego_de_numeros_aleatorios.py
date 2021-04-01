import random

numerodejugador1 = random.randint(1,200)
numerodejugador2 = random.randint(1,200)

Nombredejugador1 = input("Ingrese nombre del jugador 1 por favor:")
Nombredejugador2 = input("Ingrese nombre del jugador 2 por favor:")

jugador1 = input("Escribe  la letra j para que tengas un numero del 1 al 40:")
jugador2 = input("Escribe la letra j para que tu tengas un numero del 1 al 40:")

if numerodejugador1>numerodejugador2:
    print(f"El ganador es {Nombredejugador1} porque su numero es el " + str(numerodejugador1) + f" y el numero de su oponente es el {numerodejugador2}")

else:
    print(f"El ganador es {Nombredejugador2} porque su numero es el " + str(numerodejugador2) + f" y el numero de su oponente es el {numerodejugador1}")
