class Tren:
    def estaciones(self, cantidad):
        for i in range(1, cantidad + 1):
            print(f"El tren ha llegado a la estación {i}")

t = Tren()
t.estaciones(4)