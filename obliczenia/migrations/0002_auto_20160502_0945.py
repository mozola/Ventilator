# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parametry_wejsciowe',
            old_name='wydajnosc',
            new_name='drugi_strumien_wydajnosci',
        ),
        migrations.RenameField(
            model_name='parametry_wejsciowe',
            old_name='przyrost_cisnienia',
            new_name='przyrost_cisnienia_calkowitego',
        ),
        migrations.AddField(
            model_name='parametry_wejsciowe',
            name='n1',
            field=models.IntegerField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametry_wejsciowe',
            name='n2',
            field=models.IntegerField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametry_wejsciowe',
            name='n3',
            field=models.IntegerField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametry_wejsciowe',
            name='pierwszy_strumien_wydajnosci',
            field=models.IntegerField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametry_wejsciowe',
            name='trzeci_strumien_wydajnosci',
            field=models.IntegerField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
