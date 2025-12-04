class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.detalles = []

    def agregar_detalle(self, producto, cantidad):
        self.detalles.append((producto, cantidad))

    def mostrar(self):
        print(f"Pedido de {self.cliente.nombre}:")
        for producto, cantidad in self.detalles:
            print(f"- {producto} x{cantidad}")

cliente = Cliente("Luis")
pedido = Pedido(cliente)
pedido.agregar_detalle("Pizza", 2)
pedido.agregar_detalle("Refresco", 1)
pedido.mostrar()
