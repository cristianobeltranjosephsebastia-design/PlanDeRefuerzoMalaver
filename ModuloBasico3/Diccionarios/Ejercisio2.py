class Notas:
    def __init__(self, calificaciones):
        self.calificaciones = calificaciones

    def promedio(self):
        suma = 0
        for nota in self.calificaciones.values():
            suma += nota
        return suma / len(self.calificaciones)

calificaciones = {"Juan": 4.5, "Laura": 3.8, "Pedro": 4.2}
n = Notas(calificaciones)
print("Promedio de notas:", n.promedio())