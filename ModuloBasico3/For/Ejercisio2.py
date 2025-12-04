class Supermercado:
    def __init__(self, inventario):
        self.inventario = inventario

    def mostrar(self):
        for producto, stock in self.inventario.items():
            print(f"{producto}: {stock} disponibles")

inventario = {"Arroz": 20, "Azúcar": 15, "Sal": 25}
s = Supermercado(inventario)
s.mostrar()