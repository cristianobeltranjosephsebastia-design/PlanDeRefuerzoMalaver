class LectorArchivo:
    def __init__(self, archivo):
        self.archivo = "Texto" + archivo

    def leer(self):
        with open(self.archivo, "w") as f:
            f.write("El sol brilla en la mañana\nLas aves cantan alegres\nLa vida comienza de nuevo")
        
        with open(self.archivo, "r") as f:
            contenido = f.read()
            print("📄 Contenido del archivo:")
            print(contenido)

l = LectorArchivo("Ejemplo1.txt")
l.leer()