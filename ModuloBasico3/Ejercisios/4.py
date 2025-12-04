class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "✔" if self.completada else "✘"
        return f"{self.descripcion} [{estado}]"

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar(self, tarea):
        self.tareas.append(tarea)

    def mostrar(self):
        for tarea in self.tareas:
            print(tarea)

lista = ListaTareas()
lista.agregar(Tarea("Estudiar Python"))
lista.agregar(Tarea("Hacer ejercicio"))
lista.tareas[0].marcar_completada()
lista.mostrar()
