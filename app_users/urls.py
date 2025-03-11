from django.urls import path
from django.shortcuts import redirect
from . import views
from .views import criar_ticket_view  # Importe a função correta da view de tickets

urlpatterns = [
    # Rotas principais
    path('login/', views.login_view, name='login'),  # Página de login
    path('painel/', views.base_view, name='base'),  # Painel (após login)
    path('logout/', views.logout_view, name='logout'),  # Logout
    path("", lambda request: redirect("login"), name="home"),  # Redirecionar para login como padrão

    # Rotas para tickets
    path('tickets/novo/', criar_ticket_view, name='criar_ticket'),  # Página de criação de ticket
]
