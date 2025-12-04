class Equipo:
    def __init__(self, nombre, jugadores):
        self.nombre = nombre
        self.jugadores = jugadores 

jugadores = ("Messi", "Mbappé", "Neymar", "Suárez")
equipo = Equipo("PSG", jugadores)

print("Equipo:", equipo.nombre)
print("Jugadores:", equipo.jugadores)