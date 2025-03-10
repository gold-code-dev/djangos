from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_users.urls')),  # Incluímos as rotas do app_users
]
