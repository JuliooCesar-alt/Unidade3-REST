from rest_framework import serializers
from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarefa
        fields = '__all__'  # Seleciona todos os campos do modelo


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao']
