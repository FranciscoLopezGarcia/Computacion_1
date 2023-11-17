import unittest
from file_handling import escribir_en_archivo, leer_archivo

class TestFileHandling(unittest.TestCase):

    def test_escribir_en_archivo(self):
        contenido = "Hola, este es un nuevo contenido."
        escribir_en_archivo('nuevo_archivo.txt', contenido)
        resultado = leer_archivo('nuevo_archivo.txt')
        self.assertEqual(resultado, contenido)

if __name__ == '__main__':
    unittest.main()
