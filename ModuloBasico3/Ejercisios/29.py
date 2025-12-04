class Recurso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return f"Reserva confirmada para {self.nombre}"
        return f"{self.nombre} no está disponible"

    def liberar(self):
        self.disponible = True
        return f"{self.nombre} ha sido liberado"

class SistemaReservas:
    def __init__(self):
        self.recursos = []

    def agregar_recurso(self, recurso):
        self.recursos.append(recurso)

sala = Recurso("Sala de reuniones")
sistema = SistemaReservas()
sistema.agregar_recurso(sala)
print(sala.reservar())
print(sala.liberar())