# Generated by Django 3.1.4 on 2021-01-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(default='', max_length=50),
        ),
    ]
