class CuentaRegresiva:
    def __init__(self, inicio):
        self.inicio = inicio

    def iniciar(self):
        while self.inicio > 0:
            if self.inicio % 2 == 0:
                print(f"{self.inicio} es par")
            else:
                print(f"{self.inicio} es impar")
            self.inicio -= 1
        print("¡Despegue!")

c = CuentaRegresiva(7)
c.iniciar()