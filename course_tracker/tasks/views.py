from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from .models import Task


class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('tasks.home')

    extra_context = {
        'header': _('Create task'),
        'button_name': _('Save'),
    }


class TaskListView(ListView):
    model = Task

    extra_context = {
        'header': _('Tasks'),
    }


class TaskDetailView(DetailView):
    model = Task
    fields = '__all__'

    extra_context = {
        'header': _('Task detail'),
    }


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('tasks.home')

    extra_context = {
        'header': _('Task update'),
        'button_name': _('Save'),
    }
