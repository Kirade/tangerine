# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('content', models.TextField()),
                ('board_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('login_id', models.CharField(max_length=100)),
                ('login_password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('register_date', models.DateTimeField()),
            ],
        ),
    ]