from rest_framework import viewsets, filters, generics
from financas.models import Receita, Despesa
from financas.serializer import ReceitaSerializer, DespesaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ReceitasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']
    filter_backends[1].search_param = 'descricao'

    authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly,)

# GET /receitas/{ano}/{mes}
class ListaReceitasMes(generics.ListAPIView):
    """Listando as receitas de determinado mês"""

    def get_queryset(self):

        queryset = Receita.objects.filter(data__year=self.kwargs['ano'], data__month=self.kwargs['mes'])
        return queryset

    serializer_class = ReceitaSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly,)

class DespesasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as despesas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']
    filter_backends[1].search_param = 'descricao'

    authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly,)

# GET /despesas/{ano}/{mes}
class ListaDespesasMes(generics.ListAPIView):
    """Listando as despesas de determinado mês"""

    def get_queryset(self):

        queryset = Despesa.objects.filter(data__year=self.kwargs['ano'], data__month=self.kwargs['mes'])
        return queryset

    serializer_class = DespesaSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ResumoMesView(APIView):
    """Detalhando resumo de determinado mes"""

    def get(self, request, ano, mes):
        total_despesas =  Despesa.objects.filter(data__year=ano, data__month=mes).aggregate(Sum('valor'))['valor__sum']

        despesa_por_categoria = Despesa.objects.filter(data__year=ano,
                                                       data__month=mes).values('categoria').annotate(Sum('valor'))



        for despesa in despesa_por_categoria:
            despesa['valor'] = despesa['valor__sum']
            del despesa['valor__sum']

        if len(despesa_por_categoria) == 0:
            despesa_por_categoria = None

        total_receitas = Receita.objects.filter(data__year=ano, data__month=mes).aggregate(Sum('valor'))['valor__sum']

        if total_despesas != None:
            total_despesas = (total_despesas *-1)

        if total_receitas == None:
            saldo_final = total_despesas
        elif total_despesas == None:
            saldo_final = total_receitas
        else:
            saldo_final = total_receitas + total_despesas

        return Response({
            'total_despesas': total_despesas,
            'total_receitas': total_receitas,
            'saldo_final': saldo_final,
            'despesa_por_categoria': despesa_por_categoria

        })
    
    authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly,)