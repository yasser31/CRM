# Generated by Django 3.0.3 on 2020-03-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0014_company_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(default='', max_length=256),
        ),
    ]
