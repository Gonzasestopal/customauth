# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150915_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='user',
        ),
        migrations.DeleteModel(
            name='Tweet',
        ),
    ]
