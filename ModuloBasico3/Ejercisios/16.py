class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        return f"El vehículo {self.marca} {self.modelo} se mueve."

class Coche(Vehiculo):
    def mover(self):
        return f"El coche {self.marca} {self.modelo} conduce en la carretera."

class Bicicleta(Vehiculo):
    def mover(self):
        return f"La bicicleta {self.marca} {self.modelo} pedalea en el carril bici."

auto = Coche("Toyota", "Corolla")
bici = Bicicleta("GW", "Montañera")
print(auto.mover())
print(bici.mover())
