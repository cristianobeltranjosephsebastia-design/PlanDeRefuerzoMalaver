class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar(self, producto):
        self.productos[producto.nombre] = producto

    def buscar(self, nombre):
        return self.productos.get(nombre, "Producto no encontrado")

    def mostrar(self):
        for p in self.productos.values():
            print(f"{p.nombre} - Stock: {p.stock}")

inv = Inventario()
inv.agregar(Producto("Pan", 20))
inv.agregar(Producto("Leche", 15))
inv.mostrar()
print(inv.buscar("Pan").stock)