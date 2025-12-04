class Personaje:
    def __init__(self, nombre, vida=100, fuerza=10):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza

    def atacar(self, enemigo):
        enemigo.vida -= self.fuerza
        return f"{self.nombre} ataca a {enemigo.nombre} y le queda {enemigo.vida} de vida."

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=120, fuerza=15)

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, fuerza=25)

g1 = Guerrero("Thorin")
m1 = Mago("Gandalf")
print(g1.atacar(m1))
print(m1.atacar(g1))