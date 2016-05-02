# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obliczenia_poczatkowe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gestosc_wlasciwa', models.FloatField(max_length=5)),
                ('objetosc_wlasciwa', models.FloatField(max_length=5)),
                ('strumien_masy', models.FloatField(max_length=5)),
                ('wskaznik_szybkobierznosci', models.FloatField(max_length=5)),
                ('wskaznik_srednicy', models.FloatField(max_length=5)),
                ('srednica_wirnika', models.FloatField(max_length=5)),
                ('predkosc_obwodowa_wirnika', models.FloatField(max_length=5)),
                ('szerokosc_wirnika', models.FloatField(max_length=5)),
                ('skladowa_obwodowa_predkosci', models.FloatField(max_length=5)),
                ('przekroj_wylotowy_wirnika', models.FloatField(max_length=5)),
                ('skladowa_promieniowa_predkosci', models.FloatField(max_length=5)),
                ('predkosc_wypadkowa', models.FloatField(max_length=5)),
                ('predkosc_wzgledna', models.FloatField(max_length=5)),
                ('katy_wyplywu_z_wirnika', models.FloatField(max_length=5)),
                ('wskaznik_predkosci', models.FloatField(max_length=5)),
                ('sredni_promien_na_wlocie_do_lopatki', models.FloatField(max_length=5)),
                ('szerokosc_wirnika_na_wlocie', models.FloatField(max_length=5)),
                ('przyspieszenie_przeplywu_na_wlocie', models.FloatField(max_length=5)),
                ('pole_przekroju_wlotowego', models.FloatField(max_length=5)),
                ('srednica_na_wlocie', models.FloatField(max_length=5)),
                ('predkosc_obwodowa', models.FloatField(max_length=5)),
                ('kat_naplywu', models.FloatField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parametry_wejsciowe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wydajnosc', models.IntegerField(max_length=5)),
                ('przyrost_cisnienia', models.FloatField(max_length=5)),
                ('cisnienie_otoczenia', models.FloatField(max_length=5)),
                ('temperatura_otoczenia', models.FloatField(max_length=5)),
                ('cieplo_parowania', models.FloatField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
