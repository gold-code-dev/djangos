from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Página de login
    path('painel/', views.painel_view, name='painel'),  # Painel (após login)
    path('logout/', views.logout_view, name='logout'),  # Logout
]
