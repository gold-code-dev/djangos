from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('login/', views.login_view, name='login'),  # Página de login
    path('painel/', views.painel_view, name='painel'),  # Painel (após login)
    path('logout/', views.logout_view, name='logout'),  # Logout
    path("", lambda request: redirect("login")),

]
