from django.views.generic import CreateView

from .models import User
from .forms import UserCreateForm


class CreateUserView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'form.html'
