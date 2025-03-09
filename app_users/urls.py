from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Rota para a página de login
    path('painel/', views.painel_view, name='painel'),  # Rota para o painel após login
]