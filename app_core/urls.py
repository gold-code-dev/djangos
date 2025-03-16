from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Rotas principais
    path('login/', views.login_view, name='login'),  # Nome correspondente a "login.html"
    path('painel/', views.painel_view, name='painel'),  # Nome correspondente a "painel.html"
    path('logout/', views.logout_view, name='logout'),  # Não precisa de HTML, mas é consistente
    path("", lambda request: redirect("login"), name="home"),  # Redirecionar como padrão para login

    path('painel/tickets/novo/', views.criar_ticket, name="criar_ticket"),
    path('painel/tickets/lista/', views.lista_tickets, name='listar_tickets'),  # Configura a rota 'lista_tickets'

    # path('tarefas/criar/', views.criar_tarefa, name='criar_tarefa'),
    path('painel/tickets/tarefas/criar/<int:numero_ticket>/', views.criar_tarefa, name='criar_tarefa'),

    path('painel/tickets/detalhes/<int:ticket_id>/', views.detalhe_ticket, name='detalhe_ticket'),

    # Dentro de urlpatterns, adicione:
    path('painel/atendimentos/novo/', views.criar_atendimento, name="criar_atendimento"),
    path('painel/atendimentos/lista/', views.lista_atendimentos, name='listar_atendimentos'),
    path('painel/atendimentos/detalhes/<int:atendimento_id>/', views.detalhe_atendimento, name='detalhe_atendimento'),

]

