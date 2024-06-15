# myapp/models.py
from django.db import models  # Importa o módulo models do Django

# Define o modelo Inscription que representará uma inscrição no banco de dados


class Inscription(models.Model):
    num_identificacao = models.CharField(max_length=100)  # Campo de texto para o num_identificacao
    local = models.CharField(max_length=100) # Campo de local
    image = models.ImageField(
        upload_to="inscriptions/", null=True, blank=True
    )  # Campo de imagem


def __str__(self):
    return (
        self.name
    )  # Retorna o nome da inscrição quando o objeto é representado como string