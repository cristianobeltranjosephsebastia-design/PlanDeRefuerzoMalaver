class Numero:
    def __init__(self, valor):
        self.valor = valor

    def par_o_impar(self):
        if self.valor % 2 == 0:
            return "Par"
        else:
            return "Impar"

n = Numero(7)
print("El número es:", n.par_o_impar())