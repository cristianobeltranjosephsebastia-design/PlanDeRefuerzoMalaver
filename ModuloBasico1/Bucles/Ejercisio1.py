class Contador:
    def contar(self, limite):
        for i in range(1, limite + 1):
            print("Número:", i)

c = Contador()
c.contar(5)