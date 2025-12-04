class Pelota:
    def rebotar(self, veces):
        i = 1
        while i <= veces:
            print(f"Rebote número {i}")
            i += 1

p = Pelota()
p.rebotar(6)