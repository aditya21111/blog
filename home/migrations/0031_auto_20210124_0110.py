# Generated by Django 3.1.4 on 2021-01-24 09:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20210124_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacted_at',
            field=models.DateTimeField(default="2021-01-24 04:12:52.268804"),
        ),
    ]
