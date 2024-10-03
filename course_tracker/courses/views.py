from django.views.generic import ListView, CreateView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from .models import Course
from users.mixins import LoginRequiredWithMsgMixin


class CoursesListView(LoginRequiredWithMsgMixin, ListView):
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
