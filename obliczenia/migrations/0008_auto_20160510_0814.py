# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0007_auto_20160505_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obliczenia_poczatkowe',
            name='przekroj_wylotowy_kolektora',
        ),
        migrations.RemoveField(
            model_name='obliczenia_poczatkowe',
            name='srednia_predkosc_na_wylocie',
        ),
        migrations.RemoveField(
            model_name='obliczenia_poczatkowe',
            name='wysokosc_h',
        ),
    ]
