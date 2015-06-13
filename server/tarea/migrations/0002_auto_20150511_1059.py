# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
