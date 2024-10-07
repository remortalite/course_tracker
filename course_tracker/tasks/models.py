from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    STATUS_CHOICES = (
        ("INPROGRESS", _("In progress")),
        ("FINISHED", _("Finished")),
        ("FREEZED", _("Freezed")),
    )

    name = models.CharField(verbose_name=_('Name'), max_length=128)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    link = models.CharField(verbose_name=_('Link'), max_length=255, null=True, blank=True)
    status = models.CharField(verbose_name=_('Status'), max_length=12, choices=STATUS_CHOICES)
