from django.db import models
from django.utils.translation import gettext_lazy as _

from courses.models import Course


class Task(models.Model):
    STATUS_CHOICES = (
        ("inprogress", _("In progress")),
        ("finished", _("Finished")),
        ("freezed", _("Freezed")),
    )

    name = models.CharField(verbose_name=_('Name'), max_length=128)
    description = models.TextField(verbose_name=_('Description'),
                                   null=True, blank=True)
    link = models.CharField(verbose_name=_('Link'), max_length=255,
                            null=True, blank=True)
    status = models.CharField(verbose_name=_('Status'), max_length=12,
                              choices=STATUS_CHOICES)
    course = models.ForeignKey(verbose_name=_('Course'), to=Course,
                               on_delete=models.PROTECT, null=True,
                               blank=True, related_name='tasks')

    def __str__(self):
        return self.name
