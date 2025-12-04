class Semaforo:
    def ciclo(self, vueltas):
        for i in range(1, vueltas + 1):
            print(f"Vuelta {i}: Verde -> Amarillo -> Rojo")

s = Semaforo()
s.ciclo(3)