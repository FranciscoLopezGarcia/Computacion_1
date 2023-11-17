import unittest
from file_handling import sumar_datos_archivo

class TestFileHandling(unittest.TestCase):

    def test_sumar_datos_archivo(self):
        resultado = sumar_datos_archivo('datos.txt')
        self.assertEqual(resultado, 15)

if __name__ == '__main__':
    unittest.main()
