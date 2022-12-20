from django.shortcuts import render
from django.views.generic import CreateView
from .models import Usuario
from .forms import RegistrarseForm
from django.urls import reverse

# Create your views here.

class Registrarse(CreateView):
    model = Usuario
    template_name = "registrarse.html"
    form_class = RegistrarseForm

    def get_success_url(self, **kwargs):
        return reverse("home")
