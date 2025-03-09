from django.shortcuts import render
from django.http import HttpResponse

def domingo(request):
    return HttpResponse('Hello Domingo')
