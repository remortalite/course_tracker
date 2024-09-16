from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _

from .models import User
from .forms import UserCreateForm


class CreateUserView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'form.html'
    next_page = reverse_lazy('home')

    extra_context = {
        'title': _('Create user'),
        'header': _('Create user'),
        'button_name': _('Sign up'),
    }
