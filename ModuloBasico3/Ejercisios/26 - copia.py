class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = {}

    def agregar_nota(self, materia, nota):
        if 0 <= nota <= 100:
            self.calificaciones[materia] = nota

    def promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones.values()) / len(self.calificaciones)

    def __str__(self):
        return f"{self.nombre} - Promedio: {self.promedio():.2f}"

est = Estudiante("Laura")
est.agregar_nota("Matemáticas", 90)
est.agregar_nota("Historia", 80)
print(est)