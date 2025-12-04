class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def decir_hola(self):
        return f"¡Hola {self.nombre}!"

s = Saludo("Camila")
print(s.decir_hola())