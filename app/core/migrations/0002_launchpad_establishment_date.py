# Generated by Django 3.0.1 on 2020-01-01 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='launchpad',
            name='establishment_date',
            field=models.DateField(default='1955-07-02'),
            preserve_default=False,
        ),
    ]
