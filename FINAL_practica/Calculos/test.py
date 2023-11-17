import unittest
from math_operations import sumar, restar, multiplicar

class TestMathOperations(unittest.TestCase):

    def test_sumar(self):
        resultado = sumar(3, 5)
        self.assertEqual(resultado, 8)

    def test_restar(self):
        resultado = restar(10, 4)
        self.assertEqual(resultado, 6)

    def test_multiplicar(self):
        resultado = multiplicar(2, 3)
        self.assertEqual(resultado, 6)

if __name__ == '__main__':
    unittest.main()
