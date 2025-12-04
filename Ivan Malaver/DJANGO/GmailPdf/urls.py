from django.urls import path
from .views import enviar_pdf

urlpatterns = [
    path("enviar/", enviar_pdf, name="enviar_pdf"),
]
