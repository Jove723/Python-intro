class Carro:

    def __init__(self, marca, modelo, year, vel):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.vel = vel = 0

    def acelerar(self):
        self.vel += 10
        print(self.vel)
        print("fiiiiiuuuuuuuuum")

    def frenar(self):
        if self.vel < 10 and self.vel >= 0:
            self.vel = 0
        else:
            self.vel -= 10
        
        print(self.vel)
        print("Fiuuuummn´t")


carro1 = Carro("Renault", "Logan", 2018)