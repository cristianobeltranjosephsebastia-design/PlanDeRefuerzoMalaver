class Juego:
    def __init__(self, vidas):
        self.vidas = vidas

    def jugar(self):
        while self.vidas > 0:
            print(f"Te quedan {self.vidas} vidas")
            self.vidas -= 1
        print("Game Over")

j = Juego(3)
j.jugar()