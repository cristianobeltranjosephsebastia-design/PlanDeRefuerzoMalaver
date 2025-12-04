class Elevador:
    def subir(self, pisos):
        piso = 1
        while piso <= pisos:
            print(f"El elevador está en el piso {piso}")
            piso += 1

e = Elevador()
e.subir(6)