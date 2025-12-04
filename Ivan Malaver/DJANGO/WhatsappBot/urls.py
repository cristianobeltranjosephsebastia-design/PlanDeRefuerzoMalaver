from django.urls import path, include
from . import views

urlpatterns = [
    path("whatsapp/", views.whatsapp_webhook, name="whatsapp_webhook"),
    path("bots/", include("Bots.urls")),
]

