# Generated by Django 3.0.2 on 2020-01-06 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200106_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spacestation',
            name='no_revs',
        ),
        migrations.RemoveField(
            model_name='spacestation',
            name='revs_per_day',
        ),
    ]