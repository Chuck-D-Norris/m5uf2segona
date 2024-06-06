import unittest
from calculadora import Calculadora

class Testcalculadora(unittest.TestCase):
    def setUp(self):
        self.Calculadora = Calculadora () #instanciem la classe a self.calculadora


    def test_sumar(self):  #instancia del test per poder realitzar la suma amb el asertequal indiquem per exemple 2 i 3 i la suma es 5
        self.assertEqual(self.Calculadora.sumar(2, 3), 5)


    def test_restar (self): #instancia del test per poder realitzar la resta amb el asertequal indiquem per exemple 5 i 3 i la resta es 2
        self.assertEqual(self.Calculadora.restar(5, 3), 2)


    def test_multiplicar(self): #instancia del test per poder realitzar la multiplicacio amb el asertequal indiquem per exemple 5 i 3 i la resta es 15
        self.assertEqual(self.Calculadora.multiplicar(5, 3), 15)

    
    def test_dividir(self): #instancia del test per poder realitzar la divisio amb el asertequal indiquem per exemple 8 i 2 i la divisio es 4
        self.assertEqual(self.Calculadora.dividir(8, 2), 4)
        with self.assertRaises(ValueError): # el asertRaises es per indica si algu fica en mes del 2 un 0 que saltigue
            self.Calculadora.dividir(8, 0)

    
    def test_factorial(self):
        self.assertEqual(self.Calculadora.factorial(0),1)
        with self.assertRaises(ValueError): # el asertRaises es per indica en aquest cas que el factorial en cas de que no estigue definit
            self.Calculadora.dividir(1,0)
        

