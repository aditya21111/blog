# Generated by Django 3.1.4 on 2021-01-24 08:57

from django.db import migrations, models

from django.utils import timezone
class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210124_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacted_at',
            field=models.DateTimeField(default="2021-01-24"),
        ),
    ]
