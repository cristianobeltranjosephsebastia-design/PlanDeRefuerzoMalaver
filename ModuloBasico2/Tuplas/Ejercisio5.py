class Universidad:
    def __init__(self, nombre, carreras):
        self.nombre = nombre
        self.carreras = carreras  
carreras = ("Ingeniería", "Medicina", "Derecho", "Arquitectura")
u = Universidad("Universidad Nacional", carreras)

print("Carreras en", u.nombre)
for c in u.carreras:
    print("-", c)