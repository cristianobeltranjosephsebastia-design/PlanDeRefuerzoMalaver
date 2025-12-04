class Persona:
    def __init__(self, edad):
        self.edad = edad

    def mayor_edad(self):
        if self.edad >= 18:
            return "Es mayor de edad"
        else:
            return "Es menor de edad"

p = Persona(16)
print(p.mayor_edad())