class Semaforo:
    def __init__(self):
        self.estado = "Rojo"

    def cambiar(self):
        if self.estado == "Rojo":
            self.estado = "Verde"
        elif self.estado == "Verde":
            self.estado = "Amarillo"
        else:
            self.estado = "Rojo"

    def __str__(self):
        return f"Semáforo en {self.estado}"

semaforo = Semaforo()
print(semaforo)
semaforo.cambiar()
print(semaforo)
semaforo.cambiar()
print(semaforo)
