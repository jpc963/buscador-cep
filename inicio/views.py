from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
import requests
from .models import *
from .serializers import *


@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/ceps/',
            'method': 'GET',
            'body': None,
            'description': 'Retorna um array de objetos com todos os ceps pesquisados'
        },
        {
            'Endpoint': '/pesquisa/numero_cep',
            'method': 'GET',
            'body': None,
            'description': 'Retorna um objeto com os dados do cep pesquisado'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def pesquisar_cep(request, cep):
    requisicao = requests.get(f'https://brasilapi.com.br/api/cep/v1/{cep}')
    dados = requisicao.json()
    if requisicao.status_code == 200:
        cep_model = Cep.objects.all()

        if not cep_model.filter(cep=dados['cep']).exists():
            cep_model_create = Cep.objects.create(
                cep=dados['cep'],
                state=dados['state'],
                city=dados['city'],
                neighborhood=dados['neighborhood'],
                street=dados['street'],
                service=dados['service'],
            )
            cep_model_create.save()
            data = request.data
            cep_serializer_create = Cep.objects.get(cep=cep)
            serializer = CepSerializer(instance=cep_serializer_create, data=data)
            if serializer.is_valid():
                serializer.save()

            return Response(dados)

        return Response(dados)

    return Response('CEP inválido')


@api_view(['GET'])
def historico_ceps(request):
    ceps = Cep.objects.all().order_by('-searched')
    serializer = CepSerializer(ceps, many=True)
    return Response(serializer.data)
