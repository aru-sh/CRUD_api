# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20200112_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='QuestionName',
            new_name='question_name',
        ),
    ]
