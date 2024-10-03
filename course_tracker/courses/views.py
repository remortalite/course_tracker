from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from .models import Course
from users.mixins import LoginRequiredWithMsgMixin


class CourseListView(LoginRequiredWithMsgMixin, ListView):
    model = Course

    message_no_auth = _('Please log in')

    extra_context = {
        "header": "Courses",
    }


class CourseCreateView(LoginRequiredWithMsgMixin, CreateView):
    model = Course
    success_url = reverse_lazy('courses.home')
    template_name = 'form.html'
    fields = '__all__'

    message_no_auth = _('Please log in')

    extra_context = {
        'header': _('Create course'),
        'button_name': _('Create'),
    }

class CourseUpdateView(LoginRequiredWithMsgMixin, UpdateView):
    model = Course
    success_url = reverse_lazy('courses.home')
    template_name = 'form.html'
    fields = ('name', 'url')

    message_no_auth = _('Please log in')

    extra_context = {
        'header': _('Update course'),
        'button_name': _('Save'),
    }

class CourseDetailView(LoginRequiredWithMsgMixin, DetailView):
    model = Course
    fields = '__all__'

    message_no_auth = _('Please log in')

    extra_context = {
        'header': _('Course detail'),
    }

class CourseDeleteView(LoginRequiredWithMsgMixin, DeleteView):
    model = Course
    template_name = 'form.html'
    success_url = reverse_lazy('courses.home')

    message_no_auth = _('Please log in')

    extra_context = {
        'header': _('Are you sure you want to delete the course?'),
        'button_name': _('Yes, delete'),
    }
