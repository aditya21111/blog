# Generated by Django 3.1.4 on 2021-01-10 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210110_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacted_at',
            field=models.DateTimeField(default="2021-01-24 "),
        ),
    ]
