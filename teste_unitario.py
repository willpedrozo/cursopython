import unittest as ut

# importa as funcoes de operacoes do arquivo
from operacoes import somar, subtrair, dividir

class Testar_operacoes(ut.TestCase):
    def testar_somar(self):
        #testa se 2 + 3 é 5
        self.assertEqual(somar(2,3),5)
        #testa se a soma de -1 e 1 é 0
        self.assertEqual(somar(-1,1),0)
        # testa se a soma de -2 e -3 é -5
        self.assertEqual(somar(-2,-3),-5)

    def testar_dividir(self):
        #testa se 10/2 é 5
        self.assertEqual(dividir(10,2),5)
        #testa se -6/3 é -2
        self.assertEqual(dividir(-6,3),-2)
        #testa se a divisao por 0 traz o erro correto
        with self.assertRaises(ValueError):
            dividir(1,0) #espera-se que levante o valueError quando tentar dividir por zero


if __name__ == '__main__':
    ut.main() #executa todos os teste definidos
    


