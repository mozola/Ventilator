# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0003_auto_20160502_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obliczenia_poczatkowe',
            old_name='srednica_wirnika',
            new_name='srednica_wirnika_1',
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='srednica_wirnika_2',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='srednica_wirnika_3',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
