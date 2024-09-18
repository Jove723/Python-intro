# Clases para determinar objetos
class Perro():
# Se definen los atributos de la clase
    def __init__(self, nombre: str, edad: int, raza: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    #IMPORTANTE PONER SELF PARA QUE FUNCIONE
    def ladrar(self):
        print("guau")

    def mover(self):
         print("me corrooo")


# Se asocia un objeto a la clase
mi_perro = Perro("Godzilla", "5", "Chihuahua")
otro_perro = Perro("Messi", 7, "Pitbull")

# Función para agilizar el proceso
def detectar_perro(i):
    print(f"Nombre: {i.nombre}\nEdad: {i.edad}\nRaza: {i.raza}")

detectar_perro(otro_perro)

mi_perro.mover()
        