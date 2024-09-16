from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
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


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'form.html'
    success_url = reverse_lazy('home')
    fields = ('first_name', 'last_name', 'username',)

    extra_context = {
        'title': _('Update user'),
        'header': _('Update user'),
        'button_name': _('Update'),
    }