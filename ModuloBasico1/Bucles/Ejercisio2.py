class NumerosPares:
    def mostrar(self, n):
        for i in range(2, n+1, 2):
            print("Par:", i)

np = NumerosPares()
np.mostrar(10)