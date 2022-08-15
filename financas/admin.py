from django.contrib import admin
from financas.models import Receita, Despesa

class Receitas(admin.ModelAdmin):
    list_display = ('id','descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao', 'valor')
    search_fields = ('descricao',)
    list_per_page = 20

admin.site.register(Receita, Receitas)

class Despesas(admin.ModelAdmin):
    list_display = ('id','descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao', 'valor')
    search_fields = ('descricao',)

admin.site.register(Despesa, Despesas)