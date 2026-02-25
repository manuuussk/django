from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello World!</h1>')

def outra(request):
    return HttpResponse('<h1>Outra Pagina</h1>')
# Create your views here.
