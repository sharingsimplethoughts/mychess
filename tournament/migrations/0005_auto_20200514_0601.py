# Generated by Django 2.2.6 on 2020-05-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_tournamentplayermanager_total_games_drawn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='is_entry_before_tournament',
            field=models.BooleanField(default=False),
        ),
    ]