class Usuario:
    def __init__(self, nombre, rol="Cliente"):
        self.nombre = nombre
        self.rol = rol

    def permisos(self):
        if self.rol == "Administrador":
            return "Acceso total"
        elif self.rol == "Moderador":
            return "Acceso parcial"
        return "Acceso limitado"

usuarios = [
    Usuario("Ana", "Administrador"),
    Usuario("Luis", "Moderador"),
    Usuario("Carlos", "Cliente")
]

for u in usuarios:
    print(f"{u.nombre} ({u.rol}): {u.permisos()}")