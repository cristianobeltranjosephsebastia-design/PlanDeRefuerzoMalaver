class Lluvia:
    def gotas(self, cantidad):
        for i in range(1, cantidad + 1):
            print(f"Gota número {i} cayó")

l = Lluvia()
l.gotas(8)