class ContarLineas:
    def __init__(self, archivo):
        self.archivo = "Texto" + archivo

    def contar(self):
        with open(self.archivo, "w") as f:
            f.write("Primera línea\nSegunda línea\nTercera línea\nCuarta línea")
        
        with open(self.archivo, "r") as f:
            lineas = f.readlines()
        print(f"📊 El archivo {self.archivo} tiene {len(lineas)} líneas")

c = ContarLineas("Ejemplo5.txt")
c.contar()