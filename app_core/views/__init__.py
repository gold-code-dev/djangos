# views/__init__.py
from .login_view import login_view
from .painel_view import painel_view
from .logout_view import logout_view




# from .painel import painel_view
from .base import base_view
from .ticket import criar_ticket_view
from .ticket_list import ticket_list

__all__ = [
    "login_view",
    "painel_view",
    "logout_view",



    "base_view",
    "criar_ticket_view",
    "ticket_list"
]
