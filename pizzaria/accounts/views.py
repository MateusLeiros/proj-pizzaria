from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    pedidos = Pedido.objects.all()
    clientes = Cliente.objects.all()

    total_clientes = clientes.count()
    total_pedidos = pedidos.count()
    entregues = pedidos.filter(status='Entregue').count()
    aguardando = pedidos.filter(status='Aguardando').count()

    context = {'pedidos':pedidos, 'clientes':clientes, 'total_pedidos':total_pedidos, 'entregues':entregues, 'aguardando':aguardando}

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    pizzas = Pizza.objects.all()
    return render(request, 'accounts/products.html', {'pizzas':pizzas})

def cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    pedidos = cliente.pedido_set.all()
    pedidos_count = pedidos.count()


    context = {'cliente':cliente, 'pedidos':pedidos, 'pedidos_count':pedidos_count}
    return render(request, 'accounts/cliente.html', context)