# Generated by Django 3.1.4 on 2021-01-24 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_auto_20210124_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]
