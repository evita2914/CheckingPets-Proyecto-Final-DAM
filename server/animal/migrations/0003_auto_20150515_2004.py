# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_animal_amo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='foto',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'fotos/', blank=True),
        ),
    ]
