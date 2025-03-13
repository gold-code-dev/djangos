from django.shortcuts import render


def ticket_list(request):
    return render(request, 'ticket_list.html')
