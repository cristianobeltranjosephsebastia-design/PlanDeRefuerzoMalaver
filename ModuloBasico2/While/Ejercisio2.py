class Contador:
    def __init__(self, limite):
        self.limite = limite

    def contar(self):
        num = 1
        while num <= self.limite:
            print("Número:", num)
            num += 1

c = Contador(5)
c.contar()