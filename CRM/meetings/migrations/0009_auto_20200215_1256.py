# Generated by Django 3.0.3 on 2020-02-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0008_setmeeting_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setmeeting',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
