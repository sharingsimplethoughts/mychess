# Generated by Django 2.2.6 on 2019-10-31 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20191031_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='preview_image_url',
            field=models.URLField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
