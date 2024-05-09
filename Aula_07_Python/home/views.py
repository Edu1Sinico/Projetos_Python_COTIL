from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request): 
    print ('Teste de Home')
    return render(request,'home.html')

def teste(request):
    return render (request,'teste.html')
