# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TurboModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('liczba_tlokow', models.IntegerField()),
                ('cykl_pracy', models.CharField(max_length=3)),
                ('objetosc_skokowa', models.FloatField()),
                ('maksymalne_obroty_silnika', models.IntegerField()),
                ('wspolczynnik_napelnienia', models.FloatField()),
                ('moc_silnika', models.IntegerField()),
                ('sprawnosc_efektywna', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
