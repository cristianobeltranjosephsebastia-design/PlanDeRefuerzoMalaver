class Reloj:
    def __init__(self, segundos):
        self.segundos = segundos

    def tic_tac(self):
        while self.segundos > 0:
            print(f"Quedan {self.segundos} segundos")
            self.segundos -= 1
        print("Tiempo terminado")

r = Reloj(5)
r.tic_tac()