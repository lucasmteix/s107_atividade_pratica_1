import unittest
import calculadora

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(calculadora.somar(3, 2), 5)

    def test_subtrair(self):
        self.assertEqual(calculadora.subtrair(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(calculadora.multiplicar(6, 7), 42)

    def test_dividir(self):
        self.assertEqual(calculadora.dividir(8, 2), 4)

    def test_dividir_por_zero(self):
        self.assertEqual(calculadora.dividir(5, 0), "Erro: divisão por zero")

    def test_potencia(self):
        self.assertEqual(calculadora.potencia(2, 4), 16)

    def test_fatorial(self):
        self.assertEqual(calculadora.fatorial(5), 120)

    def test_fatorial_negativo(self):
        self.assertEqual(calculadora.fatorial(-3), "Erro: fatorial de número negativo")

    def test_raiz_quadrada(self):
        self.assertEqual(calculadora.raiz_quadrada(25), 5)

    def test_raiz_quadrada_negativa(self):
        self.assertEqual(calculadora.raiz_quadrada(-9), "Erro: raiz de número negativo")

if __name__ == '__main__':
    unittest.main()