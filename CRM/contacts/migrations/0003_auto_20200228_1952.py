# Generated by Django 3.0.3 on 2020-02-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200228_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='client',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
