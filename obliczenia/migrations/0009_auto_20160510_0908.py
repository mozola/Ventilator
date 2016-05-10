# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0008_auto_20160510_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obliczenia_poczatkowe',
            old_name='katy_wyplywu_z_wirnika',
            new_name='katy_wyplywu_z_wirnika_alpha_1',
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='katy_wyplywu_z_wirnika_beta_1',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
