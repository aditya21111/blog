# Generated by Django 3.1.4 on 2021-01-24 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_auto_20210124_0352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contacted_at',
        ),
        migrations.AddField(
            model_name='contact',
            name='contacted',
            field=models.DateTimeField(default="2021-01-24 04:12:52.268804"),
        ),
    ]
