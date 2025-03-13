from django.shortcuts import render


def painel_view(request):
    return render(request, 'app_core/painel.html')
