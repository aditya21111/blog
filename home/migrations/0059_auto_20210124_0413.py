# Generated by Django 3.1.4 on 2021-01-24 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_auto_20210124_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacted_at',
            field=models.DateTimeField(default='2021-01-24 04:12:52.268804'),
        ),
    ]
