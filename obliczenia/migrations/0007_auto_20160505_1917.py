# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0006_auto_20160505_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='przekroj_wylotowy_kolektora',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='srednia_predkosc_na_wylocie',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='wysokosc_h',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
