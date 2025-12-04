class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"Prestaste '{self.titulo}'"
        return f"'{self.titulo}' no está disponible"

    def devolver(self):
        self.disponible = True
        return f"Devolviste '{self.titulo}'"

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"

libro = Libro("El Principito", "Antoine de Saint-Exupéry")
print(libro)
print(libro.prestar())
print(libro)
print(libro.devolver())
print(libro)


