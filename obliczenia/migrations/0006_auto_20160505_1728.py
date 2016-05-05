# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0005_auto_20160504_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obliczenia_poczatkowe',
            name='gestosc_wlasciwa',
            field=models.FloatField(max_length=10),
            preserve_default=True,
        ),
    ]
