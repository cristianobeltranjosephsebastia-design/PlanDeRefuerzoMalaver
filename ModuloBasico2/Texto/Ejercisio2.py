class EscritorArchivo:
    def __init__(self, archivo):
        self.archivo = "Texto" + archivo

    def guardar(self, texto):
        with open(self.archivo, "w") as f:
            f.write(texto)
        print(f"✅ Archivo {self.archivo} creado con el texto:")
        print(texto)

e = EscritorArchivo("Ejemplo2.txt")
e.guardar("Este es un mensaje guardado en un archivo externo.")