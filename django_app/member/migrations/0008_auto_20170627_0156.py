# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 01:56
from __future__ import unicode_literals

from django.db import migrations
import member.models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20170626_0514'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', member.models.UserManager()),
            ],
        ),
    ]
