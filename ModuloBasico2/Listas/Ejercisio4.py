class Curso:
    def __init__(self, nombre, estudiantes):
        self.nombre = nombre
        self.estudiantes = estudiantes  

estudiantes = ["Ana", "Luis", "Pedro"]
curso = Curso("Matemáticas", estudiantes)

print("Curso:", curso.nombre)
print("Estudiantes:", curso.estudiantes)