# Generated by Django 4.0.2 on 2022-08-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0011_open_position_for_un'),
    ]

    operations = [
        migrations.AddField(
            model_name='open_position_for_un',
            name='Sport',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='open_position_for_un',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
