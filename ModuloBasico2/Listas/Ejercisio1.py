class Biblioteca:
    def __init__(self, libros):
        self.libros = libros

libros = ["Cien años de soledad", "El principito", "1984"]
b = Biblioteca(libros)

for l in b.libros:
    print("Libro:", l)