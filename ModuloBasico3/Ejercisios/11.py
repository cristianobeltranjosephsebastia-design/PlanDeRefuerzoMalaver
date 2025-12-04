from datetime import datetime

class RelojDigital:
    def __init__(self):
        self.formato_24h = True

    def mostrar_hora(self):
        if self.formato_24h:
            return datetime.now().strftime("%H:%M:%S")
        else:
            return datetime.now().strftime("%I:%M:%S %p")

    def cambiar_formato(self):
        self.formato_24h = not self.formato_24h

reloj = RelojDigital()
print("Hora actual:", reloj.mostrar_hora())
reloj.cambiar_formato()
print("Hora en 12h:", reloj.mostrar_hora())
