from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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


def criarPedido(request):

    form = PedidoForm()

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'accounts/pedido_form.html', context)


def atualizarPedido(request, pk):

    pedido = Pedido.objects.get(id=pk)
    form = PedidoForm(instance=pedido)

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/pedido_form.html', context)


def deletarPedido(request, pk):
    pedido = Pedido.objects.get(id=pk)
    if request.method == "POST":
        pedido.delete()
        return redirect('/')
    context={'pedido':pedido}
    return render(request, 'accounts/deletar.html', context)