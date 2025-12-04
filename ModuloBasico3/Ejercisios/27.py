class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.publicaciones = []

    def publicar(self, texto):
        self.publicaciones.append(texto)

    def mostrar_publicaciones(self):
        print(f"Publicaciones de {self.nombre}:")
        for p in self.publicaciones:
            print("-", p)

user1 = Usuario("Ana")
user1.publicar("Hola, esta es mi primera publicación.")
user1.publicar("Aprendiendo Python con POO 🚀")
user1.mostrar_publicaciones()