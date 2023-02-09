from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=True)
    telefone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    data_criado = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nome


class Pizza(models.Model):
    CATEGORIA=(
        ('Salgada', 'Salgada'),
        ('Doce', 'Doce'),
        ('Especial', 'Especial'),
    )
    TAMANHO=(
        ('Brotinho','Brotinho'),
        ('Media', 'Media'),
        ('Familia', 'Familia'),
        ('Gigante', 'Gigante'),
    )
    nome = models.CharField(max_length=200, null=True)
    valor = models.FloatField(null=True)
    tamanho = models.CharField(max_length=200, null=True, choices=TAMANHO)
    categoria = models.CharField(max_length=200, null=True, choices=CATEGORIA)
    descricao = models.CharField(max_length=200, null=True)
    data_criado = models.DateTimeField(auto_now_add=True, null=True)

class Pedido(models.Model):
    STATUS = (
        ('Aguardando', 'Aguardando'),
        ('Saiu para entrega', 'Saiu para entrega'),
        ('Entregue', 'Entregue'),
    )

    #cliente = 
    #pizza = 
    data_criado = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)