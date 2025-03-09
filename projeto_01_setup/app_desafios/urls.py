from django.urls import path
from .views import domingo

urlpatterns = [
    path('domingo', domingo)
]
