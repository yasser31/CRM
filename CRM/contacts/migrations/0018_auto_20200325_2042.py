# Generated by Django 3.0.3 on 2020-03-25 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0017_remove_contact_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
