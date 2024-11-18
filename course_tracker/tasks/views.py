from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from .models import Task


class TaskCreateView(CreateView):
    model = Task
    fields = ('name', 'description', 'link', 'status', 'course')
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
    fields = ('name', 'description', 'link', 'status', 'course')

    extra_context = {
        'header': _('Task detail'),
    }


class TaskUpdateView(UpdateView):
    model = Task
    fields = ('name', 'description', 'link', 'status', 'course')
    template_name = 'form.html'
    success_url = reverse_lazy('tasks.home')

    extra_context = {
        'header': _('Task update'),
        'button_name': _('Save'),
    }


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks.home')
    template_name = 'form.html'

    extra_context = {
        'header': _('Are you sure you want to delete the task?'),
        'button_name': _('Yes, delete'),
    }
