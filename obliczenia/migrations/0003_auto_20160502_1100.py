# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0002_auto_20160502_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obliczenia_poczatkowe',
            old_name='wskaznik_srednicy',
            new_name='wskaznik_srednicy_1',
        ),
        migrations.RenameField(
            model_name='obliczenia_poczatkowe',
            old_name='wskaznik_szybkobierznosci',
            new_name='wskaznik_srednicy_2',
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='wskaznik_srednicy_3',
            field=models.FloatField(default=11, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='wskaznik_szybkobierznosci_1',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='wskaznik_szybkobierznosci_2',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='wskaznik_szybkobierznosci_3',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='drugi_strumien_wydajnosci',
            field=models.FloatField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='pierwszy_strumien_wydajnosci',
            field=models.FloatField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='trzeci_strumien_wydajnosci',
            field=models.FloatField(max_length=5),
            preserve_default=True,
        ),
    ]
