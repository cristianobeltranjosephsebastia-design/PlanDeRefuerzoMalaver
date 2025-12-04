class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        return self.salario

class EmpleadoTiempoCompleto(Empleado):
    def calcular_pago(self):
        return self.salario  

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, salario_por_hora, horas):
        super().__init__(nombre, salario_por_hora)
        self.horas = horas

    def calcular_pago(self):
        return self.salario * self.horas

emp1 = EmpleadoTiempoCompleto("Ana", 2000)
emp2 = EmpleadoMedioTiempo("Luis", 15, 80)
print(f"{emp1.nombre} gana ${emp1.calcular_pago()}")
print(f"{emp2.nombre} gana ${emp2.calcular_pago()}")
