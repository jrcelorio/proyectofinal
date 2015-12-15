# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunioapp', '0002_jugadores_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='foto',
            field=models.ImageField(null=True, upload_to='comunioapp/static/media'),
        ),
    ]
