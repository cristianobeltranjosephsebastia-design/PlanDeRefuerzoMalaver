class AgregarTexto:
    def __init__(self, archivo):
        self.archivo = "Texto" + archivo

    def agregar(self, texto):
        with open(self.archivo, "w") as f:
            f.write("Entrada inicial")
        
        with open(self.archivo, "a") as f:
            f.write("\n" + texto)
        
        print(f"➕ Se agregó al archivo {self.archivo}:")
        print(texto)

a = AgregarTexto("Ejemplo3.txt")
a.agregar("Nueva entrada en el registro.")