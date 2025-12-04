class Termometro:
    def __init__(self, temp_inicial):
        self.temperatura = temp_inicial

    def enfriar(self, hasta):
        while self.temperatura > hasta:
            print(f"Temperatura actual: {self.temperatura}°C")
            self.temperatura -= 1
        print("Temperatura final:", self.temperatura, "°C")

t = Termometro(30)
t.enfriar(25)