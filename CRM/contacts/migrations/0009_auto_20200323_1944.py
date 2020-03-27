# Generated by Django 3.0.3 on 2020-03-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_company_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='company',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]