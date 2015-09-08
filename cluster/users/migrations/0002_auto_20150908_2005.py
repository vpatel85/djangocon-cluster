# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]
