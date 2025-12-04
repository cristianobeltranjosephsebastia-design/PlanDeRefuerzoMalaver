class Cohete:
    def velocidad(self, incremento, maximo):
        v = 0
        while v <= maximo:
            print(f"Velocidad actual: {v} km/h")
            v += incremento
        print("Velocidad máxima alcanzada.")

c = Cohete()
c.velocidad(200, 1000)