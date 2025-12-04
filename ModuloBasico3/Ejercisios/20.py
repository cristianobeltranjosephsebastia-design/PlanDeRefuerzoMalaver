class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        raise NotImplementedError

class Guitarra(Instrumento):
    def tocar(self):
        return f"{self.nombre} suena: 🎸"

class Piano(Instrumento):
    def tocar(self):
        return f"{self.nombre} suena: 🎹"

class Bateria(Instrumento):
    def tocar(self):
        return f"{self.nombre} suena: 🥁"

inst1 = Guitarra("Gibson")
inst2 = Piano("Yamaha")
inst3 = Bateria("Pearl")

print(inst1.tocar())
print(inst2.tocar())
print(inst3.tocar())
