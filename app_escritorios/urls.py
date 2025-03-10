from django.urls import path
from . import views

urlpatterns = [
    path('', views.escritorio_list, name='escritorio_list'),  # Para listar os escritórios
    path('<int:id>/', views.escritorio_detail, name='escritorio_detail'),  # Detalhe do escritório
]
