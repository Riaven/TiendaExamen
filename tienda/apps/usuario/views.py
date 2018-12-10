from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroUsuario

class RegistroUsuario(CreateView):
    model = User
    template_name = "registration/registrar.html"
    form_class = RegistroUsuario
    success_url = reverse_lazy('rescatado_listar')