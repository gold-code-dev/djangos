from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Rotas principais
    path('login/', views.login_view, name='login'),  # Nome correspondente a "login.html"
    path('painel/', views.painel_view, name='painel'),  # Nome correspondente a "painel.html"
    path('logout/', views.logout_view, name='logout'),  # Não precisa de HTML, mas é consistente
    path("", lambda request: redirect("login"), name="home"),  # Redirecionar como padrão para login

    # Rotas relacionadas a tickets
    path('tickets_list/', views.ticket_list, name='tickets_list'),  # Nome igual ao "tickets_list.html"
    path('ticket_criar/', views.criar_ticket_view, name='ticket_criar'),  # Nome igual ao "ticket_criar.html"
]
