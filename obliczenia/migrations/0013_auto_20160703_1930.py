# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0012_auto_20160511_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktualnosci',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tytul', models.CharField(max_length=20)),
                ('tekst', models.TextField()),
                ('autor', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='cisnienie_otoczenia',
            field=models.FloatField(max_length=5, verbose_name=b'Cisnienie otoczenia (Pa):'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='drugi_strumien_wydajnosci',
            field=models.FloatField(max_length=5, verbose_name=b'strumien wydajnosci 2 (m^3/s):'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='n1',
            field=models.IntegerField(max_length=5, verbose_name=b'n1 (obr/min):'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='n2',
            field=models.IntegerField(max_length=5, verbose_name=b'n2 (obr/min)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='n3',
            field=models.IntegerField(max_length=5, verbose_name=b'n3 (obr/min)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='pierwszy_strumien_wydajnosci',
            field=models.FloatField(max_length=5, verbose_name=b'strumien wydajnosci 1 (m^3/s):'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='przyrost_cisnienia_calkowitego',
            field=models.FloatField(max_length=5, verbose_name=b'Przyrost cisnienia calkowitego (Pa):'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='temperatura_otoczenia',
            field=models.FloatField(max_length=5, verbose_name=b'Temperatura otoczenia (K):'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry_wejsciowe',
            name='trzeci_strumien_wydajnosci',
            field=models.FloatField(max_length=5, verbose_name=b'strumien wydajnosci 3 (m^3/s):'),
            preserve_default=True,
        ),
    ]
