class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes")

class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo=0, interes=0.02):
        super().__init__(titular, saldo)
        self.interes = interes

    def aplicar_interes(self):
        self.saldo += self.saldo * self.interes

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo=0, sobregiro=100):
        super().__init__(titular, saldo)
        self.sobregiro = sobregiro

    def retirar(self, monto):
        if monto <= self.saldo + self.sobregiro:
            self.saldo -= monto
        else:
            print("Límite de sobregiro excedido")

ahorro = CuentaAhorros("María", 1000)
ahorro.aplicar_interes()
print("Saldo ahorro:", ahorro.saldo)

corriente = CuentaCorriente("Pedro", 500, 200)
corriente.retirar(600)
print("Saldo corriente:", corriente.saldo)