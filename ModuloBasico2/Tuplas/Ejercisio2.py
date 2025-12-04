class Cine:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas  

peliculas = ("Inception", "Avatar", "Interstellar", "Titanic")
cine = Cine("Cinepolis", peliculas)

print("Cartelera en", cine.nombre)
for p in cine.peliculas:
    print("-", p)