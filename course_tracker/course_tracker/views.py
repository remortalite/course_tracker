from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy


class LoginUserView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'form.html'
    next_page = reverse_lazy('home')

    extra_context = {
        'title': 'Login',
        'header': 'Login',
        'button_name': 'Log in',
    }


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home')
