# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0017_realizowane_projekty_opis'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realizowane_projekty',
            options={},
        ),
        migrations.AlterField(
            model_name='realizowane_projekty',
            name='zdjecie_projektu',
            field=models.ImageField(default=b'temps/no_img.jpg', upload_to=b'temps/'),
            preserve_default=True,
        ),
    ]
