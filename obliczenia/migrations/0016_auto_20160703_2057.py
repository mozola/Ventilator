# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import obliczenia.model


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0015_realizowane_projekty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realizowane_projekty',
            options={'verbose_name': 'Zdjecie', 'verbose_name_plural': 'Zdjecia'},
        ),
        migrations.AlterField(
            model_name='realizowane_projekty',
            name='zdjecie_projektu',
            field=models.ImageField(upload_to=obliczenia.model.upload_to, verbose_name='photo'),
            preserve_default=True,
        ),
    ]
