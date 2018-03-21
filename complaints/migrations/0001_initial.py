# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 15:11
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('subject', models.CharField(max_length=140)),
                ('complaint', models.TextField()),
                ('complaint_against', models.CharField(max_length=200)),
                ('complaint_date', models.DateTimeField(auto_now_add=True)),
                ('complaint_tag', models.CharField(default='', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Complaints',
            },
        ),
    ]