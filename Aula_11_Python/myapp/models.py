# myapp/models.py
from django.db import models # Importa o módulo models do Django

# Define o modelo Inscription que representará uma inscrição no banco de dados

class Inscription(models.Model):
       name = models.CharField(max_length=100) # Campo de texto para o nome
       email = models.EmailField() # Campo de email
       dob = models.DateField() # Campo de data para a data de nascimento
       image = models.ImageField(upload_to='inscriptions/', null=True, blank=True) # Campo de imagem
       
def __str__(self):
       return self.name # Retorna o nome da inscrição quando o objeto é representado como string