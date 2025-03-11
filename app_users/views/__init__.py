# views/__init__.py
from .login import login_view
from .logout import logout_view
# from .painel import painel_view

__all__ = ["login_view", "logout_view",
           # "painel_view"
           ]
