from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from financas.views import ReceitasViewSet, DespesasViewSet, ListaReceitasMes, ListaDespesasMes, ResumoMesView
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Financas",
      default_version='v1',
      description="Controle de finanças baseado em despesas e receitas",
      terms_of_service="#",
      contact=openapi.Contact(email="exemplo@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename = 'Receitas')
router.register('despesas', DespesasViewSet, basename = 'Despesas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('receitas/<int:ano>/<int:mes>/', ListaReceitasMes.as_view()),
    path('despesas/<int:ano>/<int:mes>/', ListaDespesasMes.as_view()),
    path('resumo/<int:ano>/<int:mes>/', ResumoMesView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]