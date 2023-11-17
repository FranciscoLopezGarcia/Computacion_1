import unittest
from dict_operations import mezclar_diccionarios, obtener_valor_por_clave

class TestDictOperations(unittest.TestCase):

    def test_mezclar_diccionarios(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        resultado = mezclar_diccionarios(dict1, dict2)
        self.assertEqual(resultado, {'a': 1, 'b': 3, 'c': 4})

    def test_obtener_valor_por_clave(self):
        dict1 = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Buenos Aires'}
        resultado = obtener_valor_por_clave(dict1, 'edad')
        self.assertEqual(resultado, 25)

if __name__ == '__main__':
    unittest.main()
