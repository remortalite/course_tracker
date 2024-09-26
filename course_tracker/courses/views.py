from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _

from .models import Course
from users.mixins import LoginRequiredWithMsgMixin


class CoursesListView(LoginRequiredWithMsgMixin, ListView):
    model = Course
    template_name = 'index.html'

    message_no_auth = _('Please log in')
