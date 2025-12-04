class ElementoSistema:
    def __init__(self, nombre):
        self.nombre = nombre

class Archivo(ElementoSistema):
    def __init__(self, nombre, contenido=""):
        super().__init__(nombre)
        self.contenido = contenido

    def mostrar(self):
        return f"Archivo: {self.nombre} - Contenido: {self.contenido}"

class Carpeta(ElementoSistema):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def listar(self):
        print(f"Carpeta: {self.nombre}")
        for e in self.elementos:
            if isinstance(e, Carpeta):
                print(f"- Carpeta: {e.nombre}")
            else:
                print(f"- Archivo: {e.nombre}")

carpeta = Carpeta("Documentos")
carpeta.agregar(Archivo("notas.txt", "POO en Python"))
carpeta.agregar(Archivo("tarea.docx", "Ejercicio 19"))
sub = Carpeta("Fotos")
sub.agregar(Archivo("imagen.png"))
carpeta.agregar(sub)
carpeta.listar()