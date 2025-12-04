class Examen:
    def __init__(self, nota):
        self.nota = nota

    def resultado(self):
        if self.nota >= 3:
            return "Aprobado"
        else:
            return "Reprobado"

e = Examen(4.2)
print("Resultado:", e.resultado())