class Restaurante:
    def __init__(self, nombre, menu):
        self.nombre = nombre
        self.menu = menu

menu = ["Pizza", "Hamburguesa", "Ensalada"]
r = Restaurante("La Buena Mesa", menu)

print("Menú de", r.nombre)
for m in r.menu:
    print("-", m)