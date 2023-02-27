from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('cliente/<str:pk>/', views.cliente, name="cliente"),
    path('criar_pedido/', views.criarPedido, name="criar_pedido"),
    path('atualizar_pedido/<str:pk>/', views.atualizarPedido, name="atualizar_pedido"),
    path('deletar_pedido/<str:pk>/', views.deletarPedido, name="deletar_pedido")
]