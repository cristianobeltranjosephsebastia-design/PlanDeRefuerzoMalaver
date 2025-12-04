class Reloj:
    def horas(self, limite):
        for h in range(1, limite + 1):
            print(f"Han pasado {h} hora(s)")

r = Reloj()
r.horas(5)