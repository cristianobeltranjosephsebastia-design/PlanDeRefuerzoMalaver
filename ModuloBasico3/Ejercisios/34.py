class Estudiante:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento
        self.progreso = 0

    def practicar(self, horas):
        self.progreso += horas
        return f"{self.nombre} practicó {horas}h. Progreso total: {self.progreso}h"

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

    def ensenar(self, estudiante, horas):
        return f"{self.nombre} enseñó a {estudiante.nombre} durante {horas}h."

est = Estudiante("Sofía", "Piano")
prof = Profesor("Maestro Juan")
print(est.practicar(3))
print(prof.ensenar(est, 2))