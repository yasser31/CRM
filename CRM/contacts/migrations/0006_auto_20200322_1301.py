# Generated by Django 3.0.3 on 2020-03-22 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20200322_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.RemoveField(
            model_name='departement',
            name='user',
        ),
    ]