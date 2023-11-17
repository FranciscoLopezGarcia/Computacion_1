import unittest
from list_operations import obtener_elemento_medio, filtrar_pares

class TestListOperations(unittest.TestCase):

    def test_obtener_elemento_medio(self):
        resultado = obtener_elemento_medio([1, 2, 3, 4, 5])
        self.assertEqual(resultado, 3)

    def test_filtrar_pares(self):
        resultado = filtrar_pares([1, 2, 3, 4, 5, 6])
        self.assertEqual(resultado, [2, 4, 6])

if __name__ == '__main__':
    unittest.main()
