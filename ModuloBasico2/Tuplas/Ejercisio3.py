class Restaurante:
    def __init__(self, nombre, platos):
        self.nombre = nombre
        self.platos = platos  

platos = ("Sushi", "Ramen", "Tempura", "Takoyaki")
r = Restaurante("Restaurante Japonés", platos)

print("Menú de", r.nombre)
for p in r.platos:
    print("-", p)