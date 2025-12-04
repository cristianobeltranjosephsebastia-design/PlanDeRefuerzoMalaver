class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Saldo actual: ${self.__saldo}"
        return "Cantidad inválida"

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Saldo actual: ${self.__saldo}"
        return "Fondos insuficientes"

    def consultar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Carlos", 1000)
print(cuenta.depositar(500))
print(cuenta.retirar(300))
print(f"Saldo final: {cuenta.consultar_saldo()}")

