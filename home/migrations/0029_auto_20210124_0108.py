# Generated by Django 3.1.4 on 2021-01-24 09:08

from django.db import migrations, models
from django.utils.timezone import utc
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20210124_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacted_at',
            field=models.DateTimeField(default="2021-01-24 "),
        ),
    ]
