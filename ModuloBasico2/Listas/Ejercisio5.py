class Playlist:
    def __init__(self, nombre, canciones):
        self.nombre = nombre
        self.canciones = canciones

canciones = ["Imagine", "Bohemian Rhapsody", "Hotel California"]
p = Playlist("Favoritas", canciones)

print("Playlist:", p.nombre)
for c in p.canciones:
    print("-", c)