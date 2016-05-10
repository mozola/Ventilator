# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obliczenia', '0010_auto_20160510_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parametry_wejsciowe',
            name='cieplo_parowania',
        ),
    ]
