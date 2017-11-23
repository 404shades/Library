# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0020_books_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='subj_code',
            field=models.ManyToManyField(blank=True, help_text='Select Subject of the book', null=True, to='Launcher.Subject'),
        ),
    ]