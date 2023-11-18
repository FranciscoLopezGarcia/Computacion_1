class Tragamonedas():
    def __init__(self):
        self.monedas = 1000
        self.monedas_tirada = 0
        
    def insertar_moneda(self):
        self.monedas += 1
        self.monedas_tirada += 1
    
    def tirar(self):
        if self.monedas_tirada == 0:
            raise NoHayMonedaException()
        self.monedas -= 1
        self.monedas_tirada -= 1
        return [1,2,3]
    
    
class NoHayMonedaException(Exception):
    pass

class NoHayMonedasParaPremioException(Exception):
    pass