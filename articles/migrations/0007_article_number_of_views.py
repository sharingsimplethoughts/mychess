# Generated by Django 2.2.6 on 2019-10-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_author_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='number_of_views',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]