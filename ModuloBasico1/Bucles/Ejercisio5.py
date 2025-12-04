class Tablas:
    def multiplicar(self, numero):
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

t = Tablas()
t.multiplicar(7)