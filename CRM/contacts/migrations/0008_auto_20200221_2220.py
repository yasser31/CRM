# Generated by Django 3.0.3 on 2020-02-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20200221_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='time',
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]