from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from django.urls import reverse_lazy


class LoginUserView(SuccessMessageMixin, LoginView):
    authentication_form = AuthenticationForm
    template_name = 'form.html'
    next_page = reverse_lazy('home')
    success_message = _('Login success')

    extra_context = {
        'title': 'Login',
        'header': 'Login',
        'button_name': 'Log in',
    }


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home')

    success_message = _('Logged out')

    def post(self, request, *args, **kwargs):
        messages.info(request, self.success_message)
        return super().post(request, *args, **kwargs)
