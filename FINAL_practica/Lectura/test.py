import unittest
from file_handling import contar_lineas

class TestFileHandling(unittest.TestCase):

    def test_contar_lineas(self):
        resultado = contar_lineas('archivo.txt')
        self.assertEqual(resultado, 3)

if __name__ == '__main__':
    unittest.main()
