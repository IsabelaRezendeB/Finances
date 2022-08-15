from django.db import models

class Receita(models.Model):
    descricao = models.CharField(max_length = 100)
    valor = models.FloatField()
    data = models.DateField()

    def __str__(self):
        return self.descricao

class Despesa(models.Model):
    descricao = models.CharField(max_length = 100)
    valor = models.FloatField()
    data = models.DateField()
    CATEGORIA = (
        ('A', 'Alimentação'),
        ('S', 'Saúde'),
        ('M', 'Moradia'),
        ('T', 'Transporte'),
        ('E', 'Educação'),
        ('L', 'Lazer'),
        ('I', 'Imprevisto'),
        ('O', 'Outras')
    )
    categoria = models.CharField(max_length = 1, choices = CATEGORIA, default = 'O')

    def __str__(self):
        return self.descricao