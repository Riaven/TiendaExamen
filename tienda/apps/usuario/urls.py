from django.conf.urls import url, include
from apps.usuario.views import RegistroUsuario
from django.contrib.auth.views import LoginView, logout_then_login
# PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name='registrar'),
]