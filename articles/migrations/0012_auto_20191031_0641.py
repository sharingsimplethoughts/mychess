# Generated by Django 2.2.6 on 2019-10-31 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20191031_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='preview_image',
            field=models.ImageField(blank=True, default='', max_length=9000, null=True, upload_to='articles/preview'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author_profile_photo',
            field=models.ImageField(blank=True, default='', max_length=9000, null=True, upload_to='articles/auth_profile'),
        ),
    ]
