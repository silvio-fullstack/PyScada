# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-04 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0015_auto_20180913_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='xychart',
            name='y_axis_plotpoints',
            field=models.BooleanField(default=False, help_text='Show the plots points'),
        ),
        migrations.AddField(
            model_name='xychart',
            name='y_axis_uniquescale',
            field=models.BooleanField(default=True, help_text='To have a unique scale for all the y axis'),
        ),
        migrations.AlterField(
            model_name='form',
            name='control_items',
            field=models.ManyToManyField(blank=True, related_name='control_items_form', to='hmi.ControlItem'),
        ),
        migrations.AlterField(
            model_name='form',
            name='hidden_control_items_to_true',
            field=models.ManyToManyField(blank=True, related_name='hidden_control_items_form', to='hmi.ControlItem'),
        ),
    ]
