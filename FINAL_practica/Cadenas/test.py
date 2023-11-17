import unittest
from string_operations import contar_vocales, invertir_cadena

class TestStringOperations(unittest.TestCase):

    def test_contar_vocales(self):
        resultado = contar_vocales("python")
        self.assertEqual(resultado, 2)

    def test_invertir_cadena(self):
        resultado = invertir_cadena("hello")
        self.assertEqual(resultado, "olleh")

if __name__ == '__main__':
    unittest.main()
