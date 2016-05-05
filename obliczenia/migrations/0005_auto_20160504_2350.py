# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0004_auto_20160502_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='cisnienie_na_wylocie',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='gestosc_powietrza_za_wirnikiem',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='izentropowy_przyrost_entalpii',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='izentropowy_przyrost_entalpii_dla_stopnia_od_ssania_do_tloczenia',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='praca_techniczna_izentropowa',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='promien_r2pi',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='przyrost_entalpii_pomiedzy_przekrojem_0_0_a_2_2',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='spadek_sprawosci_w_wirniku',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='sprawnosc_termodynamiczna_wirnika',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='strata_wystepujaca_podczas_przeplywu_przez_wirnik',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='strumien_objetosci_za_wirnikiem',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='temperatura_za_wirnikiem',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obliczenia_poczatkowe',
            name='wskaznik_pracy',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
