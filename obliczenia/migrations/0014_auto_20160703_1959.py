# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0013_auto_20160703_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktualnosci',
            name='autor',
            field=models.CharField(max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aktualnosci',
            name='tytul',
            field=models.CharField(max_length=70),
            preserve_default=True,
        ),
    ]
