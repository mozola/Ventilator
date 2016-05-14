# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0011_remove_parametry_wejsciowe_cieplo_parowania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='cisnienie_otoczenia',
            field=models.FloatField(max_length=5, verbose_name=b'Cisnienie otoczenia:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='n1',
            field=models.IntegerField(max_length=5, verbose_name=b'n1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='n2',
            field=models.IntegerField(max_length=5, verbose_name=b'n2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='n3',
            field=models.IntegerField(max_length=5, verbose_name=b'n3'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='temperatura_otoczenia',
            field=models.FloatField(max_length=5, verbose_name=b'Temperatura otoczenia:'),
            preserve_default=True,
        ),
    ]
