class Semaforo:
    def __init__(self, color):
        self.color = color

    def accion(self):
        if self.color == "rojo":
            return "Detente"
        elif self.color == "amarillo":
            return "Precaución"
        elif self.color == "verde":
            return "Avanza"
        else:
            return "Color no válido"

s = Semaforo("verde")
print("Acción:", s.accion())