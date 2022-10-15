from email.mime import image
from django.urls import path
from galeria.views import imagem, index

urlpatterns = [
    path('', index),
    path('imagem/', imagem)
]