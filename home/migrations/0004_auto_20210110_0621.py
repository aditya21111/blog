# Generated by Django 3.1.4 on 2021-01-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210108_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time_stamp',
            field=models.DateTimeField(default="2021-01-24 "),
        ),
    ]
