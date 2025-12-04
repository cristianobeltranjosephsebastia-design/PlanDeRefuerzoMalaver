class Planeta:
    def __init__(self, sistema, planetas):
        self.sistema = sistema
        self.planetas = planetas  

planetas = ("Mercurio", "Venus", "Tierra", "Marte", "Júpiter")
sistema_solar = Planeta("Sistema Solar", planetas)

print("Sistema:", sistema_solar.sistema)
print("Planetas:")
for p in sistema_solar.planetas:
    print("-", p)