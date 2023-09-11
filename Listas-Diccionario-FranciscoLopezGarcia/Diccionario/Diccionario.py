import unittest
def todo(lista):
    lista = []
    rep = {}

    for n in lista:
        if n in rep:
            rep[n] +=1
        else:
            rep[n] = 1

    print ('Los elementos se repiten :', rep)

class test_rep(unittest.TestCase):
    def test_1(self):
        entrada = todo([1,1,1,1,1,1,34,4,5,6,7,7,5,1,1,1,12,4,9,9,0,5])

        

if __name__=='__main__':
    unittest.main()