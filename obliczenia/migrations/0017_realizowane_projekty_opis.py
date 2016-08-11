# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0016_auto_20160703_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='realizowane_projekty',
            name='opis',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
