class Cuadrados:
    def mostrar(self, n):
        i = 1
        while i <= n:
            print(f"El cuadrado de {i} es {i**2}")
            i += 1

c = Cuadrados()
c.mostrar(6)