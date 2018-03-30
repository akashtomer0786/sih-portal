# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 05:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0008_auto_20180330_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='complaint_taken_by',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]