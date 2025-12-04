class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre}, un {self.especie} de {self.edad} años."

mascota1 = Mascota("Firulais", "perro", 3)
mascota2 = Mascota("Michi", "gato", 2)
mascota3 = Mascota("Paco", "loro", 5)

print(mascota1.presentarse())
print(mascota2.presentarse())
print(mascota3.presentarse())

