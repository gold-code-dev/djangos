# views/__init__.py
from .login_view import login_view
from .painel_view import painel_view
from .logout_view import logout_view
# from .ticket_new_view import ticket_new_view
from .ticket_criar import ticket_criar
from .ticket_listar import ticket_listar
# from .add_info_view import add_info
from .criar_tarefa_view import criar_tarefa
from  .ticket_detalhe import ticket_detalhe

# from .painel import painel_view
# from .ticket_list import ticket_list

__all__ = [
    "login_view",
    "painel_view",
    "logout_view",
    "ticket_criar",
    # "ticket_new_view",
    "ticket_listar",
    # "add_info"
    'criar_tarefa',
    'ticket_detalhe',


    # "ticket_list"
]
