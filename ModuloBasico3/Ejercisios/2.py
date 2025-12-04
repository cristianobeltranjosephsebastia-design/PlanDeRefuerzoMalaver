class CalculadoraSimple:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: división por cero"
        return a / b

calc = CalculadoraSimple()
print("Suma:", calc.sumar(15, 5))
print("División:", calc.dividir(50, 2))
