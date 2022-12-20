from . import views
from django.urls import path

app_name = "usuarios"

urlpatterns = [
    path('registrarse', views.Registrarse.as_view(), name="registrarse"),
]
