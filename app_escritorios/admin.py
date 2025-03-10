from django.contrib import admin
from .models import Escritorio


@admin.register(Escritorio)
class EscritorioAdmin(admin.ModelAdmin):
    list_display = ('nome',)
