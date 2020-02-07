# Generated by Django 3.0.3 on 2020-02-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prospects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('photo', models.ImageField(blank=True, upload_to='media')),
                ('function', models.CharField(default='', max_length=100)),
                ('company', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField(blank=True)),
                ('twitter', models.URLField(blank=True, max_length=128, unique=True)),
                ('facebook', models.URLField(blank=True, max_length=128, unique=True)),
                ('linkedin', models.URLField(blank=True, max_length=128, unique=True)),
                ('client', models.BooleanField(default='false')),
            ],
        ),
    ]
