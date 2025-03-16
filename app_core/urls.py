from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Rotas principais
    path('login/', views.login_view, name='login'),  # Nome correspondente a "login.html"
    path('painel/', views.painel_view, name='painel'),  # Nome correspondente a "painel.html"
    path('logout/', views.logout_view, name='logout'),  # Não precisa de HTML, mas é consistente
    path("", lambda request: redirect("login"), name="home"),  # Redirecionar como padrão para login

    path('painel/tickets/novo/', views.ticket_criar, name="ticket_criar"),
    path('painel/tickets/lista/', views.ticket_listar, name='ticket_listar'),  # Configura a rota 'lista_tickets'
    path('painel/tickets/detalhes/<int:ticket_id>/', views.ticket_detalhe, name='ticket_detalhe'),

    # path('tarefas/criar/', views.criar_tarefa, name='criar_tarefa'),
    # path('painel/tickets/tarefas/criar/<int:numero_ticket>/', views.criar_tarefa, name='criar_tarefa'),


]

