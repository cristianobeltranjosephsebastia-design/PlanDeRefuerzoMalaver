import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Baraja:
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    palos = ["Corazones", "Picas", "Tréboles", "Diamantes"]

    def __init__(self):
        self.cartas = [Carta(v, p) for v in self.valores for p in self.palos]
        random.shuffle(self.cartas)

    def repartir(self, cantidad):
        mano = self.cartas[:cantidad]
        self.cartas = self.cartas[cantidad:]
        return mano

baraja = Baraja()
mano = baraja.repartir(5)
print("Cartas en la mano:")
for c in mano:
    print(c)