# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0005_books_lendby'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['-LendingDate', '-timestamp'], 'verbose_name_plural': 'books'},
        ),
    ]