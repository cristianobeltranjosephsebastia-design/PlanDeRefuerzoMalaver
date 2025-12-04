class Bateria:
    def __init__(self, carga):
        self.carga = carga

    def descargar(self):
        while self.carga > 0:
            print(f"Batería al {self.carga}%")
            self.carga -= 20
        print("Batería descargada")

b = Bateria(100)
b.descargar()