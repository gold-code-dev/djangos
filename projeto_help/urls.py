from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls), # nao vou usar admin
    path('', include('app_users.urls')),  # Incluímos as rotas do app_users
    # path('escritorios/', include('app_escritorios.urls')),  # Rotas do app_escritorios

]

# Servir arquivos de mídia (como logomarcas) em DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
