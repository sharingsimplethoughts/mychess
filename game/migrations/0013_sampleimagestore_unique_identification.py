# Generated by Django 2.2.6 on 2019-12-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_sampleimagestore'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampleimagestore',
            name='unique_identification',
            field=models.CharField(default='', max_length=50),
        ),
    ]
