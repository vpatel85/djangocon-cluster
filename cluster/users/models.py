from __future__ import unicode_literals

# from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models


class User(AbstractUser):
    location = models.PointField(null=True)
    age = models.PositiveIntegerField(null=True)

    def __unicode__(self):
        return self.username
