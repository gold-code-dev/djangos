# views/__init__.py
from .login import login_view
from .logout import logout_view
# from .painel import painel_view
from .base import base_view
from .ticket import criar_ticket_view

__all__ = [
    "login_view",
    "logout_view",
    "base_view",
    "criar_ticket_view",
]
