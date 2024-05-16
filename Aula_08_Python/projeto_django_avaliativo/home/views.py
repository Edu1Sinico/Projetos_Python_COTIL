from django.shortcuts import render

# Criação de definição de requisição para cada HTML criado:
def home(request):
    return render(request, "home.html")


