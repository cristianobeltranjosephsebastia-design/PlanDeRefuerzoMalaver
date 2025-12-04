class GuardarLista:
    def __init__(self, archivo):
        self.archivo = "Texto" + archivo

    def guardar(self, elementos):
        with open(self.archivo, "w") as f:
            for e in elementos:
                f.write(e + "\n")
        print(f"📂 Se guardó una lista en {self.archivo}:")
        for e in elementos:
            print("-", e)

g = GuardarLista("Ejemplo4.txt")
g.guardar(["Sebastian", "Krisr", "Sofia", "Ivan"])