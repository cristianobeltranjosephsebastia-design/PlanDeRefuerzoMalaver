class Vehiculo:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

class Ruta:
    def __init__(self, nombre, paradas):
        self.nombre = nombre
        self.paradas = paradas

class Pasajero:
    def __init__(self, nombre):
        self.nombre = nombre

bus = Vehiculo("Bus", 40)
ruta = Ruta("Ruta 1", ["Centro", "Plaza", "Terminal"])
pasajero = Pasajero("Carlos")
print(f"{pasajero.nombre} viaja en {bus.tipo} por {ruta.nombre} con paradas {ruta.paradas}")