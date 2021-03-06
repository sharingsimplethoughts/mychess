# Generated by Django 2.2.6 on 2019-12-26 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('title_ar', models.CharField(default='', max_length=200)),
                ('content', models.TextField()),
                ('content_ar', models.TextField(default='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('title_ar', models.CharField(default='', max_length=500)),
                ('content', models.TextField()),
                ('content_ar', models.TextField(default='')),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('title_ar', models.CharField(default='', max_length=100)),
                ('content', models.TextField()),
                ('content_ar', models.TextField(default='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Legal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('title_ar', models.CharField(default='', max_length=100)),
                ('content', models.TextField()),
                ('content_ar', models.TextField(default='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('title_ar', models.CharField(default='', max_length=100)),
                ('content', models.TextField()),
                ('content_ar', models.TextField(default='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TermsAndCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('title_ar', models.CharField(default='', max_length=100)),
                ('content', models.TextField()),
                ('content_ar', models.TextField(default='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
