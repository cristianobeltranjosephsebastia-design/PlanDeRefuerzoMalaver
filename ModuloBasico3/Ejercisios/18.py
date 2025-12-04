import math

class Forma:
    def area(self):
        raise NotImplementedError

    def perimetro(self):
        raise NotImplementedError

class Triangulo(Forma):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lados = [lado1, lado2, lado3]

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return sum(self.lados)

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

tri = Triangulo(4, 3, 3, 4, 5)
cua = Cuadrado(5)
cir = Circulo(6)
print("Triángulo área:", tri.area(), "Perímetro:", tri.perimetro())
print("Cuadrado área:", cua.area(), "Perímetro:", cua.perimetro())
print("Círculo área:", round(cir.area(), 2), "Perímetro:", round(cir.perimetro(), 2))