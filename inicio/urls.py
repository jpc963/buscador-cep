from django.urls import path
from .views import *

urlpatterns = [
    path('', get_routes, name='routes'),
    path('pesquisa/<str:cep>', pesquisar_cep, name='pesquisar_cep'),
    path('ceps', historico_ceps, name='historico_ceps'),
]
