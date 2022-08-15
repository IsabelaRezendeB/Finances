from django.test import TestCase
from financas.models import Despesa, Receita
from financas.serializer import DespesaSerializer, ReceitaSerializer

class ReceitaSerializerTestCase(TestCase):

    def setUp(self):
        self.receita = Receita(
            descricao = 'Herança',
            valor = 200.0,
            data = '2022-07-04',
        )
        self.serializer = ReceitaSerializer(instance = self.receita)
    
    def test_verifica_campos(self):
        """Verifica se os campos de Receita estão sendo serializados corretamente"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'descricao', 'valor', 'data']))
    
    def test_verifica_conteudo(self):
        """Verifica se o conteúdo de Receita está sendo serializado corretamente"""
        data = self.serializer.data
        self.assertEqual(data['descricao'], self.receita.descricao)
        self.assertEqual(data['valor'], self.receita.valor)
        self.assertEqual(data['data'], self.receita.data)

class DespesaSerializerTestCase(TestCase):

    def setUp(self):
        self.despesa = Despesa(
            descricao = 'Supermercado',
            valor = 200.0,
            data = '2022-07-04',
            categoria = 'O'
        )
        self.serializer = DespesaSerializer(instance = self.despesa)
    
    def test_verifica_campos(self):
        """Verifica se os campos de Despesa estão sendo serializados corretamente"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'descricao', 'valor', 'data', 'categoria']))
    
    def test_verifica_conteudo(self):
        """Verifica se o conteúdo de Despesa está sendo serializado corretamente"""
        data = self.serializer.data
        self.assertEqual(data['descricao'], self.despesa.descricao)
        self.assertEqual(data['valor'], self.despesa.valor)
        self.assertEqual(data['data'], self.despesa.data)
        self.assertEqual(data['categoria'], self.despesa.categoria)