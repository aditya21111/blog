# Generated by Django 3.1.4 on 2021-01-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time_stamp',
            field=models.DateTimeField(default="2021-01-24 "),
        ),
    ]
