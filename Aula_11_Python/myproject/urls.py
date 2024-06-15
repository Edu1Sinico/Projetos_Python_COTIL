# myproject/urls.py
from django.contrib import admin  # Importa o módulo admin do Django
from django.urls import path  # Importa a função path
from myapp import views  # Importa as views do aplicativo myapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),  # URL para a administração do site
    path("", views.index, name="index"),  # URL para a página inicial
    path("signup/", views.signup, name="signup"),  # URL para a página de inscrição
    path(
        "inscriptions/", views.view_inscriptions, name="view_inscriptions"
    ),  # URL para a página de visualização das inscrições
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)