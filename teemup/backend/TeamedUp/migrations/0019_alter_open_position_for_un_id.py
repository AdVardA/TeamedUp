# Generated by Django 4.0.2 on 2022-08-09 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0018_club_profile_count_pos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='open_position_for_un',
            name='id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='TeamedUp.univer_profile'),
        ),
    ]
