class CuentaRegresiva:
    def iniciar(self, n):
        while n >= 0:
            print(n)
            n -= 1

cr = CuentaRegresiva()
cr.iniciar(5)