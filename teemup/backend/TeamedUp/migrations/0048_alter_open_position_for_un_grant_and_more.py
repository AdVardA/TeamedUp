# Generated by Django 4.0.2 on 2022-08-30 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0047_alter_teem_link_alter_teem_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='open_position_for_un',
            name='grant',
            field=models.CharField(default='----', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='agree_to_private_rule',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
