class Calendario:
    def __init__(self, mes):
        self.mes = mes

    def dias(self, cantidad):
        for d in range(1, cantidad + 1):
            print(f"Día {d} de {self.mes}")

c = Calendario("Septiembre")
c.dias(10)