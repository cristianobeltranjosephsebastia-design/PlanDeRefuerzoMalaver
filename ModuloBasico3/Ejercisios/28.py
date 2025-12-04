class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"Prestaste '{self.titulo}'"
        return f"'{self.titulo}' ya está prestado"

    def devolver(self):
        self.disponible = True
        return f"Devolviste '{self.titulo}'"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            print(f"{libro.titulo} - {libro.autor} ({estado})")

biblio = Biblioteca()
lib1 = Libro("1984", "George Orwell")
lib2 = Libro("El Quijote", "Cervantes")
biblio.agregar_libro(lib1)
biblio.agregar_libro(lib2)
biblio.mostrar_libros()
print(lib1.prestar())
biblio.mostrar_libros()
