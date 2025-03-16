# views/__init__.py
from .login_view import login_view
from .painel_view import painel_view
from .logout_view import logout_view
# from .ticket_new_view import ticket_new_view
from .criar_ticket_view import criar_ticket
from .tickets_lista import tickets_lista
# from .add_info_view import add_info
from .criar_tarefa_view import criar_tarefa
from  .detalhe_ticket import detalhe_ticket

# from .painel import painel_view
# from .ticket import criar_ticket_view
# from .ticket_list import ticket_list

__all__ = [
    "login_view",
    "painel_view",
    "logout_view",
    "criar_ticket",
    # "ticket_new_view",
    "tickets_lista",
    # "add_info"
    'criar_tarefa',
    'detalhe_ticket',


    # "criar_ticket_view",
    # "ticket_list"
]
