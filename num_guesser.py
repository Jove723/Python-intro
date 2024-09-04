import random

random_num = random.randint(1, 100)

jugando = True

while jugando:
    user_num = int(input("Ingrese un número: "))
    if user_num < random_num:
        print("Su número es menor que el número aleatorio")
    elif user_num > random_num:
        print("Su número es mayor que el número aleatorio")
    else:
        print("¡Felicidades! Adivinaste el número :D")
        jugando = False