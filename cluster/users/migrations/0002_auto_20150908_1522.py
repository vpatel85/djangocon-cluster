# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
        ),
    ]
