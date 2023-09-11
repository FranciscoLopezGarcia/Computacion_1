import unittest

class Persona:
    def __init__(self, dni = 1, apellido = "Fernandez", nombre = "Alberto"):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
    def __repr__(self):
        return f'Persona: {self.dni}, {self.apellido}, {self.nombre}'

class TestPersona(unittest.TestCase):
    def test_persona(self):
        persona = Persona()
        self.assertEqual(persona.__dict__, "{'dni': 1, 'apellido': 'Fernandez', 'nombre': 'Alberto'}")


    if __name__== "__main__":
        unittest.main()
