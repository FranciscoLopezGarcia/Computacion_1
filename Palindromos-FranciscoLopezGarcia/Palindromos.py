import unittest


def Palindromo(palabras):
    words = palabras.replace(" ","").replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').lower()

    if words == words[::-1]:
        return True
    else:
       return False

class test_palindromo(unittest.TestCase):
    def test_mayusc(self):
        self.assertTrue(Palindromo('NeuQuen'))
    def test_espacios(self):
        self.assertTrue(Palindromo('anita lava la tina'))
    def test_nmr(self):
        self.assertTrue(Palindromo('404'))
    def test_error(self):
        self.assertFalse(Palindromo('Hola que tal'))


if __name__ == '__main__':
    unittest.main()
