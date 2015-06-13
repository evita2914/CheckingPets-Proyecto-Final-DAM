# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('animal', models.ForeignKey(to='animal.Animal')),
            ],
        ),
    ]
