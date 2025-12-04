class Candidato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.votos = 0

    def votar(self):
        self.votos += 1

class Eleccion:
    def __init__(self):
        self.candidatos = []

    def agregar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def mostrar_resultados(self):
        for c in self.candidatos:
            print(f"{c.nombre}: {c.votos} votos")

cand1 = Candidato("Alice")
cand2 = Candidato("Bob")

eleccion = Eleccion()
eleccion.agregar_candidato(cand1)
eleccion.agregar_candidato(cand2)

cand1.votar()
cand2.votar()
cand2.votar()

eleccion.mostrar_resultados()