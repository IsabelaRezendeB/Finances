from django.test import TestCase
from financas.models import Despesa, Receita

class ReceitaModelTestCase(TestCase):

    def setUp(self):
        self.despesa = Receita(
            descricao = 'Herança',
            valor = 200.0,
            data = '2022-07-04'
        )
    
    def test_verifica_atributos(self):
        """Verifica Atributos do model Receita"""
        self.assertEqual(self.despesa.descricao, 'Herança')
        self.assertEqual(self.despesa.valor, 200.0)
        self.assertEqual(self.despesa.data, '2022-07-04')

class DespesaModelTestCase(TestCase):

    def setUp(self):
        self.despesa = Despesa(
            descricao = 'Supermercado',
            valor = 200.0,
            data = '2022-07-04'
        )
    
    def test_verifica_atributos(self):
        """Verifica Atributos do model Despesa"""
        self.assertEqual(self.despesa.descricao, 'Supermercado')
        self.assertEqual(self.despesa.valor, 200.0)
        self.assertEqual(self.despesa.data, '2022-07-04')
        self.assertEqual(self.despesa.categoria, 'O')