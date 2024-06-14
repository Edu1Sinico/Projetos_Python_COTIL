from django.shortcuts import render, redirect # Importa as funções render e redirect
from django.http import HttpResponse # Importa a classe HttpResponse

from .models import Inscription # Importa o modelo Inscription

# View para a página inicial
def index(request):
    return render(request, 'index.html') # Renderiza o template index.html

# View para a página de inscrição
def signup(request):
    if request.method == 'POST': # Verifica se o método da requisição é POST

    # Obtém os dados do formulário
        num_identificacao = request.POST['num_identificacao']
        local = request.POST['local']
        image = request.FILES.get('image') # Obtém o arquivo de imagem
        # Cria uma nova inscrição no banco de dados
        Inscription.objects.create(num_identificacao=num_identificacao, local=local, image=image) # Salva a inscrição com a imagem
        # Redireciona para a página de visualização das inscrições
        return redirect('view_inscriptions')
        # Renderiza o template signup.html para GET requests
    return render(request, 'signup.html')

# View para a página de visualização das inscrições

def view_inscriptions(request):
    inscriptions = Inscription.objects.all() # Obtém todas as inscrições do banco de dados
# Renderiza o template view_inscriptions.html com a lista de inscrições
    return render(request, 'view_inscriptions.html', {'inscriptions': inscriptions})