# Generated by Django 2.2.6 on 2019-11-27 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20191126_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('1', 'waiting'), ('2', 'started'), ('3', 'declined'), ('4', 'timeout')], default='1', max_length=20),
        ),
    ]