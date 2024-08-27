numeroA = int(input("Ingresa un número: "))
numeroB = int(input("Ingresa otro número: "))

if numeroA > numeroB:
    print(f"{numeroA} es mayor que {numeroB}")
elif numeroA < numeroB:
    print(f"{numeroB} es mayor que {numeroA}")
else:
    print(f"{numeroA} y {numeroB} son iguales")