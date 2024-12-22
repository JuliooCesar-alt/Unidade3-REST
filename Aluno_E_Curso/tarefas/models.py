from django.db import models


class Tarefa(models.Model):
  nome = models.CharField(max_length=100)
  descricao = models.TextField()
  data_criacao = models.DateTimeField(auto_now_add=True)
  data_conclusao = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return self.nome


class Categoria(models.Model):
  nome = models.CharField(max_length=255)
  descricao = models.TextField()

  def __str__(self):
    return self.nome
