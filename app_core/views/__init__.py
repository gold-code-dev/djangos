# views/__init__.py
from .login_view import login_view
from .painel_view import painel_view
from .logout_view import logout_view
# from .ticket_new_view import ticket_new_view
from .criar_ticket_view import criar_ticket


# from .painel import painel_view
# from .ticket import criar_ticket_view
# from .ticket_list import ticket_list

__all__ = [
    "login_view",
    "painel_view",
    "logout_view",
    "criar_ticket"
    # "ticket_new_view",


    # "criar_ticket_view",
    # "ticket_list"
]
