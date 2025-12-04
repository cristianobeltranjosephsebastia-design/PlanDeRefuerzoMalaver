class Estacionamiento:
    def __init__(self, capacidad):
        self.capacidad = capacidad

    def mostrar_espacios(self):
        for i in range(1, self.capacidad + 1):
            print(f"Espacio {i} disponible")

e = Estacionamiento(5)
e.mostrar_espacios()