from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.utils.translation import gettext_lazy as _

from .mixins import LoginRequiredWithMsgMixin
from .models import User
from .forms import UserCreateForm


class CreateUserView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'form.html'
    success_url = reverse_lazy('home')
    success_message = _('User created')

    extra_context = {
        'title': _('Create user'),
        'header': _('Create user'),
        'button_name': _('Sign up'),
    }


class UpdateUserView(SuccessMessageMixin,
                     LoginRequiredWithMsgMixin,
                     UpdateView):
    model = User
    template_name = 'form.html'
    success_url = reverse_lazy('home')
    fields = ('first_name', 'last_name', 'username',)

    message_no_auth = _('You need to log in')
    success_message = _('User updated')

    extra_context = {
        'title': _('Update user'),
        'header': _('Update user'),
        'button_name': _('Update'),
    }
