# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('nacimiento', models.DateField(null=True, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('foto', models.ImageField(null=True, upload_to=b'fotos/', blank=True)),
                ('color', models.IntegerField(default=0, choices=[(0, b'gris'), (1, b'amarillo'), (2, b'azul'), (3, b'celeste'), (4, b'morado'), (5, b'naranja'), (6, b'rojo'), (7, b'verde')])),
            ],
        ),
        migrations.CreateModel(
            name='TipoAnimal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='tipo',
            field=models.ForeignKey(to='animal.TipoAnimal'),
        ),
    ]
