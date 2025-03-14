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
    # path('painel/tickets/<int:numero_escritorio>/add_info/', views.add_info, name='add_info'),

    # path('painel/ticket_new/', views.ticket_new_view, name='ticket_new'),

    # Rotas relacionadas a tickets
    # path('tickets_list/', views.ticket_list, name='tickets_list'),  # Nome igual ao "tickets_list.html"
    # path('ticket_criar/', views.criar_ticket_view, name='ticket_criar'),  # Nome igual ao "ticket_criar.html"

    # path('taref/as/', TarefaListView.as_view(), name='tarefa-list'),

    # path('tarefas/criar/', views.criar_tarefa, name='criar_tarefa'),
    path('painel/tickets/tarefas/criar/<int:numero_ticket>/', views.criar_tarefa, name='criar_tarefa'),

    # path('tarefas/criar/<int:numero_ticket>/', views.criar_tarefa_com_ticket, name='criar_tarefa_com_ticket'),

]

