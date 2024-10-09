class Personaje:
    def __init__(self, nombre, defensa, vida) -> None:
        self.nombre = nombre
        self.defensa = defensa
        self.vida = vida

    def mostrar_atributos(self):
        print(f"{self.nombre} Status: ")
        print(f"Fuerza: {self.fuerza}")
        print(f"Magia: {self.magia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
    
    def esta_vivo(self):
        return self.vida > 0
    
    
    
    def atacar(self, enemigo):
        daño = self.obtener_daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(f"{self.nombre} le ha hecho {daño} de daño a {enemigo.nombre}")
        if not self.esta_vivo():
            print(f"{self.nombre} ha muerto")


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, defensa, vida) -> None:
        super().__init__(nombre, defensa, vida)
        self.fuerza = fuerza
        
    def obtener_daño(self, enemigo):
        return self.fuerza - enemigo.defensa

class Mago(Personaje):
    def __init__(self, nombre, magia, defensa, vida) -> None:
        super().__init__(nombre, defensa, vida)
        self.magia = magia
    
    def obtener_daño(self, enemigo):
        return self.magia - enemigo.defensa

player_1 = Guerrero("Guerrero", 20, 40, 100)
player_2 = Mago("Mago", 15, 25, 100)

def combate():
    while player_1.esta_vivo() and player_2.esta_vivo():
        turno = 0
        player_1.atacar(player_2)
        player_2.atacar(player_1)
        turno += 1
        print("-----------------------------")
        print(f"Turno {turno}")

combate()