#inputs
nombre = input("Ingresa tu nombre: ")
#int = numeros enteros
year = int(input("Ingresa tu año de nacimiento: "))
edad = 2024 - year
#se pueden poner los inputs en {} solo si se pone una f antes de empezar el texto

#condicionales
if year <= 1948:
    print(f"Hola, {nombre} tienes {edad} años y perteneces a la generación Niños de la posguerra")
elif year <= 1968:
    print(f"Hola, {nombre} tienes {edad} años y perteneces a la generación Baby boomer")
elif year <= 1980:
    print(f"Hola, {nombre} tienes {edad} años y perteneces a la generación X")
elif year <= 1993:
    print(f"Hola, {nombre} tienes {edad} años y perteneces a la generación Millenial")
elif year <= 2010:
    print(f"Hola, {nombre} tienes {edad} años y perteneces a la generación Z")
elif year <= 2024:
    print(f"Hola, {nombre} tienes {edad} años y perteneces a la generación Alfa")
else:
    print(f"Hola {nombre}, tienes {edad} años, por ende, no has nacido")
