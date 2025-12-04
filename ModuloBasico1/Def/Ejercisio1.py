class Cohete:
    def cuenta_atras(self, segundos):
        while segundos >= 0:
            print(f"Lanzamiento en: {segundos} segundos")
            segundos -= 1
        print("¡Despegue!")

c = Cohete()
c.cuenta_atras(7)