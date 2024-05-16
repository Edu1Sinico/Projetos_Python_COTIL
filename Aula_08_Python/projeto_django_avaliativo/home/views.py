from django.shortcuts import render

# Criação de definição de requisição para cada HTML criado:
def home(request):
    return render(request, "home.html")

def producao(request):
    return render (request, "producao.html")

def expedicao(request):
    return render (request,"expedicao.html")

def engenharia(request):
    return render (request,"engenharia.html")

def controleQualidade(request):
    return render (request,"controleQualidade.html")



