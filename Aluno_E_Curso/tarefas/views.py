from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer


class TarefaViewSet(viewsets.ModelViewSet):
  queryset = Tarefa.objects.all()
  serializer_class = TarefaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerializer
