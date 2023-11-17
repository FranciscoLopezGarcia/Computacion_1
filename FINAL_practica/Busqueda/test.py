import unittest
from file_handling import buscar_palabra

class TestFileHandling(unittest.TestCase):

    def test_buscar_palabra(self):
        resultado = buscar_palabra('archivo.txt', 'Python')
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()
