from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('cliente/<str:pk>/', views.cliente),
]