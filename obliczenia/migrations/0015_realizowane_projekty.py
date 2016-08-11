# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import obliczenia.model


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0014_auto_20160703_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realizowane_projekty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tytul_projektu', models.CharField(max_length=100)),
                ('zdjecie_projektu', models.ImageField(upload_to=obliczenia.model.upload_to, verbose_name=b'tets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
