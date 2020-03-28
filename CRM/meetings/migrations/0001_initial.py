# Generated by Django 3.0.3 on 2020-02-28 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=100,
                                           null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('attended', models.BooleanField(blank=True, default=False,
                                                 null=True)),
                ('contact', models.ForeignKey(null=True,
                                              on_delete=django.db.models.deletion.CASCADE,
                                              to='contacts.Contact')),
                ('user', models.ForeignKey(null=True,
                                           on_delete=django.db.models.deletion.CASCADE,
                                           to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=100,
                                           unique=True)),
                ('summary', models.TextField(null=True)),
                ('contact', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='contacts.Contact')),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                 to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
