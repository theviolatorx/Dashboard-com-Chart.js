import datetime

from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome do Produto')

    def __str__(self):
        return self.nome


class Vendedor(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome do Vendedor')

    def __str__(self):
        return self.nome


class Venda(models.Model):
    nome_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    nome_vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    total = models.FloatField()
    data = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.nome_produto.nome
