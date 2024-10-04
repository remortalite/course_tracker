from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class Course(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=128)
    url = models.CharField(verbose_name=_("URL"), max_length=255)

    author = models.ForeignKey(to=User, verbose_name=_('Author'), on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
