import random
class Tragamonedas():
    def __init__(self):
        self.monedas = 1000
        self.monedas_tirada = 0

    def insertar_moneda(self):
        if self.monedas == 55 and self.monedas_tirada == 5:
            raise NoHayMonedasParaPremioException()
        else:
            self.monedas += 1
            self.monedas_tirada += 1

    def tirar(self):
        if self.monedas_tirada == 0:
            raise NoHayMonedaException()
        else:
            self.monedas -= 1
            self.monedas_tirada = 0
            return 0
            
        

class NoHayMonedaException(Exception):
    pass

class NoHayMonedasParaPremioException(Exception):
    pass