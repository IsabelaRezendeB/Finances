from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Despesas-list')
        self.user = User.objects.create_user('c3po', password = '123456')
    
    def test_autenticacao_credenciais(self):
        """Verifica autenticação das credenciais"""
        user = authenticate(username = 'c3po', password = '123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_autenticacao_username_incorreto(self):
        """Verifica se o username está incorreto"""
        user = authenticate(username = 'c3pp', password = '123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_password_incorreto(self):
        """Verifica se a senha está incorreta"""
        user = authenticate(username = 'c3po', password = '654321')
        self.assertFalse((user is not None) and user.is_authenticated)