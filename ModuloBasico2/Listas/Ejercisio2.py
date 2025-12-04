class Tienda:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

productos = [("Pan", 2000), ("Leche", 3500), ("Queso", 8000)]
t = Tienda("Supermercado", productos)

print("Tienda:", t.nombre)
for p in t.productos:
    print(f"{p[0]} - ${p[1]}")