# Generated by Django 3.0.3 on 2020-03-24 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_auto_20200324_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
