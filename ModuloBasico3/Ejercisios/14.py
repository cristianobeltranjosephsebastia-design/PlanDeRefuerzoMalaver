import random

class Dado:
    def __init__(self, caras=6):
        self.caras = caras

    def lanzar(self):
        return random.randint(1, self.caras)

dado = Dado()
print("Lanzamiento del dado:", dado.lanzar())