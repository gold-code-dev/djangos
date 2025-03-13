from django.urls import path
from django.shortcuts import redirect
from . import views
from .views import criar_ticket_view  # Importe a função correta da view de tickets
from .views import ticket_list

urlpatterns = [
    # Rotas principais
    path('login/', views.login_view, name='login'),  # Página de login
    path('painel/', views.base_view, name='base'),  # Painel (após login)
    path('logout/', views.logout_view, name='logout'),  # Logout
    path("", lambda request: redirect("login"), name="home"),  # Redirecionar para login como padrão


    # Nova rota para ticket_list
    path('tickets_list/', ticket_list, name='ticket_list'),

]

