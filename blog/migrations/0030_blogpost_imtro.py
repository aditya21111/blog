# Generated by Django 3.1.4 on 2021-02-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20210217_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='imtro',
            field=models.CharField(default='', max_length=50),
        ),
    ]
