from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    age = models.PositiveIntegerField(null=True)

    def __unicode__(self):
        return self.username
