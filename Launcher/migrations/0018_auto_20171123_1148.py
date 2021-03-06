# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0017_auto_20171121_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='ISBN',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='page_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='subj_code',
            field=models.ManyToManyField(blank=True, help_text='Select Subject of the book', null=True, to='Launcher.Subject'),
        ),
    ]
