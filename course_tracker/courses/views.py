from django.views.generic import (ListView, CreateView,
                                  UpdateView, DetailView, DeleteView)
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Course
from users.mixins import LoginRequiredWithMsgMixin


class CourseListView(LoginRequiredWithMsgMixin, ListView):
    model = Course

    message_no_auth = _('Please log in')

    extra_context = {
        'header': 'Courses',
    }

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(Q(public=True) | Q(author=self.request.user))
        return qs


class CourseCreateView(LoginRequiredWithMsgMixin, CreateView):
    model = Course
    fields = ('name', 'url', 'public')
    success_url = reverse_lazy('courses.home')
    template_name = 'form.html'

    message_no_auth = _('Please log in')

    extra_context = {
        'header': _('Create course'),
        'button_name': _('Create'),
    }

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form, *args, **kwargs)


class CourseUpdateView(LoginRequiredWithMsgMixin, UpdateView):
    model = Course
    success_url = reverse_lazy('courses.home')
    template_name = 'form.html'
    fields = ('name', 'url', 'public')

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
