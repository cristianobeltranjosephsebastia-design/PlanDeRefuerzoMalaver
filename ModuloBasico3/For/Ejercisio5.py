class Temperatura:
    def mostrar(self, inicio, fin):
        for t in range(inicio, fin + 1):
            print(f"Temperatura: {t}°C")

temp = Temperatura()
temp.mostrar(18, 22)