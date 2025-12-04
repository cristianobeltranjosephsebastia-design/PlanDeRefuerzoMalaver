class Elevador:
    def __init__(self, piso):
        self.piso = piso

    def bajar(self):
        while self.piso > 0:
            print(f"El elevador está en el piso {self.piso}")
            self.piso -= 1
        print("El elevador llegó a la planta baja")
        
e = Elevador(5)
e.bajar()